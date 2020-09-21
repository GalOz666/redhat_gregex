import sys

from matchers import StringMatcher, FileMatcher
import argparse

parser = argparse.ArgumentParser()

parser.add_argument('-r', '--regex', help="regex expression for searching")
parser.add_argument('-f', '--files', help="list of files to search in")

# mutually exclusive:
parser.add_argument('-u', '--underline', help="print matches with '^' underneath them")
parser.add_argument('-c', '--color', help="print colored matches")
parser.add_argument('-m', '--machine', help="print matches with 'print the output in the format:"
                                            "\n'file_name:line_number:start_position:matched_text'")

args = parser.parse_args()


def main():
    if not args.regex:
        print("please provide a regex pattern!")

    if args.files:
        matchers = [FileMatcher(file) for file in args.files.split()]
    else:
        matchers = StringMatcher(sys.argv[-1])


