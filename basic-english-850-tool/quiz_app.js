(function () {
    let words = [];
    let progress = {};
    let plan = { newCount: 5, reviewCount: 10 };
    let session = null;
    let currentAudio = null;

    const $ = id => document.getElementById(id);

    async function init() {
        bindEvents();
        plan = WordStore.loadPlan();
        progress = WordStore.loadProgress();
        updatePlanDisplay();
        setStatus('正在准备词库…');
        $('startBtn').disabled = true;
        try {
            words = await WordStore.loadWords();
            $('startBtn').disabled = false;
            setStatus(`词库已准备好，共 ${words.length} 个词`);
            updateStats();
        } catch (error) {
            setStatus(`${error.message}。请通过本地网站打开本页面。`, true);
        }
    }

    function bindEvents() {
        $('startBtn').addEventListener('click', startSession);
        $('nextBtn').addEventListener('click', nextQuestion);
        $('backBtn').addEventListener('click', goHome);
        $('settingsModal').addEventListener('click', event => {
            if (event.target === $('settingsModal')) hideSettings();
        });
        window.showSettings = showSettings;
        window.hideSettings = hideSettings;
        window.confirmSettings = confirmSettings;
        window.goHome = goHome;
        window.pronounceText = pronounceText;
    }

    function setStatus(message, isError = false) {
        let status = $('loadStatus');
        if (!status) {
            status = document.createElement('p');
            status.id = 'loadStatus';
            status.className = 'load-status';
            $('startBtn').parentElement.after(status);
        }
        status.textContent = message;
        status.classList.toggle('error', isError);
    }

    function showSettings() {
        $('settingNewCount').value = plan.newCount;
        $('settingReviewCount').value = plan.reviewCount;
        $('settingsModal').classList.add('show');
    }

    function hideSettings() {
        $('settingsModal').classList.remove('show');
    }

    function confirmSettings() {
        plan.newCount = clamp($('settingNewCount').value, 1, 20, 5);
        plan.reviewCount = clamp($('settingReviewCount').value, 0, 30, 10);
        WordStore.savePlan(plan);
        updatePlanDisplay();
        hideSettings();
    }

    function updatePlanDisplay() {
        $('planNew').textContent = plan.newCount;
        $('planReview').textContent = plan.reviewCount;
    }

    function updateStats() {
        const mastered = words.filter(word => LearningScheduler.isMastered(progress[word.word])).length;
        const total = words.length || 850;
        const percent = Math.round(mastered / total * 100) || 0;
        const counts = LearningScheduler.dueCounts(words, progress);
        $('masteredCount').textContent = mastered;
        $('totalWordCount').textContent = total;
        $('masteredPercent').textContent = `${percent}%`;
        $('progressFillHome').style.width = `${percent}%`;
        $('rescueCountHome').textContent = counts.rescue;
        $('estimateMinutes').textContent = Math.max(5, Math.ceil((plan.newCount * 2 + plan.reviewCount) * 0.7));
    }

    function startSession() {
        const selected = LearningScheduler.selectWords(words, progress, plan.newCount, plan.reviewCount);
        if (!selected.length) {
            setStatus('今天的复习已经完成，可以稍后再来。');
            return;
        }
        const queue = [];
        selected.forEach(word => {
            const p = LearningScheduler.normalizeProgress(progress[word.word]);
            if (p.seenCount === 0) queue.push({ word, mode: 'study' });
            queue.push({ word, mode: 'quiz', firstQuiz: p.seenCount === 0, type: chooseQuestionType(word, p, p.seenCount === 0) });
        });
        session = { queue, index: 0, results: [], correct: 0, wrong: 0, answered: false };
        showPage('quizPage');
        loadQuestion();
    }

    function loadQuestion() {
        stopAudio();
        if (session.index >= session.queue.length) return showSessionComplete();
        session.answered = false;
        resetQuestionDisplay();
        updateProgressBar();
        const item = session.queue[session.index];
        if (item.mode === 'study') showStudyCard(item.word);
        else showQuiz(item.word);
    }

    function showStudyCard(word) {
        $('questionType').textContent = `先认识新词 · ${difficultyLabel(word.difficulty)}`;
        $('question').textContent = '先听一遍，再跟读';
        $('phonetic').innerHTML = `<button type="button" class="sound-btn" id="replayWordBtn">再听一次</button>`;
        $('options').style.display = 'none';
        showDetail(word, false);
        $('replayWordBtn').addEventListener('click', () => pronounceWord(word));
        $('nextBtn').textContent = '我认识了，来做题 →';
        $('nextBtn').disabled = false;
        pronounceWord(word);
    }

    function showQuiz(word) {
        const item = session.queue[session.index];
        const type = item.type || chooseQuestionType(word, LearningScheduler.normalizeProgress(progress[word.word]), item.firstQuiz);
        if (type === 'listen') showListeningQuestion(word);
        else if (type === 'spelling') showSpellingQuestion(word);
        else if (type === 'usage') showUsageQuestion(word);
        else if (type === 'example') showExampleQuestion(word);
        else showMeaningQuestion(word);
    }

    function chooseQuestionType(word, p, isFirstQuiz = false) {
        if (p.lastMistakeType) {
            return ({ listening: 'listen', meaning: 'meaning', spelling: 'spelling', usage: 'usage' })[p.lastMistakeType] || 'meaning';
        }
        if (isFirstQuiz || p.seenCount < 2) return Math.random() < 0.55 ? 'listen' : 'meaning';
        const pool = ['listen', 'meaning'];
        if (word.exampleQuestion) pool.push('example');
        if (word.usage && word.usage.length) pool.push('usage');
        if (p.seenCount >= 2) pool.push('spelling');
        return pool[Math.floor(Math.random() * pool.length)];
    }

    function showMeaningQuestion(word) {
        $('questionType').textContent = '看英文，选意思';
        $('question').textContent = word.word;
        $('phonetic').textContent = word.phonetic;
        const choices = [word, ...getDistractors(word, 3)].map(item => item.childMeaning);
        renderOptions(LearningScheduler.shuffle(choices), word.childMeaning, answer => answer === word.childMeaning, 'meaning');
        pronounceWord(word);
    }

    function showListeningQuestion(word) {
        $('questionType').textContent = '听发音，选单词';
        $('question').textContent = '点击喇叭再听一次';
        $('phonetic').textContent = '';
        $('question').classList.add('speak-question');
        $('question').onclick = () => pronounceWord(word);
        const choices = [word, ...getDistractors(word, 3)].map(item => item.word);
        renderOptions(LearningScheduler.shuffle(choices), word.word, answer => answer === word.word, 'listening');
        pronounceWord(word);
    }

    function showSpellingQuestion(word) {
        $('questionType').textContent = '根据意思拼写';
        $('question').textContent = word.childMeaning;
        $('phonetic').textContent = '';
        $('options').innerHTML = `
            <form id="spellingForm" class="spelling-form">
                <label for="spellingInput">输入英文单词</label>
                <input id="spellingInput" autocomplete="off" autocapitalize="none" spellcheck="false">
                <button type="submit" class="option">检查答案</button>
            </form>`;
        $('spellingForm').addEventListener('submit', event => {
            event.preventDefault();
            if (session.answered) return;
            const answer = $('spellingInput').value.trim().toLowerCase();
            finishAnswer(answer === word.word.toLowerCase(), word, 'spelling');
        });
        $('spellingInput').focus();
    }

    function showExampleQuestion(word) {
        const question = word.exampleQuestion || { sentence: firstExampleSentence(word).replace(word.word, '___'), answer: word.word };
        $('questionType').textContent = '看例句，选单词';
        $('question').textContent = question.sentence;
        $('phonetic').textContent = '';
        const choices = [word.word, ...getDistractors(word, 3).map(item => item.word)];
        renderOptions(LearningScheduler.shuffle(unique(choices)), word.word, answer => answer === word.word, 'usage');
    }

    function showUsageQuestion(word) {
        $('questionType').textContent = '选择常见搭配';
        $('question').textContent = word.word;
        $('phonetic').textContent = '哪个表达最常见？';
        const correct = (word.usage && word.usage[0]) || `${word.word} in a sentence`;
        const choices = [correct, ...getDistractors(word, 3).map(item => {
            const usage = item.usage && item.usage[0];
            return usage || `${item.word} in a sentence`;
        })];
        renderOptions(LearningScheduler.shuffle(unique(choices)), correct, answer => answer === correct, 'usage');
    }

    function renderOptions(choices, correct, checker, mistakeType = 'meaning') {
        $('options').innerHTML = '';
        choices.forEach(choice => {
            const button = document.createElement('button');
            button.type = 'button';
            button.className = 'option';
            button.textContent = choice;
            button.addEventListener('click', () => {
                if (session.answered) return;
                [...$('options').children].forEach(item => {
                    if (item.textContent === correct) item.classList.add('correct');
                });
                const isCorrect = checker(choice);
                if (!isCorrect) button.classList.add('wrong');
                finishAnswer(isCorrect, session.queue[session.index].word, mistakeType);
            });
            $('options').appendChild(button);
        });
    }

    function finishAnswer(isCorrect, word, mistakeType = 'meaning') {
        session.answered = true;
        session[isCorrect ? 'correct' : 'wrong']++;
        const before = LearningScheduler.normalizeProgress(progress[word.word]);
        progress[word.word] = LearningScheduler.recordAnswer(progress[word.word], isCorrect, new Date(), isCorrect ? null : mistakeType);
        if (word.difficulty === 'extension' || (word.tags || []).includes('needs-parent-help')) {
            progress[word.word].needsParentHelp = true;
        }
        WordStore.saveProgress(progress);
        session.results.push({ word, isCorrect, mistakeType, rescued: isCorrect && Boolean(before.lastMistakeType) });
        if (!isCorrect) {
            const position = Math.min(session.queue.length, session.index + 3);
            session.queue.splice(position, 0, { word, mode: 'quiz', retry: true, type: typeForMistake(mistakeType) });
        } else if (session.queue[session.index].firstQuiz) {
            const position = Math.min(session.queue.length, session.index + 4);
            session.queue.splice(position, 0, { word, mode: 'quiz', retry: true, type: 'meaning' });
        }
        showDetail(word, true);
        $('nextBtn').textContent = '下一题 →';
        $('nextBtn').disabled = false;
        updateProgressBar();
        pronounceWord(word);
    }

    function showDetail(word, revealMeaning) {
        $('wordDetail').style.display = 'block';
        $('wordDetail').classList.toggle('study-mode', !revealMeaning);
        const family = word.phonics && word.phonics.family && word.phonics.family.length
            ? `<div class="study-step">同规律词：${word.phonics.family.slice(0, 4).join(' / ')}</div>` : '';
        const usage = word.usage && word.usage.length
            ? `<div class="usage-list">${word.usage.slice(0, 3).map(item => `<span class="usage-chip">${escapeHtml(item)}</span>`).join('')}</div>` : '';
        const studySteps = !revealMeaning ? `<div class="study-steps">
            <div class="study-step">1. 先听声音，再跟读 2 遍。</div>
            <div class="study-step">2. 看拼写：${escapeHtml(word.word)}</div>
            <div class="study-step">3. 想意思：${escapeHtml(word.childMeaning)}</div>
            ${family}
        </div>` : '';
        $('detailWord').textContent = word.word;
        $('detailWord').onclick = () => pronounceWord(word);
        $('detailPhonetic').textContent = word.phonetic;
        $('detailMeaning').textContent = word.childMeaning;
        $('detailExamples').innerHTML = studySteps + usage;
        word.examples.slice(0, 1).forEach(example => {
            const button = document.createElement('button');
            button.type = 'button';
            button.className = 'example-button';
            button.textContent = `${example.en}  🔊`;
            button.addEventListener('click', () => pronounceExample(example));
            $('detailExamples').appendChild(button);
        });
        $('nextBtnContainer').style.display = 'block';
        if (!revealMeaning) $('options').style.display = 'none';
    }

    function nextQuestion() {
        session.index++;
        loadQuestion();
    }

    function showSessionComplete() {
        const attempts = session.correct + session.wrong;
        const uniqueLearned = new Set(session.results.filter(x => x.isCorrect).map(x => x.word.word)).size;
        const retryWords = [...new Map(session.results.filter(x => !x.isCorrect).map(x => [x.word.word, x.word])).values()];
        const rescuedWords = [...new Map(session.results.filter(x => x.rescued).map(x => [x.word.word, x.word])).values()];
        $('resultEmoji').textContent = uniqueLearned ? '✓' : '↻';
        $('resultTitle').textContent = `今天练会了 ${uniqueLearned} 个词`;
        $('resultRate').textContent = retryWords.length
            ? `还有 ${retryWords.length} 个词会优先帮你练`
            : `今天救回 ${rescuedWords.length} 个词`;
        $('resultCorrect').textContent = session.correct;
        $('resultWrong').textContent = session.wrong;
        $('resultTotal').textContent = attempts;
        $('resultWordList').innerHTML = '';
        const latest = new Map(session.results.map(result => [result.word.word, result]));
        latest.forEach(result => {
            const item = document.createElement('button');
            item.type = 'button';
            item.className = 'result-word-item result-word-button';
            item.innerHTML = `<span class="rw-icon ${result.isCorrect ? 'correct' : 'wrong'}">${result.isCorrect ? '✓' : '↻'}</span>
                <span class="rw-info"><span class="rw-word">${escapeHtml(result.word.word)} <span class="rw-phonetic">${escapeHtml(result.word.phonetic)}</span></span>
                <span class="rw-meaning">${escapeHtml(result.word.childMeaning)}</span></span>`;
            item.addEventListener('click', () => pronounceWord(result.word));
            $('resultWordList').appendChild(item);
        });
        renderParentPractice([...retryWords, ...rescuedWords, ...session.results.map(result => result.word)]);
        updateStats();
        showPage('resultPage');
    }

    function getDistractors(word, count) {
        const configured = (word.confusables || [])
            .map(name => words.find(item => item.word === name))
            .filter(item => item && item.word !== word.word);
        if (configured.length >= count) return configured.slice(0, count);
        const fallback = words.filter(item => item.word !== word.word && item.category === word.category && !configured.some(x => x.word === item.word))
            .map(item => ({ item, score: similarity(word.word, item.word) }))
            .sort((a, b) => b.score - a.score || Math.random() - 0.5)
            .slice(0, count).map(entry => entry.item);
        return [...configured, ...fallback].slice(0, count);
    }

    function typeForMistake(mistakeType) {
        return ({ listening: 'listen', meaning: 'meaning', spelling: 'spelling', usage: 'usage' })[mistakeType] || 'meaning';
    }

    function renderParentPractice(candidates) {
        const container = $('parentPracticeList');
        container.innerHTML = '';
        const picked = [];
        const seen = new Set();
        candidates.forEach(word => {
            if (!word || seen.has(word.word) || picked.length >= 3) return;
            seen.add(word.word);
            picked.push(word);
        });
        if (!picked.length) picked.push(...words.slice(0, 3));
        picked.slice(0, 3).forEach(word => {
            const example = firstExampleSentence(word);
            const card = document.createElement('div');
            card.className = 'parent-card';
            card.innerHTML = `<div class="parent-card-title"><span>${escapeHtml(word.word)} <small>${escapeHtml(word.phonetic)}</small></span><button type="button">发音</button></div>
                <div>意思：${escapeHtml(word.childMeaning)}</div>
                <div>例句：${escapeHtml(example)}</div>
                <div class="parent-tip">家长问：${escapeHtml(word.parentTip || `你能用 ${word.word} 说一句话吗？`)}</div>`;
            card.querySelector('button').addEventListener('click', () => pronounceWord(word));
            container.appendChild(card);
        });
    }

    function firstExampleSentence(word) {
        return (word.examples && word.examples[0] && word.examples[0].en) || `We can use ${word.word} today.`;
    }

    function unique(values) {
        return [...new Set(values)].slice(0, 4);
    }

    function similarity(a, b) {
        let score = 0;
        if (a[0] === b[0]) score += 3;
        if (a.length === b.length) score += 2;
        score -= Math.abs(a.length - b.length);
        return score;
    }

    function updateProgressBar() {
        const total = session.queue.length;
        const current = Math.min(session.index + 1, total);
        $('progressCorrect').style.width = `${session.correct / total * 100}%`;
        $('progressWrong').style.width = `${session.wrong / total * 100}%`;
        $('progressCount').textContent = `${current} / ${total}`;
        $('correctCount').textContent = session.correct;
        $('wrongCount').textContent = session.wrong;
    }

    function resetQuestionDisplay() {
        $('question').classList.remove('speak-question');
        $('question').onclick = null;
        $('phonetic').textContent = '';
        $('options').innerHTML = '';
        $('options').style.display = 'grid';
        $('wordDetail').style.display = 'none';
        $('nextBtnContainer').style.display = 'none';
        $('backBtnContainer').style.display = 'none';
    }

    function pronounceWord(word) {
        const source = word.voice && word.voice.female;
        playAudio(source, word.word);
    }

    function pronounceExample(example) {
        playAudio(example && example.audio, example && example.en);
    }

    function playAudio(source, fallbackText) {
        stopAudio();
        if (source) {
            currentAudio = new Audio(source);
            currentAudio.play().catch(() => pronounceText(fallbackText));
        } else pronounceText(fallbackText);
    }

    function pronounceText(text) {
        stopAudio();
        if (!text) return;
        if (!('speechSynthesis' in window)) return;
        const utterance = new SpeechSynthesisUtterance(text);
        utterance.lang = 'en-US';
        utterance.rate = 0.88;
        speechSynthesis.speak(utterance);
    }

    function stopAudio() {
        if (currentAudio) {
            currentAudio.pause();
            currentAudio = null;
        }
        if ('speechSynthesis' in window) speechSynthesis.cancel();
    }

    function showPage(id) {
        document.querySelectorAll('.page').forEach(page => page.classList.remove('active'));
        $(id).classList.add('active');
    }

    function goHome() {
        stopAudio();
        updateStats();
        showPage('homePage');
    }

    function difficultyLabel(value) {
        return ({ basic: '基础', advanced: '进阶', extension: '拓展' })[value] || '进阶';
    }

    function clamp(value, min, max, fallback) {
        const number = Number(value);
        return Number.isFinite(number) ? Math.max(min, Math.min(max, number)) : fallback;
    }

    function escapeHtml(value) {
        return String(value).replace(/[&<>"']/g, char => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' })[char]);
    }

    document.addEventListener('DOMContentLoaded', init);
})();
