from core import *
import turtle as t
import bins

def merge_main2aux(sorter, aux, l, m, r, delay, rewrite=False):
    lp, rp = l, m
    ls = sorter.ls
    for i in range(l, r):
        if lp >= m:
            aux[i] = ls[rp]
            sorter.highlight(m-1, 1)
            sorter.highlight(rp, 2)
            Sorter.aux_wri += 1
            Sorter.ops += 1
            sorter.refresh()
            sleep(delay)
            rp += 1

        elif rp >= r:
            aux[i] = ls[lp]
            sorter.highlight(r-1, 2)
            sorter.highlight(lp, 1)
            Sorter.aux_wri += 1
            Sorter.ops += 1
            sorter.refresh()
            sleep(delay)
            lp += 1

        else:
            Sorter.aux_wri += 1
            res = sorter.compare(lp, rp, delay)
            if res <= 0:
                aux[i] = ls[lp]
                lp += 1
            else:
                aux[i] = ls[rp]
                rp += 1

    sorter.resetcolor()
    if rewrite:
        for i in range(l, r):
            sorter.write(i, aux[i], delay)

def merge_aux2main(sorter, aux, l, m, r, delay):
    lp, rp = l, m
    ls = sorter.ls
    for i in range(l, r):
        if lp >= m:
            sorter.write(i, aux[rp], delay)
            rp += 1

        elif rp >= r:
            sorter.write(i, aux[lp], delay)
            lp += 1

        else:
            Sorter.cmp += 1
            if aux[lp] <= aux[rp]:
                sorter.write(i, aux[lp], delay)
                lp += 1
            else:
                sorter.write(i, aux[rp], delay)
                rp += 1

def sort_half(sorter, aux, l, r, delay):
    ls = sorter.ls
    for i in range(l, r, 7):
        if r-i >= 7:
            bins.bins_sort(sorter, i, 7, delay)
        else:
            bins.bins_sort(sorter, i, r-i, delay)
    seg = 7
    aux_merge = True
    while 1:
        i = l
        if seg < r-l <= seg*2:
            merge_main2aux(sorter, aux, l, l+seg, r, delay, True)
            return
        while r-i >= seg*2:
            merge_main2aux(sorter, aux, i, i+seg, i+seg*2, delay)
            i += seg*2
        if seg < r-i < seg*2:
            merge_main2aux(sorter, aux, i, i+seg, r, delay)
        else:
            while i < r:
                aux[i] = ls[i]
                Sorter.aux_wri += 1
                Sorter.ops += 1
                sorter.resetcolor()
                sorter.highlight(i, 1)
                sorter.refresh()
                sleep(delay)
                i += 1
        i = l
        seg *= 2
        if seg < r-l <= seg*2:
            merge_aux2main(sorter, aux, i, i+seg, r, delay)
            return
        while r-i >= seg*2:
            merge_aux2main(sorter, aux, i, i+seg, i+seg*2, delay)
            i += seg*2
        if seg < r-i < seg*2:
            merge_aux2main(sorter, aux, i, i+seg, r, delay)
        else:
            while i < r:
                ls[i] = aux[i]
                Sorter.wri += 1
                Sorter.ops += 1
                sorter.resetcolor()
                sorter.highlight(i, 1)
                sorter.refresh()
                sleep(delay)
                i += 1
        seg *= 2

def final_merge(sorter, aux, l, m, r, delay):
    sorter.resetcolor()
    ls = sorter.ls
    for i in range(l, m):
        sorter.highlight(i, 1)
        aux[i] = ls[i]
        Sorter.aux_wri += 1
        Sorter.ops += 1
        sorter.refresh()
        sleep(delay)
    lp, rp = l, m
    for i in range(l, r):
        if lp >= m:
            sorter.write(i, ls[rp], delay)
            rp += 1
        elif rp >= r:
            sorter.highlight(r-1, 2)
            sorter.write(i, aux[lp], delay)
            lp += 1
        else:
            Sorter.cmp += 1
            sorter.highlight(rp, 2)
            if aux[lp] <= ls[rp]:
                sorter.write(i, aux[lp], delay)
                lp += 1
            else:
                sorter.write(i, ls[rp], delay)
                rp += 1

def stable_sort(sorter, aux, l, r, delay):
    m = (l+r)//2
    sort_half(sorter, aux, l, m, delay)
    sort_half(sorter, aux, m, r, delay)
    final_merge(sorter, aux, l, m, r, delay)

if __name__ == '__main__':
    sz = 400
    aux = [0]*sz
    delay = 0
    skip = 6
    stb = Sorter(sz, skip, 'STL std::stable_sort')
    stb.shuffle(delay)
    stb.refresh(True)
    sleep(1)
    stable_sort(stb, aux, 0, sz, delay)
    stb.resetcolor()
    stb.refresh(True)
    t.mainloop()
