# Sa se introduca primul nr, al doilea nr si operatorul si sa se returneze rezultatul
def validare_variabila(variabila):
    while variabila.isdigit() is False:
        variabila = input('reintroduceti numarul: ')
    return int(variabila)

def validare_operator(op):
    while op not in ['+','-','*','/']:
        op = input('reintroduceti operatorul: ')
    return op

def calculator(a,b,c):
    if c == '+':
        return a+b
    elif c == '-':
        return a-b
    elif c == '*':
        return a*b
    else:
        while b == 0:
            b = validare_variabila(input("alegeti un numar diferit de 0 "))
        return a/b

primul_numar = validare_variabila(input("introduceti primul numar: "))
al_doilea_numar = validare_variabila(input("introduceti al doilea numar: "))
operator= validare_operator(input("alegeti operatorul: "))
total = calculator(primul_numar, al_doilea_numar, operator)
print("numarul total este: ", total)