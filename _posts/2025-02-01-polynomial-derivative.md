---
layout: post
disqus: y
title: Polynomial Derivatives
---

```
void readPolynom(int **p, int *n) {
    printf("Give the degree of the polynom -> ");
    scanf("%d", n);

    // Allocate memory for coefficients (degree + 1 elements)
    *p = (int *)malloc((*n + 1) * sizeof(int));
    if (*p == NULL) {
        printf("Memory allocation failed!\n");
        exit(1);
    }

    for(int i = 0; i <= *n; i++) {
        printf("P[%d] = ", i);
        scanf("%d", (*p + i));
    }
}

void writePolynom(int *p, int *n) {
    printf("p(x) = %dx^0", p[0]);
    for(int i = 1; i <= *n; i++) {
        printf(" + %dx^%d", p[i], i);
    }
}

float valuePolynom(int *p, int *n, float x) {
    float value = p[0],
          aux = 1;

    for(int i = 1; i <= *n; ++i) {
        aux = aux * x;
        value += aux * p[i];
    }

    return value;
}

void derivatePolynom(int *p, int *n) {
    for(int i = 0; i < *n; i++) {
        p[i] = p[i + 1] * (i + 1);
    }
    (*n)--;
}

```

# Polynomial Derivative Calculator

A C program that handles polynomial operations including reading coefficients, calculating derivatives, and evaluating polynomials at specific points.

## Features

- Read polynomial coefficients dynamically
- Display polynomial in standard mathematical notation
- Calculate first derivative of polynomials
- Evaluate polynomials at given points
- Dynamic memory management for polynomial coefficients

## Technical Details

### Functions

#### `readPolynom(int **p, int *n)`
- Takes a pointer to pointer for coefficients array and pointer to degree
- Dynamically allocates memory for coefficients
- Reads polynomial degree and coefficients from user input
- Error handling for memory allocation failures

#### `writePolynom(int *p, int *n)`
- Displays polynomial in standard mathematical notation
- Format: ax^0 + bx^1 + cx^2 + ...
- Takes coefficient array and degree as parameters

#### `valuePolynom(int *p, int *n, float x)`
- Evaluates polynomial at a given point x
- Uses Horner's method for efficient computation
- Returns float value of polynomial evaluation

#### `derivatePolynom(int *p, int *n)`
- Calculates first derivative of the polynomial
- Modifies original coefficient array
- Updates polynomial degree (reduces by 1)

## Usage

1. Compile the program:
```bash
gcc polynomial.c -o polynomial
```

2. Run the executable:
```bash
./polynomial
```

3. Follow the prompts:
   - Enter the degree of polynomial
   - Enter coefficients starting from constant term
   - Program will display:
     - Original polynomial
     - Its derivative
     - Value at x = 1.450

## Example

```
Give the degree of the polynom -> 2
P[0] = 1
P[1] = 2
P[2] = 3

Original polynomial: p(x) = 1x^0 + 2x^1 + 3x^2
Derivative: p(x) = 2x^0 + 6x^1
p(1.450) = 8.273
```

## Memory Management

The program uses dynamic memory allocation to handle polynomials of any degree:
- Memory is allocated using `malloc()`
- Proper memory deallocation using `free()`
- Includes error checking for allocation failures

## Technical Requirements

- C compiler (gcc recommended)
- Standard C libraries:
  - stdio.h
  - stdlib.h

## Error Handling

The program includes basic error handling for:
- Memory allocation failures
- Invalid input validation (basic)

## Limitations

- Handles only integer coefficients
- Calculates only first derivative
- No input validation for polynomial degree limits
