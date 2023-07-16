from core import *
import turtle as t

def bsearch(sorter, start, sz, key, delay):
    tmp = sorter.skip
    bsearch_delay = delay
    if __name__ == '__main__':
        bsearch_delay = 0.04 if sorter.sz <= 128 else delay
        if sz <= 200:
            sorter.skip = 1
    ls = sorter.ls
    col = sorter.col
    l, r = start, sz
    while r-l >= 2:
        Sorter.cmp += 1
        Sorter.ops += 1
        sorter.highlight(l, 1)
        sorter.highlight(r, 2)
        sorter.refresh()
        sleep(bsearch_delay)
        m = (l+r)//2
        if key >= ls[m]:
            l = m
        else:
            r = m
    Sorter.cmp += 1
    Sorter.ops += 1
    sorter.highlight(l, 1)
    sorter.highlight(r, 2)
    sorter.refresh()
    sleep(bsearch_delay)
    if __name__ == '__main__':
        sorter.skip = tmp
    if key < ls[l]:
        return l
    else:
        return r

def bins_sort(sorter, start, sz, delay):
    ls = sorter.ls
    for i in range(1, sz):
        if i == 1:
            if sorter.compare(start, start+1, delay) > 0:
                tmp = ls[start+1]
                sorter.write(start+1, ls[start], delay)
                sorter.write(start, tmp, delay)
            continue
        pos = bsearch(sorter, start, start+i, ls[start+i], delay)
        tmp = sorter.ls[start+i]
        sorter.highlight(pos, 2)
        for j in range(start+i, pos, -1):
            sorter.write(j, ls[j-1], delay)
        sorter.write(pos, tmp, delay)

if __name__ == '__main__':
    sz = 128
    delay = 0
    skip = 8
    bins = Sorter(sz, skip, 'Binary Insertion Sort')
    bins.shuffle(delay)
    bins.refresh(True)
    sleep(1)
    bins.resetstatus()
    bins_sort(bins, 0, sz, delay)
    bins.resetcolor()
    bins.refresh(True)
    t.mainloop()

