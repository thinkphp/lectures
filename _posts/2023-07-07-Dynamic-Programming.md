---
layout: post
disqus: y
title: Dynamic Programming
---
```
Programarea dinamica se aplica in rezolvarea problemelor de optim si consta in determinarea solutiei pe baza unui sir de decizii
d1, d2, d3, ... , dn, unde di transforma problema din starea s(i-1)in starea s(i). Spre deosebire de metoda Divide et Inpera, unde subproblemele rezultate trebuie
sa fie independente, in cadrul acestei metode, subproblemele care apar in descompunere nu sunt independete, iar in descompunerea unei probleme vor aparea subprobleme comune mai multor subprobleme de dimensiuni mai mari. Pentru a fi eficienta, metoda programarii dinamice trebuie sa rezolve fiecare suproblema o singura data si sa memoreze solutia acesteia pentru a o utiliza in cadrul reaparitiei sale in alte subprobleme. Spre deosebire de Divide Et Impera, metoda programarii dinamice opereaza de jos in sus, nerecursiv, si presupune cunoasterea exacta de la inceput a subproblemelor care apar in descompunerea unei probleme. Nu este o tehnica standardizata asa cum este tehnica Backtracking, iar elaborarea algoritmului trebuie sa se bazeze pe cateva principii generale. Din acest motiv, abordarea acestei metode devine anevoioasa si presupune serioase aptitudini de programare, deseori insotite de cunostinte matematice. 
