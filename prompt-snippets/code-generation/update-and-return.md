---
title: "Make changes, then return the whole program"
---

## Asking an LLM to apply updates then send back script

If you're working on a Python script and you ask an LLM to make a couple of changes, by default many LLMs will assume the (probably better!) role of a helpful educator.

That is to say:

Rather than just say: *"did that, here's your script back*" they will:

- Show you the changes you need  
- Provide snippets

But sometimes, you want to override that behavior and have the LLM just .... do all the work for you.

This snippet works reliably for me if I'm confident in the LLM's ability to not mess up the original code (tip: preserve your previous version before trying this!).

**To ask the LLM to iterate onto `V2`, provide `V1` as its context then prompt:**

> Make the following changes and then return the whole program *with all the changes applied:{change-requests}

To be a bit more explicit, you can also write an instruction like:

>Make the following changes. Then, return an updated version of the program with all those changes applied. Do not output snippets or provide explanations for the edits you made or why you made them. Just output the updated code.