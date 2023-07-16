from core import *
import turtle as t
import ins

# gap sequence generator
def gap(sz):
    ls = [1577, 701, 301, 132, 57, 23, 10, 4, 1]
    for n in ls:
        yield n

def shell_sort(sorter, sz, delay):
    for n in gap(sz):
        if n == 1:
            ins.ins_sort(sorter, 0, sz, delay)
            break
        for i in range(n, sz):
            tmp = sorter.ls[i]
            j = i
            while j-n >= 0:
                sorter.highlight(j-n, 2)
                Sorter.cmp += 1
                if tmp < sorter.ls[j-n]:
                    sorter.write(j, sorter.ls[j-n], delay)
                    j -= n
                else:
                    sorter.highlight(-1, 2)
                    break
            sorter.write(j, tmp, delay)

if __name__ == '__main__':
    sz = 400
    delay = 0
    skip = 15
    sh = Sorter(sz, skip, 'Shell Sort')
    sh.shuffle(delay)
    sh.refresh(True)
    sleep(1)
    sh.resetstatus()
    shell_sort(sh, sz, delay)
    sh.resetcolor()
    sh.refresh(True)
    t.mainloop()
