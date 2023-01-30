import time
import module


def test_submit():
    module.open_page('/puzzle/triangle')
    module.submit()

    module.clear_data()

    module.set_data(b=3)
    module.submit()
    
    module.clear_data()

    module.set_data(a='where')
    module.submit()
    
    module.clear_data()

    module.set_data(a='<script>')
    module.submit()
    
    module.clear_data()

    module.set_data(a='<SCRIPT>')
    module.submit()
    
    module.clear_data()

    list_a = (3, 2, 66, 3, 6, 2, 'q', 2147483647, 0, 2.2)
    list_b = (4, 3, 67, 3, 6, 3, 'w', 4294967295, 0, 4)
    list_c = (5, 4, 68, 5, 6, 10, 'e', 4294967295, 0, 5)
    module.set_big_data(list_a, list_b, list_c)
    time.sleep(20)
