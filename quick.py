from core import *
import turtle as t

def partition(sorter, l, r, delay):
    ls = sorter.ls
    col = sorter.col
    piv = (l+r) // 2
    lp, rp = l, r
    while 1:
        sorter.highlight(piv, 3)
        sorter.highlight(rp, 2)
        ptr_moved = False
        while ls[lp] < ls[piv]:
            lp += 1
            Sorter.cmp += 1
            Sorter.ops += 1
            sorter.highlight(lp, 1)
            sorter.refresh()
            sleep(delay)
            ptr_moved = True
        if not ptr_moved:
            Sorter.cmp += 1
            Sorter.ops += 1
            sorter.refresh()
        ptr_moved = False
        while ls[rp] > ls[piv]:
            rp -= 1
            Sorter.cmp += 1
            Sorter.ops += 1
            sorter.highlight(rp, 2)
            sorter.refresh()
            sleep(delay)
        if not ptr_moved:
            Sorter.cmp += 1
            Sorter.ops += 1
            sorter.refresh()
        if lp >= rp:
            return rp
        sorter.swap(lp, rp, delay)
        if piv == lp: piv = rp
        elif piv == rp: piv = lp
        lp += 1
        rp -= 1

def quick_sort(sorter, l, r, delay):
    if r-l < 2:
        return
    else:
        m = partition(sorter, l, r, delay)
        quick_sort(sorter, l, m, delay)
        quick_sort(sorter, m, r, delay)

if __name__ == '__main__':
    sz = 400
    delay = 0
    skip = 11
    quick = Sorter(sz, skip, 'Quick Sort')
    quick.shuffle(delay)
    # quick.reverse(0, sz-1, delay)
    quick.refresh(True)
    sleep(1)
    quick.resetstatus()
    quick_sort(quick, 0, sz-1, delay)
    quick.resetcolor()
    quick.refresh(True)
    t.mainloop()
    
