#print("ana are mere")
#var1 = input("adauga un numar: ")
#print(var1)
#var1= "ana are \'3\' mere" #escape, ne aguta sa tratam ghilimeaua ca un string
#print(var1)

#numar_mere = 3
#umar_pere = 2
#ar1 = f"ana are {numar_mere} mere si {numar_pere} pere"
#var1= "ana are {0} mere si {1} pere". format(numar_mere, numar_pere) #pt fiecare pereche de acolada, adaugi o variabila la format
#var1= "ana are " + str(numar_mere) + " mere si " + str(numar_pere) + " pere"
#print(var1)


#def my_function(a, b:int=0, c:int=0):   #asa declaram o functie
 #   return a + b + c   #modalitatea de a exporta din functie

#suma = my_function(1, 2)
#suma = my_function(4, c=3, b=2)
#print(suma)

#var1= "ana are {0} mere si {1} pere".format(numar_mere), numar_pere)
#print(var1)


#def my_function(a, b:int=0, c:int=0, *args) -> (int, dict):
#    return a + b + c, { 'diferenta' : a - b - c}

#suma, diferenta = my_function(numar_mere, c= numar_pere, b=2)
#print(suma, diferenta)

#def suma(a, b, *args, **kwargs):
    '''
    :param a: primul parametru
    :param b: al doilea parametru
    :param args: argumente
    :param kwargs: argumente tip cheie - valoare
    :return: suma tuturor parametrilor
    '''
#    total = 0
#    variabila_temp = a + b
#    for i in args:
#        total = total + i    #definita doar in functia suma, nu este disponibila in afara, DECAT daca returnam
#    print(type(args))
#    print(type(kwargs)) #dictionar
#    for i, v in kwargs.items():
#        print(i, v)
#        total = total + v
#    return variabila_temp + total
#    print(' ana are mere')  # asta nu se executa, ca este dupa return

#variabila = suma(1, 2, 3, 4, 5, c=4, d=7, e=9)    #functia args ne permite sa adaugam oricati parametrii dorim, dar acesti parametrii ar trebuii parcursi
#print(variabila)


#EXCEPTII
#my_var = input('adauga un numar: ')
#try:
#    my_int = int(my_var)   #teoretic nu se poate converti string in int
#    print(my_int)
#    variabila_nedefinita = None
#    print(variabila_nedefinita)
#except NameError:
#    print('variabila nu este definita')
#    variabila_nedefinita = 0
#except ValueError:
#    print(' eroare de valoare')
#except Exception as e:
#    print('exceptie', e)
#else:   # apare doar cand nu sunt exceptii
#    print(' nu sunt exceptii')
#finally:
#    print(' s-a rulat programul')

def test_function(first, second, third):
    result = first*3 + second*3 + third*3
    return result