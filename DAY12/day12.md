'''

- Name : Tejal Dadaji Pagar
- Cohort : AIML & TEP cohort 2026
- Day : Sunday
- Date : 23/08/2026
- Description :This file covers prompting techniques , then how function calling works in llms

'''

# Day 12

# Prompting Techniques

![ Prompting Types](prompting_types_overview.png)

## 1. Zero-Shot Prompting

Asking the model to do a task with no examples given.

**Example:**

> "Translate this sentence to French: 'I love reading books.'"

## 2. Few-Shot Prompting

Giving a few examples before the actual task so the model can learn the pattern.

**Example:**

> "English: Hello → French: Bonjour
> English: Thank you → French: Merci
> English: Good night → French: ?"

## 3. Chain-of-Thought (CoT) Prompting

Asking the model to reason step-by-step before giving the final answer.

**Example:**

> "If a store has 10 apples and sells 4, then gets 6 more, how many apples does it have? Think step by step."

![Chain of thought Prompting](chain_of_thought_age_example.png)

## 4. Zero-Shot Chain-of-Thought

Just adding "think step by step" without giving examples.

**Example:**

> "What is 15% of 240? Let's think step by step."

## 5. Role-Based (Persona) Prompting

Assigning a role or identity to the model to shape its tone/expertise.

**Example:**

> "You are an experienced nutritionist. Suggest a healthy meal plan for a diabetic patient."

## 6. Instruction-Based Prompting

Giving clear, direct instructions about the desired output format or behavior.

**Example:**

> "Summarize the following article in exactly 3 bullet points."

## 7. Contextual Prompting

Providing background/context before asking the question.

**Example:**

> "I'm a beginner in Python. Explain what a for-loop is, using simple language."

## 8. Self-Consistency Prompting

Asking the model to generate multiple reasoning paths and pick the most consistent answer (usually done programmatically, not just in one prompt).

**Example:**

> Generate 5 different step-by-step solutions to a math problem, then choose the answer that appears most frequently.

## 9. Prompt Chaining

Breaking a complex task into multiple prompts, where the output of one feeds into the next.

**Example:**

> Prompt 1: "Extract the key points from this article."
> Prompt 2: "Using those key points, write a 2-paragraph summary."

## 10. Tree-of-Thought Prompting

The model explores multiple possible reasoning branches before settling on an answer (more advanced/structured than CoT).

**Example:**

> "Consider three different strategies to solve this puzzle. Evaluate each, then pick the best one."

## 11. Retrieval-Augmented Prompting (RAG-style)

Providing external documents/data as context, then asking questions based on that content.

**Example:**

> "Here is a document about company policy: [text]. Based on this, what is the refund policy?"

## 12. Negative Prompting

Telling the model what NOT to do or include.

**Example:**

> "Write a product description, but do not use exaggerated marketing language."
