from core import *
import turtle as t

def stooge_sort(sorter, l, r, delay):
    ls = sorter.ls
    if sorter.compare(l, r, delay) > 0:
        sorter.swap(l, r, delay)
    if (r-l + 1) > 2:
        t = (r-l + 1)//3
        stooge_sort(sorter, l, r-t, delay)
        stooge_sort(sorter, l+t, r, delay)
        stooge_sort(sorter, l, r-t, delay)

if __name__ == '__main__':
    sz = 64
    delay = 0
    skip = 16
    stooge = Sorter(sz, skip, 'Stooge Sort')
    stooge.shuffle(delay)
    stooge.refresh(True)
    sleep(1)
    stooge.resetstatus()
    stooge_sort(stooge, 0, sz-1, delay)
    stooge.resetcolor()
    stooge.refresh(True)
    t.mainloop()
