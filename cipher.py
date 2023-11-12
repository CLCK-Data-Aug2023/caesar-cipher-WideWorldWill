caesar = input("Please enter a sentence: ")
dressing = 5

salad = ""
alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

for char in caesar:
  if char in alphabet:
    index = alphabet.index(char)
    new_index = (index + shift) % len(alphabet)
    new_char = alphabet[new_index]
    salad += new_char
  else:
    salad += char
salad=salad.lower()
print("The encrypted sentence is:", salad)
