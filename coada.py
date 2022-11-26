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