# num_calls = 0
#
# def exercitiu(x):
#     global num_calls
#     num_calls=3
#     num_calls += 1
#     return x*x
#
# print(exercitiu(4))

# x=1
#
# def f():
#     return x
#
# print(x)
# print(f())

# x= [1,2,"hello", "world", ["another", "list"]]
# print(len(x[3]))

# x= (1,2,3)
# x[1] = 4

# a= [1,2,3]
# b=[4,5]
# print(a+b*3)

# x= [1,2,3,4]
# print(x[-1])   raspuns 4

# x= [0,1,[2]]
# x[2][0] = 3
# x[2].append(4)
# x[2]=2
# print(x)

#
# def exercitiu(i):
#     for i in range(i):
#         return i     -> return te scoate din functie
#
# x= exercitiu(3)
# print(x)    raspuns= 0


# a = range(10)
# y= [x*x for x in a if x%2 == 0]
# print(y)

# def make_account():
#     return{'balance': 0}
#
# def deposit(account, amount):
#     account['balance'] += amount
#     return account['balance']
#
# a= make_account()
# print(deposit(a,10))

# print("foo" + 2)

# try:
#     print("a")
# except:
#     print("b")
# else:
#     print("c")
# finally:
#     print("d")


# print(list("python"))

# def func(*args):
#     return 3 + len(args)
#
# print(func(4,4,4))

# count=(3,2,5,4)
# while len(count) <5:
#     count0=count[0]+1
#     print("hello geek")


# def exercitiu(var):
#     for letter in "geeksforgeeks":
#         if letter == 'e' or letter =='s':
#             continue
#         print("Current letter:", letter)
#         var=10
#         return var
#
# print(exercitiu(20))


# def f(a,list=[]):
#     for i in range(a):
#         list.append(i*i)
#     print(list)
#
# print(f(3))
# print(f(2,[1,2,3]))
# print(f(2))

'''# list= ['1','2','3','4','5']
# print(list[12:])'''

# i = 2
# while True:
#     if i%3==0:
#         break
#     print(i)
#     i+=2

# list1= [2, 33, 222,14,25]
# print(list1[-1])

'''# x= ['ab', 'cd']
# for i in x:
#     i.upper()
# print(x)'''

# def my_function(my_list):
#     lenght=len(my_list)
#     temp= my_list[-1]
#     my_list[0]=my_list[lenght-1]
#     my_list[lenght-1]= temp
#     return my_list
#
# print(my_function([22,11,9,44,56]))

# my_var=['a','b',{'x':1,'z':{'key':30}, 'w':2},10]
# print(my_var[2]['z']['key'])
# lista=['a','b','12','cde']
#
# def my_function(lista):
#     lista=[1,2,'abc']
#     new_list=[i for i in lista]
#     return new_list

# print(my_function(lista))

'''1. Realizati o functie care sa inlocuiasca textul din variabila string aflat
intre valorile “start” si “end” cu textul din “text”.'''
# string = "The Inquisitor must meet Varric on top of Skyhold's battlements to be introduced."
#
# patches = [[5, 14, "Conquistador"], [26, 31, "King"], [43, 49, "Palace"]]
# patches = sorted(patches,reverse = True)
#
# def functie(*args):
#     lista = list(string)
#     for i in args[0]:
#         lista[i[0]-1:i[1]] = i[2]
#     return "".join(lista)
#
# print(functie(patches))

#
'''2. Se da urmatoarea lista:
lista_nume = [‘Maria’, ‘Irina’, ‘Claudiu’, ‘Ionut’, ‘Irina’, ‘Matei’, ‘Irina’, ‘Maria’,
‘Claudiu’]
Se cere:
1. Sortati lista dupa nume
2. Determinati numarul de aparitii al fiecarui nume
3. Listati numele care apare de cele mai multe ori in lista initiala.
4. Listati numele care apare de cele mai putine ori in lista initiala.'''

#
# lista = ['Maria', 'Irina', 'Claudiu', 'Ionut', 'Irina', 'Matei', 'Irina', 'Maria', 'Claudiu']
#
# lista_sortata = sorted(lista)
# print(lista_sortata)
#
# def count(*args):
#     occurences = [lista.count(i) for i in lista]
#     dictionar = dict(zip(lista, occurences))
#     return dictionar
# print(count(lista))
# #
# def count_max(*args):
#     occurences = [lista.count(i) for i in lista]
#     dictionar = dict(zip(lista, occurences))
#     keymax = max(dictionar, key = lambda x: dictionar[x])
#     return keymax
# print(count_max(lista))
#
# def count_min(*args):
#     occurences = [lista.count(i) for i in lista]
#     dictionar = dict(zip(lista, occurences))
#     keymin = min(dictionar, key = lambda x: dictionar[x])
#     return keymin
# print(count_min(lista))
# #
# #
# #

'''ANAGRAME '''
# def anagram(a,b):
#     if sorted(a) == sorted(b):
#         return "Sunt anagrame"
#     else:
#         return "Nu sunt anagrame"
#
# print(anagram('listen', 'silent'))
#
#
# print(set(lista))
#
''' PALINDROAME'''
# def palidrom(a):
#     if list(a) == list(a)[::-1]:
#         return "Este palidrom"
#     else:
#         return "Nu este palidrom"
#
# print(palidrom('kayak'))
#
#
''' CE NUMERE LIPSESC DINTR-UN INTERVAL'''
# a = [1, 2, 4, 6, 7, 9, 10]
# def find_missing(a):
#     return [x for x in range(a[0], a[-1]+1) if x not in a]
# print(find_missing(a))
#
#
''' INVERSUL UNUI STRING'''
# def invers(a):
#     return ''.join(list(a)[::-1])
# print(invers('scoala'))
#

''' TOATE PERMUTARILE DINTR-UN STRING'''
# def permutations(string, step = 0):
#     if step == len(string):
#         print("".join(string))
#     for i in range(step, len(string)):
#         string_copy = [c for c in string]
#         string_copy[step], string_copy[i] = string_copy[i], string_copy[step]
#         permutations(string_copy, step + 1)
#     return ""
# print (permutations ('one'))

'''1. Scrie un program care sa calculeze suma dintre trei numere. 
Daca valorilesunt egale, returnati de trei ori suma acestora.(1 punct)'''

# def suma(a,b,c):
#     suma=0
#     if a == b and b == c:
#         return (a+b+c)*3
#     return a+b+c
#
# print(suma(3,3,3))
'''2. Scrie un program care sa elimine si sa printeze numerele din 3 in 3 pana cand lista devine goala. 
Lista =[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
'''
# lista =[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# for i in lista:
#     if lista[i]%3==0:
#         print(lista[i])
#         lista.pop[i]
#
# print(lista)
'''
3. Scrie un program care sa afiseze toate combinarile de 2 litere dintre valorile dictionarului de mai jos:
dictionar = {“1”: “abc”,“2”: “s”,“3”: “o”,“4”: “n”,“5”: “lm”,“6”: “jk”,“7”: “gi”,“8”: “def”,“9”: “abc”}'''