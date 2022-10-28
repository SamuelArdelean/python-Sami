# validator CNP
#1. CNP de 13 caractere, doar cifre
#2. CNP care respecta sexul
#3. CNP care respecta data de nastere
import datetime
def validare_lungime_caractere_cnp(variabila):
    while len(variabila) != 13 or variabila.isdigit() is False:
        variabila = input("reintroduceti CNP-ul: ")
    return variabila

def validare_sex(sex):
    if int(sex[0]) in range(1,10):
        return True
    return False

def validare_judet(cnp):
    judet = int(cnp[7:9])
    if judet < 47:
        return True
    elif judet == (51 or 52):
        return True
    elif judet!= (47 and 48 and 49 and 50):
        return False
    else:
        return False

def validare_datanastere(cnp):
    data_nastere = cnp[1:7]
    try:
        datetime.datetime.strptime(data_nastere, '%y%m%d')
        return True
    except Exception:
        return False

def validator_cnp(cnp):
    if cnp and validare_sex(cnp) and validare_judet(cnp) and validare_datanastere(cnp):
        return "Valid"
    return "Invalid"

variabila_cnp = validare_lungime_caractere_cnp(input("introduceti CNP-ul: "))
validator = validator_cnp(variabila_cnp)
print(validator)
