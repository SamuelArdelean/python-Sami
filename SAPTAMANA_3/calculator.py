def validare_variabile(variabila):
    while variabila.isdigit() is False:
        variabila = input("reintroduceti numarul: ")
    return int(variabila)


def validare_operator(op):
    while op not in ['+', '-', '*', '/']:
        op = input('reintrodu operatorul: ')
    return op


def calculator(a, b, c):
    """

    :param a: primul numar
    :param b: al doilea nr
    :param c: operatorul (+, -, *, /)
    :return: calculeaza operatia dintre doua numere
    """

    if c == '+':
        return a + b
    elif c == '-':
        return a - b
    elif c == '*':
        return a * b
    else:
        while b == 0:
            b = validare_variabile(input('ai incercat sa imparti la 0! introdu un numar diferit de 0: '))
        return a / b


primul_numar = validare_variabile(input("numar:"))
al_doilea_numar = validare_variabile(input("numar:"))
operator = validare_operator(input('operator: '))

total = calculator(primul_numar, al_doilea_numar, operator)

print(f"rezultatul este: {total}")