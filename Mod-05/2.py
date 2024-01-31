luvut =[]
luku = input(f"Syötä lukuja,tyhjä luku lopettaa ")

while luku!='':
    luvut.append(int(luku))
    luku = input (f"Syötä lukuja, tyhjä luku lopettaa ")

luvut.sort (reverse=True)
print (luvut[:5])