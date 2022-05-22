def generatedictionary():

    estringue = '!"#$%&' + "'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~"
    dictionary = dict()

    #Cria dicionario usando o numero decimal de cada simbolo como chave valendo o simbolo
    for character in estringue:
        dictionary[ord(character)] = character

    return dictionary

def encrypt(dictionary, string):
    
    wordlist = [] #guarda a lista de palavras
    newstring = string.split(sep = '\n') #divide a string por quebra de linha
    #separa as palavras por espaços adicionando quebra de linha no fim a cada quebra de linha
    for word in newstring:
        if word == '':
            break
        else:
            if ' ' in word:
                for palavra in word.split(' '):
                    wordlist.append(palavra)
            else:
                wordlist.append(word)
            wordlist.append('\n')        
    encrypted = '' #variavel para guardar a string criptografada

    for word in wordlist:
        for letter in word:
            #se palavra for um quebra linha manter
            if word == '\n':
                encrypted += word
            else:
                #se chegar no fim da lista ir para o começo
                if ord(letter) + 4 > 126:
                    encrypted += dictionary[((ord(letter)+4)-94)]
                else:
                    encrypted += dictionary[ord(letter)+4]
        if word != wordlist[-1]:
            encrypted += ' '

    return encrypted

def decrypt(dictionary, string):
    
    wordlist = [] #guarda a lista de palavras
    newstring = string.split(sep = ' ') #divide a string por espaços em uma lista
    newstring = string.split(sep = '\n') #divide a string por quebra de linha
    #separa as palavras por espaços adicionando quebra de linha no fim a cada quebra de linha
    for word in newstring:
        if word == '':
            break
        else:
            if ' ' in word:
                for palavra in word.split(' '):
                    wordlist.append(palavra)
            else:
                wordlist.append(word)
            wordlist.append('\n')      
    decrypted = '' #variavel para guardar a string descriptografada

    for word in wordlist:
        for letter in word:
            #se palavra for um quebra linha manter
            if word == '\n':
                decrypted += word
            else:
                #se chegar no começo da lista ir para o fim
                if ord(letter) - 4 < 33:
                    decrypted += dictionary[((ord(letter) - 4)+94)]
                else:
                    decrypted += dictionary[ord(letter)-4]
        if word != wordlist[-1]:
            decrypted += ' '

    return decrypted