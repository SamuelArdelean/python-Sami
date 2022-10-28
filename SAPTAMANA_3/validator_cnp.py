import datetime

def validare(variabila):
    '''

    :param variabila: cnp-ul introdus de la tastatura
    :return: CNP-ul valid
    '''
    while len(variabila) != 13 or variabila.isdigit() is False:
        variabila = input("reintrodu cnp-ul")
    return variabila

def validare_judet(cnp):
    judet = int(cnp[7:9])
    if judet in range(1, 47):
        return True
    elif judet == (51 or 52):
        return True
    elif judet!= (47 and 48 and 49 and 50):
        return False
    else:
        return False
def validare_sex(a):
    if int(a[0]) in range (1,10):
        return True
    return False

def validare_data_nastere(cnp):
    data_nastere = cnp[1:7]
    try:
        datetime.datetime.strptime(data_nastere, '%y%m%d')
        return True
    except Exception:
        return False

def validator_cnp(cnp):
    if cnp and validare_sex(cnp) and validare_judet(cnp) and validare_data_nastere(cnp) and validator_NNN(cnp) and cifra_control(cnp):
        return "valid"
    return "invalid"

def validator_NNN(cnp):
    NNN= int(cnp[9:12])
    if NNN in range(1, 1000):
        return True
    return False

def cifra_control(cnp):
    constanta = '279146358279'
    cod_autodetector = 0

    for i, v in enumerate(constanta):
        cod_autodetector += int(v)*int(cnp[i])

    if cod_autodetector % 11 == 10 and int(cnp[12]) != 1:
        return False
    elif cod_autodetector % 11!= int(cnp[12]):
        return False
    else:
        return True

variabila_cnp= validare(input("introdu cnp: "))
validator = validator_cnp(variabila_cnp)
print(validator)
