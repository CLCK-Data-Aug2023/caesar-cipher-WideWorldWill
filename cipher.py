caesar = input("enter message: ")
dressing = 5

salad = ""
for char in caesar:
  if char.isalpha():
    ascii_code = ord(char)
    if ascii_code >= 65 and ascii_code <= 90:
      new_ascii_code = (ascii_code + dressing) % 91
    else:
      new_ascii_code = (ascii_code + dressing) % 123
    new_char = chr(new_ascii_code)
    salad += new_char
  else:
    salad += char
salad=salad.lower()
print(salad)
