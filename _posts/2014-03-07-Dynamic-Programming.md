---
layout: post
disqus: y
title: Dynamic Programming
---

Dynamic Programming, like the divide-and-conquer method, solves problemes by combining the solutions to subproblems. "Programming" in this context refers to a tabular method, not to writing computer code. As we saw in DivideEtImpera algorithms partion the problem into dijoint subproblems, solve the subproblems recursively, and then combine their solutions to solve the original problem. In contrast, dynamic programming applies when the subproblems overlap-that is, when subproblems share subsubproblems. In this context, a divideEtImpera algorithm does more work than necessary, repeatedly solving the common subsubproblems. A dynamic programming algorithm solves each subsubproblem just once and then saves its answer in a table, thereby avoiding the work of recomputing the answer every time it solves each subsubproblem.

We typically apply dynamic programming to optimization problems. Such problems can have many possible solutions. Each solution has a value, and we wish to find a solution with the optimal (minimum or maximum) value. We call such a solution an optimal solution to the problem, as opposed to the optimal solution, since there may be several solutions that achive the optimal value.

When developing a dynamic programming algorithm, we follow a sequence of four steps:

Characterize the structure of an optimal solution.
Recursively define the value of an optimal solution.
Compute the value of an optimal solution, typically in a bottom-up fashion.
Construct an optimal solution from computed information.

Programarea dinamica se aplica in rezolvarea problemelor de optim si consta in determinarea solutiei pe baza unui sir de decizii
d1, d2, d3, ... , dn, unde di transforma problema din starea s(i-1)in starea s(i). Spre deosebire de metoda Divide et Inpera, unde subproblemele rezultate trebuie
sa fie independente, in cadrul acestei metode, subproblemele care apar in descompunere nu sunt independete, iar in descompunerea unei probleme vor aparea subprobleme comune mai multor subprobleme de dimensiuni mai mari. Pentru a fi eficienta, metoda programarii dinamice trebuie sa rezolve fiecare suproblema o singura data si sa memoreze solutia acesteia pentru a o utiliza in cadrul reaparitiei sale in alte subprobleme. Spre deosebire de Divide Et Impera, metoda programarii dinamice opereaza de jos in sus, nerecursiv, si presupune cunoasterea exacta de la inceput a subproblemelor care apar in descompunerea unei probleme. Nu este o tehnica standardizata asa cum este tehnica Backtracking, iar elaborarea algoritmului trebuie sa se bazeze pe cateva principii generale. Din acest motiv, abordarea acestei metode devine anevoioasa si presupune serioase aptitudini de programare, deseori insotite de cunostinte matematice.


### Applications

* LIS
* LCS
