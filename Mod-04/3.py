luvut =[]
luku = input(f"Syötä lukuja,tyhjä luku lopettaa ")

while luku!='':
    luvut.append(int(luku))
    luku = input (f"Syötä lukuja, tyhjä luku lopettaa ")
print (f"Pienin luku on {(min(luvut))}, isoin luku on {(max(luvut))}")