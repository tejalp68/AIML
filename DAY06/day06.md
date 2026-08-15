# DAY 06
```
- Name : Tejal Dadaji Pagar
- Cohort : AIML & TEP cohort 2026
- Day : Friday
- Date : 14/08/2026
- Description : this program involves function is also a value,Iterators, Generators, Decorators, Context Managers
```

# Iterators, Generators, Decorators, Context Managers

so basically these 4 things look totally unrelated when you first see them but they're not, they're all connected under the hood. this readme is just a quick description + explanation of each one and how they tie together.

---

## Iterators

an iterator is basically any object that knows how to give you one value at a time, and knows when to stop. it does this using two methods:

- `__iter__` - returns itself
- `__next__` - gives the next value, or raises `StopIteration` when it's done

that's it. a `for` loop in python is literally just calling `iter()` once and then `next()` again and again in a loop until it hits `StopIteration`.

problem with writing iterators by hand though - you gotta manually track the state yourself (like a counter variable), and for anything complex this gets messy real fast.

---

## Generators

generators are basically the shortcut version of iterators. instead of writing a whole class with `__iter__` and `__next__`, you just write a normal function but use `yield` instead of `return`.

the moment you use `yield`, python turns that function into a generator - it doesn't run all at once, it pauses at `yield`, remembers exactly where it was, and picks back up right there next time you ask for a value.

why this matters - laziness. you can write a generator for an infinite sequence and it won't blow up your memory because it only computes a value when you actually ask for it. you could never do that with a normal list.

---

## Decorators

a decorator is a function that wraps another function to add extra behavior without touching the original function's code. this works because in python, functions are just objects - you can pass them around, return them, wrap them.

`@something` above a function is literally just shorthand for `func = something(func)`.

this relies on something called a closure - basically the wrapper function "remembers" the original function even after the outer function has already finished running. that's the real engine behind decorators.

common uses - logging, timing, caching, auth checks, retries. basically anything you want to run "before or after" a bunch of different functions, without copy pasting the same code everywhere.

---

## Context Managers

a context manager handles setup and guaranteed cleanup, used with the `with` statement. the protocol here is:

- `__enter__` - runs when the `with` block starts
- `__exit__` - runs when the block ends, no matter what, even if an exception happened inside

this solves the problem of stuff like closing files, releasing locks, closing db connections - basically anything where you absolutely need the cleanup to happen, instead of hoping you remembered to write a `try/finally` everywhere.

there's also a shortcut for this too using `@contextmanager` from `contextlib` - you write it as a generator with one `yield` in the middle. everything before the yield is the "enter" part, everything after (in a `finally`) is the "exit" part.

---

## how they're all connected

this is the actual interesting part.

- **generators are just an easier way to build iterators.** every generator automatically follows the iterator protocol, python just writes the `__next__`/state tracking for you behind the scenes so you don't have to.

- **`@contextmanager` is a decorator that turns a generator into a context manager.** this is where all four ideas literally collapse into one thing - it's a decorator, applied to a generator function, that produces something following the context manager protocol. one `yield` splits the function into setup and teardown.

- **decorators are the glue that makes this possible.** they're just the mechanism python gives you to take one kind of object (like a generator function) and turn it into a different kind of object (like a context manager) without changing how it's used.

- underneath all of it is really just one idea repeated - python doesn't care what class something is, it cares whether it has the right methods (`__next__`, `__enter__`, `__exit__` etc). that's basically duck typing formalized. generators and decorators are just convenient syntax so you don't have to write that boilerplate by hand every time.

so the chain looks something like:

```
iterator protocol (manual, verbose)
   -> generators (yield auto-builds the protocol for you, plus laziness)
        -> context manager protocol (manual, verbose)
             -> @contextmanager (decorator + generator = protocol built automatically)
```

and decorators sit around this whole chain as the tool that connects everything together.
