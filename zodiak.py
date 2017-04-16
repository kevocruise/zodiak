import enchant
import random


lexicon = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
          'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def apply_lexicon_to_message(message):
    lex_message = ''
    addressed = {}
    for symbol in message:
        if symbol not in addressed:
            addressed[symbol] = random.choice(lexicon)

        lex_message = f'{lex_message}{addressed[symbol]}'

    return lex_message


def zodiak(message, language='en_US'):
    dictionary = enchant.Dict(language)

    count = 0
    while True:
        count += 1

        # Tokenize the message into letters
        lex_message = apply_lexicon_to_message(message)
        if dictionary.check(lex_message):
            break

    return lex_message


def main():
    message = ['square', 'circle', 'triangle', 'triangle', 'diamond', 'kitten']
    print(zodiak(message))

if __name__ == '__main__':
    main()
