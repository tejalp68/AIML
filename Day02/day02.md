# Day 02 — Python Basics

- Name: Tejal Dadaji Pagar
- Cohort: AIML & TEP cohort 2026
- Day: Monday
- Date: 10/08/2026
- Description:this notebook covers arithmetic operators, string concatenation, string replication, 
 type conversion, round(), abs(), comparison operators, logical operators.
 at the end i also added my energy vault game where all these operators get used.

## variable naming rules

- start with a letter or underscore, not a number
- no spaces allowed
- no special characters like @ # $ %
- can't use python keywords like if, for, class
- case-sensitive, age and Age are different

## what's in the notebook

### 1. Arithmetic operations
- exponent (**) — raises a number to a power, like 7 ** 2
- modulus (%) — gives the remainder after division
- integer division (//) — divides and drops the decimal part
- division (/) — normal division, gives a decimal answer
- multiplication (*) — multiplies two numbers
- addition (+) — adds two numbers
- subtraction (-) — subtracts one number from another

### 2. String operations
- string concatenation — joining two strings together using +
- string replication — repeating a string multiple times using *
- changed a variable's type  — same variable held a number, then a string

### 3. Type conversion
- string to int — using int() to turn text like "123" into a number
- int to string — using str() to turn a number into text
- float to int — using int() to drop the decimal part of a float

### 4. round() and abs()
- round() — rounds a decimal to the nearest whole number
- abs() — turns a negative number into a positive one

### 5. Comparison operators
- == checks if two values are equal
- != checks if two values are not equal
- '>' and '<' used to compare numbers, like finding the biggest among three
- also used to check if a number falls in a range, like 0 to 10

### 6. Logical operators
- and — both conditions need to be true, used in a voting example
- or — even one condition being true is enough, used in a payment example
- not — flips a condition, used in a weather example

### 7. Game — Energy Vault
my own hacker vault game where every level uses a different operator:
- level 1 collect energy (+) — add found energy to your total
- level 2 power boost (*) — multiply energy by a chosen multiplier
- level 3 break laser wall (-) — subtract the laser's energy cost
- level 4 split energy among team (/) — divide energy equally among hackers
- level 5 power full hackers (//) — find how many hackers can be fully powered
- level 6 leftover energy (%) — find the energy left after powering hackers
- level 7 final power (**) — square the final power level
