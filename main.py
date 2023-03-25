from checker import NorvigSpellChecker


def main():
    checker = NorvigSpellChecker(mt_phone=True)
    text = 'Speling Errurs IN somethink. Whutever; unusuel misteakes? Fantomas World.'
    print(text)
    print(checker.correct_text(text))
    text = 'The show eeneashiallea struggles to asstubleash a tone, but the premise is interesting enuff to make it worth ' \
           'sticking with.'
    print(text)
    print(checker.correct_text(text))


if __name__ == '__main__':
    main()
