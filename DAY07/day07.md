# DAY 07

- **Name:** Tejal Dadaji Pagar
- **Cohort:** AIML & TEP cohort 2026
- **Day:** Sunday
- **Date:** 16/08/2026
- Description :Basically this notebook is about numpy library, diff between list and array, some array operations, and how to get/post data from a website

## Topics covered

### 1. Libraries 
- Started with `math` library, used `math.sqrt()` to find square root.
- Also made my own `sqrt()` function just to check.
- Talked about what libraries are used for in general — math/calc, graphs, databases, files, web scraping, data processing, ML models, dates/time, internet stuff.

### 2. Numpy basics
- Installed/updated numpy (`pip install --upgrade pip`), then imported it as `np`.
- Made a normal python list and a numpy array, checked their `type()`.

### 3. List vs Array (the main diff)
| List | Array |
|---|---|
| can store different data types together | stores same data type only |
| operation happens on one element at a time | operation happens on all elements at once |
| not organized | organized |

Showed this with an example — multiplying every element by 2. In list you gotta loop through it, in array you just do `arr * 2` directly. Array is way easier for this.

### 4. Creating arrays
- `np.ones()` → array full of 1s
- `np.zeros()` → array full of 0s
- `np.arange()` → same as range() but gives array
- `np.zeros([2,2])` → 2D array of zeros

### 5. Accessing & changing elements
- How to get an element by index `numbers[2]`
- How to change an element `numbers[1] = 99`
- Compared with list — same-ish but list can't do direct math operations like `numbers + 5`, array can.

### 6. Array math (this is where numpy shines)
- Add, multiply, divide directly on arrays: `numbers + 5`, `numbers * 2`, `numbers / 10`
- Adding/multiplying two arrays together: `a + b`, `a * b`

### 7. Useful numpy functions
- `np.sum()` → total
- `np.mean()` → average
- `np.max()` / `np.min()` → highest/lowest value
- `.shape` → tells rows and columns of a 2D array
- Indexing 2D array like `num[0,1]`

### 8. Mini example — Students marks
Used everything above on a marks array to print total, average, highest, and lowest marks. Small practice problem basically.

### 9. Working with websites (requests)
- Used `urllib.request` first to hit a website and check status code (200 = success).
- Then used the `requests` library (easier way) — `req.get()`, checking `status_code`, `response.text`.
- `raise_for_status()` — auto raises error if something's wrong (like 404, 500).
- `response.json()` — to get data as a proper python object instead of just text. Tried this with github api (`api.github.com/users/octocat`).
- Last part: difference between **GET** (asking for data) and **POST** (sending data), with quick examples of both.
