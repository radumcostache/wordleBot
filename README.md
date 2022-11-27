# _**Wordle**_

Wordle este, in mod normal, un joc web in care jucatorul are al dispozitie 6 incercari pentru a ghici un cuvant de 5 litere din limba engelza. In cadrul acestui proiect, am creat un program care sa joace in mod cat mai eficient Wordle in romana, bazandu-ne pe concepte ale teoriei informatiei, precum entropia.

## **Metode**

Pentru a putea colabora in timpuul realizarii proiectului si pentru a putea beneficia de controlul versiunilor, am utilizat Git si platforma Github. 
Proiectul a fost realizat in exclusivitate in limbajul de programare Python.
In construirea interfetei grafice, am utilizat biblioteca pygame, pentru a reproduce grafica si functionalitatea jocului.
Comunicarea dintre AI Bot si interfata a fost realizata cu ajutorul multiprocessing.

## **Fundamente teoretice**

Entropia reprezinta un concept din teoria informatiei prin care putem exprima cantitatea de incertitudine dintr-un eveniment.
In cazul general, valoarea medie de informatie primita despre o variabila X ce poate lua n valori x1, x2,..., xn, ale caror probabilitati sunt cunoscute, este:
$H(X)=-\sum_{i=1}^{n} P(X=x_i)log_2 P(X=x_i)$
Acum vom vedea cum putem aplica acest concept in proiectul nostru. Pentru fiecare cuvant incercat, avem $3^5=243$ colorari posibile (avem trei culori si 5 litere) pe care le afiseaza jocul. Dupa fiecare rezultat, raman ca variante posibile doar acele cuvinte care corespund colorarii. Evident, daca toate literele sunt verzi, inseamna ca acesta este cuvantul pe care il cautam.
Pentru fiecare cuvant apare urmatoarea problema: cu cat este mai probabil sa obtinem o anumita colorare, cu atat vor ramane mai multe cuvinte de incercat. De aceea, ne vor interesa cuvintele care creeaza o distributie uniforma a liste de cuvinte pe colorari. Acest lucru este echivalent, de fapt, cu gasirea cuvantului cu entropie maxima (Formula entropiei fiind o medie ponderata).

## **Structura**

Proiectul contine patru fisiere cu extensia .py:
* bot.py - care se ocupa, al fiecare pas, cu identificarea cuvantului optim
* inter.py - care se ocupa cu grafica si verificarea cuvantului ales de bot, dupa regulile jocului Wordle
* main.py - fisierul pe care il rulam si care realizeaza interprocesarea dintre bot si inter
* words_list.py - in care avem o lista ce retine toate cuvintele de 5 litere din limba romana

## **Explicarea programului**



## **Concluzii**

## **Bibliogarfie**
* https://aditya-sengupta.github.io/coding/2022/01/13/wordle.html
* 