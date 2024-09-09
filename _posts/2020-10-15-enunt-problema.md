---
layout: post
disqus: y
title: Enuntul unei probleme.
---

### Enuntul unei probleme. Data de intrare. Date de iesire. Etapele rezolvarii unei probleme.

Se consira functia:

                    x^2 - 2, x < 0
                    
f : R -> R, f(x)=    3, x = 0
                    
                     x + 2, x > 0
                     
Se cere sa se calculeze f(x) pentru 10 valori reale ale lui x. De exemplu: -3.1, 7, 0, 2.23, etc.

Consideram prima valoare a lui x si anume -3.1. Observam ca aceasta valoare este mai mica decat 0. Calculam x^2 - 2
A doua valoare pemtru care trebuie calculata functia este 7, pentru ca ea este mai mare decat 0, calculam x + 2, adica 7 + 2.
A treia valoare este 0, rezulta ca functia ia valoarea 3. 

Repetam calculul pentru cele 7 valori ramase. Aceasta metoda este plicticoasa si necesita timp. Pentru astfel de probleme a fost inventat computerul.

Observam ca pentru a efectua calculele, calculatorul trebuie sa ia anumite decizii in mod automat. Astfel in functie de valoarea lui x (negativa, zero sau pozitiva)
acesta va decide ce expresie calculeaza pentru a obtine f(x). Deciziile se iau in urma aplicarii algoritmului.

Calculatorul rezolva o problema atunci cand executa un anumit program corespunzator problemei. In esenta programul este alcatuit din instructiuni pe care 
calculatorul le executa. Programul se obtine prin codificarea algoritmilor intr-un limbaj de programare.

In continuare prezentam in linii mari etapele rezolvarii unei probleme:

1. Identificarea datelor de intrare si a celor de iesire.

   Am vazut faptul ca in orice algoritm se porneste de la ceva si se urmareste un anumit rezultat. Cu alte cuvinte trebuie sa ne fie clar de la ce plecam si ce 
   vrem sa obtinem. Asta inseamna ca trebuie sa cunoastem datele de intrare(de unde plecam) si datale de iesire(ce vrem sa obtinem).
   
   Pentru exemplul considerat, datele de intrare sunt cele 10 valori reale x1, x2, x3, ...., x10;
                               datele de iesire sunt cele 10 valori calculate f(x1), f(x2), f(x3), ..., f(x10); 

2. Elaborarea algoritmului de rezolvare.

   In linii mari, algoritmul specifica instructiunile pe care le are de facut calculatorul pentru ca, pornind de la datele de intrare, sa obtina datele de iesire.
   
   Iata algoritmul simplificat de rezolvare a problemei:
   
   Se parcurg urmatoarea etape de 10 ori:
   
   - se citeste valoarea lui x
   - in functie de valoarea lui x se procedeaza astfel:
     daca este negativa se calculeaza f = x^2 - 2
     daca este 0 valoarea functie f = 3    
     daca este positiva se calculeaza f = x + 2
    - se scrie valoarea calculata f.  
    
    Algoritmul a fost scris in limbaj natural. In practica se folosesc limbajele pseudocod (un limbaj asemanator unui limbaj de programare). Oricine poate sa         creeze unul. Pentru redactarea algoritmilor se folosesc si schemele logice (ocupa mult spatiu pe hartie privind reprezentarea grafica)

3. Transpunerea algoritmului in limbaj de programare

    In aceasta etapa se opereaza aproape mecanic. Odata cunoscut un limbaj de programare, transpunerea algoritmlui nu este o problema dificila

4. Testarea programului si corectarea sa pana cand functioneaza corect.
                     
    Atunci cand programul este complex, este aproape imposibil sa fie scris corect de la inceput. Din acest motiv este necesara faza de mai sus.  
    
### Notiunea de algoritm. Caracteristi.

     Notiunea de algoritm a mai fost prezentata. O particularizam pentru programarea calculatoarelor si evidentiam caracteristicile sale. Prin algoritm intelegem      o succesiune de etape care se pot aplica mecanic pentru ca, pornind de la date de intrare, sa se obtina datele de iesire. Retineti: Pentru orice algoritm          trebuie precizat in mod clar care sunt datele de intrare si datele de iesire. Daca aceasta precizare nu a fost facuta, nu se mai poate vorbi de algoritm.

  
