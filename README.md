# _**Wordle**_

Wordle is a game where the player has 6 tries to guess a 5-letter word in English.
In this project, we developed a Bot that can guess a word given in Romanian in a minimum amount of guesses, using concepts of information theory, such as entropy.

## **Theoretical Foundations**

Entropy is a concept originating from information theory through which we can express the amount of uncertainty in an event.

In general, the average amount of information received about a variable $X$ that can take $N$ values $x_1$, $x_2$, ..., $x_n$, whose probabilities are known, is:

$$H(X)=-\sum_{i=1}^n P(X=x_i) log_2 P(X=x_i)\$$

Now, let's see how we can apply this concept in our project. For each word tried, we have $3^5=243$ possible colorings (we have $3$ colors and $5$ letters) that the game displays. After each result, only those words that correspond to the coloring remain as possible variants. Obviously, if all the letters are green, it means that this is the word we are looking for.

For each word, the following problem appears: the more likely we are to get a certain coloring, the more words will remain to be tried. Therefore, we will be interested in the words that create a uniform distribution of the list of words on colorings. This is actually equivalent to finding the word with the maximum entropy (the entropy formula being a weighted average).

## **Structure**

The project contains four files with the extension .py:
* bot.py - which identifies the optimal word at each step
* inter.py - responsible for the GUI and the checking of the word chosen by the Bot, according to the rules of the Wordle game
* main.py - the file we run and which realizes the IPC between bot and inter
* words_list.py - in which we have a list that contains all the 5-letter words in the Romanian language

## **Code Design**

The project was made exclusively in the Python programming language.
For the graphical interface, we used the Pygame library (that is needed to be downloaded by the user), to reproduce the graphics and functionality of the Wordle game.
The communication between the Bot and the Interface was made using interprocessing.

We will start by running main.py, where we integrated the interprocessing between the Bot and the GUI. The two processes communicate through two queues, one for the words to be tested and one for the results of the checking done according to the rules of the Wordle game.

A word will be randomly chosen from the list through inter.py. Now, bot.py starts sending the words to be tested. At each step, the interface will check that word and return a string of 5 characters, having the encoding: 0-gray, 1-yellow and 2-green. 

Throughout the program, we will keep two lists of words: one that will not be modified and one from which we will remove the words that do not correspond to the colorings so far. We are interested in finding, at each moment, the word with the maximum entropy from the first list, following with the filtration of the second list. Also, we will keep a dictionary in order not to try the same word several times. If we have tried at least 6 words or there are at most two words left in the filtered list, we will start looking among the remaining words in the short list.

For a given word, we will compute the entropy based on its letters. Before starting to guess the words, we will precalculate how many times each letter appears on each of the 5 positions. By translating the entropy of a word to the entropy of a letter, we are interested in a uniform distribution relative to the colors obtained (gray, yellow, green). Thus, using the letter frequencies, we will calculate the probabilities of each color appearing and we will apply the formula above.

## **Conclusions**

Simulating the game for all the possible words in the list, we obtained an average of 4.56 tries per word. It can be observed by playing that, in practice, the bot manages to find the solution in 4 tries.

Comparing our results with the ones found online for the English language, it can be noticed that, on average, more tries are needed in the Romanian language.

## **Resources**
* https://aditya-sengupta.github.io/coding/2022/01/13/wordle.html
* https://youtu.be/mJ2hPj3kURg
* https://www.youtube.com/watch?v=v68zYyaEmEA
* https://www.youtube.com/watch?v=TQx3IfCVvQ0
* https://cs.unibuc.ro/~crusu/asc/Arhitectura%20Sistemelor%20de%20Calcul%20(ASC)%20-%20Curs%200x02.pdf
