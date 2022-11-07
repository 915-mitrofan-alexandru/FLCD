
class PIF:
    def __init__(self):
        self.__table = []

    def put(self, token, id):
        self.__table.append((token, id))

    def __str__(self):
        string = "token | ST Pos\n\n"
        for element in self.__table:
            string += str(element[0]) + " | " + str(element[1]) + "\n"
        return string
