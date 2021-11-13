import numpy as np

class TologatosJatek:
    def __init__(self, tabla):
        #  A tabla egy 2 dimenzios 4x4-es meretu numpy array
        #  A tabla elemei 0-tol 15-ig a szamok ahol a 0 jelenti az ures mezot
        self.A = tabla
        self.lepesek = []
        self.lepesekszama = 0
        self.d = {}  # d egy dictionary ahol minden szamhoz feljegyezzuk hogy hol szerepel a tablaban
        for i in range(4):
            for j in range(4):
                self.d[self.A[i][j]] = [i, j]

    def megoldhatosag(self):
        inv=0
        for i in range(1,16):
            if self.A[int((i-i%4)/4)][i%4] == 0:
                pass
            else:
                for j in range(i):
                    if self.A[int((j-j%4)/4)][j%4] == 0:
                        pass
                    elif self.A[int((i-i%4)/4)][i%4] < self.A[int((j-j%4)/4)][j%4]:
                        inv=inv+1
        inv += self.d[0][0]
        if inv % 2 == 0:
            return False
        elif inv % 2 == 1:
            return True

    def nullrendezes(self):
        [k,l] = self.d[0]
        self.le(3-k)
        self.jobbra(3-l)

    def fel(self, j=1):
        #  j parameter jelenti, hogy hanszor ismeteljuk a felfele mozgatast
        for _ in range(j):
            self.A[self.d[0][0] - 1][self.d[0][1]], self.A[self.d[0][0]][self.d[0][1]] = \
                self.A[self.d[0][0]][self.d[0][1]], self.A[self.d[0][0] - 1][self.d[0][1]]
            self.d[self.A[self.d[0][0]][self.d[0][1]]] = [self.d[0][0], self.d[0][1]]
            self.d[0] = [self.d[0][0] - 1, self.d[0][1]]
            self.lepesek.append("fel")
        self.lepesekszama += j

    def le(self, j=1):
        #  j parameter jelenti, hogy hanszor ismeteljuk a lefele mozgatast
        for _ in range(j):
            self.A[self.d[0][0] + 1][self.d[0][1]], self.A[self.d[0][0]][self.d[0][1]] = \
                self.A[self.d[0][0]][self.d[0][1]], self.A[self.d[0][0] + 1][self.d[0][1]]
            self.d[self.A[self.d[0][0]][self.d[0][1]]] = [self.d[0][0], self.d[0][1]]
            self.d[self.A[self.d[0][0]][self.d[0][1]]] = [self.d[0][0], self.d[0][1]]
            self.d[0] = [self.d[0][0] + 1, self.d[0][1]]
            self.lepesek.append("le")
        self.lepesekszama += j

    def jobbra(self, j=1):
        #  j parameter jelenti, hogy hanszor ismeteljuk a jobbra mozgatast
        for _ in range(j):
            self.A[self.d[0][0]][self.d[0][1] + 1], self.A[self.d[0][0]][self.d[0][1]] = self.A[self.d[0][0]][
                                                                                             self.d[0][1]], \
                                                                                         self.A[self.d[0][0]][
                                                                                             self.d[0][1] + 1]
            self.d[self.A[self.d[0][0]][self.d[0][1]]] = [self.d[0][0], self.d[0][1]]
            self.d[0] = [self.d[0][0], self.d[0][1] + 1]
            self.lepesek.append("jobbra")
        self.lepesekszama += j

    def balra(self, j=1):
        #  j parameter jelenti, hogy hanszor ismeteljuk a balra mozgatast
        for _ in range(j):
            self.A[self.d[0][0]][self.d[0][1] - 1], self.A[self.d[0][0]][self.d[0][1]] = self.A[self.d[0][0]][
                                                                                             self.d[0][1]], \
                                                                                         self.A[self.d[0][0]][
                                                                                             self.d[0][1] - 1]
            self.d[self.A[self.d[0][0]][self.d[0][1]]] = [self.d[0][0], self.d[0][1]]
            self.d[0] = [self.d[0][0], self.d[0][1] - 1]
            self.lepesek.append("balra")
        self.lepesekszama += j

    def kor(self, i, j, k, e):
        #  k: forgatasok szama
        #  e: forgatas iranya
        if e > 0:
            for _ in range(k):
                self.fel(i)
                self.balra(j)
                self.le(i)
                self.jobbra(j)
        if e < 0:
            for _ in range(k):
                self.balra(j)
                self.fel(i)
                self.jobbra(j)
                self.le(i)

    def h(self, l, k):
        x = l[0] - self.d[0][0]
        y = l[1] - self.d[0][1]
        if l[0] - k[0] == 0:
            self.kor(abs(x), abs(y), 1, -1)
        if l[1] - k[1] == 0:
            self.kor(abs(x), abs(y), 1, 1)

    def g(self, n, l):

        if l[1] - self.d[n][1] > 0:
            if self.d[n][0] < 3:
                self.kor(3 - self.d[n][0], 3, l[1] - self.d[n][1], 1)
            if self.d[n][0] == 3:
                self.kor(1, 3, l[1] + 1, 1)
        x = l[0] - self.d[n][0]
        y = l[1] - self.d[n][1]
        v = []
        if self.d[n][0] == 3:
            if y != 0 and x != 0:
                for i in range(1, int(abs(x)) + 1):
                    v.append([self.d[n][0] + i * int(x / abs(x)), self.d[n][1]])
                for i in range(1, int(abs(y)) + 1):
                    v.append([self.d[n][0] + x, self.d[n][1] + i * int(y / abs(y))])

            else:
                if y != 0:
                    for i in range(1, int(abs(y)) + 1):
                        v.append([self.d[n][0], self.d[n][1] + i * int(y / abs(y))])
                if x != 0:
                    for i in range(1, int(abs(x)) + 1):
                        v.append([self.d[n][0] + i * int(x / abs(x)), self.d[n][1]])
        else:

            if y != 0 and x != 0:
                for i in range(1, int(abs(y)) + 1):
                    v.append([self.d[n][0], self.d[n][1] + i * int(y / abs(y))])
                for i in range(1, int(abs(x)) + 1):
                    v.append([self.d[n][0] + i * int(x / abs(x)), self.d[n][1] + y])
            else:
                if y != 0:
                    for i in range(1, int(abs(y)) + 1):
                        v.append([self.d[n][0], self.d[n][1] + i * int(y / abs(y))])
                if x != 0:
                    for i in range(1, int(abs(x)) + 1):
                        v.append([self.d[n][0] + i * int(x / abs(x)), self.d[n][1]])

        return v

    def fv(self, n, l):
        v = self.g(n, l)
        if len(v) != 0:
            for i in range(len(v)):
                self.h(v[i], self.d[n])

    def kirakas(self):
        self.nullrendezes()
        self.fv(2, [0, 0])
        self.fv(3, [0, 1])
        self.fv(4, [0, 2])
        if self.d[1] == [0, 3]:
            self.kor(3, 3, 1, 1)
            self.kor(2, 3, 1, -1)
            self.kor(2, 3, 1, -1)
        self.fv(1, [1, 0])
        self.kor(3, 3, 1, 1)
        self.fv(6, [1, 0])
        self.fv(7, [1, 1])
        self.fv(8, [1, 2])
        if self.d[5] == [1, 3]:
            self.kor(2, 3, 1, 1)
            self.kor(1, 3, 1, -1)
            self.kor(2, 3, 1, -1)
        self.fv(5, [2, 0])
        self.kor(2, 3, 1, 1)
        self.fv(13, [2, 0])
        if self.d[9] == [3, 0]:
            self.kor(1, 3, 3, 1)
            self.kor(1, 1, 1, -1)
            self.kor(1, 3, 1, 1)
            self.kor(1, 1, 2, -1)
            self.kor(1, 3, 2, 1)
        else:
            self.fv(9, [2, 1])
            self.kor(1, 3, 6, 1)
        self.fv(14, [2, 1])
        if self.d[10] == [3, 1]:
            self.kor(1, 2, 2, 1)
            self.kor(1, 1, 1, -1)
            self.kor(1, 2, 1, 1)
            self.kor(1, 1, 2, -1)
            self.kor(1, 2, 1, 1)
        else:
            self.fv(10, [2, 2])
            self.kor(1, 2, 4, 1)
        if self.d[11] == [3, 2]:
            self.kor(1, 1, 2, -1)
        if self.d[11] == [2, 3]:
            self.kor(1, 1, 1, -1)
