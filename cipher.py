caesar = input("enter message:")
dressing = int(input("enter key:"))
salad = ""
for i in range(len(caesar)):
  #Using ascii to convert characters into their numerical equivalents
  ascii = ord(caesar[i])
  if ascii >= 32 and ascii <= 122:
    #using chr to convert ascii number back to it's character equivalent
    salad += chr((ascii + dressing - 65) % 26 + 65)
  elif ascii >= 97 and ascii <= 122:
    salad += chr((ascii + dressing - 97) % 26 + 97)
  else:
    salad += caesar[i]
print(salad)# add your code here
