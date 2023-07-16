from core import *
import turtle as t

def slow_sort(sorter, l, r, delay):
    if l >= r:
        return
    m = (l+r)//2
    slow_sort(sorter, l, m, delay)
    slow_sort(sorter, m+1, r, delay)
    # if sorter.ls[m] > sorter.ls[r]:
    if sorter.compare(m, r, delay) > 0:
        sorter.swap(m, r, delay)
    slow_sort(sorter, l, r-1, delay)

if __name__ == '__main__':
    sz = 64
    delay = 0
    skip = 16
    slow = Sorter(sz, skip, 'Slow Sort')
    slow.shuffle(delay)
    slow.refresh(True)
    sleep(1)
    slow.resetstatus()
    slow_sort(slow, 0, sz-1, delay)
    slow.resetcolor()
    slow.refresh(True)
    t.mainloop()
