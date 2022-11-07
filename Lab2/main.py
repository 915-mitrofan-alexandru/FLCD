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
    tokens = lA.analyze(p3)
    symbolTable = ST()
    pif = PIF()

    for group in tokens:
        token = group[0]
        if token in lA.all:
            pif.put(lA.codification[token], (-1, -1))
        elif is_identifier(token):
            id = symbolTable.put(token)
            pif.put(lA.codification['identifier'], id)
        elif is_constant(token):
            id = symbolTable.put(token)
            pif.put(lA.codification['constant'], id)
        else:
            raise Exception("Unknown token " + token)

    print('PIF: \n', pif)
    print('Symbol Table: \n', symbolTable)

    print('\n\n Codification table: ')
    for e in lA.codification:
        print(e, " - ", lA.codification[e])



