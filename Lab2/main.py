from Lab2.LexicalAnalyzer import LexicalAnalyzer, is_identifier, is_constant
from Lab2.PIF import PIF
from ST import ST

if __name__ == '__main__':
    reserved = "C:\\Users\\Alex\\Documents\\GitHub\\FLCD\\Lab1\\token.in"
    lA = LexicalAnalyzer(reserved)
    p1 = "C:\\Users\\Alex\\Documents\\GitHub\\FLCD\\Lab2\\p1.txt"
    p2 = "C:\\Users\\Alex\\Documents\\GitHub\\FLCD\\Lab2\\p2.txt"
    p3 = "C:\\Users\\Alex\\Documents\\GitHub\\FLCD\\Lab2\\p3.txt"
    p1err = "C:\\Users\\Alex\\Documents\\GitHub\\FLCD\\Lab2\\p1err.txt"
    tokens = lA.analyze(p1)
    symbolTable = ST()
    pif = PIF()

    for group in tokens:
        token = group[0]
        if token in lA.all:
            pif.put(token, (-1, -1))
        elif is_identifier(token):
            id = symbolTable.put(token)
            pif.put('identifier', id)
        elif is_constant(token):
            id = symbolTable.put(token)
            pif.put('constant', id)
        else:
            raise Exception("Unknown token " + token + " at line " + str(group[1]))

    f = open("PIF.out", "w")
    f.write(str(pif))
    f.close()

    f = open("ST.out", "w")
    f.write(str(symbolTable))
    f.close()

    print("lexically correct")



