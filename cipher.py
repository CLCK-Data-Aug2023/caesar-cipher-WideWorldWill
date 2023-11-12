caesar = input("enter message: ")
dressing = 5

salad = ""
words = caesar.split() # Split the input message into words

for word in words: # Encrypt each word separately
  new_word = ""
  for char in word:
    if char.isalpha():
      ascii_code = ord(char)
      if ascii_code >= 65 and ascii_code <= 90:
        new_ascii_code = (ascii_code + dressing) % 91
      else:
        new_ascii_code = (ascii_code + dressing) % 123
      new_char = chr(new_ascii_code)
      new_word += new_char
    else:
      new_word += char
  salad += new_word + " "

print(salad)
