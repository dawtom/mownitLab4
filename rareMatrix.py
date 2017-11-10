class MyTuple:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def eq(self, other):
        if (self.x == other.x and self.y == other.y):
            return True
        else:
            return False
    def greaterThan(self, other):
        if (self.y > other.y or (self.y == other.y and self.x > other.x)):
            return True
        else:
            return False
    def lessThan(self, other):
        if (self.y < other.y or (self.y == other.y and self.x < other.x)):
            return True
        else:
            return False


class RareMatrix:
    def __init__(self):
        self.xIndexes = []
        self.yIndexes = []
        self.values = []
    def addValueOnIndex(self, xIndex,yIndex, value):
        self.xIndexes.append(xIndex)
        self.yIndexes.append(yIndex)
        self.values.append(value)
    def print(self):
        print("XIndexes: ", self.xIndexes)
        print("YIndexes: ", self.yIndexes)
        print("Values ", self.values)
    def add(self, other):
        selfIterator = 0
        otherIterator = 0
        result = RareMatrix()
        while (selfIterator < len(self.xIndexes) or otherIterator < len(other.xIndexes)):
            xIndex = -1
            yIndex = -1
            value = 0
            if (selfIterator < len(self.xIndexes) and otherIterator < len(other.xIndexes)):
                selfIndexTuple = MyTuple(self.xIndexes[selfIterator], self.yIndexes[selfIterator])
                otherIndexTuple = MyTuple(other.xIndexes[otherIterator], other.yIndexes[otherIterator])

                if (selfIndexTuple.eq(otherIndexTuple)):
                    xIndex = selfIndexTuple.x
                    yIndex = selfIndexTuple.y
                    value = self.values[selfIterator] + other.values[otherIterator]
                    selfIterator += 1
                    otherIterator += 1
                else:
                    if selfIndexTuple.lessThan(otherIndexTuple):
                        xIndex = selfIndexTuple.x
                        yIndex = selfIndexTuple.y
                        value = self.values[selfIterator]
                        selfIterator += 1
                    else:
                        if (selfIndexTuple.greaterThan(otherIndexTuple)):
                            xIndex = otherIndexTuple.x
                            yIndex = otherIndexTuple.y
                            value = other.values[otherIterator]
                            otherIterator += 1
            else:
                if (selfIterator >= len(self.xIndexes)):
                    xIndex = other.xIndexes[otherIterator]
                    yIndex = other.yIndexes[otherIterator]
                    value = other.values[otherIterator]
                    otherIterator += 1
                else:
                    if (otherIterator >= len(other.indexes)):
                        xIndex = self.xIndexes[selfIterator]
                        yIndex = self.xIndexes[selfIterator]
                        value = self.values[selfIterator]
                        selfIterator += 1
            result.xIndexes.append(xIndex)
            result.yIndexes.append(yIndex)
            result.values.append(value)
        self.xIndexes = result.xIndexes
        self.yIndexes = result.yIndexes
        self.values = result.values
    def multiplyByScalar(self, scalar):
        self.values = [i * 5 for i in self.values]
    def multiplyByDenseVector(self, vector):
        result = RareMatrix()
        resultVectorIndex = -1
        indexInResult = -1
        for matrixIterator in range(0, len(self.xIndexes)):
            print("Result vector index: ", resultVectorIndex, ", self.yIndexes[matrixIterator]: ", self.yIndexes[matrixIterator])
            if (resultVectorIndex < self.yIndexes[matrixIterator]):
                resultVectorIndex  = self.yIndexes[matrixIterator]
                indexInResult += 1
                result.xIndexes.append(0)
                result.yIndexes.append(self.yIndexes[matrixIterator])
                result.values.append(self.values[matrixIterator] * vector[self.xIndexes[matrixIterator]])
            else:
                result.values[indexInResult] += self.values[matrixIterator] * vector[self.xIndexes[matrixIterator]]

            result.print()
        result.print()
    #mnożenie przez macierz byłoby podobne tylko trzeba by pokombinować
        # podobnie jak wcześniej przy dodawaniu z krotkami jako indeksami





r1 = RareMatrix()
r2 = RareMatrix()

for j in range(1,4):
    for i in range (1,5):
        r1.addValueOnIndex(i-1, j-1, i * j)

r1.print()
r1.multiplyByDenseVector([16,15,14,13])


# r = RareVector()
# p = RareVector()
# r.addValueOnIndex(0,9)
# r.addValueOnIndex(1,11)
# r.addValueOnIndex(5,55)
# r.addValueOnIndex(6,66)
#
#
# p.addValueOnIndex(5,55)
# p.addValueOnIndex(7,77)
# print(r.indexes)
# print(r.values)
# print(p.indexes)
# print(p.values)
#
# r.add(p)
# print(r.indexes)
# print(r.values)
#
# r.multiplyByScalar(5)
# print(r.indexes)
# print(r.values)






#można zrobić wykres zależności błędu, który otrzymamy w przybliżonej metodzie
#od ilości iteracji
#PRZEĆWICZYĆ MATPLOTLIBA - PRZYDA SIĘ POTEM
#mnożyć rzadkie macierze przez gęste wektory
#rzadką macierz przez gęstą też pomnożyć
