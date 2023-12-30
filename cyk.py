from cnf import *

rule = main()
#print(rule)

def parse(string):
    
    n = len(string.split())
    table = [[set([]) for j in range(n)] for i in range(n)]

    string2 = string.split()
    for j in range(0, n):
        for lhs, rule in lResult.items():
            for rhs in rule:
                if len(rhs.split()) == 1 and rhs == string2[j]:
                    table[j][j].add(lhs)
                    #print(table[j][j])
                    
    for l in range(1, n):
        for i in range(n - l):
            #print(l)
            #print(j)
            j = i + l
            for k in range(i, j):
                #print(k)
                for lhs, rule in lResult.items():
                    for rhs in rule:
                        if len(rhs.split()) == 2 and rhs.split()[0] in table[i][k] and rhs.split()[1] in table[k + 1][j]:
                            table[i][j].add(lhs)

    #print(table[0][n-1])
    if 'K' in table[0][n-1]:
        return True
    else:
        return False
