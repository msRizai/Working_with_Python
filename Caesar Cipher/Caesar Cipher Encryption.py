import os
alphabet = [' ', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']
number_of_alphabets = len(alphabet)
shifted_alphabet = [' ', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                    'u',
                    'v', 'w', 'x', 'y', 'z']

direction = input("please enter 'encode' for encryption and 'decode' for decryption: ").upper()
shift = int(input("enter the number of shifts: "))

if direction == 'ENCODE':
    for i in range(number_of_alphabets):
        if i + shift < number_of_alphabets:
            shifted_alphabet[i + shift] = alphabet[i]
        else:
            shifted_alphabet[i + shift - 27] = alphabet[i]
elif direction == 'DECODE':
    for i in range(number_of_alphabets):
        if i - shift >= 0:
            shifted_alphabet[i - shift] = alphabet[i]
        else:
            shifted_alphabet[i-shift] = alphabet[i]
else:
    print("You entered wrong choice.")

message = input("please enter your message : ").lower()
new_message = ''
for letter in message:
    new_message += shifted_alphabet[alphabet.index(letter)]

print(new_message)
os.system("PAUSE")
