'''FUNCTII LAMBDA- se mai numesc si functii ANONIME  (fara def/ fara nume)'''

#my_lambda= lambda x,y:x+y
#my_sum=my_lambda(2,4)
#print("suma este: ", my_sum)

# players =[{"first_name":"John", "last_name":"Doe", "rank":3},
#           {"first_name":"Kevin", "last_name":"McDonald", "rank":1},
#           {"first_name":"Bradd", "last_name":"Kelvin","rank":1}]
# print(type(players))
# sorted_players = sorted(players, key= lambda player:player["first_name"])
# print(sorted_players)




# element = lambda x: x*10  #  x este argumentul, x*10 este expresia, functii temporare


# def element(x):
#     return x*10

# element2 = lambda x, y: x+y
import copy

'''FILTER - intoarce un obiect al clasei filter( care este defapt un iterator) rezultat prin 
aplicarea unei functii fiecarui element dintr-un obiect iterat(lista, tuplu, set...etc'''


 # players =[{"first_name":"John", "last_name":"Doe", "rank":3},
 #          {"first_name":"Kevin", "last_name":"McDonald", "rank":1},
 #          {"first_name":"Bradd", "last_name":"Kelvin","rank":1}]

# print(type(players))

# all_mcdonalds = filter(filter_all_mcdonalds, players)
# def filter_all_mcdonalds(player):
#     if player["last_name"]=="McDonald":
#         return True
#     return False

# all_mcdonalds= filter(filter_all_mcdonalds, players)
# print('all_mcdonalds', list(all_mcdonalds))

# all_mcdonalds= filter(lambda player: True if player["last_name"=="McDonald" esle False, players])
# print('all_mcdonalds', list(all_mcdonalds))

#Program care sa returneze o lista cu numere pare dintr-o lista initiala
# lista_1=[1,5,4,6,8,11,3,12]
# lista_2=list(filter(lambda x: (x % 2 == 0), lista_1))
# print(lista_2)

#Exemplu cu for loop
# lista_forloop = []
# for i in lista_1:
#     if i % 2 == 0:
#         lista_forloop.append(i)
# print(lista_forloop)

#Exemplul cu functie clasica
# def filtrare(variabila):
#     if variabila % 2 == 0:
#         return True
#     else:
#         return False
#
# filtered = filter(filtrare, lista_1)
# print(list(filtered))

'''FUNCTIA TIP MAP
- intoarce un obiect al clasei MAP( care este defapt un iterator) rezultat prin 
aplicarea unei functii fiecarui element dintr-un obiect iterat(lista, tuplu, set...etc
--> MODIFICA FIECARE ELEMENT AL UNEI LISTE'''

# players =[{"first_name":"John", "last_name":"Doe", "rank":3},
#           {"first_name":"Kevin", "last_name":"McDonald", "rank":1},
#           {"first_name":"Bradd", "last_name":"Kelvin","rank":2}]
# print(type(players))
# sorted_players = sorted(players, key= lambda player:player["first_name"])
# print(sorted_players)

#players_with_top_3_value= map(check_top_3_player, players)
# def check_top_3_player(player):
#     updated_player=copy.deepcopy(player)
#     updated_player["is_top_3"] = True if updated_player["rank"] <= 3 else False
#     return updated_player
#
# players_with_top_3_value = map(check_top_3_player, players)
# print('players_with_top_3_values = ', list(players_with_top_3_value))



#
# lista_1=[1,5,4,6,8,11,3,12]
# lista_3=list(map(lambda x: x*2, lista_1))
# print(lista_3)

'''FUNCTIA TIP ZIP
- functia zip preia parametrii iterabili ( pot fi 0 parametrii sau mai multi parametrii) si returneaza
un obiect al clasei ZIP (care este un iterator) sub forma de TUPLURI, formate din grupuri de elemente
provenite din parametrii initiali.
 Lungimea finala a obiectului iterabil este egala cu lungimea celei mai scurte structuri initiale.'''

# list_with_int=[1,2,3,4]
# list_with_str=['one', 'two', 'three', 'four']

# result = list(zip(list_with_int, list_with_str))
# result1 = dict(zip(list_with_int, list_with_str))
# result2 = set(zip(list_with_int, list_with_str))

# result=zip(list_with_int, list_with_str)

# print(result)
# print(result1)
# print(result2)
# result_list = list(result)
# print(result_list)
#
# val_1, val_2= zip(*result)
# print('val_1= ', list(val_1))
# print('val_2=',list(val_2))

'''LISTE TIP COMPREHENSION'''
#CASE FOR LOOP
# var = 'comprehension'
# list_for_loop=[]
# for character in var:
#     list_for_loop.append(character)
# print(list_for_loop)
#
# #CASE LAMBDA
# list_map = list(map(lambda x: x, var))
# print(list_map)
#
# #CASE COMPREHENSION
# list_string = [character for character in var]   #expresie for item in lista
# print(list_string)
#
# numbers_list = [x for x in range(100) if x % 2 == 0 if x % 5 == 0]
# print(numbers_list)
#
# obj = ['Par' if i % 2 == 0 else 'Impar' for i in range (10)]
# print(obj)

'''COMPREHENSION DICTIONARY'''

# my_dict={1:'car', 2:'bike'}

# square_dict = dict()
# for num in range(1,11):
#     square_dict[num] = num*num
# print(square_dict)
#
# square_dict = {num:num*num for num in range(1,11)}  #expresion for iterator in iterabil
# print(square_dict)