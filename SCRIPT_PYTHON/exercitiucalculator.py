# Sa se introduca primul nr, al doilea nr si operatorul si sa se returneze rezultatul

def validare_variabile(variabila):
    while variabila.isdigit() is False:
        # toate stringurile de la 0 la 9
        variabila = input(f"Reintroduceti Numar: ")
    return int(variabila)

def validare_operator(op):
    while op not in ['+','-','*','/']:
        op = input('Reintroduceti operatorul: ')
    return op

def calculator(a,b,c):
    """

    :param a: primul nr
    :param b: al doilea nr
    :param c: operator(+,-,*,/)
    :return: calculeaza folosind operatorul ales
    """

    if c == '+':
        return a+b
    elif c == '-':
        return a-b
    elif c == '*':
        return a*b
    else:
        while b == 0:
            b = validare_variabile(input("ai incercat sa imparti la 0! introdu un numar diferit de 0: "))
        return a/b


primul_numar = validare_variabile(input("Primul numar: "))
al_doilea_numar = validare_variabile(input("Al doilea numar: "))
operator = validare_operator(input('Operator: '))
total = calculator(primul_numar, al_doilea_numar, operator)
print(f"rezultatul este: {total}")
