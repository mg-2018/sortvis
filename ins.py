from core import *
import turtle as t

def ins_sort(sorter, start, sz, delay):
    for i in range(sz):
        tmp = sorter.ls[start+i]
        j = i
        while j > 0:
            Sorter.cmp += 1
            if sorter.ls[start+j-1] > tmp:
                sorter.write(start+j, sorter.ls[start+j-1], delay)
                j -= 1
            else:
                break
        sorter.write(start+j, tmp, delay)

if __name__ == '__main__':
    sz = 400
    delay = 0
    skip = 32
    ins = Sorter(sz, skip, 'Insertion Sort')
    ins.shuffle(delay)
    ins.refresh(True)
    sleep(1)
    ins.resetstatus()
    ins_sort(ins, 0, sz, delay)
    for i in range(sz):
        ins.col[i] = 2
    ins.refresh(True)
    t.mainloop()
