# var1 = 'ana are \'3\' mere'
# print(var1)
# numar_mere = 3
# var1 = "ana are mere"
# print(f"ana are {numar_mere} mere")

# numar_mere=3
# numar_pere=2

# def my_function(a:int=0, b:int=0, c:int=0) -> (int,dict):  #parametrii sunt numere intregi
#     return a+b+c, {'diferenta':a-b-c}
#
# suma, diferenta = my_function(numar_mere, c=numar_pere, b=2)
# print(suma, diferenta)

# var1="ana are {1} mere si {0} pere".format(numar_mere, numar_pere)
# print(var1)

#
# def my_function(a:int=0, b:int=0, c:int=0, *args) -> (int,dict):
#     return a+b+c, {'diferenta':a-b-c}

# suma, diferenta = my_function(numar_mere, c=numar_pere, b=2)
# print(suma, diferenta)


# def suma(a, b, *args):
#     total = 0
#     variabila_temp= a+b
#     for i in args:
#         total = total + i
#     print(type(args))
#     return variabila_temp + total   #-> dupa ce ajunge la return, nu mai executa nimic altceva dupa!!
#
#
# variabila = suma(1,2,3, 4, 5)
# print(variabila)


# def suma(a, b, *args, **kwargs):
#     total = 0
#     variabila_temp= a+b
#     for i in args:
#         total = total + i
#     print(type(kwargs))
#     for i,v in kwargs.items():
#         print(i,v)
#         total = total + v
#     return variabila_temp + total   #-> dupa ce ajunge la return, nu mai executa nimic altceva dupa!!
#
#
# variabila = suma(1,2,3, 4, 5,c=4,d=7,e=9)
# print(variabila)

# def suma(a, b, *args, **kwargs):
#     """
#
#     :param a:
#     :param b:
#     :param args: argumente tip tuple
#     :param kwargs: argumente cheie:valoare
#     :return: returneaza suma
#     """
#     total = 0
#     variabila_temp = a + b
#     for i in args:
#         total = total + i
#     print(type(kwargs))
#     for i, v in kwargs.items():
#         print(i, v)
#         total = total + v
#     return variabila_temp + total  # -> dupa ce ajunge la return, nu mai executa nimic altceva dupa!!
#
#
# variabila = suma(1, 2, 3, 4, 5, c=4, d=7, e=9)
# print(variabila)

# def suma(a, b, *args, **kwargs):
#     total = 0
#     variabila_temp = a + b
#     for i in args:
#         total = total + i
#     print(type(kwargs))
#     for i, v in kwargs.items():
#         print(i, v)
#         total = total + v
#     return variabila_temp + total  # -> dupa ce ajunge la return, nu mai executa nimic altceva dupa!!
#
#
# variabila = suma(1, 2, 3, 4, 5, c=4, d=7, e=9)
# print(variabila)
#
#
# my_var = input('adauga un numar: ')
# try:
#     my_int = int(my_var)
#     #print(variabila_nedefinita)
# except ValueError:
#     print('eroare de valoare')   #afiseaza doar tipul de eroare cel mai superior, nu si restul
# except NameError:
#     print('variabila nu este definita')
#     variabila_nedefinita = 0
# except Exception as e:
#     print('exceptie', e)
# else:
#     print('nu sunt exceptii')

#print(variabila_nedefinita)


'''FUNCTII'''

# - reprezinta un bloc organizat de cod ce poate fi refolosit pt a realiza o singura actiune
# - exista si functii predefinite, dar si functii care pot fi create de utilizator
# - exemple functii predefinite Python:
# print() - afisam mesajul
# format()- formatam un sir de caractere
# input() - citim date

# def my_function(*args, **kwargs):
#     pass
#
# return  -  pentru a returna valoarea in urma calculelor din functie

#def get_sum(a, b,*args, **kwargs):
#    return a+b
#my_sum = get_sum(2, 5, 5, 8)
#print(my_sum)

# def my_function(a, b:int=0, c:int=0):   #asa declaram o functie
#    return a + b + c   #modalitatea de a exporta din functie
# suma = my_function(1, 2)
# # suma = my_function(4, c=3, b=2)
# print(suma)

# -parametrii functiei
# def my_function(param_1, param_2):
#     print(param_1)
#     print(param_2)
# my_function(2,5)

#def my_function(param_1, param_2, param_3=20):
#     print(param_1)
#     print(param_2)
#     print(param_3)
#     suma= param_1 + param_2 + param_3
#     print(suma)
#my_function(2, 5)

# def my_function(param_1, param_2, *args):
#     print(param_1)
#     print(param_2)
#     print(args)
# my_function(2,5,9,'ana', 2)
# -> in args se vor regasi toti parametrii pozitionali nedeclarati in semnatura functiei
# intr-o forma de lista in ordinea in care au fost transmisi restul valorilor


