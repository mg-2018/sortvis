# core.py
# before: multiple turtles with square
# after: single turtle with pen (Scratch-style)

import turtle as t
from random import seed, randint
from time import sleep

class Sorter:
    # sort statistics; class variable
    cmp = 0
    wri = 0
    aux_wri = 0
    ops = 0
    def __init__(self, sz, skip, name):
        self.sz = sz
        self.ls = [i for i in range(sz)]
        self.aux = [0 for i in range(sz)]
        self.col = [-1]*32
        self.xunit = 800/(sz-1)
        self.yunit = 600/sz
        self.skip = skip
        self.name = name
        self.font = ('Times New Roman', 15, 'normal')

        # t.setworldcoordinates(-450, -350, 450, 350)
        t.hideturtle()
        t.colormode(255)
        t.bgcolor("#000040")
        t.tracer(0, 0)
        t.pensize(800/sz if sz <= 400 else 1)
        t.pu()
        t.lt(90)

    def resetstatus(self):
        Sorter.cmp = 0
        Sorter.wri = 0
        Sorter.aux_wri = 0
        Sorter.ops = 0

    def highlight(self, idx, slot):
        self.col[slot] = idx

    def resetcolor(self):
        for i in range(len(self.col)):
            self.col[i] = -1

    def refresh(self, force=False):
        if not force and Sorter.ops%self.skip != 0:
            return
        stat = f'{Sorter.cmp} comps\n{Sorter.wri} writes\n{Sorter.aux_wri} aux writes'
        ls = self.ls
        sz = self.sz
        col = self.col
        t.clear()
        t.goto(-400, -300)
        if self.sz <= 512:
            for i in range(sz):
                t.pd()
                if i in self.col:
                    t.pencolor('#ff0000')
                else:
                    t.pencolor('#d8d8d8')
                t.fd(self.yunit * ls[i]+1)
                t.pu()
                t.goto(-400 + self.xunit*(i+1), -300)
        else:
            for i in range(512):
                n1 = int(i/512 * self.sz)
                n2 = int((i+1)/512 * self.sz)
                mark = False
                t.pd()
                for j in range(n1, n2):
                    if j in self.col:
                        mark = True; break
                if mark:
                    t.pencolor('#ff0000')
                else:
                    t.pencolor('#d8d8d8')
                t.fd(self.yunit * ls[n1]+1)
                t.pu()
                t.goto(-400 + self.xunit*(n1+1), -300)
        
        t.goto(-400, 200)
        t.pencolor('#ffffff')
        t.write(stat, False, 'left', self.font)
        t.goto(-400, 350)
        t.write(f'{self.name}, {self.sz} Items', False, 'left', self.font)
        t.update()
    
    def swap(self, a, b, delay):
        tmp = self.ls[a]
        self.ls[a] = self.ls[b]
        self.ls[b] = tmp
        self.highlight(a, 1)
        self.highlight(b, 2)
        Sorter.wri += 2
        Sorter.ops += 1
        self.refresh()
        sleep(delay)

    def shuffle(self, delay, sd=None):
        tmp = self.skip
        self.skip = (self.sz//50)+1
        if sd != None:
            seed(sd)
        for i in range(self.sz):
            self.swap(i, randint(i, self.sz-1), delay)
        self.skip = tmp
        self.resetcolor()
    
    def reverse(self, start, end, delay):
        for i in range(start, start+(end+1)//2):
            self.swap(i, (start+end-i), delay)
        self.resetcolor()
        self.refresh()
    
    def compare(self, a, b, delay):
        self.highlight(a, 1)
        self.highlight(b, 2)
        Sorter.cmp += 1
        Sorter.ops += 1
        self.refresh()
        sleep(delay)
        if self.ls[a] < self.ls[b]:
            return -1
        elif self.ls[a] > self.ls[b]:
            return 1
        else:
            return 0
    
    def write(self, a, val, delay):
        self.highlight(a, 1)
        self.ls[a] = val
        Sorter.wri += 1
        Sorter.ops += 1
        self.refresh()
        sleep(delay)

    def aux_write(self, a, val, delay):
        self.highlight(a, 1)
        self.aux[a] = val
        Sorter.aux_wri += 1
        Sorter.ops += 1
        self.refresh()
        sleep(delay)
    
    # TODO: every single class must override this method
    # after switching to object-oriented project
    def run_sort(self, sz, delay):
        raise NotImplementedError

if __name__ == '__main__':
    sz = 100
    test = Sorter(sz, 1, 'Array Visualize Process: Done')
    t.tracer(1, 1)
    t.showturtle()
    t.bgcolor('#ffffff')
    test.highlight(sz//2, 1)
    t.speed(10)
    test.refresh(True)
    t.bgcolor('#000040')
    t.mainloop()
