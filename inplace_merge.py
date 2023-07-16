from core import *
import turtle as t

sz = 400
delay = 0
skip = 72
imge = Sorter(sz, skip, 'In-Place Merge Sort')
imge.shuffle(delay)
# imge.reverse(0, sz-1, delay)
imge.refresh(True)
sleep(1)
imge.resetstatus()

def merge(sorter, l, m, r, delay):
    lp = l
    while lp < m:
        if sorter.compare(lp, m, delay) > 0:
            sorter.swap(lp, m, delay)
            for i in range(m, r-1):
                Sorter.cmp += 1
                if sorter.ls[i] > sorter.ls[i+1]:
                    sorter.swap(i, i+1, delay)
                else:
                    break
        lp += 1

def mergesort(sorter, l, r, delay):
    if r-l < 2:
        return
    m = (l+r)//2
    mergesort(sorter, l, m, delay)
    mergesort(sorter, m, r, delay)
    merge(sorter, l, m, r, delay)

mergesort(imge, 0, sz, delay)
imge.resetcolor()
imge.refresh(True)
t.mainloop()

