# Brady Bellini
# I certify this is my own work

import string

alphabet = list(string.ascii_lowercase)

message = 'Screw you Zeus, I hate scorpions!'

keyword = 'ORION'

def encode():
    mesg_list = []
    msg = []
    key = []
    cipher = []
    for letter in message:
        mesg_list.append(letter)
        if letter.lower().isalpha() and letter.lower() in alphabet:
            index_msg = alphabet.index(letter.lower())
            msg.append(index_msg)
    for kletter in keyword:
        if kletter.lower() in alphabet:
            index_key = alphabet.index(kletter.lower())
            key.append(index_key)
    for i in range(len(message) - len(keyword)):
        key.append(key[i % len(keyword)])
    for x in range(len(msg)):
        new_index = (msg[x] + key[x]) % 26
        cipher.append(alphabet[new_index])
    print(''.join(str(i) for i in cipher))
    return ''.join(str(i) for i in cipher)        

def decode(cipher):
    og = []
    enc = []
    keyw = []
    for kletter in keyword:
        if kletter.lower() in alphabet:
            keyw.append(alphabet.index(kletter.lower()))
    for y in range(len(cipher) - len(keyword)):
        keyw.append(keyw[y % len(keyword)])
    for letter in cipher:
        if letter in alphabet:
            enc.append(alphabet.index(letter))
    for i in range(len(cipher)):
        og_index = (enc[i] - keyw[i]) % 26
        og.append(alphabet[og_index])
    return ''.join(str(i) for i in og)


if __name__ == "__main__":
    print(decode(encode()))

