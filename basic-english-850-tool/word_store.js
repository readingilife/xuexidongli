(function (root) {
    const DATA_URL = 'basic_english_850_data.json';
    const PROGRESS_KEY = 'basicEnglish850_progress_v2';
    const LEGACY_PROGRESS_KEY = 'basicEnglish850_progress';
    const PLAN_KEY = 'basicEnglish850_plan';

    async function loadWords() {
        let words = Array.isArray(root.BASIC_ENGLISH_850_DATA) ? root.BASIC_ENGLISH_850_DATA : null;
        if (!words) {
            try {
                const response = await fetch(DATA_URL, { cache: 'no-store' });
                if (!response.ok) throw new Error(`词库加载失败（${response.status}）`);
                words = await response.json();
            } catch (error) {
                throw new Error('词库加载失败：请检查 basic_english_850_data.js 是否存在，或通过本地网站打开本页面');
            }
        }
        if (!Array.isArray(words) || words.length < 800) throw new Error('词库格式不完整');
        return words.filter(word => word.enabled !== false);
    }

    function safeRead(key, fallback) {
        const raw = localStorage.getItem(key);
        if (!raw) return fallback;
        try {
            return JSON.parse(raw);
        } catch (error) {
            localStorage.setItem(`${key}_broken_${Date.now()}`, raw);
            localStorage.removeItem(key);
            return fallback;
        }
    }

    function loadProgress() {
        const current = safeRead(PROGRESS_KEY, null);
        if (current) return current;
        const legacy = safeRead(LEGACY_PROGRESS_KEY, {});
        const migrated = {};
        Object.entries(legacy).forEach(([word, value]) => {
            migrated[word] = LearningScheduler.normalizeProgress(value);
        });
        saveProgress(migrated);
        return migrated;
    }

    function saveProgress(progress) {
        localStorage.setItem(PROGRESS_KEY, JSON.stringify(progress));
    }

    function loadPlan() {
        const plan = safeRead(PLAN_KEY, {});
        return {
            newCount: clamp(plan.newCount, 1, 20, 5),
            reviewCount: clamp(plan.reviewCount, 0, 30, 10)
        };
    }

    function savePlan(plan) {
        localStorage.setItem(PLAN_KEY, JSON.stringify(plan));
    }

    function clamp(value, min, max, fallback) {
        const number = Number(value);
        return Number.isFinite(number) ? Math.max(min, Math.min(max, number)) : fallback;
    }

    root.WordStore = { loadWords, loadProgress, saveProgress, loadPlan, savePlan };
})(typeof globalThis !== 'undefined' ? globalThis : this);
