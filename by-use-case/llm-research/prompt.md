---
title: "Understanding LLM capabilities by prompt"
---

This is an interesting prompting strategy that attempts to use LLMs to understand, from a prompt, what kind of capabilities would be required by a model to effectively deliver a useful output in response to it.

This can be interesting because it can provide insight not only into the capabilities a prompt demands of an LLM, but also what kind of capabilities a prompt might demand for augmented information retrieval.

## Prompt example:

Here's an example prompt:

Summarise this page of documentation:

https://www.librechat.ai/docs/configuration/librechat_yaml/ai_endpoints/openrouter

Please explain: 

- What capabilities an LLM API would need to perform this task

## Other Notes

This is a very light example. 

You can elaborate greatly upon this structure, like:

>If I were to prompt as follows: {prompt} what processes would the LLM be required to undertake during its inference in order to deliver the kind of output that you can assume I would be expecting based upon the way the prompt is written.
