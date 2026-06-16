#!/usr/bin/env python3
import json
import subprocess
from pathlib import Path

BASE = Path(__file__).resolve().parent


def test_data():
    subprocess.run(["python3", str(BASE / "validate_word_data.py")], check=True)


def test_scheduler():
    script = r"""
const s = require('./learning_scheduler.js');
const day1 = new Date('2026-01-01T00:00:00Z');
let p = s.recordAnswer(s.emptyProgress(), true, day1);
p = s.recordAnswer(p, true, day1);
if (s.isMastered(p)) throw new Error('same-day answers must not master a word');
p = s.recordAnswer(p, true, new Date('2026-01-04T00:00:00Z'));
p = s.recordAnswer(p, true, new Date('2026-01-12T00:00:00Z'));
if (!s.isMastered(p)) throw new Error('cross-day reviews should master a word');
const wrong = s.recordAnswer(p, false, new Date('2026-01-13T00:00:00Z'));
if (wrong.level >= p.level || new Date(wrong.nextReviewAt).getTime() > new Date(wrong.lastReviewedAt).getTime()) {
  throw new Error('wrong answer must lower level and become due now');
}
let spellingWrong = s.recordAnswer(s.emptyProgress(), false, new Date('2026-01-13T00:00:00Z'), 'spelling');
if (spellingWrong.lastMistakeType !== 'spelling') throw new Error('mistake type must be recorded');
spellingWrong = s.recordAnswer(spellingWrong, false, new Date('2026-01-13T00:05:00Z'), 'spelling');
if (!spellingWrong.needsParentHelp) throw new Error('repeated wrong answers should request parent help');
const rescued = s.recordAnswer(spellingWrong, true, new Date('2026-01-14T00:00:00Z'));
if (rescued.lastMistakeType !== null || rescued.rescueCount < 1) throw new Error('correct retry should rescue the word');
const words = [{word:'new',difficulty:'basic'},{word:'wrong',difficulty:'basic'}];
const selected = s.selectWords(words, {wrong}, 1, 1, new Date('2026-01-13T00:00:00Z'));
if (!selected.some(x => x.word === 'wrong')) throw new Error('wrong word must be reviewed');
const counts = s.dueCounts(words, {wrong}, new Date('2026-01-13T00:00:00Z'));
if (counts.rescue < 1 || counts.due < 1) throw new Error('dueCounts should expose rescue and due words');
"""
    subprocess.run(["node", "-e", script], cwd=BASE, check=True)


if __name__ == "__main__":
    test_data()
    test_scheduler()
    print("learning tests passed")
