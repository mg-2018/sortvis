from core import *
import turtle as t

def bubble_sort(sorter, sz, delay):
    for i in range(sz-1, 0, -1):
        swapped = False
        for j in range(i):
            if sorter.compare(j, j+1, delay) > 0:
                sorter.swap(j, j+1, delay)
                swapped = True
        if not swapped:
            break

if __name__ == '__main__':
    sz = 400
    delay = 0
    skip = 72
    bubble = Sorter(sz, skip, 'Bubble Sort')
    bubble.shuffle(delay)
    bubble.refresh(True)
    sleep(1)
    bubble.resetstatus()
    bubble_sort(bubble, sz, delay)
    bubble.resetcolor()
    bubble.refresh(True)
    t.mainloop()
