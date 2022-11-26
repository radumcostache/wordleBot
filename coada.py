from inter import *
from main import *
from multiprocessing import Process, Queue
def pickRandom(guessQueue, patternQueue):
    n = 0
    while True:
        if guessQueue.empty:
            guessQueue.put(WORDS[random.randrange(len(WORDS))])
            n = n + 1
        if n == 10:
            break
def chooseWord(guessQueue, patternQueue):
#picked_word = "VATRA"#words_list[random.randint(0, dim-1)]
#print (picked_word)
    guessQueue.put("TARIE")
    dict1 = {word: 0 for word in init_words_list}
    dict1["TARIE"] = 1
    sol = "TARIE"
    while True:
        maxim = -1

        if patternQueue.empty() == 0 :
            current_pattern = patternQueue.get()
            filter_words_pattern(sol, current_pattern)
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
                break
            dict1[sol] = 1
            guessQueue.put(sol)
            print (sol + " " + str(len(words_list)))
    if len(words_list) == 1:
        guessQueue.put(words_list[0])
def getWord(guessQueue, patternQueue):
    print(picked_word)
    while True:
        if guessQueue.empty() == 0:
            Word = guessQueue.get()
            for letter in Word:
                addLetter(letter)
            while True:
                nextWord = 0
                for event in pygame.event.get() :
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                        pattern = check_guess(current_guess)
                        patternQueue.put(pattern)
                        nextWord = 1
                        break
                if nextWord == 1:
                    break



if __name__ == '__main__':
    guessQueue = Queue()
    patternQueue = Queue()
    #getWord(guessQueue)
    process_guessword = Process(target=getWord,args=(guessQueue,patternQueue))
    process_randomword = Process(target=chooseWord, args=(guessQueue,patternQueue))
    process_randomword.start()
    process_guessword.start()
    process_guessword.join()
    process_randomword.join()



#    process_guessword = Process(target=getWord,args=(guessQueue,))
#   process_guessword.start()
#    process_guessword.join()