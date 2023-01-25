---
layout: post
disqus: y
title: Obiectele cu care lucreaza algoritmii
---

### Obiectele cu care lucreaza algoritmii si operatii permise

In linii mari, algoritmii lucreaza cu doua tipuri de obiecte:

- date si variabile

#### 1. DATE

Asa cum am vazut, ori algoritm porneste de la anumite date de intrare, le prelucreaza, iar in final obtine date de iesire. In exemplul prezentat cu functia, 
datele de intrare sunt reprezentate de cele 10 valori ale lui x, iar datele de iesire sunt cele 10 valori ale lui f(x).

Datele pot fi clasificate dupa tipul lor:

- intregi
- reale
- logice 
- siruri de caractere.

Datele din primele doua tipuri poarta numele de date numerice (intregi si reale). Datele intregi sunt numere apartinand multimii numerelor intregi: +-1, +-2, +-3,...
Datele reale sunt numere cu zecimale. La o astfel de data, inloc de virgula se foloseste punctul. Exemplu: inloc de 2,34, se scrie 2.34. 
Dupa cum stim din matematica, multimea numerelor reale este o reuniune intre multimea numerelor rationale si multimea numerelor irationale. Niciun calculator din lume
nu poate retine un numar irational, intrucat aceasta are o infinitate de zecimale. Din acest motiv, in informatica printr-o data reala intelegem o valoare cu un numar finit 
de zecimale.

Datele logice au numai doua valori: TRUE (adevarat) si FALSE (fals).

Datele de tip sir de caractere sunt reprezentate de siruri de caractere cuprinse intre apostrof. Exemplu: "Acesta este un sir de caractere".

Acum este momentul sa vorbim despre o categorie aparte de date si anume constantele. Constantele sunt date care nu se modifica pe parcursul aplicarii
algoritmului. Acestea pot fi date de oricare dintre tipuri precizate. Ele se caracterizeaza prin faptul ca sunt utilizate in algoritm, fara a fi citite sau obtinute
prin calcule. Se folosesc in calculele care se fac sau sunt mesaje care trebuie sa apara la fiecare rulare a programului.

#### 2. Variabile.

In problema analizata aveam de citit 10 valori de intrare. In matematica acestea ar fi notate x1,x2,x3,...,x10. In prelucrare, pentru orice data de intrare de acest tip se fac aceleasi operatii. Este lipsit de sens sa explicam ce facem cu x1, pentru ca apoi sa explicam ce facem cu x2, x3,..., x10. Din acest motiv se explica ce facem cu un anume x, oricare ar fi el din cele 10. De asemenea nu are rost sa precizam ca se tipareste f(x1), apoi f(x2),...,f(x10). Se noteaza pur si simplu ca se tipareste f. 

Pentru algoritmul nostru x si f sunt variabile.

Ne imaginam variabilele ca pe niste containere (cutiute) care retin DATE. Fiecare variabila are un nume.

Variabila a retine data intreaga 0
variabila a retine data reala 3.14
variabila c retine data logica TRUE
variabila d retine data de tip sir de caractere "un text"

O variabila poate retine date de un tip anume. Astfel avem variabile care pot retine date intregi, variabile care pot retine date reale, variabile care pot retine
date logice, variabile care pot retine date de tip sir de caractere.

De aici rezulta o caracteristica fundamentala a variabilelor: tipul lor. Acesta determina natura valorilor care pot fi retinute de variabila respectiva. 
Astfel avem:

- variabila de tip intreg - notate intreg
- variabile de tip real - notate real
- variabile de tip logic - notate logic
- variabile de tip sir de caractere - notate sir

Facem urmatoarea conventie: pentru ca un algoritm sa poata folosi o variabila, aceasta trebuie DECLARATA - adica anuntata. IAta cum arata declaratiile variabilelor a, b, c.

intreg a
real b
logic c

Daca trebuie sa declaram mai multe variabile de acelasi tip procedam ca in exemplul urmator:

intreg a,b,c,d
real e,f

Observatie: Cu toate ca o variabila are un nume unic, continutul ei poate sa fie diferit de la un moment la altul, pe parcursul executarii programtului. De aici provine denumire de variabila.

#### 3. Expresii

In scopul efectuarii calculelor, sau a luarii anumitor decizii algoritmii folosesc expresii. O expresie este alcatuita din unul sau mai multi operanzi legati intre ei prin operatori.

- Operanzii pot fi variabile sau constante
- Operatorii au rolul de a preciza operatiile care se efectueaza.

Expresii sunt de doua feluri:

a)- Expresii aritmetice
b)- Expresii logice

a) Expresii aritmetice. Operanzii sunt variabile sau constante de tip intreg sau real, Operatorii mai des intalniti sunt:
   - pentru adunare se foloseste operatorul '+'
   - pentru scadere se foloseste operatorul '-'
   - pentru inmultire se foloseste operatorul '*'
   - pentru impartire se foloseste operatorul '/'
   
   Exemplu: 
   Daca a si b sunt variabile de tip intreg care retin 5 , respectiv 8, atunci expresia a + 5 * b + 1 ia valoarea 5 + 5 * 8 + 1, adica 46
   
   In pseudocod putem utiliza ca operator orice simbol cu semnificatia  matematica: Radical, partea intreaga []. Daca x este o valoare reala care retine 4.5
   atunci [x] ia valoarea 4
   
 b) Expresii logice

   Anumiti operatori, desi au ca operanzi variabile, constante sau expresii aritmetice produc ca rezultat valori logice: TRUE sau FALSE
   
   Din prima categorie fac parte operatorii de comparare:
   
   - pentru egalitate folosim operatorul '='
   - pentru mai mic folosim operatorul '<'
   - pentru mai mare folosim operatorul '>'
   - pentru mai mare sau egal folosim operatorul '>='
   - pentru mai mic sau egal folosim operatorul '<='
   - pentru inegalitate folosim operatorul '>='
   
   Exemplu: Variabila a retine 2, iar variabila b retine 5, Atunci:
   
   a < b ia valoarea TRUE
   a > b ia valoarea FALSE
   a = b ia valoarea FALSE
   a != b ia valoarea TRUE
   a >= 2 ia valoarea TRUE
   b <= 6 ia valoarea TRUE
   
   Alti operatori au ca operanzi valori ogice, expresii logice si produc ca rezultat valori logice: true sau false.
   
   Operatorul SAU actioneaza asupra a doi operanzi logici si daca cel putin unul dintre ei este true , rezultatul este true, contrar rezultatul este false.
   
   false SAU true ia valoarea true
   false SAU false ia valoarea false
   
   Operatorul SI actioneaza asupra a doi operanzi logici si daca ambii sunt true, rezultatul este true , rezultatul este true, contrar rezultatul este false.
   
   true SI true ia valoarea true
   true SI false ia valoarea false
   
   Operatorul NOT actioneaza asupra unui operand logic si daca operandul este true, rezultatul este false, contrar rezultatul este true
   
   NOT true ia valoarea false
   NOT false ia valoarea true
   
   Relatii importante:
   
   NOT (a > b) este echivalent cu a scrie a <= b. Se poate gandi asa: daca a nu este mai mare sau egal cu b, atunci a este mai mic sau egal cu b si este corect.
   
   NOT(a<b) <=> a >= b
   NOT(a<=b) <=> a > b
   NOT(a>=b) <=> a < b
   
   RElatiile lui de Morgan:
   
   NOT (a SI B) = NOT(a) SAU NOT(b)
   NOT (a SAU B) = NOT(a) SI NOT(b)
   
   
 
   

