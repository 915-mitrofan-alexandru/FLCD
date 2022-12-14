# Recursive Descendent - functions corresponding to moves
# (expand, advance, momentary insuccess, back, another try, success)
from Lab5.lab5 import Grammar


def read_sequence(file):
    fa = open(file, "r")
    w = []
    while True:
        line = fa.readline()
        if not line or line == "\n":
            break
        w.append(line.split("\n")[0])
    fa.close()
    return w


def get_string_from_list(string):
    strn = ""
    for el in string:
        if el[1] != -1:
            strn += str(el[0])+str(el[1])+ " "
    return strn


class RecursiveDescendent:
    def __init__(self):
        self.s = "q"
        self.i = 0
        self.alpha = []
        self.beta = []
        self.grammar = Grammar()
        file = "C:\\Users\\Alex\\Documents\\GitHub\\FLCD\\Lab5\\g1.txt"
        self.grammar.read_from_file(file)
        self.terminals = self.grammar.get_terminals()
        self.non_terminals = self.grammar.get_non_terminals()
        self.initial = self.non_terminals[0]

    def expand(self):
        current = self.beta.pop(0)
        self.alpha.append((current, 0))
        productions = self.grammar.get_productions_for_a_given_non_terminal(current)
        x = 0
        for el in productions[0]:
            self.beta.insert(x, el)
            x += 1

    def advance(self):
        self.i += 1
        current = self.beta.pop(0)
        self.alpha.append((current, -1))

    def momentary_insuccess(self):
        self.s = "b"

    def back(self):
        self.i -= 1
        current = self.alpha.pop()
        self.beta.insert(0, current[0])

    def another_try(self):
        (current, nr) = self.alpha.pop()
        productions = self.grammar.get_productions_for_a_given_non_terminal(current)
        if nr < len(productions) - 1:
            self.s = "q"
            self.alpha.append((current, nr + 1))
            x = 0
            for _ in productions[nr]:
                self.beta.pop(0)
            for el in productions[nr + 1]:
                self.beta.insert(x, el)
                x += 1
        else:
            if self.i == 0 and current == self.initial:
                self.s = "e"
            else:
                for _ in productions[nr]:
                    self.beta.pop(0)
                self.beta.insert(0, current)

    def success(self):
        self.s = "f"

    def algorithm_run(self):
        self.beta = ["S"]
        w = read_sequence("C:\\Users\\Alex\\Documents\\GitHub\\FLCD\\Lab7\\seq.txt")
        n = len(w)
        while self.s != "f" and self.s != "e":
            print("i: " + str(self.i) +
                  "\ns: " + str(self.s) +
                  "\nALPHA: " + str(self.alpha) + "\nBETA: " + str(self.beta) + "\n\n")
            if self.s == "q":
                if self.i == n:
                    if len(self.beta) == 0:
                        self.success()
                    else:
                        self.momentary_insuccess()
                        print("momentary insuccess")
                elif len(self.beta) == 0:
                    self.momentary_insuccess()
                elif self.grammar.is_non_terminal(self.beta[0]):
                    self.expand()
                    print("expanding")
                elif self.beta[0] == w[self.i]:
                    self.advance()
                    print("advancing")
                else:
                    self.momentary_insuccess()
                    print("momentary insuccess")
            elif self.s == "b":
                if self.grammar.is_terminal(self.alpha[-1][0]):
                    print("back")
                    self.back()
                else:
                    print("another try")
                    self.another_try()
        if self.s == "e":
            print("Error parsing, sequence not accepted")
            return []
        else:
            print("Sequence accepted")
            print(self.alpha)
            return get_string_from_list(self.alpha)


if __name__ == '__main__':
    rd = RecursiveDescendent()
    result = rd.algorithm_run()
    print(result)

    with open("C:\\Users\\Alex\\Documents\\GitHub\\FLCD\\Lab7\\out1.txt", "wt") as file:
        file.write(str(result))
    file.close()
