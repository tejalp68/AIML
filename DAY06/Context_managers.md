# Day 06 — Context Managers
- Name: Tejal Dadaji Pagar
- Cohort: AIML & TEP cohort 2026
- Day: Friday
- Date: 14/08/2026
- Description: this program is assignment of context managers in python

## what's in the notebook

### 1. with statement
- with guarantees setup and cleanup automatically, no need to close file manually
- opened and wrote to a file using with open()
- read a file line by line using readline()
- handled FileNotFoundError using try/except/finally

### 2. custom context manager class
- made my own class using __init__, __enter__ and __exit__
- __init__ runs first when object is created
- __enter__ runs when with block starts
- __exit__ runs automatically when with block ends, even if error happens
- built a FileManager class that opens file in __enter__ and closes it in __exit__

### 3. reading files
- readline() reads one line at a time
- read() reads everything, and cursor moves to end so calling read() again gives blank
- learned why storing result in a variable matters, since cursor position changes after reading

### 4. exc_type, exc_val, exc_tb in __exit__
- exc_type — type of exception, like ZeroDivisionError
- exc_val — the actual error message
- exc_tb — traceback, tells where error occurred in code
- if no error happens all three come as None

### 5. handling errors inside context manager
- if __exit__ returns True, python ignores the error and program continues normally
- tested this with ZeroDivisionError, string + int error, and ValueError from int() conversion
- without returning True, the error would stop the program like normal

### 6. torch.no_grad() vs tf.GradientTape()
- torch.no_grad() (PyTorch) — turns gradient tracking OFF, used during inference/testing so it doesn't waste memory
- tf.GradientTape() (TensorFlow) — turns gradient tracking ON, used during training to actually compute gradients
- both are context managers, just opposite purpose — one turns tracking off, other turns it on

# 
