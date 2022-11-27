import copy
import random
import math
from multiprocessing import Process, Pipe
from time import sleep

file = open("words_list.txt", 'r')

words_list = []
for line in file:
    len1 = len(line)
    line = line[:len1-1]
    words_list.append(line)
words_list.pop()
words_list.append("ZVONI")
init_words_list = words_list.copy()

freq = { chr(letter+65): [0]*5 for letter in range(26) }
for word in words_list:
    for i in range(5):
        freq[word[i]][i] += 1

freq1 = copy.deepcopy(freq)
init_freq = copy.deepcopy(freq)

dim = 11454

patterns = []
v = [0, 0, 0, 0, 0, 0]
while v[0] == 0:
    var = ""
    for i in range(1, 6):
        var += str(v[i])
    patterns.append(var)
    i = 5
    while i > 0 and v[i] == 2:
        v[i] = 0
        i -= 1
    v[i] += 1

file.close()

#functiile pentru joc

'''
def pattern(pickedWord, guessWord):
    res = ['0'] * 5
    for i in range(5):
        if guessWord[i] == pickedWord[i]:
            res[i] = '2'
            pickedWord = pickedWord[:i] + "#" + pickedWord[i+1:]
            guessWord = guessWord[:i] + "@" + guessWord[i+1:]
        else:
            res[i] = '!'
    for i in range(5):
        if res[i] == '2':
            continue
        ind = pickedWord.find(guessWord[i])
        if ind != -1:
            res[i] = '1'
            pickedWord = pickedWord[:ind] + "#" + pickedWord[ind+1:]
        else:
            res[i] = '0'
    return "".join(res)


#functiile pentru jucator


def filter_words_pattern(guessWord, givenPattern):
    aux = []
    aux.clear()
    for word in words_list:
        word1 = (word+'.')[:-1]
        guessWord1 = (guessWord+'.')[:-1]
        ok = 0
        for i in range(5):
            if givenPattern[i] == "2":
                if word1[i] != guessWord1[i]:
                    ok = 1
                    break
                #words_list[index], words_list[len(words_list) - 1] = words_list[len(words_list) - 1], words_list[index]
                #words_list[len(words_list) - 1], words_list[index] = words_list[index], words_list[len(words_list) - 1]
                #words_list.pop()
                word1 = word1[:i] + "#" + word1[i+1:]
                guessWord1 = guessWord1[:i] + "@" + guessWord1[i + 1:]
        if ok == 1:
            continue
        for i in range(5):
            if givenPattern[i] == "1":
                if word1.find(guessWord1[i]) == -1:
                    ok = 1
                    break
                else:
                    ind = word1.find(guessWord1[i])
                    word1 = word1[:ind] + "#" + word1[ind + 1:]
                #words_list[index], words_list[len(words_list) - 1] = words_list[len(words_list) - 1], words_list[index]
                #words_list[len(words_list) - 1], words_list[index] = words_list[index], words_list[len(words_list) - 1]
                #words_list.pop()

            if givenPattern[i] == "0":
                if word1.find(guessWord1[i]) != -1:
                    ok = 1
                    break
                #else:
                    #ind = word1.find(guessWord1[i])
                    #word1 = word1[:ind] + "#" + word1[ind + 1:]
                #words_list[index], words_list[len(words_list) - 1] = words_list[len(words_list) - 1], words_list[index]
                #words_list.pop()

        if ok == 0:
            #words_list[index], words_list[len(words_list) - 1] = words_list[len(words_list) - 1], words_list[index]
            #words_list.pop()
            aux.append(word)
    words_list.clear()
    for i in range(len(aux)):
        words_list.append(aux[i])

'''

def pattern(pickedWord, guessWord):
    res = ['0'] * 5
    for i in range(5):
        if guessWord[i] == pickedWord[i]:
            res[i] = '2'
            #pickedWord = pickedWord[:i] + "#" + pickedWord[i+1:]
            #guessWord = guessWord[:i] + "@" + guessWord[i+1:]
        else:
            res[i] = '!'
    for i in range(5):
        if res[i] == '2':
            continue
        ind = pickedWord.find(guessWord[i])
        if ind != -1:
            res[i] = '1'
            #pickedWord = pickedWord[:ind] + "#" + pickedWord[ind+1:]
        else:
            res[i] = '0'
    return "".join(res)


