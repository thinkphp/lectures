---
layout: post
disqus: y
title: Caracteristicile algorimilor
---

Caracteristicile algoritmilor.
----------

Notiunea de algoritm a mai fost prezentata in primul paragraf al acestui capitol. Aici o particularizam pentru programara calculatoarelor si evidentiem 
caracteriscile sale. Prin algoritm intelegem o succesiune de etape care se pot aplica mecanic pentru ca, pornind de la datele de intrare, sa se obtina
datele de iesire. Observatie: pentru orice algoritm trebuie precizat in mod clar care sunt datele de intrare si care sunt cele de iesire. Daca aceasta precizare
nu a fost facuta, nu se poate vorbi de algoritm. Iata cateva caracteristici ale algoritmilor:

1. Finitudinea - este proprietatea algoritmilor de a furniza datele de iesire intr-un timp finit. Nu trebuie inteles de aici ca daca un algoritm furnizeaza
rezultatele intr-un timp finit este neaparat bun. El trebuie sa fie si eficient, adica sa alegem calea cea mai simpla de rezolvare, intelegand prin aceasta, cea care
presupune un efort de calcul cat mai mic. 

   exemplu: se cere sa se elaboreze algoritmul prin care se listeaza primele 100 patrate perfecte. 
   
   O prima idee ar fi sa testam care numar este patrat perfect, inceput cu 1,2,3,...,10 000. Daca acesta indeplineste conditia este tiparit, altfel se trece mai departe.
   Algoritm se termina atunci cand am listat cele 100 de patrate perfecte. 
   Alta idee ar fi sa tiparim valorile 1^2, 2^2, 3^2,..,100^2. Este mai simplu si eficient.
   
   In primul caz se analizeaza primele 10 000 numere naturale si se tiparesc cele care sunt patrate perfecte.
   In al doilea caz de efectueaza doar 100 de inmultiri.
   
   Atunci cand elaboram un algoritm nu ne oprim la prima solutie gasita.

2. Claritatea - este propritatea algortimilor prin care procesul de calcul este descris clar , fara ambiguitati.

3. Generalitatea - este proprietatea algorimilor de a rezolva o intreaga clasa de probleme. Sa consideram problema cu functia. De fapt
, functia se calculeaza pentru oricare 10 valori reale. Mai general ar fi fost sa calculam valorile pe care le ia functia pentru oricare n valori reale, cu n 
numar natural citit de la tastatura. Mai mult, se poate elabora un algoritm care sa primeasca drept date de intrare:

   atat numarul de valori, valorile
   propriu-zise, cat si functia ale carei valori trebuie calculate.
