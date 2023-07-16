from core import *
import turtle as t

sz = 8
delay = 0
skip = 111
bogo = Sorter(sz, skip, 'Bogo Sort')
bogo.shuffle(delay)
bogo.refresh(True)
sleep(1)
bogo.resetstatus()

def is_sorted(sorter, sz):
    ls = sorter.ls
    res = True
    for i in range(sz-1):
        Sorter.cmp += 1
        Sorter.ops += 1
        if ls[i] > ls[i+1]:
            res = False
            break
    sorter.highlight(sz-1, 1)
    bogo.refresh()
    return res

def bogoshuffle(sorter, sz):
    ls = sorter.ls
    for i in range(sz):
        pick = randint(i, sz-1)
        ls[i], ls[pick] = ls[pick], ls[i]
    Sorter.wri += 2*sz
    Sorter.ops += sz

def bogosort(sorter, sz, delay):
    while not is_sorted(bogo, sz):
        bogoshuffle(sorter, sz)
        sorter.refresh()
        sleep(delay)

bogosort(bogo, sz, delay)
bogo.resetcolor()
bogo.refresh(True)
t.mainloop()
