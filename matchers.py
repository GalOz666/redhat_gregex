import os
from abc import ABC, abstractmethod
import re
from typing import Iterable

GREEN_COLOR = '\033[92m'
END_STYLE = '\x1b[0m'


class BaseMatcherMeta(ABC):

    def print_color(self):
        for match in self.line_dict.values():
            match_list = list(match)
            match_str_list = list(match_list[0].string)
            match_start_ends = [(m.start(), m.end()) for m in match_list]
            for start, end in match_start_ends:
                match_str_list[start:start] = GREEN_COLOR
                match_str_list[end:end] = END_STYLE
            print(str(match_str_list))

    def print_machine(self, file: str):
        for line_num, match in self.line_dict.items():
            for m in match:
                print(f'{file}:{line_num}:{m.string[m.start():m.end()]}')

    def print_with_caret(self):
        for match in self.line_dict.values():
            line = list(match)[0].string
            caret_line = list(" "*len(line))
            for m in match:
                caret_line[m.start():m.start()+1] = "^"
            print(line)
            print(str(caret_line))

    def print_normal(self):
        for line_match in self.line_dict.values:
            print(list(line_match)[0].string)

    @property
    @abstractmethod
    def line_dict(self) -> {int: Iterable[re.Match]}:
        pass


class StringMatcher(BaseMatcherMeta):

    def __init__(self, string: str, regex: str):
        self.string = string
        self.regex = regex
        self.file = "STDIN"

    @property
    def line_dict(self):
        l_dict = dict()
        for idx, line in enumerate(self.string.split('\n')):
            result = re.finditer(self.regex, line)
            if len(list(result)):
                l_dict[idx] = result
        return l_dict


class FileMatcher(BaseMatcherMeta):

    def __init__(self, file: str, regex: str):
        if os.path.isfile(file):
            self.file = file
        else:
            raise FileNotFoundError(f"Cannot find file {file}")
        self.regex = regex

    @property
    def line_dict(self):
        l_dict = dict()
        with open(self.file) as f:
            for idx, line in enumerate(f):
                result = re.finditer(self.regex, line)
                if len(list(result)):
                    l_dict[idx] = result
        return l_dict