# def my_function(param_1, param_2, **kwargs):
#     print(param_1)
#     print(param_2)
#     print(kwargs)
# my_function(2,5, a=2)
# -> rolul de a prelua toti parametrii cheie:valoare nedeclarati. Se vor regasi intr-un ditionar

# def suma(a, b, *args, **kwargs):
#     '''
#     :param a: primul parametru
#     :param b: al doilea parametru
#     :param args: argumente
#     :param kwargs: argumente tip cheie - valoare
#     :return: suma tuturor parametrilor
#     '''
#     total = 0
#     variabila_temp = a + b
#     for i in args:
#         total = total + i    #definita doar in functia suma, nu este disponibila in afara, DECAT daca returnam
#     print(type(args))
#     print(type(kwargs)) #dictionar
#     for i, v in kwargs.items():
#         print(i, v)
#         total = total + v
#     return variabila_temp + total
# print(' ana are mere')  # asta nu se executa, ca este dupa return
# variabila = suma(1, 2, 3, 4, 5, c=4, d=7, e=9)    #functia args ne permite sa adaugam oricati parametrii dori
# # dar acesti parametrii ar trebuii parcursi
# print(variabila)

# def test_function(first, second, third):
#     result = first*3 + second*3 + third*3
#     print(result)
#     return result
# test_function(2,3,4)

# def test_function(first, second, third):
#     result = first*3+second*3+third*3
#     return result

'''FUNCTIE RECURSIVA'''
# def get_sum(n):
#     if n == 0:
#         return 0
#     return n+ get_sum(n-1)
# print(get_sum(6))
# #
# - o functie recursiva trebuie sa se auto-apeleze si sa contina o conditie pentru oprirea recusivitatii

'''EXCEPTII'''
# excetia este un obiect care reprezinta o eroare
# tratarea exeptiilor se face atunci cand codul scris poate intampina o eroare, aceasta abordare reprezentand
# o masura de precautie a developerului

# my_var = input('adauga un numar: ')
# try:
#    my_int = int(my_var)   #teoretic nu se poate converti string in int
# try:
#     my_int = int(my_var)  # -> va da o VauError daca nu este trecut de la tastatura un numar
# except: ValueError as e:
#     print('Do something with ValueError exception.', e)
# except: NameError as e:
#     print('Do something with NameError exception.', e)
# else:
#     print('Reaches here if there is no excepton.')
# finally:
#     print('Reaches here no mather if there is an exception or not.')
#
# try -> pt a rula codul care ne intereseaza, poate fi problematic
# except -> prinde xceptia si o trateaza. Daca nu se doreste tratarea exceptiei, putem scrie doar pass in
#     blocul exceptiei
# else -> executarea unor instructiuni cand codul din ramura try a functionat fara proleme. Nu e obligatorie
# finally -> rularea unor instructiuni indiferent daca a fost aruncata sau nu o exceptie. Nu eobligatorie

# my_var = input('adauga un numar: ')
# try:
#    my_int = int(my_var)   #teoretic nu se poate converti string in int
#    print(my_int)
#    variabila_nedefinita = None
#    print(variabila_nedefinita)
# except NameError:
#    print('variabila nu este definita')
#    variabila_nedefinita = 0
# except ValueError:
#    print(' eroare de valoare')
# except Exception as e:
#    print('exceptie', e)
# else:   # apare doar cand nu sunt exceptii
#    print(' nu sunt exceptii')
# finally:    ->  apare fie ca exista sau nu eroare!
#    print(' s-a rulat programul')

'''TEMA FUNCTII'''
#Sa se scrie o functie care primeste parametrii nedefinit.
#Sa se calculeze suma tuturor parametrilor care reprezinta nr intregi sau reale

# def suma(*args,**kwargs):
#     total_args = 0
#     total_kwargs = 0
#     for i in args:
#         if type(i)==int:
#             total_args +=i
#         else:
#             pass
#     for k in kwargs:
#         if type(k)==int:
#             total_kwargs +=k
#         else:
#             pass
#     return total_args+total_kwargs
#
# variabila = suma(1,5,-3,'abc',[12,56,'cad'])
# variabila_n = suma()
# variabila_nn=suma(2,4,'abc',param_1=2)
# print(variabila)
# print(variabila_n)
# print(variabila_nn)

###sa se scrie o functie recursiva care primeste ca parametru un nr intreg si returneaz
###suma tuturor numerelor de la 0 la n


# def get_sum(n):
#     if n == 0:
#         return 0
#     return n+ get_sum(n-1)
# print(get_sum(6))
# #

# def get_sum(n):
#     if n == 0:
#         return 0
#     return n+ get_sum(n-1)
# print(get_sum(6))
# #

#suma numere pare de la 0 la n
# def get_sum_pare(n):
#     if n == 0:
#         return 0
#     if n%2==0:
#         return n+ get_sum_pare(n-1)
#     else:
#         return n-2
# print(get_sum_pare(6))
# #
