import random
import math

file = open("words_list.txt", 'r')

words_list = []
for line in file:
    len1 = len(line)
    line = line[:len1-1]
    words_list.append(line)
words_list.pop()
words_list.append("ZVONI")
init_words_list = words_list.copy()

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

#def guess():


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

#se poate face si pe litere entropia
#si se aduna informatia de pe fiecare litera


#distribution closer to flat <=> higher entropy
#corpus = words_list
#numar de cate ori apare fiecare litera pe fiecare pozitie
#cand apare A cu galben, caut mai intai cuv in care apare A pe poz cu nr aparitii maxim
#print ("Cuvantul care trebuie ghicit este:", picked_word)

#print (entropy("TAREI"), end="\n")
#print (entropy("TARIE"), end="\n")

'''
#calc cu epsilon
maxim = -100000
sol_list = []
sol_dict = {}
for word in words_list:
    val = entropy(word)
    sol_dict[word] = val
    if val > maxim:
        maxim = val
        sol_list.clear()
        sol_list.append(word)
    else:
        if val == maxim:
            sol_list.append(word)
print (sol_dict)
'''

picked_word = "VIDAI"#words_list[random.randint(0, dim-1)]
print (picked_word)


pattern1 = pattern(picked_word, "TARIE")
filter_words_pattern("TARIE", pattern1)
print ("TARIE", end="\n")


sol = "@@@@@"

dict1 = {word: 0 for word in init_words_list}
dict1["TARIE"] = 1

while pattern(picked_word, sol) != "22222" and len(words_list) > 1:
    maxim = -1
    sol = "@@@@@"
    if len(words_list) > 4:
        for word in init_words_list:
            if dict1[word] == 0:
                val = entropy(word)
                if val > maxim:
                    maxim = val
                    sol = word
    else:
        for word in words_list:
            if dict1[word] == 0:
                val = entropy(word)
                if val > maxim:
                    maxim = val
                    sol = word
    if len(words_list) == 0:
        break
    if len(words_list) == 1:
        #print (words_list[0])
        break
    print(sol)
    dict1[sol] = 1
    current_pattern = pattern(picked_word, sol)
    filter_words_pattern(sol, current_pattern)
    print(words_list)
    if picked_word not in words_list:
        print("nu mai e")
if len(words_list) == 1 and sol != words_list[0]:
    print (words_list[0])

#print (sol)

#snaps, hobai, colai, angli - dureaza mult !!update snaps ok, hobai 6 try-uri, colai merge prost probabil mai trebuie calibrat programul pentru trecerea la entropia totala, angli 5 incercari
#votul, totul - dureaza mult, sunt multe cuvinte articulate si trebuie gasite literele prin metoda cealalta
#nopti - dureaza mult pe varianta cu entropie toatala !!update rezolvat dupa calibrare
#brahe - multe incercari !!update: 5 incercari dupa implementare hibrida
#vidai - 7 try-uri vs 8 in varianta initiala
#pare ca atunci cand se duce la pasul 2 pe CALII devine naspa
