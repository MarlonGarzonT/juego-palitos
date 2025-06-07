from random import shuffle

# Lista inicial

palitos  = ['-', '--', '---', '----']


# Mezclar palitos

def mezclar(lista):
    shuffle(lista)
    return lista



#P edir intento

def probar_suerte():
    intento = ''

    while intento not in ['1', '2', '3', '4']:
        intento = input("Elige un número dentro del 1 al 4: ")

    return int(intento)

# Comprobar intento

def comprobar_intento(lista, intento):
    if lista[intento - 1] == '-':
        print("Haz perdido.")
    else:
        print("Te haz salvado.")

    print(f"Te ha tocado {lista[intento - 1]} ")

palitos_mezclados = mezclar(palitos)
seleccion = probar_suerte()
comprobar_intento(palitos_mezclados, seleccion)