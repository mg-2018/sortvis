from core import *
import turtle as t

if __name__ == '__main__':
    sz = 400
    delay = 0
    skip = 72
    sel = Sorter(sz, skip, 'Selection Sort')
    sel.refresh()
    sel.shuffle(delay)
    sel.refresh(True)
    sleep(1)
    sel.resetstatus()
    for i in range(sz):
        min = i
        for j in range(i+1, sz):
            if sel.compare(min, j, delay) > 0:
                min = j
        if i < sz-1:
            sel.swap(i, min, delay)
    sel.resetcolor()
    sel.refresh(True)
    t.mainloop()
