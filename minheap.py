from core import *
import turtle as t
import heap

if __name__ == '__main__':
    sz = 400
    delay = 0
    skip = 9
    minheap = Sorter(sz, skip, 'Min Heap Sort')
    minheap.shuffle(delay)
    # minheap.reverse(0, sz-1, delay)
    minheap.refresh(True)
    sleep(1)
    minheap.resetstatus()
    heap.heap_sort(minheap, 0, sz, delay, True)
    minheap.resetcolor()
    minheap.refresh(True)
    t.mainloop()

