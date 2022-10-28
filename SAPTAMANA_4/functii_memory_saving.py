#functii lambda - se mai numsc si functii anonime (fara def/ fara nume)

element = lambda x: x * 10 # unde x este argumentul si x * 10 este expresia


#def element(x):
#    return x*10

"""FILTER"""

#program care sa returneze o lista cu numere pare dintr-o lista initiala
#functia filter intoarce un obiect al clasei filter (care este defapt un iterator) rezultat prin aplicarea
#unei functii fiecaui element din tr-un obiect (lista, tuplu, etc...)

list_1 = [1, 5, 4, 6, 8, 11, 3, 12]
#list_2 = filter(lambda x: (x % 2 == 0), list_1) # filtreaza prin functia anonima ce am nevoie
#print(list_2)
#print(type(list_2))

#ex cu for loop:
#lista_forloop = []
#for i in list_1:
#   if i%2==0:
#       lista_forloop.append(i)
#print(lista_forloop)

#ex cu functia clasica

#def filtrare(variabila):
#    if variabila % 2 == 0:
#        return True
#    else:
#        return False

#filtrered = filter(filtrare, list_1)
#print(list(filtrered))

"""MAP"""
#FUNCTIA map intoarce un pbiect al clasei map (care este defapt un iterator) rezultat prin aplicarea
#unei functii fiecarui element dintr-un obiect iterabil (lista, tuplu, set....etc.)
list_3 = list(map(lambda x: x * 2, list_1))
print(list_3)

"""ZIP"""
#functia zip preia parametrii iterabili (pot fi 0 sau mai multi parametrii) si returneaza un obiect
#al clasei zip(care este defapt un iterator) sub forma de tupluri, formate din grupuri de elemente
#provenite din parametrii initiali
#lungimea finala a aobiectului iterabil este egala cu lungimea celei mai scurte structuri initiale

list_with_int = [1, 2, 3, 4]
list_with_str = ['one', 'two', 'three', 'four']

result = list(zip(list_with_int, list_with_str))
print(result)
#result_list = list(result)
#print(result_list)

"""COMPREHENSION LIST"""
#CASE FOR LOOP
var = 'comprehension'
list_for_loop = []
for character in var:
    list_for_loop.append(character)
print(list_for_loop)

#CASE LAMBDA

list_map = list(map(lambda x: x, var))
print(list_map)

#CASE COMPREHENSION
list_string = [character for character in var] # exprese fr item in lista
print(list_string)

numbers_list = [x for x in range(20) if x % 2 == 0]
print(numbers_list)

obj = ['par' if i % 2 == 0 else 'impar' for i in range (10)]
print(obj)

"""COMPREHENSION DICTIONARY"""

#my_dict = {1: 'car', 2: 'bike'}
square_dict = dict()
for num in range (1, 11):
    square_dict[num] = num*num
print(square_dict)

square_dict = {num: num*num for num in range(1, 11)} # expression for variabila_temporara iterator in iterabil
print(square_dict)

