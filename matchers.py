import copy
import os
from abc import ABC, abstractmethod
import re
from typing import Iterable, List

RED_COLOR = '\033[91m'
END_STYLE = '\033[0m'

# I am implementing an abstract class for either File or String operations.
# I'm using ABCs as these give us more rigid enforcing of our concrete class structures.
# They will share most printing options as they will both organize their results in 'line_dict' type.
# The main difference is how to get this dictionary, which will be left to each concrete class.
# These classes will then be used in the main module and each function will match a different argument from the shell


class BaseMatcherMeta(ABC):

    def print_color(self):
        for match in self.line_dict.values():
            match_str_list = list(match[0].string)
            match_start_ends = [(m.start(), m.end()) for m in match]
            for start, end in match_start_ends:
                match_str_list[start:start] = RED_COLOR
                match_str_list[end:end] = END_STYLE
            print("".join(match_str_list))

    def print_machine(self):
        for line_num, match in self.line_dict.items():
            for m in match:
                print(f'{self.file}:{line_num}:{m.start()}:{m.string[m.start():m.end()]}')

    def print_with_caret(self):
        for match in self.line_dict.values():
            line = match[0].string
            caret_line = list(" "*len(list(line)))
            for m in match:
                caret_line[m.start():m.start()+1] = "^"
            print(line)
            print("".join(caret_line))
            print('\n')

    def print_normal(self):
        for line_num, match in self.line_dict.items():
            m = match[0]
            print(f'{self.file} {line_num} {m.string}')

    @property
    @abstractmethod
    def line_dict(self) -> {int: List[re.Match]}:
        pass

    @property
    @abstractmethod
    def file(self) -> str:
        pass


class StringMatcher(BaseMatcherMeta):

    def __init__(self, string: str, regex: str):
        self.string = string
        self.regex = regex

    @property
    def file(self):
        return 'STDIN'

    @property
    def line_dict(self):
        l_dict = dict()
        for idx, line in enumerate(self.string.split('\n')):
            result = list(re.finditer(self.regex, line))
            if len(result):
                l_dict[idx] = result
        return l_dict


class FileMatcher(BaseMatcherMeta):

    def __init__(self, file: str, regex: str):
        if os.path.isfile(file):
            self._file = file
        else:
            raise FileNotFoundError(f"Cannot find file {file}")
        self.regex = regex

    @property
    def line_dict(self):
        l_dict = dict()
        with open(self.file) as f:
            for idx, line in enumerate(f):
                result = list(re.finditer(self.regex, line))
                if len(result):
                    l_dict[idx+1] = result
        return l_dict

    @property
    def file(self):
        return self._file
