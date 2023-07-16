'''
original source code (std::sort) (remove newlines)

https://github.com/gcc-mirror/gcc/blob/
d9375e490072d1aae73a93949aa158fcd2a27018/
libstdc%2B%2B-v3/include/bits/stl_algo.h#L1867

starts from line 1863 to line 1962

std::__move_median_to_first didn't showed the code so I implemented for myself
'''

from core import *
import turtle as t
import heap
import ins
from math import log2

# basic method: simply sort 3 items and choose middle
def mo3(sorter, l, m, r, delay):
    if sorter.compare(l, m, delay) > 0:
        sorter.swap(l, m, delay)
    if sorter.compare(m, r, delay) > 0:
        sorter.swap(m, r, delay)
    if sorter.compare(l, m, delay) > 0:
        sorter.swap(l, m, delay)

# STL's method: move median to left position (uses this)
def stl_mo3(sorter, l, m, r, delay):
    ls = sorter.ls
    Sorter.cmp += 1
    Q = [ls[l], ls[m], ls[r]]
    if min(Q) == Q[0]:
        if sorter.compare(m, r, delay) < 0:
            sorter.swap(l, m, delay)
        else:
            sorter.swap(l, r, delay)
        return
    elif min(Q) == Q[1]:
        if sorter.compare(l, r, delay) > 0:
            sorter.swap(l, r, delay)
        return
    elif min(Q) == Q[2]:
        if sorter.compare(l, m, delay) > 0:
            sorter.swap(l, m, delay)
        return

def partition(sorter, l, r, delay):
    sorter.resetcolor()
    ls = sorter.ls
    m = (l+r)//2
    stl_mo3(sorter, l, m, r-1, delay)
    piv = ls[l]
    lp, rp = l+1, r
    sorter.highlight(l, 3)
    while 1:
        while ls[lp] < piv:
            lp += 1
            sorter.highlight(lp, 1)
            Sorter.cmp += 1
            Sorter.ops += 1
            sorter.refresh()
            sleep(delay)
        rp -= 1
        while ls[rp] > piv:
            rp -= 1
            sorter.highlight(rp, 2)
            Sorter.cmp += 1
            Sorter.ops += 1
            sorter.refresh()
            sleep(delay)
        if not lp < rp:
            return lp
        sorter.swap(lp, rp, delay)
        lp += 1

def intro_loop(sorter, l, r, depth, delay):
    while r-l > 16:
        if depth == 0:
            sorter.resetcolor()
            heap.heap_sort(sorter, l, r-l, delay)
            return
        depth -= 1
        m = partition(sorter, l, r, delay)
        intro_loop(sorter, m, r, depth, delay)
        r = m

def intro_sort(sorter, l, r, delay):
    depth = int(log2(r-l)) * 2
    intro_loop(sorter, l, r, depth, delay)
    sorter.resetcolor()
    ins.ins_sort(sorter, l, r, delay)

if __name__ == '__main__':
    sz = 400
    delay = 0
    skip = 11
    intro = Sorter(sz, skip, 'STL std::sort')
    # intro.shuffle(delay)
    intro.reverse(0, sz-1, delay)
    intro.refresh(True)
    sleep(1)
    intro.resetstatus()
    intro_sort(intro, 0, sz, delay)
    intro.resetcolor()
    intro.refresh(True)
    t.mainloop()
