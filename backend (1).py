#ex 1

#lines="int x=5;"

#file  = open("./add.c", 'r')
#lines = file.readlines()

lines=""

keywords    = ["void", "main", "int", "float", "bool", "if", "for", "else", "while", "char", "return"]
operators   = ["=", "==", "+", "-", "*", "/", "++", "--", "+=", "-=", "!=", "||", "&&"]
punctuations= [";", "(", ")", "{", "}", "[", "]"]


def is_int(x):
    try:
        int(x)
        return True
    except:
        return False

def parsefn(b):
    def first(start, production, fir):
        if start in fir:
            return fir[start]
        fir[start] = []
        prod = production[start].split("|")
        for x in prod:
            i = 0
            if x[i].isupper():
                fir[start] += first(x[i], production, fir)
            else:
                fir[start].append(x[0])
            if start == 'A':
                print("", end="")
            i += 1
            try:
                while i < len(x) and ('#' in fir[x[i - 1]] or '#' in production[x[i - 1]]):
                    fir[start].remove('#')
                    if x[i].isupper():
                        fir[start] += first(x[i], production, fir)
                        i += 1
                    else:
                        fir[start].append(x[i])
                        break
            except:
                pass
        return fir[start]

    def follow(start, parent, production, fol, first):
        if parent in fol:
            return fol[parent]
        fol[parent] = []
        if parent == start:
            fol[start].append('$')
        for var in production:
            prod = production[var]
            i = 0
            flag = False
            while i < len(prod):
                if prod[i] == parent or flag:
                    flag = False
                    if i == len(prod) - 1 or prod[i + 1] == '|':
                        fol[parent] += follow(start, var, production, fol, first)
                    elif not prod[i + 1].isupper():
                        fol[parent].append(prod[i + 1])
                    elif prod[i + 1].isupper():
                        fol[parent] += first[prod[i + 1]]
                        if '#' in first[prod[i + 1]]:
                            fol[parent].remove('#')
                            flag = True
                i += 1
        return fol[parent]

    main_input = b.split('\n')
    production = {}
    start = main_input[0][0]
    fir = {}
    variables = []
    for element in main_input:
        if element=='':
            continue
        pr = element.split("->")
        # print(pr)
        production[pr[0]] = pr[1]
        variables.append(pr[0])

    first(start, production, fir)
    for var in variables:
        if var not in fir:
            first(var, production, fir)
    ans = []
    ans.append("first:-")
    for f in fir:
        ans.append(str(f)+" "+(str(set(fir[f])) if len(fir[f])>0 else '{ }'))

    fol = {}
    # states = []
    # for prod in production.values():
    #     states+=prod.split('|')

    follow(start, start, production, fol, fir)
    for prod in production:
        follow(start, prod, production, fol, fir)

    ans.append("follow:-")
    for f in fol:
        ans.append(str(f)+" "+(str(set(fol[f])) if len(fol[f])>0 else '{ }'))
    return ans
    # def first(string):
    #     #print("first({})".format(string))
    #     first_ = set()
    #     if string in non_terminals:
    #         alternatives = productions_dict[string]
    #
    #         for alternative in alternatives:
    #             first_2 = first(alternative)
    #             first_ = first_ |first_2
    #
    #     elif string in terminals:
    #         first_ = {string}
    #
    #     elif string=='' or string=='#':
    #         first_ = {'#'}
    #
    #     else:
    #         first_2 = first(string[0])
    #         if '#' in first_2:
    #             i = 1
    #             while '#' in first_2:
    #                 #print("inside while")
    #
    #                 first_ = first_ | (first_2 - {'#'})
    #                 #print('string[i:]=', string[i:])
    #                 if string[i:] in terminals:
    #                     first_ = first_ | {string[i:]}
    #                     break
    #                 elif string[i:] == '':
    #                     first_ = first_ | {'#'}
    #                     break
    #                 first_2 = first(string[i:])
    #                 first_ = first_ | first_2 - {'#'}
    #                 i += 1
    #         else:
    #             first_ = first_ | first_2
    #
    #
    #     print("returning for first({})".format(string),first_)
    #     return  first_
    #
    #
    #
    # def follow(nT):
    #     #print("inside follow({})".format(nT))
    #     follow_ = set()
    #     #print("FOLLOW", FOLLOW)
    #     prods = productions_dict.items()
    #     if nT==starting_symbol:
    #         follow_ = follow_ | {'$'}
    #     for nt,rhs in prods:
    #         #print("nt to rhs", nt,rhs)
    #         for alt in rhs:
    #             for char in alt:
    #                 if char==nT:
    #                     following_str = alt[alt.index(char) + 1:]
    #                     if following_str=='':
    #                         if nt==nT:
    #                             continue
    #                         else:
    #                             follow_ = follow_ | follow(nt)
    #                     else:
    #                         follow_2 = first(following_str)
    #                         if '#' in follow_2:
    #                             follow_ = follow_ | follow_2-{'#'}
    #                             follow_ = follow_ | follow(nt)
    #                         else:
    #                             follow_ = follow_ | follow_2
    #     #print("returning for follow({})".format(nT),follow_)
    #     return follow_
    #
    # a = []
    # flag = 0
    # starting_symbol = 'S'
    # productions=[]
    #
    # for line in b.split('+'):
    #     if flag==0:
    #         terminals=line.split()
    #     elif flag==1:
    #         non_terminals=line.split()
    #     else:
    #         productions.append(line)
    #     flag+=1
    #
    # starting_symbol=non_terminals[0]
    #
    # productions_dict = {}
    # productions_len=0
    #
    #
    # for nT in non_terminals:
    #     productions_dict[nT] = []
    #
    #
    # for production in productions:
    #     nonterm_to_prod = production.split("->")
    #     print(nonterm_to_prod)
    #     alternatives = nonterm_to_prod[1].split("|")
    #     for alternative in alternatives:
    #         productions_len+=1
    #         productions_dict[nonterm_to_prod[0]].append(alternative)
    #
    #
    #
    # FIRST = {}
    # FOLLOW = {}
    #
    # for non_terminal in non_terminals:
    #     FIRST[non_terminal] = set()
    #
    # for non_terminal in non_terminals:
    #     FOLLOW[non_terminal] = set()
    #
    # for non_terminal in non_terminals:
    #     FIRST[non_terminal] = FIRST[non_terminal] | first(non_terminal)
    #
    # FOLLOW[starting_symbol] = FOLLOW[starting_symbol] | {'$'}
    # for non_terminal in non_terminals:
    #     FOLLOW[non_terminal] = FOLLOW[non_terminal] | follow(non_terminal)
    #
    # #print("FOLLOW", FOLLOW)
    #
    # a.append("{: ^20}{: ^20}{: ^20}".format('Non Terminals','First','Follow'))
    # for non_terminal in non_terminals:
    #     a.append("{: ^20}{: ^20}{: ^20}".format(non_terminal,str(FIRST[non_terminal]),str(FOLLOW[non_terminal])))
    # print(a)
    # return(["just a random string"])

    
##
##for line in lines:
##    for i in line.strip().split(" "):
##        if i in keywords:
##            print (i, " is a keyword")
##        elif i in operators:
##            print (i, " is an operator")
##        elif i in punctuations:
##            print (i, " is a punctuation")
##        elif is_int(i):
##            print (i, " is a number")
##        else:
##            print (i, " is an identifier")

