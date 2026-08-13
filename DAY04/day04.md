# Day 04 — Functions and Error Handling

- Name: Tejal Dadaji Pagar
- Cohort: AIML & TEP cohort 2026
- Day: Wednesday
- Date: 12/08/2026
- Description: this notebook covers function definition, function calling, parameters vs arguments,
  return values, global scope, local scope, and error handling using try/except.

## what's in the notebook

### 1. Functions basics
- defining a function — using def to create a function, like hello()
- calling a function — running the function by writing its name with ()
- calling multiple times — same function can be called again and again, like hello() three times in a row

### 2. Parameters and arguments
- parameter — the variable written in the function definition, like a, b in add(a, b)
- argument — the actual value passed when calling the function, like num1, num2 in add(num1, num2)
- argument gets stored in parameter when the function runs

### 3. Return values
- return — sends a value back from the function instead of just printing it
- used return in add(a, b) to get the sum back and store it in a variable
- None — used when a value is absent

### 4. Local scope
- a variable created inside a function only exists inside that function
- tried printing eggs from inside spam() function, only works within it

### 5. Global scope
- a variable created outside all functions is global, accessible everywhere
- rule of same name — if a local variable has the same name as a global one, python uses the local value inside the function
- global variable stays unaffected outside the function, even if local one changes

### 6. Exception handling
- try block — code that could potentially fail goes here, python tries to run it normally
- except block — if an error occurs in try, this block handles it instead of crashing the program
- handled ZeroDivisionError using try/except in a divide function

7. Animation program

- a small sliding animation to see try/except handle a real interruption:
  
- prints a line of ******** and increases the indent a bit each time
- once indent hits max, it's supposed to start decreasing — creating a back and forth sliding effect
- runs inside an infinite while True loop so it keeps going continuously
- wrapped in try/except KeyboardInterrupt, so pressing Ctrl+C exits the program cleanly using sys.exit() instead of crashing
