# Python Data Types Cheatsheet

---

## 1. Numbers — `int` and `float`

| Data type | Examples |
|---|---|
| Integer (`int`) | `-2, -1, 0, 1, 2, 3` |
| Floating-point (`float`) | `-1.25, -1.0, 0.0, 0.5, 1.25` |

> An `int` mixed with a `float` in math always evaluates to a `float` (`3 + 4.0` → `7.0`). The `/` operator always returns a `float`, even when dividing two ints evenly (`16 / 4` → `4.0`).

### Math operators (highest to lowest precedence)

| Operator | Operation | Example | Result |
|---|---|---|---|
| `**` | Exponent | `2 ** 3` | `8` |
| `%` | Modulus/remainder | `22 % 8` | `6` |
| `//` | Integer (floor) division | `22 // 8` | `2` |
| `/` | Division | `22 / 8` | `2.75` |
| `*` | Multiplication | `3 * 5` | `15` |
| `-` | Subtraction | `5 - 2` | `3` |
| `+` | Addition | `2 + 2` | `4` |

`**`, then `* / // %` (left to right), then `+ -` (left to right). Use `()` to override.

### Augmented assignment operators

| Operator | Equivalent to |
|---|---|
| `spam += 1` | `spam = spam + 1` |
| `spam -= 1` | `spam = spam - 1` |
| `spam *= 1` | `spam = spam * 1` |
| `spam /= 1` | `spam = spam / 1` |
| `spam //= 1` | `spam = spam // 1` |
| `spam %= 1` | `spam = spam % 1` |
| `spam **= 1` | `spam = spam ** 1` |

### Comparison operators
`==`  `!=`  `<`  `>`  `<=`  `>=`

### Boolean operators
`and`  `or`  `not` — evaluated after comparison operators, `not` first, then `and`, then `or`.

---

## 2. Strings (`str`)

```python
'single quotes'
"double quotes (lets you include ' without escaping)"
'''triple-quoted strings can span multiple lines'''
```

### Escape characters

| Escape | Meaning |
|---|---|
| `\'` | Single quote |
| `\"` | Double quote |
| `\t` | Tab |
| `\n` | Newline |
| `\\` | Backslash |
| `r'...'` | **Raw string** — ignores all escape characters (useful for file paths/regex) |

### Concatenation, replication, membership

```python
'Alice' + 'Bob'      # 'AliceBob'  (str + str)
'Alice' * 5          # 'AliceAliceAliceAliceAlice'  (str * int)
'a' in 'apple'        # True
'x' not in 'apple'    # True
```

### Indexing and slicing (strings act like a list of characters)

```python
spam = 'Hello world!'
spam[0]        # 'H'
spam[-1]       # '!'          negative index counts from the end
spam[0:5]      # 'Hello'      slice: start included, end excluded
spam[:5]       # 'Hello'      omit start = from beginning
spam[6:]       # 'world!'     omit end = to the end
spam[:]        # copy of the whole string
```

### Useful string methods

| Method | Purpose |
|---|---|
| `.upper()` / `.lower()` | Return new string in all upper/lowercase |
| `.isupper()` / `.islower()` | `True` if string has case AND matches |
| `.isalpha()` | True if letters only, not blank |
| `.isalnum()` | True if letters/numbers only, not blank |
| `.isdecimal()` | True if numbers only, not blank |
| `.isspace()` | True if spaces/tabs/newlines only, not blank |
| `.istitle()` | True if title-cased (`'This Is Title Case'`) |
| `.startswith(s)` / `.endswith(s)` | True/False test |
| `.join(list)` | Joins a list of strings using the string as separator: `', '.join(['cats','rats'])` → `'cats, rats'` |
| `.split(sep)` | Splits a string into a list: `'My name is Al'.split()` → `['My','name','is','Al']` |
| `.strip()` / `.lstrip()` / `.rstrip()` | Remove whitespace (or given chars) from both/left/right |
| `.rjust(n)` / `.ljust(n)` / `.center(n)` | Pad string to width `n` (right/left/center-justify) |
| `.replace(old, new)` | Replace all occurrences |
| `.find(sub)` | Index of first occurrence, or `-1` |
| `len(spam)` | Number of characters |

### Formatting strings — f-strings (preferred)

```python
name, age = 'Al', 4000
f'My name is {name}. I am {age} years old.'
f'The sum is {2 + 2}.'          # expressions allowed inside {}
f'{{literal curly braces}}'     # double braces to escape
```

Older alternatives you may still see: `'%s is %s.' % (name, age)` and `'{}  is {}.'.format(name, age)`.

### Type conversion functions
`str(42)` → `'42'`  |  `int('42')` → `42`  |  `float('3.14')` → `3.14`

---

## 3. Lists (`list`) — mutable, ordered sequences

```python
spam = ['cat', 'bat', 'rat', 'elephant']
```

### Indexing and slicing (same rules as strings)

