LUODIT_KERROIN = 13.3
NAULAT_KERROIN = LUODIT_KERROIN * 32
LEIVISKAT_KERROIN = LUODIT_KERROIN * NAULAT_KERROIN * 20

leiviskat = float(input("Leiviskät: "))
naulat = float(input("Naulat: "))
luodit = float(input("Luodit: "))

leiviskat_gr = LEIVISKAT_KERROIN * leiviskat
naulat_gr = NAULAT_KERROIN * naulat
luodit_gr = LEIVISKAT_KERROIN * luodit

paino_gr = leiviskat_gr + naulat_gr + luodit_gr

kg = int (paino_gr / 1000)
g = int (paino_gr% 1000)

print (f"Paino nykymitoissa on {kg} kg ja {g}g")