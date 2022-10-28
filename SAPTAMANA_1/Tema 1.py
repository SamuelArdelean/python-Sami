print('lista initiala este formata din: ')
lista_initiala = [7, 8, 9, 2, 3, 1, 4, 10, 5, 6]
print(lista_initiala)
lista_ascendenta = lista_initiala
lista_ascendenta.sort()
print('lista ordonata ascendent = ', lista_ascendenta)
lista_descendenta = lista_initiala
lista_descendenta.reverse()
print(' lista ordonata descendent = ', lista_descendenta)
lista_ascendenta = lista_initiala
lista_ascendenta.sort()
print('lista cu valorile pare este = ', lista_ascendenta[1:10:2])
print('lista cu valorile impare este = ', lista_ascendenta[0:10:2])
print('lista cu multiplii de 3 este = ', lista_ascendenta[2:10:3])