def filter_words_pattern(guessWord, givenPattern):
    aux = []
    aux.clear()
    for word in words_list:
        word1 = (word+'.')[:-1]
        guessWord1 = (guessWord+'.')[:-1]
        ok = 0
        for i in range(5):
            if givenPattern[i] == "2":
                if word1[i] != guessWord1[i]:
                    ok = 1
                    break
                #word1 = word1[:i] + "#" + word1[i+1:]
                #word1 = word1[:i] + "@" + word1[i + 1:]
        if ok == 1:
            for i in range(5):
                freq[word[i]][i] -= 1
            continue
        for i in range(5):
            if givenPattern[i] == "1":
                if word1.find(guessWord1[i]) == -1 or word1[i] == guessWord1[i]:
                    ok = 1
                    break
                #else:
                    #ind = word1.find(guessWord1[i])
                    #word1 = word1[:ind] + "#" + word1[ind + 1:]

            if givenPattern[i] == "0":
                if word1.find(guessWord1[i]) != -1:
                    ok = 1
                    break
                #else:
                    #ind = word1.find(guessWord1[i])
                    #word1 = word1[:ind] + "#" + word1[ind + 1:]

        if ok == 0:
            aux.append(word)
        else:
            for i in range(5):
                freq[word[i]][i] -= 1
    words_list.clear()
    for i in range(len(aux)):
        words_list.append(aux[i])

'''
def entropy(guessWord):
    events = {possible_pattern: 0 for possible_pattern in patterns}
    for word in words_list:
        try:
            current_pattern = pattern(guessWord, word)
            events[current_pattern] += 1
        except:
            print (word, end=" - picat \n")
    res = 0
    for possible_pattern in patterns:
        if events[possible_pattern] == 0:
            continue
        prob = events[possible_pattern] / len(words_list)
        res -= prob * math.log2(prob)
    return res
'''

#acum trb actualizat freq la fiecare pas
def entropy(guessWord):
    res = 0
    for i in range(5):
        letter = guessWord[i]
        green = freq[letter][i]
        yellow = 0
        for j in range(5):
            if i != j:
                yellow += freq[letter][j]
        grey = len(words_list) - green - yellow
        event_green = green / (green + yellow + grey)
        event_yellow = yellow / (green + yellow + grey)
        event_grey = grey / (green + yellow + grey)
        if green > 0:
            res -= event_green * math.log2(event_green)
        if yellow > 0:
            res -= event_yellow * math.log2(event_yellow)
        if grey > 0:
            res -= event_grey * math.log2(event_grey)
    return res

outfile = open("tries.txt", 'w')
tries = 0
#print(len(words_list))
wordindex = 0
for picked_word in init_words_list:
    outfile.write(picked_word + ", ")
    tries += 1
    freq = copy.deepcopy(init_freq)
    freq1 = copy.deepcopy(init_freq)
    words_list = init_words_list.copy()
    pattern1 = pattern(picked_word, "TAREI")
    filter_words_pattern("TAREI", pattern1)
    outfile.write("TAREI, ")
    sol = "@@@@@"
    dict1 = {word: 0 for word in init_words_list}
    dict1["TAREI"] = 1
    all_pattern = "00000"
    used = [0 for letter in range(26)]
    linie = ""
    wordindex += 1
    print(wordindex)
    kk = 0
    while pattern(picked_word, sol) != "22222" and len(words_list) > 1:
        maxim = -1000000
        if picked_word == "AFANA":
            kk = 1
        nr = 0
        current_pattern = pattern(picked_word, sol)
        filter_words_pattern(sol, current_pattern)
        guesses = 0
        if guesses < 6 and len(words_list) > 2:
            for i in range(5):
                if current_pattern[i] == "2":
                    all_pattern = all_pattern[:i] + "2" + all_pattern[i + 1:]
            for i in range(5):
                if all_pattern[i] == "2":
                    nr += 1
                    used[ord(sol[i]) - 65] = 1
            if nr < 3:
                for word in init_words_list:
                    if dict1[word] == 0:
                        val = entropy(word)
                        if val > maxim:
                            maxim = val
                            sol = word
            else:
                for word in init_words_list:
                    ok = 0
                    for i in range(5):
                        if used[ord(word[i]) - 65]:
                            ok += 1
                    if ok >= 3:
                        continue
                    if dict1[word] == 0:
                        val = entropy(word)
                        if val > maxim:
                            maxim = val
                            sol = word
        else:
            for word in words_list:
                ok = 0
                if dict1[word] == 0:
                    val = entropy(word)
                    if val > maxim:
                        maxim = val
                        sol = word
        if len(words_list) == 0:
            break
        if len(words_list) == 1:
            break
        dict1[sol] = 1
        linie += sol + ", "
        tries += 1
