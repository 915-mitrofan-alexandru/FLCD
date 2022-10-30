
class HashTab:
    def __init__(self):
        self.__table = []
        for i in range(0, 50):
            self.__table.append([])
        self.__m = 49

    def hash_f(self, value):
        s = 0
        for c in value:
            s += ord(c)
        return s % self.__m + 1

    def add(self, value):
        if value not in self.__table[self.hash_f(value)]:
            self.__table[self.hash_f(value)].append(value)

    def get_index(self, value):
        if value not in self.__table[self.hash_f(value)]:
            return None
        return self.hash_f(value), self.__table[self.hash_f(value)].index(value)
