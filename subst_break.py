import argparse
import string

alphabet = string.ascii_lowercase * 2


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
