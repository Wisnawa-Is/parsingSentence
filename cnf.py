# inisialisasi variabel
result = {}
startSymbol = 'K'

# Penyesuaian rule CFG
def fixingCFG():
    keys = list(result.keys())
    for leftSide in keys:
        for rightSide in keys:
            if leftSide in result[rightSide]:
                result[rightSide].remove(leftSide)
                result[rightSide].extend(result[leftSide])
    #print(result)


# Cek panjang non terminal
def checkLength():
    length = 0
    for i in result[startSymbol]:
        cekLen = len(i.split(' '))
        if cekLen > length:
            length = cekLen
    return length 

# Cari index
def getIndex(newTerminal, i):
    for index, j in enumerate(newTerminal):
        if j in i:
            return index
    return -1

# konversi ke CNF
def konversi():
    newTerminal = []
    newVariabel = []
    newVar = ['X', 'Y', 'Z', 'A', 'B', 'C', 'D', 'E', 'F', 'G']
    while checkLength() > 2:
        for i in result[startSymbol]:
            if len(i.split(' ')) > 2:
                temp = ''
                lst_check_val = i.split(' ')
                index = getIndex(newTerminal, i)
                if index == -1:
                    addVal = ' '.join(lst_check_val[0:2])
                    newVariabel.append(newVar[len(newVariabel)])
                    newTerminal.append(addVal)
                    temp = i.replace(addVal, newVariabel[-1])
                    result.update({newVariabel[-1]: [addVal]})
                else:
                    temp = i.replace(newTerminal[index], newVariabel[index])
                result[startSymbol][result[startSymbol].index(i)] = temp
    return result
                      
# fungsi utama
def main():
    # Baca rule CFG
    txt = open('cfg.txt', 'r')
    rule = txt.read().splitlines()
    for i in range(len(rule)):
        newRule = rule[i].split(' -> ') 
        result[newRule[0]] = []
        rSide = set(newRule[1].split(' | '))
        result[newRule[0]].extend(rSide)
    
    fixingCFG()
    cnfRule = konversi()
    return cnfRule

lResult = main()

#with open("cnfRule.txt", "w") as file:
#        for i in lResult:
#            file.write(f"{i} -> {' | '.join(lResult[i])}\n")