from HashTab import HashTab


class ST:
    def __init__(self):
        self.__table = HashTab()

    def put(self, value):
        if not self.__table.get_index(value):
            self.__table.add(value)
        return self.__table.get_index(value)

    def __str__(self):
        return str(self.__table)
