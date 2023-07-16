from core import *
import turtle as t

def combsort(sorter, sz, shrink):
    gap = sz
    while 1:
        swapped = False
        if gap > 1:
            gap = int(gap/shrink)
        for i in range(sz-gap):
            if sorter.compare(i, i+gap, delay) > 0:
                sorter.swap(i, i+gap, delay)
                swapped = True
        if not swapped:
            return

if __name__ == '__main__':
    sz = 400
    delay = 0
    skip = 16
    comb = Sorter(sz, skip, 'Comb Sort')
    comb.shuffle(delay)
    comb.refresh(True)
    sleep(1)
    comb.resetstatus()
    combsort(comb, sz, 1.3)
    comb.resetcolor()
    comb.refresh(True)
    t.mainloop()
