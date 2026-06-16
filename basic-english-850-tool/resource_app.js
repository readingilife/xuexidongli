(function () {
    let wordMap = new Map();
    const sectionMap = {
        'Operations': 'operations',
        'Things — General': 'things-general',
        'Things — Picturable': 'things-picturable',
        'Qualities': 'qualities'
    };

    async function init() {
        try {
            const words = Array.isArray(window.BASIC_ENGLISH_850_DATA)
                ? window.BASIC_ENGLISH_850_DATA
                : await loadJsonWords();
            wordMap = new Map(words.map(item => [item.word, item]));
            renderLists(words);
            initWordElements();
        } catch (error) {
            console.error('词库加载失败', error);
        }
    }

    async function loadJsonWords() {
        const response = await fetch('basic_english_850_data.json', { cache: 'no-store' });
        if (!response.ok) throw new Error(`HTTP ${response.status}`);
        return response.json();
    }

    function renderLists(words) {
        Object.values(sectionMap).forEach(id => {
            const lists = document.querySelectorAll(`#${id} .word-list`);
            lists.forEach((list, index) => {
                if (index > 0) list.remove();
                else list.innerHTML = '';
            });
        });
        words.forEach(item => {
            const id = sectionMap[item.category];
            const list = id && document.querySelector(`#${id} .word-list`);
            if (!list) return;
            const li = document.createElement('li');
            li.textContent = item.word;
            li.dataset.difficulty = item.difficulty;
            list.appendChild(li);
        });
    }

    function initWordElements() {
        document.querySelectorAll('.word-list li').forEach(element => {
            element.tabIndex = 0;
            element.setAttribute('role', 'button');
            const activate = () => {
                const word = wordMap.get(element.textContent.trim());
                if (!word) return;
                pronounce(word);
                showWordInfo(word, element);
            };
            element.addEventListener('click', activate);
            element.addEventListener('keydown', event => {
                if (event.key === 'Enter' || event.key === ' ') activate();
            });
        });
    }

    function showWordInfo(word, element) {
        const card = document.getElementById('wordInfo');
        document.getElementById('infoWord').textContent = word.word;
        document.getElementById('infoPhonetic').textContent = word.phonetic;
        document.getElementById('infoMeaning').textContent = word.childMeaning;
        const rect = element.getBoundingClientRect();
        card.style.left = `${Math.max(16, Math.min(rect.right + 16, window.innerWidth - 316))}px`;
        card.style.top = `${Math.max(16, Math.min(rect.top, window.innerHeight - 200))}px`;
        card.classList.add('show');
    }

    function pronounce(word) {
        const audio = new Audio(word.voice.female);
        audio.play().catch(() => {
            if (!('speechSynthesis' in window)) return;
            const utterance = new SpeechSynthesisUtterance(word.word);
            utterance.lang = 'en-US';
            utterance.rate = 0.9;
            speechSynthesis.speak(utterance);
        });
    }

    window.setActive = element => {
        document.querySelectorAll('.grade-nav a').forEach(link => link.classList.remove('active'));
        element.classList.add('active');
    };
    window.copyLink = () => navigator.clipboard.writeText(window.location.href).then(() => alert('链接已复制！'));
    document.addEventListener('click', event => {
        if (!event.target.closest('.word-list')) document.getElementById('wordInfo').classList.remove('show');
    });
    document.addEventListener('DOMContentLoaded', init);
})();
