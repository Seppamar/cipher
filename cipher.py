##användaren väljer vilket tekst skall cipheras och hur mycket
##ord("A") returnerar ascii 65
##chr(90) returnerar Z

word = "Ree"

def cipher(tekst, key):
    ciphered  = ""
    for letter in tekst:
        ##Ändrar parametern till ascii
        To_acii = ord(letter)
        ##Förflyttar ascii tecknet med key
        Key_ascii = To_acii + key
        To_letter = chr(Key_ascii)
        ##Vi lägger nya letterin i en string
        ciphered = ciphered + To_letter

    print(ciphered)

cipher(word, 1)