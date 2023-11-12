message = input("Please enter a sentence: ")
shift = 5

encrypted_message = ""
alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

for char in message:
  if char in alphabet:
    index = alphabet.index(char)
    new_index = (index + shift) % len(alphabet)
    new_char = alphabet[new_index]
    encrypted_message += new_char
  else:
    encrypted_message += char
encrypted_message=encrypted_message.lower()
print("The encrypted sentence is:", encrypted_message)
