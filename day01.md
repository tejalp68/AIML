'''
Name : Tejal Dadaji Pagar
- Cohort : AIML & TEP cohort 2026
- Day : Sunday
- Date : 09/08/2026
- Description :This program covers variables & data types, typecasting(str to int, int to str, and using pandas to_numeric),
- string indexing/slicing, list indexing/slicing,if-else conditions to check student attendance, and for loop & while loop examples

'''

# Why Python

1. Easy to read and write
2. large num of library's
3. easy to use
4. icreases readability
5. easy to understand

### virtual environment for python

venv is an virually created environment for python.we use it to create a separate space for each project.The dependencies downloaded in that project will be only accesible to that project.so using this we can download diff versions of each library or language.

#### Need

1. diff project need diff versions of python or its libraries
2. globally downloaded package can cause conflicts
3. venv gives each project a diff space
4. like a shoe rack,or CLOSET

## Visual Studio code

1. It is a free code editor
2. entire code executed at once

## Google collab / Jupyter Notebook

_Google collab_ is a free notebook environment which works on browser(Google server).nothing is installed on laptop
Key points:

1. Runs on Google's servers, not your computer
2. lets write code in cells,need internet connectivity.
3. Colab gives access to a virtual machine with a specific CPU and RAM configuration when you create a notebook, plus optional GPU/TPU access
4. Free tier gives roughly 12–13 GB of system RAM, and lets you run 2 notebooks at once.
5. For GPU: free tier typically gives a Tesla T4 or K80 GPU with 12GB GPU memory
6. Files/data usually don't persist after the session ends unless saved to Google Drive
7. Great for ML/AI work since heavy computation happens on Google's hardware, not yours

_Jupyter Notebook_ is a free notebook creation environment which works locally on your computer
Key points:

1. Runs using YOUR computer's RAM, CPU, GPU (no free cloud GPU) Needs to be installed (usually via Anaconda or pip)
2. No internet required once installed
3. Full control, no time limits, no session disconnects
4. RAM/GPU = whatever your own machine has

## debugging

a guide that tell what to improve

## Python

**Variables**
A container to store a value

Constrains

1. Can contain letters, numbers, and underscore ( \_ )
2. Cannot start with a number → 1name ❌, name1 ✅
3. Cannot use spaces → use \_ instead → student_name ✅
4. Case-sensitive → Name and name are different variables
5. Cannot use Python keywords as variable names → class, if, for, etc. ❌

**Data type in Python**

1. int
2. float
3. string
4. complex
5. bool
6. none type

7. list tuple range (seq types)
8. dict(mapping)
9. set,frozenset
10. binary types

# String

**Indexing**

- Sarts from 0 from left
- from right starts with -1

**slicing**
[ start : stop : step ]
ex.[:5]

# List

- list is a data type that contains diff ele of diff data types

```python
lst =[1,"Abc","sabnam",45,44.5,True]
```

- indexing and slicing is same as the string
  but the diff is tht the single ele is consider as single index

# Dict

- Dict is data type is data type which includes key-value pair
- methods
  - key.items()
  - key.values ()
  - key.items()

# tuple

- tuple is immutable (cannot make changes)
- Methods
  - count(value) Returns the number of times a given value appears in the tuple
  - index(value) Returns the index of the first occurrence of a given value (raises error if not found)
    Examples

```python
t = (1, 2, 3, 2, 5, 2)

t.count(2)     # 3   → 2 appears 3 times
t.index(3)     # 2   → 3 is at index 2
```

# Conditional statements

## if only

- executes only if it becomes true
- otherwise next line executes

## if else

- if block executes when its has True value
- else block executes when if block becomes false

## if elif else

- used when we have to give multiple conditions
- elif executes when if block becomes false
- if elif becomes false then else executes

# For loop

- used when number of repetitions are known
- works with sequences

# While Loop

- used when number of repetition is depend on a condition
- it works until the condition becomes false
- runs until the condition is true
