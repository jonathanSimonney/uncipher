import argparse


parser = argparse.ArgumentParser(description='Tries to decode the encoded string by trying every combinaison in the latin alphabet range.')


parser.add_argument('dictionary_path', type=str,
                    help='path of a dictionary of words in the original language of the encoded string')
parser.add_argument('encoded_string', type=str,
                    help='a string encoded in cesar that you\'d like to decode')

args = parser.parse_args()

print(args.encoded_string, args.dictionary_path)
