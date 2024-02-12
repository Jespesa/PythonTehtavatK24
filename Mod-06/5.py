def parittomatluvut (lista):
    parittomat = []
    for i in lista:
        if i % 2 != 0:
            parittomat.append(i)
    return parittomat

lista = [1,2,3,4,5,6,7,8,9,10]
print ("Alkuperäinen lista: ", lista)

parittomat = (parittomatluvut)(lista)
print ("Parittomat luvut: ",parittomat)