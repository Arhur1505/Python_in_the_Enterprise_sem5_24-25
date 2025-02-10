class Matrix:
    def __init__(self, a, b, c, d): #tablica
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def __add__(self, o):
        return Matrix(self.a + o.a, self.b + o.b, self.c + o.c, self.d + o.d)

    def __sub__(self, other):
        return Matrix(self.a - o.a, self.b - o.b, self.c - o.c, self.d - o.d)

    def cout(self):
        print("Macierz 2x2: ") #nie printujemy tu, return string, przeładuj print
        print(self.a, self.b, self.c, self.d)


#if name = main
matrix_1 = Matrix(4.,5.,6.,7.)
matrix_2 = Matrix(2.,2.,2.,1.)

#matrix_3 = matrix_2 @ matrix_1
matrix_4 = matrix_2 + matrix_1
#matrix_4 = 6 + matrix_1
#matrix_4 = matrix_1 + 6

matrix_1.cout()
matrix_2.cout()
matrix_4.cout()

#3 przykłacdy każdej operacji
#NxM matrix, uniwersalna
#m2 += 1
#m2 + m1
#m3 = m1 + m2
#dla minusa to samo
#m3 = m2 @ m1
#m2 += 4.5
#m3 = m2 @ 4.5
#m3 =  m2 * m1
#m3 = m1 * 4.5
#m3 = 1 + m2
#m3 = 2.5 @ m2

#print only in script
#use expections
