from core import *
import turtle as t
import merge

if __name__ == '__main__':
    sz = 400
    delay = 0
    skip = 12
    bmge = Sorter(sz, skip, 'Binary Merge Sort')
    bmge.shuffle(delay)
    # bmge.reverse(0, sz-1, delay)
    bmge.refresh(True)
    sleep(1)
    bmge.resetstatus()
    merge.mergesort(bmge, 0, sz, delay, True)
    bmge.resetcolor()
    bmge.refresh(True)
    t.mainloop()
