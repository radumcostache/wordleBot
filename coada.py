import pygame
import sys
from inter import *
from main import *
from multiprocessing import Process, Queue

mainqueue = Queue()
mainqueue.put("TARIE")
process_guessword = Process(target=check_guess,args=guess_to_check)

process_guessword.start()
process_guessword.join()