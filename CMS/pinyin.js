const pinyinMap = {
    '刘':'liu','品':'pin','延':'yan','北':'bei','京':'jing','师':'shi','范':'fan','大':'da','学':'xue','亚':'ya','太':'tai','实':'shi','验':'yan','7':'7'
};

function toPinyin(text) {
    let result = '';
    for (let char of text) {
        if (pinyinMap[char]) {
            result += pinyinMap[char];
        } else if (/[a-zA-Z0-9]/.test(char)) {
            result += char.toLowerCase();
        }
    }
    return result;
}

function extractGradeNumber(gradeText) {
    const match = gradeText.match(/\d+/);
    return match ? match[0] : '';
}

if (typeof module !== 'undefined') {
    module.exports = { toPinyin, extractGradeNumber };
}
