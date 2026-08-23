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
---

1. Natural Language Query (Direct Answer)

Input:

what is the weather in pune

Output:

Pune right now is around 29°C with a shower, and today looks like a mix of
sunny spells and occasional showers.
The next few days stay pretty monsoon-y, with temperatures around 28–29°C
and intermittent showers/thunderstorms.
(Includes a 7-day forecast card: Sun 29°/22°, Mon 29°/23°, Tue 29°/22°,
Wed 29°/23°, Thu 29°/23°, Fri 28°/24°, Sat 29°/26°, Sun 29°/26°)

Observation: The model answered directly from a live weather lookup/tool integration, returning real-time data (current temperature, condition, hourly trend, and a multi-day forecast). No code or function was involved — this is a direct natural language → natural language response backed by an external data source (a weather tool/API called internally by the assistant).

2. Code Generation Request (Function Simulation)

Input:

write a function to get_weather(city) and shows how it would call it for pune

Output:

python
def get_weather(city):
    # In a real program, you'd call a weather API here.
    return f"The weather in {city} is sunny and 29°C."


# Call the function for Pune
weather = get_weather("Pune")
print(weather)

Result when run:

The weather in Pune is sunny and 29°C.

Observation: Here the request shifted from asking for live weather data to asking for code that demonstrates the concept. Since no real API key/tool was wired into the generated code, the model produced a stubbed/mocked function with a hard-coded return value rather than an actual API call. It correctly demonstrated the calling convention (get_weather("Pune")) and used Pune as the example city per the request, but explicitly noted that a real implementation would need an actual API call instead of hard-coded data. This shows the model's ability to translate a conceptual request into working, illustrative code while being transparent about its limitations.
