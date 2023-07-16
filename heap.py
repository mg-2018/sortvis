from core import *
import turtle as t

def siftdown(sorter, start, i, sz, delay, minheap):
    ls = sorter.ls
    while i <= sz//2:
        p, l, r = i-1, i*2-1, i*2
        if i*2 == sz:
            res = sorter.compare(p+start, l+start, delay)
            if not minheap and res < 0:
                sorter.swap(p+start, l+start, delay)
            elif minheap and res > 0:
                sorter.swap(p+start, l+start, delay)
            i *= 2
        else:
            if not minheap:
                pick = l if ls[l+start]>=ls[r+start] else r
            else:
                pick = l if ls[l+start]<=ls[r+start] else r
            # Sorter.ops += 1
            Sorter.cmp += 1
            res = sorter.compare(p+start, pick+start, delay)
            if not minheap and res < 0:
                sorter.swap(p+start, pick+start, delay)
            elif minheap and res > 0:
                sorter.swap(p+start, pick+start, delay)
            else:
                break
            i = pick+1

def heapify(sorter, start, sz, delay, minheap):
    for i in reversed(range(1, sz//2+1)):
        siftdown(sorter, start, i, sz, delay, minheap)

def heap_sort(sorter, start, sz, delay, minheap=False):
    heapify(sorter, start, sz, delay, minheap)
    for i in reversed(range(0, sz)):
        sorter.swap(start, start+i, delay)
        if i > 1:
            siftdown(sorter, start, 1, i, delay, minheap)
    if minheap:
        sorter.reverse(start, start+sz-1, delay)

if __name__ == '__main__':
    sz = 400
    delay = 0
    skip = 9
    heap = Sorter(sz, skip, 'Max Heap Sort')
    heap.shuffle(delay)
    # heap.reverse(0, sz-1, delay)
    heap.refresh(True)
    sleep(1)
    heap.resetstatus()
    heap_sort(heap, 0, sz, delay)
    heap.resetcolor()
    heap.refresh(True)
    t.mainloop()
