import os
from abc import ABC, abstractmethod
import re


class BaseMatcherMeta(ABC):

    def print_color(self):
        pass

    def print_verbose_path(self):
        pass

    def print_with_caret(self):
        pass

    def print_normal(self):
        pass

    @property
    @abstractmethod
    def line_dict(self) -> dict:
        pass


class StringMatcher(BaseMatcherMeta):

    def __init__(self, string: str, regex):
        self.string = string
        self.regex = regex

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