#        outfile.write(sol + ", ")
        guesses = guesses + 1.0
    if len(words_list) == 1:
        linie += words_list[0]
        tries = tries + 1
    linie = linie.strip(' ')
    linie = linie.strip(',')
    outfile.write(linie + "\n")
print(tries/11454.0)
outfile.close()

'''
VOTUL
TAREI
CUCUL
OOGON
SMASH
BIBIL
FIFUL
PAPAL
AVIVA
VOTUL
nemodif



'''

'''
SUTAI
TAREI
OUATI
CUTAI
MUTAI
SUTAI
cu lista modif

SUTAI
TAREI
OUTUL
ACCES
SUTAI
cu lista nemodif

SUTAI
TAREI
OUATI
CUTAI
MAMOS
SUTAI
hibrid 2
'''

'''
NAZUL
TAREI
SULUL
CACIC
NINGA
BAZZZ
NAZUL
cu lista nemodif

NAZUL
TAREI
SALUL
NANUL
NAPUL
NAZUL
cu lista modif

NAZUL
TAREI
SALUL
NANUL
BAZZZ
NAZUL
hibrid
'''

'''
SOSIT
TAREI
OOCIT
BOBIT
DODIT
MOMIT
GOGIT
POPIT
SOLIT
SOSIT
lista modif

SOSIT
TAREI
COCUL
MOMIM
PODIS
SOSIT
lista nemodif

SOSIT
TAREI
OOCIT
SPLIN
SOSIT
hibrid

'''

'''
IUBIM
TAREI
LINUL
SUDIM
GOGIM
JUPIM
IUBIM
hibrid 2

IUBIM
TAREI
MOLUL
SUDIC
INFIG
IUBIM
lista nemodif

IUBIM
TAREI
LINUL
SUDIM
FUGIM
JUPIM
IUBIM
lista modif


'''


'''
avg = 0

for word in init_words_list:
    freq = freq1.copy()
    words_list = init_words_list.copy()
    picked_word = word
    pattern1 = pattern(picked_word, "TAREI")
    filter_words_pattern("TAREI", pattern1)
    #print("TAREI", end="\n")

    sol = "@@@@@"
    nr = 1
    dict1 = {word: 0 for word in init_words_list}
    dict1["TAREI"] = 1

    while pattern(picked_word, sol) != "22222" and len(words_list) > 1:
        maxim = -1
        sol = "@@@@@"
        for word in words_list:
            if dict1[word] == 0:
                val = entropy(word)
                if val > maxim:
                    maxim = val
                    sol = word
        if len(words_list) <= 1:
            break
        #print(sol)
        nr += 1
        dict1[sol] = 1
        current_pattern = pattern(picked_word, sol)
        filter_words_pattern(sol, current_pattern)
        if nr > 9:
            print("bucla inf")
            break
    if len(words_list) == 1 and sol != words_list[0]:
        nr += 1
        #print(words_list[0])
    avg += nr
avg /= len(init_words_list)
print ("average ul este:")
print(avg)

'''


#snaps, hobai, colai, angli - dureaza mult !!update snaps ok, hobai 6 try-uri, colai merge prost probabil mai trebuie calibrat programul pentru trecerea la entropia totala, angli 5 incercari
#votul, totul - dureaza mult, sunt multe cuvinte articulate si trebuie gasite literele prin metoda cealalta
#nopti - dureaza mult pe varianta cu entropie toatala !!update rezolvat dupa calibrare
#brahe - multe incercari !!update: 5 incercari dupa implementare hibrida
#vidai - 7 try-uri vs 8 in varianta initiala
#pare ca atunci cand se duce la pasul 2 pe CALII devine naspa