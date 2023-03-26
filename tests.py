# ref1: https://www.kaggle.com/datasets/bittlingmayer/spelling?select=spell-testset2.txt
# ref2: https://www.kaggle.com/code/bittlingmayer/spell-py/script

from checker import NorvigSpellChecker


def spell_test(tests, checker, verbose=False):
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


def test_corpus(filename, checker):
    print("Testing " + filename)
    spell_test(test_set(open('datasets/' + filename)), checker)


if __name__ == '__main__':
    datasets = ['spell-testset1.txt', 'spell-testset2.txt', 'wikipedia.txt', 'aspell.txt', 'birkbeck.txt']
    checkers = [NorvigSpellChecker(), NorvigSpellChecker(mt_phone=True)]
    for test_checker in checkers:
        for ds_filename in datasets:
            test_corpus(ds_filename, test_checker)
