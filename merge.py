from core import *
import turtle as t
import bins

def merge(sorter, l, m, r, delay):
    lp, rp = l, m
    ls = sorter.ls
    col = sorter.col
    aux = []
    for _ in range(r-l):
        if lp >= m:
            aux.append(ls[rp])
            sorter.highlight(m-1, 1)
            sorter.highlight(rp, 2)
            Sorter.aux_wri += 1
            Sorter.ops += 1
            sorter.refresh()
            sleep(delay)
            rp += 1

        elif rp >= r:
            aux.append(ls[lp])
            sorter.highlight(r-1, 1)
            sorter.highlight(lp, 2)
            Sorter.aux_wri += 1
            Sorter.ops += 1
            sorter.refresh()
            sleep(delay)
            lp += 1

        else:
            Sorter.aux_wri += 1
            res = sorter.compare(lp, rp, delay)
            if res <= 0:
                aux.append(ls[lp])
                lp += 1
            else:
                aux.append(ls[rp])
                rp += 1

    sorter.highlight(-1, 2)
    for i in range(r-l):
        sorter.write(i+l, aux[i], delay)

def mergesort(sorter, l, r, delay, binary=False):
    if r-l < 2:
        return
    elif r-l < 48 and binary:
        bins.bins_sort(sorter, l, r-l, delay)
        return
    m = (l+r)//2
    mergesort(sorter, l, m, delay, binary)
    mergesort(sorter, m, r, delay, binary)
    merge(sorter, l, m, r, delay)

if __name__ == '__main__':
    sz = 400
    delay = 0
    skip = 12
    mge = Sorter(sz, skip, 'Merge Sort')
    mge.shuffle(delay)
    # mge.reverse(0, sz-1, delay)
    mge.refresh(True)
    sleep(1)
    mge.resetstatus()
    mergesort(mge, 0, sz, delay)
    mge.resetcolor()
    mge.refresh(True)
    t.mainloop()
