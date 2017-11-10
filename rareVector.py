class RareVector:
    def __init__(self):
        self.indexes = []
        self.values = []
    def addValueOnIndex(self, index, value):
        self.indexes.append(index)
        self.values.append(value)

    def add(self, other):
        i = 0
        j = 0
        result = RareVector()
        while (i < len(self.indexes) or j < len(other.indexes)):
            index = -1
            value = 0
            if (i < len(self.indexes) and j < len(other.indexes)):
                if (self.indexes[i] == other.indexes[j]):
                    index = self.indexes[i]
                    value = self.values[i] + other.values[j]
                    i += 1
                    j += 1
                else:
                    if self.indexes[i] < other.indexes[j]:
                        index = self.indexes[i]
                        value = self.values[i]
                        i += 1
                    else:
                        if (self.indexes[i] > other.indexes[j]):
                            index = other.indexes[j]
                            value = other.values[j]
                            j += 1
            else:
                if (i >= len(self.indexes)):
                    index = other.indexes[j]
                    value = other.values[j]
                    j += 1
                else:
                    if (j >= len(other.indexes)):
                        index = self.indexes[i]
                        value = self.values[i]
                        i += 1
            result.indexes.append(index)
            result.values.append(value)

        self.values = result.values
        self.indexes = result.indexes

    def multiplyByScalar(self, scalar):
        for i in range(0,len(self.values)):
            self.values[i] *= scalar