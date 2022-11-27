import pygame
import random
from words import *
pygame.init()

width = 600
height = 800

screen = pygame.display.set_mode((width, height))
background = pygame.image.load("assets/white.jpg") #aici nu stiu exact cum sa punem patratele pentru ca noi nu avem
                                                      #maxim 6 incercari si nu gasesc poza pe google, asa ca ar trebui sa
                                                      #o facem noi
background_rect = background.get_rect(center=(318,300)) #punem poza in dreptunghi
logo = pygame.image.load("assets/logo.png")#stiti ce punem in o-ul de la wordle

pygame.display.set_caption("Wordle")
pygame.display.set_icon(logo)

green = "#178f21"
yellow = "#bee31b"
grey = "#909e80"
outline = "#d6dbce"
filled_outline = "#676963"


picked_word = WORDS[random.randrange(len(WORDS))]

guessed_letter_font = pygame.font.Font("assets/FreeSansBold.otf", 50)
keyboard_letter_font = pygame.font.Font("assets/FreeSansBold.otf", 25)

screen.fill("white")
screen.blit(background, background_rect)
pygame.display.update()

letterSpacingOriz = 85
letterSpacingVert = 12
letterSize = 75 #astea depind de poza pe care o punem cu patratele pt litere


guesses_count = 0

guesses = [[]] * 9 #nu stiu daca avem mai mult de 9 guess uri pe cuvant sau daca vreti sa avem un numar maxim de guessuri,
                   #dar atfel nu stiu cate casute sa punem

current_guess = []
current_guess_string = ""
current_letter_bg_x = 110
indicators = []

game_result = ""

class Letter:
    def __init__(self, text, background_position):
        self.background_color = "white"
        self.text_color = "black"
        self.background_position = background_position
        self.background_x = background_position[0]
        self.background_y = background_position[1]
        self.background_rect = (background_position[0], self.background_y, letterSize, letterSize)
        self.text = text
        self.text_position = (self.background_x+36, self.background_position[1]+34)
        self.text_surface = guessed_letter_font.render(self.text, True, self.text_color)
        self.text_rect = self.text_surface.get_rect(center = self.text_position)

    def draw(self):
        pygame.draw.rect(screen, self.background_color, self.background_rect)
        if self.background_color == "white":
            pygame.draw.rect(screen, filled_outline, self.background_rect, 3)
        self.text_surface = guessed_letter_font.render(self.text, True, self.text_color)
        screen.blit(self.text_surface, self.text_rect)
        pygame.display.update()

    def delete(self):
        pygame.draw.rect(screen, "white", self.background_rect)
        pygame.draw.rect(screen, outline, self.background_rect, 3)
        pygame.display.update()

class Indicator:
    def __init__(self, x, y, letter):
        self.x = x
        self.y = y
        self.text = letter
        self.rect = (self.x, self.y, 57, 75)
        self.background_color = outline

    def draw(self):
        pygame.draw.rect(screen, self.background_color, self.rect)
        self.text_surface = keyboard_letter_font.render(self.text, True, "white")
        self.text_rect = self.text_surface.get_rect(center=(self.x + 27, self.y + 30))
        screen.blit(self.text_surface, self.text_rect)
        pygame.display.update()

indicator_x = 20
indicator_y = 600

def check_guess(guess_to_check):
    global current_guess, current_guess_string, guesses_count, current_letter_bg_x, game_result
    patternofguess = ""
    game_decided = False
    for i in range(5):
        uppercase_letter = guess_to_check[i].text.upper()
        if uppercase_letter in picked_word:
            if uppercase_letter == picked_word[i]:
                guess_to_check[i].background_color = green
                patternofguess += '2'
                for indicator in indicators:
                    if indicator.text == uppercase_letter.upper():
                        indicator.background_color = green
                        indicator.draw()
                guess_to_check[i].text_color = "white"
                if not game_decided:
                    game_result = "W"
            else:
                guess_to_check[i].background_color = yellow
                patternofguess += '1'
                for indicator in indicators:
                    if indicator.text == uppercase_letter.upper():
                        indicator.background_color = yellow
                        indicator.draw()
                guess_to_check[i].text_color = "white"
                game_result = ""
                game_decided = True
        else:
            guess_to_check[i].background_color = grey
            patternofguess += '0'
            for indicator in indicators:
                if indicator.text == uppercase_letter.upper():
                    indicator.background_color = grey
                    indicator.draw()
            guess_to_check[i].text_color = "white"
            game_result = ""
            game_decided = True
        guess_to_check[i].draw()
        pygame.display.update()
    guesses_count += 1
    current_guess = []
    current_guess_string = ""
    current_letter_bg_x = 110

    if guesses_count == 9 and game_result == "":
        game_result = "L"
    return patternofguess
def play_again():
    pygame.draw.rect(screen, "white", (10, 600, 1000, 600))
    play_again_font = pygame.font.Font("assets/FreeSansBold.otf", 40)
    play_again_text = play_again_font.render("Press ENTER to Play Again!", True, "black")
    play_again_rect = play_again_text.get_rect(center=(width / 2, 700))
    word_was_text = play_again_font.render(f"The word was {picked_word}!", True, "black")
    word_was_rect = word_was_text.get_rect(center=(width / 2, 650))
    screen.blit(word_was_text, word_was_rect)
    screen.blit(play_again_text, play_again_rect)
    pygame.display.update()

def reset():
    global guesses_count, picked_word, guesses, current_guess, current_guess_string, game_result
    screen.fill("white")
    screen.blit(background, background_rect)
    guesses_count = 0
    picked_word = random.choice(WORDS)
    guesses = [[]] * 6
    current_guess = []
    current_guess_string = ""
    game_result = ""
    pygame.display.update()
    for indicator in indicators:
        indicator.background_color = outline
        indicator.draw()


def create_new_letter():
    global current_guess_string, current_letter_bg_x
    current_guess_string += key_pressed
    new_letter = Letter(key_pressed, (current_letter_bg_x, guesses_count * 100 + letterSpacingVert))
    current_letter_bg_x += letterSpacingOriz
    guesses[guesses_count].append(new_letter)
    current_guess.append(new_letter)
    for guess in guesses:
        for letter in guess:
            letter.draw()

def delete_letter():
    global current_guess_string, current_letter_bg_x
    guesses[guesses_count][-1].delete()
    guesses[guesses_count].pop()
    current_guess_string = current_guess_string[:-1]
    current_guess.pop()
    current_letter_bg_x -= letterSpacingOriz

def addLetter(newl):
    global current_guess_string, current_letter_bg_x
    current_guess_string += newl
    new_letter = Letter(newl, (current_letter_bg_x, guesses_count * 100 + letterSpacingVert))
    current_letter_bg_x += letterSpacingOriz
    guesses[guesses_count].append(new_letter)
    current_guess.append(new_letter)
    for guess in guesses:
        for letter in guess:
            letter.draw()
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