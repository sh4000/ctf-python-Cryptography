import random

# Trouve la clé qui a ete use pour chiffrer le message, en utilisant un chiffrement vigenère / Find the key that was used to encrypt the message, using a strong encryption
# *as4h

ciphertext = "xliw wldqw xli qlrq"

possible_keys = []
for i in range(1, 26):
    possible_keys.append("".join([chr((i + ord(x) - ord('a')) % 26 + ord('a')) for x in "abcdefghijklm"]))

for key in possible_keys:
    plaintext = ""
    j = 0
    for i in range(len(ciphertext)):
        if ciphertext[i].isalpha():
            plaintext += chr((ord(ciphertext[i]) - ord(key[j % len(key)]) + 26) % 26 + ord('a'))
            j += 1
        else:
            plaintext += ciphertext[i]
    if "flag" in plaintext:
        print("Clé secrète trouvée :", key)
        print("Message déchiffré :", plaintext)
        break
else:
    print("Clé secrète non trouvée.")