```python
spam[0]        # 'cat'
spam[-1]       # 'elephant'
spam[1:3]      # ['bat', 'rat']
spam[:2]       # ['cat', 'bat']
spam + ['x']   # concatenation → new list
spam * 2       # replication → new list
```

### Changing values / `del`

```python
spam[1] = 'aardvark'   # replace an item
del spam[2]             # remove item at index 2
```

### List methods

| Method | Purpose |
|---|---|
| `.append(v)` | Add `v` to the end (in place) |
| `.insert(i, v)` | Insert `v` at index `i` (in place) |
| `.remove(v)` | Remove the **first** matching value (raises `ValueError` if absent) |
| `.pop(i)` | Remove & return item at index `i` (default: last item) |
| `.index(v)` | Return index of first match (raises `ValueError` if absent) |
| `.sort()` | Sort in place (`reverse=True` for descending; `key=str.lower` for case-insensitive) |
| `.reverse()` | Reverse the list in place |
| `.count(v)` | Count occurrences of `v` |
| `len(spam)` | Number of items |
| `sorted(spam)` | Return a **new** sorted list (doesn't modify original) |

> `.append()`, `.insert()`, `.sort()`, and `.reverse()` all modify the list **in place** and return `None` — don't write `spam = spam.append(x)`.

### Looping with index

```python
for i, item in enumerate(spam):
    print(i, item)
```

### Multiple assignment (unpacking)

```python
cat = ['fat', 'orange', 'loud']
size, color, disposition = cat
```

### List of lists

```python
grid = [['A', 'B'], ['C', 'D']]
grid[1][0]   # 'C'
```

### `in` / `not in`
```python
'rat' in spam
'dog' not in spam
```

---

## 4. Tuples (`tuple`) — immutable, ordered sequences

```python
eggs = ('cat', 'bat', 105.5)
eggs[0]         # 'cat'  — indexing/slicing work like lists
eggs[0] = 99    # TypeError: tuples cannot be modified
```

- Written with parentheses `()` instead of `[]`.
- A one-item tuple needs a trailing comma: `('cat',)` — otherwise it's just a value in parentheses.
- Faster and "safer" than lists since they can't be accidentally changed.
- Convert between the two: `tuple(['a','b'])` and `list(('a','b'))`.

---

## 5. Dictionaries (`dict`) — unordered key-value pairs

```python
my_cat = {'size': 'fat', 'color': 'gray', 'disposition': 'loud'}
my_cat['size']          # 'fat'
my_cat['age'] = 4        # add a new key
```

- Keys can be any immutable type (str, int, float, tuple); unlike lists, dicts aren't compared by order — `{'a':1,'b':2} == {'b':2,'a':1}` is `True`.
- Looking up a missing key raises `KeyError`.

### Dictionary methods

| Method | Purpose |
|---|---|
| `.keys()` | View of all keys (loop or wrap in `list()`) |
| `.values()` | View of all values |
| `.items()` | View of `(key, value)` tuples |
| `.get(key, default)` | Return value, or `default` if key doesn't exist (avoids `KeyError`) |
| `.setdefault(key, default)` | Set the key to `default` **only if** it doesn't already exist; returns the value either way |
| `.update(other_dict)` | Merge another dict's keys/values in |
| `.pop(key)` | Remove key and return its value |

```python
for k, v in my_cat.items():
    print(k, v)

'color' in my_cat.keys()      # membership check on keys
'gray' in my_cat.values()     # membership check on values
```

---

## 6. Sets (`set`) — unordered collections of unique items

```python
s = {'cat', 'dog', 'cat'}   # duplicates auto-removed → {'cat', 'dog'}
s.add('bird')
s.remove('dog')
'cat' in s                   # fast membership test
s2 = {'dog', 'bird'}
s | s2   # union
s & s2   # intersection
s - s2   # difference
```

Use curly braces like a dict, but with single values instead of key-value pairs. `set()` creates an empty set (`{}` creates an empty **dict**, not a set).

---

## 7. Booleans and `None`

```python
True, False        # bool type — capitalized, no quotes
spam = None         # represents "no value" — its own type, NoneType
```

- `bool(0)`, `bool('')`, `bool([])`, `bool({})`, `bool(None)` → all `False` (falsy)
- Anything else is generally truthy.

---

## 8. Checking a value's type

```python
type(42)         # <class 'int'>
type(3.14)       # <class 'float'>
type('hi')       # <class 'str'>
type([1,2])      # <class 'list'>
type((1,2))      # <class 'tuple'>
type({'a':1})    # <class 'dict'>
type({1,2})      # <class 'set'>
isinstance(42, int)   # True
```

---

## 9. Mutable vs. Immutable — quick reference

| Mutable (can change in place) | Immutable (cannot change) |
|---|---|
| `list`, `dict`, `set` | `int`, `float`, `bool`, `str`, `tuple`, `NoneType` |

This matters for variable assignment: two variables pointing to the same **mutable** object (e.g., a list) both see changes made through either name, since both are references to the same object in memory. Immutable values are always copied by value, not by reference, when reassigned.