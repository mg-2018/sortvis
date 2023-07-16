from core import *
import turtle as t
import math

def get_max_depth(sorter, sz, base, delay):
    M = -1
    ls = sorter.ls
    for i in range(sz):
        sorter.highlight(i, 1)
        Sorter.ops += 1
        sorter.refresh()
        sleep(delay)
        if M < ls[i]:
            M = ls[i]
    sorter.resetcolor()
    sorter.refresh()
    sleep(delay)
    return int(math.log(M)/math.log(base))+1 if M>0 else 1

def radix_sort_msd(sorter, l, r, base, depth, delay):
    if depth == 0:
        return
    ls = sorter.ls
    sorter.highlight(l, 2)
    sorter.highlight(r, 3)
    aux = [[] for _ in range(base)]
    sub_radix = base**(depth-1)
    prefix = [0 for _ in range(base+1)]
    prefix[0] = l
    for i in range(l, r+1):
        n = ls[i]//sub_radix % base
        prefix[n+1] += 1
        aux[n].append(ls[i])
        sorter.highlight(i, 1)
        Sorter.aux_wri += 1
        Sorter.ops += 1
        sorter.refresh()
        sleep(delay)
    for i in range(1, base+1):
        prefix[i] += prefix[i-1]
    i = l
    for single in aux:
        for n in single:
            sorter.write(i, n, delay)
            i += 1
    for i in range(1, base+1):
        radix_sort_msd(sorter, prefix[i-1], prefix[i]-1, base, depth-1, delay)

if __name__ == '__main__':
    sz = 128
    delay = 0
    skip = 1
    msd = Sorter(sz, skip, 'MSD Radix Sort')
    try:
        base = int(t.numinput('Setup', 'Enter base of this sort:', 4, 2, sz))
    except:
        base = 4
    msd.shuffle(delay)
    msd.refresh(True)
    sleep(1)
    msd.resetstatus()
    depth = get_max_depth(msd, sz, base, delay)
    radix_sort_msd(msd, 0, sz-1, base, depth, delay)
    msd.resetcolor()
    msd.refresh(True)
    t.mainloop()
    