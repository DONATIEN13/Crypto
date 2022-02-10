def decalage(text, dest):
    decal = ord(dest) - 97
    result = ''
    for i in range(len(text)):
        if text[i] >= 'a' and text[i] <= 'z':
            k = (ord(text[i]) - 97 + decal) % 26
            result += (chr(97 + k))
        else:
            result += text[i]
    return result

if __name__ == '__main__':

    texte = 'bonjour je suis etudiant en master informatique'
    desti = 'e'
    print(texte)
    #print('||||||||||||||||||||||||||')
    print(decalage(texte, desti))

