---
layout: post
disqus: y
title: Algoritmica
---


#### Algoritmica 

  Este ramura informaticii care se ocupa cu proiectarea si analizarea algoritmilor destinati a fi implementati cu ajutorul computerului.

  Prin Proiectare (design) intelegem doua etape:

  1. descrierea algoritmului utilizand un pseudolimbaj (schema logica, pseudocod, descrierea cuprinzatoare sugestiva pe o foaie de hartie)
  2. demonstrarea corectitudinii, adica a faptului ca indiferent de datele de intrare posibile introduse, rezultatul satisface cerintele problemei.

  Analiza algoritmului se refera la evaluarea performantei acestuia, adica a timpului necesar pentru a determina solutia, dar si a altor aspecte, cum 
  ar fi spatiul de memorie folosit si optimalitatea.

#### Proprietatile unui algorithm.

1. Trebuie sa posede date de intrare (input).
2. Trebuie sa posede date de iesire (output).
3. Determinismul (la executarea oricarui pas, trebuie sa cunoastem succesorul acestuia).
4. Corectitudinea datelor de iesire in raport cu datele de intrare.
5. Finitudinea - pentru orice set de date de intrare posibile ale problemei, solutia furnizata
   intr-un numar finit de pasi.
6. Eficienta - furnizarea solutiei trebuie sa fie realizabila prin consumul eficient al resurselor.
7. Generalizatea - algoritmul este aplicabil unei clase de probleme, cele ale caror date de intrare
   satisfac anumite conditii.

#### Complexitatea algoritmilor

   Prin complexitatea unui algoritm intelegem de fapt COSTUL, masurat cu ajutorul unor anumiti parametri
   (timp de executie, memoria necesara, numarul anumitor operatii). Pentru a calcula complixitatea unui 
   algoritm, avem nevoie sa decidem care sunt acesti parametri si sa gasim o functie de determinare a costului
   corepunzatoare.
   
   Dat fiind ca resursele de memorie sunt, in practica, foarte mari, deducem ca timpul de executie al unui
   algoritm este parametrul de baza. Complexitate-timp poate fi calculata in functie de numarul de operatii
   elementare(unitati de timp) necesare atunci cand datele de intrare au o anumita dimensiune N. Aceste
   operatii de baza pot fi comparatii (numar foarte mare, de exemplu), in cazul unui algoritm de cautare, 
   asignari (de exemplu in cazul unui algoritm de sortare), adunari, inmultiri, diviziuni, modulo, apeluri de metoda, etc.



  
