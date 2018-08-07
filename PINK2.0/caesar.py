def caesar(t, k, decode = False):
    if decode: k = 26- k

    return"".join([chr((ord(i) - 65 + k) % 26 + 65)
                   for i in t.upper()
                   if ord(i) >= 65 and ord(i) <= 90])

text = "The quick brown fox jumped over the lazy dogs"
key = 11

encr = caesar(text, key)
decr = caesar(encr, key, decode = True)

print(text)
print(encr)
print(decr)
