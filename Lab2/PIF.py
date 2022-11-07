
class PIF:
    def __init__(self):
        self.__table = []

    def put(self, code, id):
        self.__table.append((code, id))

    def __str__(self):
        string = "Code | ST Pos\n"
        for element in self.__table:
            str_el = str(element[0])
            if len(str(element[0])) == 1:
                str_el = "0" + str(element[0])
            string += str_el + " | " + str(element[1]) + "\n"
        return string