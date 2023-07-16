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

def radix_sort_lsd(sorter, sz, base, delay):
    depth = get_max_depth(sorter, sz, base, delay)
    ls = sorter.ls
    sub_radix = 1
    for _ in range(depth):
        aux = [[] for _ in range(base)]
        for i in range(sz):
            r = ls[i]//sub_radix % base
            aux[r].append(ls[i])
            sorter.highlight(i, 1)
            Sorter.aux_wri += 1
            Sorter.ops += 1
            sorter.refresh()
            sleep(delay)
        i = 0
        for single in aux:
            for n in single:
                sorter.write(i, n, delay)
                i += 1
        sub_radix *= base

if __name__ == '__main__':
    sz = 128
    delay = 0
    skip = 1
    lsd = Sorter(sz, skip, 'LSD Radix Sort')
    try:
        base = int(t.numinput('Setup', 'Enter base of this sort:', 4, 2, sz))
    except:
        base = 4
    lsd.shuffle(delay)
    lsd.refresh(True)
    sleep(1)
    lsd.resetstatus()
    radix_sort_lsd(lsd, sz, base, delay)
    lsd.resetcolor()
    lsd.refresh(True)
    t.mainloop()
    