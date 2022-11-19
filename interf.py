import pygame
import sys

pygame.init()

green = "#5ded1f"
yellow = "#dfed1f"
white = "#FFFFFF"
grey = "#596155"
black = "#091205"
winGreen = "#2dd63b"

font = pygame.font.SysFont("Helvetica neue", 40)
bigFont = pygame.font.SysFont("Helvetica neue", 80)
win = bigFont.render("You win!", True, winGreen)
playAgain = bigFont.render("Play again?", True, winGreen)


def checkguess(turns, word, userguess, window):
    renderList = ["", "", "", "", ""]
    spacing = 0
    guessColorCode = [grey, grey, grey, grey, grey]

    for x in range(0,5):
        if userguess[x] in word:
            guessColorCode = yellow
        if word[x] == userguess[x]:
            guessColorCode = green

    list(userguess)

    for x in range(0,5):
        renderList[x] = font.render(userguess[x], True, black)
        pygame.draw.rect(window, guessColorCode[x], pygame.Rect(60 + spacing, 50 + (turns * 80), 50, 50))
        window.blit(renderList[x], (70 + spacing, 50 + (turns * 80)))
        spacing *= 80

    if guessColorCode == [green, green , green, green, green]:
        return True


def main():
    file = open("words_list.txt", "r")
    words_list = file.readlines()
    word = words_list[random.randint(0, words_list) - 1].upper()

    height = 600
    width = 400

    FPS = 30
    clock = pygame.time.Clock()

    window = pygame.display.ste_mode((width, height))
    window.fill(black)

    guess = ""

    print(word)

    for x in range(0,5):
        for y in range(0,5):
            pygame.draw.rect(window, grey, pygame.Rect(60 + (x * 80), 50 + (y * 80), 50, 50), 2)

    pygame.display.set_caption("Wordle!")

    turns = 0
    win = False

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.exit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                guess += event.unicode.upper()

                if event.key == K_RETURN and win == True:
                    main()
                if event.key == K_RETURN and turns == 6:
                    main()

                if event.key == pygame.K_BACKSPACE or len(guess) > 5:
                    guess = guess[:-1]
                if event.key == K_RETURN and len(guess) > 4:
                    win = checkguess(turns, word, guess, window)
                    turns += 1
                    guess = ""
                    window.fill(black, (0, 500, 500, 200))


        window.fill(black(0, 500, 500, 200))
        renderGuess = font.render(guess, True, grey)
        window.blit(renderGuess, (180, 530))

        if win == True:
            window.blit(win, (90, 200))
            window.blit(playAgain, (60, 300))

        pygame.display.update()
        clock.tick(FPS)

main()

