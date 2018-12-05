import argparse
import string
import re

alphabet = string.ascii_lowercase * 2
non_words_regex = re.compile('[^a-zA-Z\s]')


def decode_string(encoded_string, shift):
    decoded_string = ''

    for letter in encoded_string:
        lowered_letter = letter.lower()

        is_letter_capped = lowered_letter != letter

        if lowered_letter in alphabet:
            decoded_letter = alphabet[alphabet.index(lowered_letter) + shift]
            if is_letter_capped:
                decoded_string += decoded_letter.upper()
            else:
                decoded_string += decoded_letter
        else:
            decoded_string += letter
    return decoded_string


def get_translation_score(translation):
    score = 0
    # First parameter is the replacement, second parameter is your input string
    translation = non_words_regex.sub('', translation)
    translation_words = translation.split(' ')

    for word in translation_words:
        if word.lower() in words_set or word in words_set:
            score += 1
    return score


parser = argparse.ArgumentParser(description='Tries to decode the encoded string by trying every combinaison in the '
                                             'latin alphabet range.')


parser.add_argument('dictionary_path', type=str,
                    help='path of a dictionary of words in the original language of the encoded string')
parser.add_argument('encoded_string', type=str,
                    help='a string encoded in cesar that you\'d like to decode')

args = parser.parse_args()

print(args.encoded_string, args.dictionary_path)

words_set = set()
try:
    for line in open(args.dictionary_path, 'r'):
        line = line.strip()
        words_set.add(line)
except FileNotFoundError:
    print("There is no dictionary at " + args.dictionary_path + ". Please pass a valid file path for the program to "
                                                                "function.")
    exit()

for i in range(0, 26):
    possible_translation = decode_string(args.encoded_string, i)
    print(possible_translation)
    translation_score = get_translation_score(possible_translation)
    print(translation_score)
