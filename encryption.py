import string

# we need 2 helper mappings, from letters to ints and the inverse
L2I = dict(zip(string.ascii_uppercase, range(26)))
I2L = dict(zip(range(26), string.ascii_uppercase))

def encrypt(plaintext, key):
    # encipher
    ciphertext = ""
    for c in plaintext.upper():
        if c.isalpha():
            ciphertext += I2L[(L2I[c] + key) % 26]
        else:
            ciphertext += c

    return ciphertext

def decrypt(ciphertext, key):
    # decipher
    plaintext2 = ""
    for c in ciphertext.upper():
        if c.isalpha():
            plaintext2 += I2L[(L2I[c] - key) % 26]
        else:
            plaintext2 += c

    return plaintext2

def getkey(plaintext, ciphertext):
	# get cipher key
    keys = []
    plaintext.upper()
    ciphertext.upper()
    for i,p in enumerate(plaintext):
        if p.isalpha():
            c = ciphertext[i]
            key = L2I[c] - L2I[p]
            keys.append(key)

    if all(i == keys[0] for i in keys):
        return keys[0]
    else:
        return "Invalid"


#print(encrypt("DEFEND THE EAST WALL OF THE CASTLE", 3))
#print(decrypt("GHIHQG WKH HDVW ZDOO RI WKH FDVWOH", 3))
#print(getkey("DEFEND THE EAST WALL OF THE CASTLE", "GHIHQG WKH HDVW ZDOO RI WKH FDVWOH"))
