# Day 11 

'''

- Name : Tejal Dadaji Pagar
- Cohort : AIML & TEP cohort 2026
- Day : Saturday
- Date : 22/08/2026
- Description : so this notebook is basically a hands-on tour of "how does an LLM actually work under the hood" — starting from generating text, all the way to tokenizers

'''

# LLM Working

## Setup

Nothing fancy here, just installing the usual suspects:
```
transformers, torch, sentence-transformers, gensim, tiktoken
```
And pre-downloading a couple of models so things don't stall mid-lecture — mainly `Qwen2.5-0.5B` (base) and `Qwen2.5-0.5B-Instruct` (instruct), plus `bert-base-uncased` and `gpt2` tokenizers.

## §1 — Generating your first text + the 3 knobs

We spin up a `text-generation` pipeline with the instruct model and just ask it "what is capital of france?" — nothing crazy.

The important bit is the **3 knobs** you can turn:

1. **`max_new_tokens`** — how many tokens you let the model spit out before it stops. Small number = short/cut-off answer.
2. **`do_sample`** — `False` means greedy decoding (always pick the most likely next token → same output every time). `True` means it samples from the probability distribution → different output each run, more "creative"/random.
3. **`return_full_text`** — whether you get your prompt + generated text back, or just the newly generated part.

Basically: these three control *how long*, *how random*, and *how much text* you get back.

## §2 — Base model vs Instruct model

Same exact model family, same size (`Qwen2.5-0.5B`) — the only difference is the **base** one hasn't gone through instruction-tuning (phase 2 of training), while the **instruct** one has.

We ask both the same question directly, and:
- **Base model** — tends to just continue the text like autocomplete, doesn't really "answer" like a chatbot.
- **Instruct model** — actually responds like an assistant, because it's been fine-tuned to follow instructions/chat format.

We also peek at what `apply_chat_template()` does — it wraps your plain question into the special chat format (with role tags etc.) that the instruct model was trained to expect. That's literally why instruct models behave differently — the input itself is structured differently.

## §3 — Inside the tokenizer

This is the "text isn't magic, it's numbers" section.

- **`input_ids`** — every model doesn't see words, it sees a list of integer IDs. We tokenize a weird string like `"    hey!@1\`"` and print the raw ID list + how many tokens it became.
- **Decoding one token at a time** — looping through each ID and decoding it individually shows you that a single "word" can be split into multiple sub-word tokens (e.g. `"unbelievable"` might become `un` + `believ` + `able`). This is the classic "words arrive in pieces" idea — tokenizers don't work at the word level, they work at the sub-word level.

## §4 — Tokenizer comparison

Here we compare how different tokenizers (`bert-base-uncased`, `gpt2`, `gpt-4`'s `cl100k_base`, `Qwen2.5-0.5B`, `Qwen2.5-Coder-0.5B`) chop up the *same* text, with color-coded blocks so you can literally see the token boundaries.

Things it demonstrates:
- **Mixed content** (English + CAPS + emoji + symbols + numbers) → tokenizers split this very differently depending on their vocab.
- **Code / indentation** → some tokenizers handle whitespace/indentation more efficiently than others (matters a lot for code models).
- **Non-English text** (English vs Hindi) → non-English text usually needs *way* more tokens for the same meaning — meaning it's more expensive/slower to process. That's a real, practical limitation of most tokenizers.
- **Emoji handling** → some tokenizers represent emojis as a single token, others break them into multiple byte-level tokens.
- **Whitespace changes the IDs** → literally adding an extra space changes the token IDs completely. Tokenization is *very* sensitive to whitespace.
- **Letters are invisible inside a token** → this is why LLMs are famously bad at things like counting letters in "strawberry" or comparing `9.11` vs `9.9` — the model isn't seeing individual letters/digits, it's seeing whole chunks (tokens), so character-level reasoning doesn't come naturally to it.

### TL;DR — what today's notebook is really teaching

| Concept | Key takeaway |
|---|---|
| Generation knobs | Control length, randomness, and output format |
| Base vs Instruct | Instruction-tuning is what makes a model "chat-like" |
| Tokenization | Models see sub-word tokens, not words or letters — explains weird LLM failures |
| Tokenizer comparison | Different tokenizers = different efficiency, especially for code/non-English |

