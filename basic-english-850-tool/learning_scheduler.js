(function (root, factory) {
    const api = factory();
    if (typeof module === 'object' && module.exports) module.exports = api;
    root.LearningScheduler = api;
})(typeof globalThis !== 'undefined' ? globalThis : this, function () {
    const DAY = 24 * 60 * 60 * 1000;
    const INTERVALS = [0, 1, 3, 7, 14, 30];

    function emptyProgress() {
        return {
            seenCount: 0,
            correctCount: 0,
            wrongCount: 0,
            lastReviewedAt: null,
            nextReviewAt: null,
            level: 0,
            successfulDays: [],
            lastMistakeType: null,
            rescueCount: 0,
            needsParentHelp: false,
            consecutiveWrong: 0
        };
    }

    function normalizeProgress(value) {
        const base = emptyProgress();
        if (!value || typeof value !== 'object') return base;
        if ('streak' in value || 'mastered' in value || 'reviewCount' in value) {
            base.seenCount = Number(value.reviewCount || 0);
            base.correctCount = Number(value.streak || 0);
            base.level = value.mastered ? 3 : Math.min(Number(value.streak || 0), 2);
            base.nextReviewAt = value.mastered ? new Date(Date.now() + 7 * DAY).toISOString() : null;
            return base;
        }
        return {
            ...base,
            ...value,
            seenCount: Number(value.seenCount || 0),
            correctCount: Number(value.correctCount || 0),
            wrongCount: Number(value.wrongCount || 0),
            level: Math.max(0, Math.min(5, Number(value.level || 0))),
            successfulDays: Array.isArray(value.successfulDays) ? value.successfulDays.slice(-10) : [],
            lastMistakeType: value.lastMistakeType || null,
            rescueCount: Number(value.rescueCount || 0),
            needsParentHelp: Boolean(value.needsParentHelp),
            consecutiveWrong: Number(value.consecutiveWrong || 0)
        };
    }

    function dayKey(date) {
        return new Date(date).toISOString().slice(0, 10);
    }

    function recordAnswer(progress, isCorrect, now = new Date(), mistakeType = null) {
        const next = normalizeProgress(progress);
        const nowDate = new Date(now);
        next.seenCount++;
        next.lastReviewedAt = nowDate.toISOString();
        if (isCorrect) {
            next.correctCount++;
            next.level = Math.min(5, next.level + 1);
            if (next.lastMistakeType) next.rescueCount++;
            next.lastMistakeType = null;
            next.consecutiveWrong = 0;
            const key = dayKey(nowDate);
            if (!next.successfulDays.includes(key)) next.successfulDays.push(key);
        } else {
            next.wrongCount++;
            next.level = Math.max(0, next.level - 2);
            next.lastMistakeType = mistakeType || 'meaning';
            next.consecutiveWrong++;
            if (next.consecutiveWrong >= 2) next.needsParentHelp = true;
        }
        const days = isCorrect ? INTERVALS[next.level] : 0;
        next.nextReviewAt = new Date(nowDate.getTime() + days * DAY).toISOString();
        return next;
    }

    function isMastered(progress) {
        const p = normalizeProgress(progress);
        return p.level >= 4 && new Set(p.successfulDays).size >= 3 && p.consecutiveWrong === 0;
    }

    function selectWords(words, progressMap, newCount, reviewCount, now = new Date()) {
        const time = new Date(now).getTime();
        const scored = words.map(word => {
            const p = normalizeProgress(progressMap[word.word]);
            const unseen = p.seenCount === 0;
            const due = !unseen && (!p.nextReviewAt || new Date(p.nextReviewAt).getTime() <= time);
            const errorRate = p.seenCount ? p.wrongCount / p.seenCount : 0;
            return { word, p, unseen, due, score: p.wrongCount * 20 + p.consecutiveWrong * 30 + errorRate * 10 - p.level };
        });
        const reviews = scored.filter(x => !x.unseen && (x.due || x.p.wrongCount > 0))
            .sort((a, b) => b.score - a.score).slice(0, reviewCount).map(x => x.word);
        const newWords = scored.filter(x => x.unseen && x.word.enabled !== false)
            .sort((a, b) => difficultyRank(a.word.difficulty) - difficultyRank(b.word.difficulty))
            .slice(0, newCount).map(x => x.word);
        return shuffle([...reviews, ...newWords]);
    }

    function difficultyRank(value) {
        return ({ basic: 0, advanced: 1, extension: 2 })[value] ?? 1;
    }

    function shuffle(values) {
        const copy = [...values];
        for (let i = copy.length - 1; i > 0; i--) {
            const j = Math.floor(Math.random() * (i + 1));
            [copy[i], copy[j]] = [copy[j], copy[i]];
        }
        return copy;
    }

    function dueCounts(words, progressMap, now = new Date()) {
        const time = new Date(now).getTime();
        return words.reduce((counts, word) => {
            const p = normalizeProgress(progressMap[word.word]);
            if (p.lastMistakeType || p.consecutiveWrong > 0) counts.rescue++;
            if (p.seenCount > 0 && (!p.nextReviewAt || new Date(p.nextReviewAt).getTime() <= time)) counts.due++;
            return counts;
        }, { rescue: 0, due: 0 });
    }

    return { DAY, emptyProgress, normalizeProgress, recordAnswer, isMastered, selectWords, dueCounts, shuffle };
});
