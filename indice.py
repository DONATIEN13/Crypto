def indicemax(freq):
    ind = 0

    for i in range(len(freq)):
        if freq[i] > freq[ind]:
            ind = i
    return ind

def frequence(text):
    l = [0]*26
    for i in range (len(text)):
        c = ord(text[i])
        if c >= ord('a') and c <= ord('z'):
            l[c - ord('a')] += 1
    return l


if __name__ == '__main__':

    texte = 'bonjour a vous je suis etudiant en master informatique'
    print(frequence(texte))
    indice = frequence(texte)
    print(indicemax(indice))