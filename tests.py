# ref1: https://www.kaggle.com/datasets/bittlingmayer/spelling?select=spell-testset2.txt
# ref2: https://www.kaggle.com/code/bittlingmayer/spell-py/script

from checker import NorvigSpellChecker


def spell_test(tests, verbose=False):
    import time
    start = time.time()
    good, unknown = 0, 0
    n = len(tests)
    for right, wrong in tests:
        w = checker.correct(wrong)
        good += (w == right)
        if w != right:
            unknown += (right not in checker.words)
            if verbose:
                print('correction({}) => {} ({}); expected {} ({})'
                      .format(wrong, w, checker.words[w], right, checker.words[right]))
    dt = time.time() - start
    print('{:.0%} of {} correct ({:.0%} unknown) at {:.0f} words per second '
          .format(good / n, n, unknown / n, n / dt))


def test_set(lines):
    return [(right, wrong)
            for (right, wrongs) in (line.split(':') for line in lines)
            for wrong in wrongs.split()]


def test_corpus(filename):
    print("Testing " + filename)
    spell_test(test_set(open('datasets/' + filename)))


if __name__ == '__main__':
    checker = NorvigSpellChecker()
    test_corpus('spell-testset1.txt')  # Development set
    test_corpus('spell-testset2.txt')  # Final test set
    # Supplementary sets
    test_corpus('wikipedia.txt')
    test_corpus('aspell.txt')
    checker = NorvigSpellChecker(mt_phone=True)
    test_corpus('spell-testset1.txt')  # Development set
    test_corpus('spell-testset2.txt')  # Final test set
    # Supplementary sets
    test_corpus('wikipedia.txt')
    test_corpus('aspell.txt')
