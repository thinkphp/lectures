---
layout: post
disqus: y
title: Cook–Levin Theorem
---

## Overview

The Cook–Levin Theorem is one of the fundamental results in theoretical computer science and complexity theory. It establishes the first known NP-complete problem and forms the foundation of the theory of NP-completeness.

It was independently proven by **Stephen Cook (1971)** and **Leonid Levin (1973)**.

---

## Statement of the Theorem

The theorem states that:

> **The Boolean Satisfiability Problem (SAT) is NP-complete.**

This means two key properties hold:

### 1. SAT is in NP
Given a candidate assignment of variables (True/False), we can verify whether it satisfies a Boolean formula in polynomial time.

### 2. SAT is NP-hard
Every problem in NP can be reduced to SAT in polynomial time:

\[
\forall L \in NP,\quad L \leq_p SAT
\]

---

## Key Ideas Behind the Proof

The proof is based on the following concepts:

### 1. Verification in NP
Any problem in NP has a polynomial-time verifier. This means that given a solution (certificate), we can check its correctness efficiently.

### 2. Computation as a Boolean Circuit
A nondeterministic polynomial-time computation can be represented as a sequence of logical steps, which can be encoded as a Boolean circuit.

### 3. Encoding Computation into SAT
The computation of the verifier is transformed into a Boolean formula such that:
- The formula is satisfiable if and only if the computation accepts the input.
- Each step of computation is encoded using Boolean variables.

### 4. Polynomial-Time Reduction
The transformation from any NP problem to SAT is done in polynomial time.

---

## Consequences

The Cook–Levin Theorem has major consequences:

### 1. Definition of NP-completeness
It introduced the concept of NP-complete problems.

### 2. Universal Problem
SAT becomes the "universal problem" for NP:
- Any NP problem can be encoded as SAT.
- Solving SAT efficiently would solve all NP problems efficiently.

### 3. Foundation of Reductions
It introduced polynomial-time reductions as a central tool in complexity theory.

---

## Important Implications

- If SAT can be solved in polynomial time, then **P = NP**.
- If P ≠ NP, then SAT cannot be solved efficiently.
- Many important problems (TSP, Subset Sum, Vertex Cover) are NP-complete because they reduce to SAT.

---

## Intuition

The theorem shows that:

> Any efficiently verifiable computation can be encoded as a Boolean formula.

Thus, SAT acts as a universal language for all NP problems.

---

## Summary

- SAT is NP-complete
- Every NP problem reduces to SAT
- Computation can be encoded as logic
- This forms the basis of modern complexity theory

---

## Authors

- Stephen Cook (USA)
- Leonid Levin (independent discovery, USSR)

---

## Conclusion

The Cook–Levin Theorem is the starting point of NP-completeness theory and shows that SAT is the central problem of the class NP.
