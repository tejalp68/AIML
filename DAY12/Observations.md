

## 1. Zero-Shot Prompting

**Definition:**
A model is given a task without any examples.

**Example:**

```text
Translate: Goodbye
```

**Expected output:**

```text
au revoir
```

There are no examples provided to guide the model.

---

## 2. One-Shot Prompting

**Definition:**
A model is given **one example** before being asked to perform a similar task.

**Example:**

```text
hello → bonjour

goodbye → ?
```

**Answer:**

```text
au revoir
```

The single example demonstrates the desired input-output pattern.

---

## 3. Few-Shot Prompting

**Definition:**
A model is given **multiple examples** before receiving the actual task.

**Example:**

```text
hello → bonjour
thanks → merci
Goodbye → ?
```

**Answer:**

```text
au revoir
```

Because two examples were provided, this is **few-shot prompting**.

### Quick comparison

| Technique |  Examples |
| --------- | --------: |
| Zero-shot |         0 |
| One-shot  |         1 |
| Few-shot  | 2 or more |

---

## 4. Role Prompting

**Definition:**
The user assigns the AI a particular role or persona to influence how it responds.

**Example:**

```text
You are a senior doctor.
Explain fever in simple terms.
Formal tone.
```

The prompt contains:

* **Role:** Senior doctor
* **Task:** Explain fever
* **Style:** Simple language
* **Tone:** Formal

The assigned role influences the perspective and style of the response.

---

## 5. Instruction-Based Prompting

**Definition:**
The user gives explicit instructions about the task, format, length, or tone.

**Example:**

```text
Summarize the water cycle in 2 bullet points, formal tone.
```

The instructions specify:

* **Task:** Summarize
* **Subject:** Water cycle
* **Length/format:** 2 bullet points
* **Tone:** Formal

Another example:

```text
Summarize the water cycle in 1 bullet point, formal tone.
```

Changing the instruction changes the required output format.

---

# 6. Structured Output with JSON

JSON can be used to request information in a predictable structure.

### Example request

```text
Extract the user's name and age.
```

### Example output

```json
{
  "name": "John",
  "age": 25
}
```

Here:

* `name` is a string.
* `age` is a number.

---

# 7. JSON Schema

A JSON Schema describes what a valid JSON object should look like.

### Example

```json
{
  "type": "object",
  "properties": {
    "name": {
      "type": "string"
    },
    "age": {
      "type": "number"
    }
  }
}
```

This schema says that:

* The overall value should be an object.
* `name` should contain a string.
* `age` should contain a number.

The schema itself does **not** contain the user's actual information. It only describes the expected structure.

---

# 8. Required Fields in JSON Schema

A field can be marked as required.

### Example

```json
{
  "type": "object",
  "properties": {
    "name": {
      "type": "string"
    },
    "age": {
      "type": "number"
    }
  },
  "required": ["name"]
}
```

Here, `name` must be present.

### Invalid output

```json
{
  "age": 25
}
```

This violates the schema because the required `name` field is missing.

This is an example of a **required-field violation**.

---

# 9. Common JSON Errors

## Missing comma

```json
{
  "name": "John"
  "age": 25
}
```

This is invalid JSON because a comma is missing between the two properties.

### Technical terminology

You can describe this as:

> **JSON syntax error due to a missing comma.**

Other useful terms include:

* Syntax error
* Malformed JSON
* Missing comma delimiter
* Invalid JSON syntax

A precise technical description is:

> "The JSON is malformed because a comma delimiter is missing between two properties."

---

## Wrong Data Type

```json
{
  "name": "John",
  "age": "25"
}
```

If the schema requires `age` to be a number, this violates the schema because `"25"` is a string.

Correct:

```json
{
  "name": "John",
  "age": 25
}
```

---

## Trailing Comma

```json
{
  "name": "John",
  "age": 25,
}
```

The trailing comma after `25` is not valid in standard JSON.

---

## Unquoted Key

```json
{
  name: "John"
}
```

JSON property names must use double quotes.

Correct:

```json
{
  "name": "John"
}
```

---

# 10. Prompting vs. JSON

These concepts solve different problems.

**Prompting techniques** control how the model is guided:

```text
Zero-shot
One-shot
Few-shot
Role prompting
Instruction-based prompting
```

**JSON / JSON Schema** controls how information can be structured and validated:

```text
Objects
Properties
Data types
Required fields
Schema validation
Syntax
```

They can also be combined.

### Example

```text
You are a data extraction assistant.

Extract the user's name and age from the following text.
Return the result as JSON.

John is 25 years old.
```

Expected structure:

```json
{
  "name": "John",
  "age": 25
}
```

---
