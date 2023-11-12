caesar = input("enter message:")
dressing = int(input("enter Key:"))
salad = ""
for i in range(len(caesar)):
  #Using ascii to convert characters into their numerical equivalents
  ascii = ord(caesar[i])
  if ascii >= 65 and ascii <= 90:
    #using chr to convert ascii number back to it's character equivalent
    salad += chr((ascii + dressing - 65) % 26 + 65)
  elif ascii >= 97 and ascii <= 122:
    salad += chr((ascii + dressing - 97) % 26 + 97)
  else:
    salad += caesar[i]
print(salad)# add your code here
