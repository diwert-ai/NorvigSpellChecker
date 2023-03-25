from requests import get
from re import findall, sub
from random import choice
from collections import Counter
from metaphone import doublemetaphone


class NorvigSpellChecker:
    text_url = 'https://norvig.com/big.txt'

    def __init__(self, mt_phone=False):
        self.mt_phone = mt_phone
        self.text = get(self.text_url).text
        self.words = self.tokens(self.text)
        self.counts = Counter(self.words)
        self.mp_dict = self.create_mp_dict() if self.mt_phone else None
        print(f'NorvigSpellChecker init: size of text: {len(self.text)}, num of words: {len(self.words)}')
        print(f'3 most common words: {self.counts.most_common(3)}')

    def create_mp_dict(self):
        mp_dict = dict()
        for word in self.counts:
            mp = doublemetaphone(word)[0]
            mp_dict[mp].append(word) if mp in mp_dict else mp_dict.update({mp: [word]})
        return mp_dict

    @staticmethod
    def tokens(text):
        return findall(r'[a-z]+', text.lower())

    @staticmethod
    def sample(bag, n=10):
        return ' '.join(choice(bag) for _ in range(n))

    def correct(self, word):
        known_tail = self.mp_dict.get(doublemetaphone(word)[0], [word]) if self.mt_phone else [word]
        candidates = (self.known(self.edits0(word)) or
                      self.known(self.edits1(word)) or
                      self.known(self.edits2(word)) or
                      known_tail)
        return max(candidates, key=self.counts.get)

    def known(self, words):
        return {w for w in words if w in self.counts}

    @staticmethod
    def edits0(word):
        return {word}

    def edits1(self, word, alphabet='abcdefghijklmnopqrstuvwxyz'):
        pairs = self.splits(word)
        deletes = [a + b[1:] for (a, b) in pairs if b]
        transposes = [a + b[1] + b[0] + b[2:] for (a, b) in pairs if len(b) > 1]
        replaces = [a + c + b[1:] for (a, b) in pairs for c in alphabet if b]
        inserts = [a + c + b for (a, b) in pairs for c in alphabet]
        return set(deletes + transposes + replaces + inserts)

    def edits2(self, word):
        return {e2 for e1 in self.edits1(word) for e2 in self.edits1(e1)}

    @staticmethod
    def splits(word):
        return [(word[:i], word[i:]) for i in range(len(word) + 1)]

    def correct_text(self, text):
        return sub('[a-zA-Z]+', self.correct_match, text)

    def correct_match(self, match):
        word = match.group()
        return self.case_of(word)(self.correct(word.lower()))

    @staticmethod
    def case_of(text):
        return (str.upper if text.isupper() else
                str.lower if text.islower() else
                str.title if text.istitle() else
                str)





