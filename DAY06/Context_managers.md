# Day 06 — Context Managers
- Name: Tejal Dadaji Pagar
- Cohort: AIML & TEP cohort 2026
- Day: Friday
- Date: 14/08/2026
- Description: this is documentation of context managers in python

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

### Gradient
- A gradient is basically the slope — it tells you how much a value changes when you slightly change something else.
- In ML terms: if you tweak a weight a little bit, the gradient tells you how much the loss (error) will change because of that tweak, and in which direction.
  - If gradient is positive → increasing the weight increases the loss (bad, so decrease the weight)
  - If gradient is negative → increasing the weight decreases the loss (good, so increase the weight)
#### 2. How training uses gradients

- Training a model = repeating this loop:
- 1. Pass data through model → get a prediction
- 2. Compare prediction to actual answer → calculate loss (error)
- 3. Calculate gradient of loss with respect to every weight (this needs gradient tracking, since it uses chain rule going backward through all operations — this step is called backpropagation)
- 4. Update weights a little bit using those gradients (this step is called optimization, like using SGD or Adam)
- 5. Repeat with next batch of data
     
### Inference 
- Inference = using an already-trained model to make a prediction on new data.
- Example: your model already learned to detect cats vs dogs, now you show it a new image and just want the answer — "cat" or "dog." You're not updating the model anymore, just using it.
- Since you're not updating weights, you don't need gradients here — that's exactly why torch.no_grad() is used during inference.

### Evaluation
- Evaluation = checking how good your trained model is, usually on a validation/test dataset it hasn't seen during training.
- It's technically also just doing inference (predictions) — but the goal is different:

- Inference → you care about the actual prediction (real-world use)
- Evaluation → you care about measuring accuracy/performance (checking how well model did)

- Both don't need gradient tracking, since no training/weight-updating is happening in either case


## what is this thing

context manager is basically something that do setup + cleanup automatically for you. you dont have to remember to close file, release lock, etc. python do it for you.

used with `with` keyword.

```python
with open('file.txt') as f:
    data = f.read()
# file auto closed here, no need f.close()
```

---

## why we need this

normal way (without context manager) - you have to remember close it yourself:

```python
f = open('file.txt')
data = f.read()
f.close()   # if you forget this = problem. file stay open forever
```

with `with` statement - cleanup happen automatically, even if error come in between. so no tension of forgetting.

---

## how it work internally

context manager = any object which have these 2 methods:

- `__enter__()` -> setup part, runs when `with` block start
- `__exit__()` -> cleanup part, runs when `with` block end (even if error come or not)

```python
class MyCM:
    def __enter__(self):
        print("enter - setup")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("exit - cleanup")

with MyCM():
    print("doing work here")
```

output:
```
enter - setup
doing work here
exit - cleanup
```

---

## easy way to make own context manager

instead of using class, `contextlib` also give a shortcut:

```python
from contextlib import contextmanager

@contextmanager
def my_cm():
    print("enter")   # this is setup
    yield              # here with block code run
    print("exit")     # this is cleanup

with my_cm():
    print("inside")
```

- code before `yield` = setup
- code after `yield` = cleanup

---

## most used context managers (real use)

### 1. open() - file handling
```python
with open('file.txt') as f:
    data = f.read()
# auto close
```

### 2. threading.Lock() - when multiple threads using same data
```python
with lock:
    counter += 1
# auto release
```

### 3. contextlib.suppress() - to ignore specific error

```python
from contextlib import suppress
with suppress(ZeroDivisionError):
    x = 1/0
# error will come but program not crash
```

### 4. sqlite3.connect() - database transactions

```python
with sqlite3.connect('data.db') as conn:
    conn.execute("INSERT INTO users VALUES (1,'Alice')")
# everything auto save (commit), if error come then auto undo (rollback)
```

### 5. tempfile.TemporaryDirectory() - for making temp folder

```python
with tempfile.TemporaryDirectory() as tmpdir:
    # use tmpdir
    pass
# folder auto delete after
```

### 6. torch.no_grad() - for ML/pytorch, turn off gradient tracking

```python
with torch.no_grad():
    predictions = model(test_data)
# not training, so no need to track gradient, this make it fast
```


> `with` = cleanup guaranteed as soon as work finish, whether error come or not. thats why we use it, no need to take tension of manual close/release.
