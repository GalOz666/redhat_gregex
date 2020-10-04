import sys

from matchers import StringMatcher, FileMatcher
import argparse

parser = argparse.ArgumentParser()

parser.add_argument('-r', '--regex', help="regex expression for searching")
parser.add_argument('-f', '--files', nargs="+", help="list of files to search in. If not used simply provide "
                                                     "a string surrounded by quotation marks as the final "
                                                     "argument to the script")

# mutually exclusive:
parser.add_argument('-u', '--underline', action='store_true', help="print matches with '^' underneath them")
parser.add_argument('-c', '--color', action='store_true', help="print colored matches")
parser.add_argument('-m', '--machine', action='store_true',
                    help="print matches with 'print the output in the format:"
                         " \n'file_name:line_number:start_position:matched_text'")

args, _ = parser.parse_known_args()


def main():
    if not args.regex:
        print("please provide a regex pattern!")

    if args.files:
        matchers = [FileMatcher(file, args.regex) for file in args.files]
    else:
        matchers = [StringMatcher(sys.argv[-1], args.regex)]

    if args.underline:
        [m.print_with_caret() for m in matchers]
    elif args.color:
        [m.print_color() for m in matchers]
    elif args.machine:
        [m.print_machine() for m in matchers]
    else:
        [m.print_normal() for m in matchers]


if __name__ == "__main__":
    main()
