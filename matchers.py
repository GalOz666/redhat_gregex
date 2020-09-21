from abc import ABC, abstractmethod


class BaseMatcherMeta(ABC):

    def print_color(self):
        pass

    def print_verbose_path(self):
        pass

    def print_with_carret(self):
        pass

    def print_normal(self):
        pass

    @property
    @abstractmethod
    def line_dict(self):
        pass


class StringMatcher:
    pass


class FileMatcher:
    pass
