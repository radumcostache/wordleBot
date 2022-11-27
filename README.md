# _**Wordle**_

Wordle este, in mod normal, un joc web in care jucatorul are la dispozitie 6 incercari pentru a ghici un cuvant de 5 litere din limba engleza. In cadrul acestui proiect, am creat un program care sa joace in mod cat mai eficient Wordle in romana, bazandu-ne pe concepte ale teoriei informatiei, precum entropia.

## **Metode**

Pentru a putea colabora in timpul realizarii proiectului si pentru a putea beneficia de controlul versiunilor, am utilizat Git si platforma Github. 
Proiectul a fost realizat in exclusivitate in limbajul de programare Python.
In construirea interfetei grafice, am utilizat biblioteca pygame, pentru a reproduce grafica si functionalitatea jocului.
Comunicarea dintre bot si interfata a fost realizata cu ajutorul interprocesarii.

## **Fundamente teoretice**

Entropia reprezinta un concept din teoria informatiei prin care putem exprima cantitatea de incertitudine dintr-un eveniment.

In cazul general, valoarea medie de informatie primita despre o variabila $X$ ce poate lua $N$ valori $x_1$, $x_2$, ..., $x_n$, ale caror probabilitati sunt cunoscute, este:

$$H(X)=-\sum_{i=1}^n P(X=x_i) log_2 P(X=x_i)\$$

Acum vom vedea cum putem aplica acest concept in proiectul nostru. Pentru fiecare cuvant incercat, avem $3^5=243$ colorari posibile (avem $3$ culori si $5$ litere) pe care le afiseaza jocul. Dupa fiecare rezultat, raman ca variante posibile doar acele cuvinte care corespund colorarii. Evident, daca toate literele sunt verzi, inseamna ca acesta este cuvantul pe care il cautam.

Pentru fiecare cuvant apare urmatoarea problema: cu cat este mai probabil sa obtinem o anumita colorare, cu atat vor ramane mai multe cuvinte de incercat. De aceea, ne vor interesa cuvintele care creeaza o distribuire uniforma a listei de cuvinte pe colorari. Acest lucru este echivalent, de fapt, cu gasirea cuvantului cu entropie maxima (formula entropiei fiind o medie ponderata).


## **Structura**

Proiectul contine patru fisiere cu extensia .py:
* bot.py - care se ocupa, la fiecare pas, cu identificarea cuvantului optim
* inter.py - care se ocupa cu grafica si verificarea cuvantului ales de bot, dupa regulile jocului Wordle
* main.py - fisierul pe care il rulam si care realizeaza interprocesarea dintre bot si inter
* words_list.py - in care avem o lista ce retine toate cuvintele de 5 litere din limba romana

## **Implementarea programului**

Vom incepe prin a rula fisierul main.py, unde am realizat interprocesarea dintre bot si GUI. Cele doua procese comunica prin intermediul a doua cozi, una pentru cuvintele de testat si una pentru rezultatele verificarii dupa regulile jocului Wordle.

Fisierul inter.py alege, la intamplare, un cuvant din lista. Acum, bot.py trebuie sa inceapa sa trimita cuvintele de incercat. La fiecare pas, interfata va verifica acel cuvant si va returna un string de 5 caractere, avand codificarea: 0-gri, 1-galben si 2-verde.

Pe parcursul programului, vom retine doua liste de cuvinte: una care nu se va modifica si una din care scoatem cuvintele ce nu corespund colorarilor de pana acum. Ne intereseaza sa gasim, in fiecare moment, cuvantul cu entropie maxima din prima lista, urmand sa filtram cea de-a doua lista. De asemenea, vom pastra un dictionar pentru a nu incerca de mai multe ori acelasi cuvant. In cazul in care am incercat cel putin 6 cuvinte sau au mai ramas cel mult doua cuvinte in lista filtrata, vom incepe sa cautam printre cuvintele ramase in lista scurta.

Pentru un cuvant dat, ii vom calcula entropia pe litere. Inainte de a incepe sa ghicim cuvintele, vom precalcula de cate ori apare fiecare litera pe fiecare dintre cele 5 pozitii. Translatand entropia unui cuvant la entropia unei litere, ne intereseaza o distribuire uniforma raportata la  culorile obtinute (gri, galben, verde). Astfel, folosindu-ne de frecventele literelor, vom calcula probabilitatile de a aparea fiecare culoare si vom aplica formula de mai sus.  

## **Concluzii**

Simuland jocul pentru toate cuvintele posibile din lista, am obtinut o medie de 4,56 incercari pe cuvant. Se poate observa jucand, ca, in practica, bot-ul reuseste sa gaseasca solutia din 4 incercari.

Comparand cu rezultatele gasite online pentru limba engleza, se observa ca in limba romana sunt necesare, in medie, mai multe incercari.


## **Bibliografie**
* https://aditya-sengupta.github.io/coding/2022/01/13/wordle.html
* https://youtu.be/mJ2hPj3kURg
* https://www.youtube.com/watch?v=v68zYyaEmEA
* https://www.youtube.com/watch?v=TQx3IfCVvQ0
* https://cs.unibuc.ro/~crusu/asc/Arhitectura%20Sistemelor%20de%20Calcul%20(ASC)%20-%20Curs%200x02.pdf
