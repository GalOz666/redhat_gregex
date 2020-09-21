from matchers import FileMatcher, StringMatcher

file = 'lorem.txt'
a = FileMatcher(file, 'ut')
b = StringMatcher('Ut enim ad minim veniam, \n'
                  'quis nostrud exercitation ullamco laboris nisi ut \n'
                  'aliquip ex ea commodo consequat.', 'ut')


def test_normal():
    c = a.line_dict
    assert len(c) == 3
    a.print_normal(file=a.file)
    b.print_normal(file=b.file)


def test_file_color():
    a.print_color()
    b.print_color()


def test_carret():
    a.print_with_caret()
    b.print_with_caret()


def test_machine():
    a.print_machine(file=a.file)
    b.print_machine(file=b.file)
