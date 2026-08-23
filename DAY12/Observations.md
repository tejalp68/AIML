# CHAT 1
---
## 1. One-Shot Prompting

**Definition:** The model is given exactly **one example** before being asked to perform the new task.

**Input:**
```
hello --> bonjour
now translate : goodbye
```

**Output:**
```
Goodbye → au revoir 🇫🇷
```

**Observation:**
Only a single example (`hello → bonjour`) was provided as a demonstration before the new query. The model correctly inferred the translation pattern from just one example and applied it to a new word, showing that even minimal demonstration can guide the model's output format and task understanding. This is a classic case of **one-shot prompting**.

---

## 2. Few-Shot Prompting

**Definition:** The model is given **two or more examples** before being asked to perform the new task.

**Input:**
```
hello -> bonjour
thanks -> merci
translate : Goodbye
```

**Output:**
```
au revoir
```

**Observation:**
Here, two examples (`hello → bonjour` and `thanks → merci`) were provided before the new input (`Goodbye`). With more examples, the model has a stronger pattern to generalize from, which can improve reliability and consistency of output, especially for more ambiguous or complex tasks. This demonstrates **few-shot prompting**.

---

## 3. Zero-Shot Prompting

**Definition:** The model is given **no examples** — only a direct instruction or question — and must rely entirely on its pre-trained knowledge.

**Input:**
```
if a train travels 60 km in 1.5 hours, what is its speed?
```

**Output:**
```
Speed = Distance ÷ Time
60 ÷ 1.5 = 40
Answer: 40 km/h 🚆
```

**Observation:**
No examples or demonstrations were given here — just a direct question. The model relied purely on its internal/pre-trained knowledge of the speed formula (Speed = Distance ÷ Time) to solve the problem and produce a correct, well-formatted answer. This illustrates **zero-shot prompting**, useful for straightforward, well-known problem types where explicit examples aren't necessary.

---
# CHAT 2
