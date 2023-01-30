import time
import module
from itertools import product


def test_submit():
    module.open_page('/puzzle/triangle')

    module.submit()
    time.sleep(2)


def test_field():
    module.open_page('/puzzle/triangle')

    module.set_data(b=3)

    module.submit()
    time.sleep(2)


def test_set_sql():
    module.open_page('/puzzle/triangle')

    module.set_data(a='where')

    module.submit()
    time.sleep(2)


def test_set_xss():
    module.open_page('/puzzle/triangle')

    module.set_data(a='<script>')

    module.submit()
    time.sleep(2)


def test_set_upload_xss():
    module.open_page('/puzzle/triangle')

    module.set_data(a='<SCRIPT>')

    module.submit()
    time.sleep(2)


list_a = [3, 2, 66, 3, 6, 2, 'q', 2147483647, 0, 2.2]
list_b = [4, 3, 67, 3, 6, 3, 'w', 4294967295, 0, 4]
list_c = [5, 4, 68, 5, 6, 10, 'e', 4294967295, 0, 5]


def test_right_triangle(arg_a, arg_b, arg_c):
    for a, b, c in zip(arg_a, arg_b, arg_c):
        module.open_page('/puzzle/triangle')
        module.set_data(a=a, b=b, c=c)

        module.submit()
        time.sleep(2)

