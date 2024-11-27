---
title: "Is this the best way to do this?"
---

# Here's a prompt, how could I use an LLM most effectively?

The idea with this prompting strategy is pretty simple:

You show an LLM a prompt which reflects something that your'e trying to achieve using an LLM.

But rather than ask the LLM to *do* something, you ask it to advise upon *how* you should use an LLM to do this.

I find this strategy very useful when (for example) there are a few potential ways to achieve the same objective.

Take the below example: I took a fairly basic assistant configuration text, but then used the LLM to take me a step back.

Roughly saying something like:

> Let's pause for a moment. Is configuring this as an assistant actually the most logical way to achieve this pretty simple job? What about using a prompt template? Or ... perhaps you can think of a better idea again?

Like many, this prompting strategy works off the assumed premise that LLMs have good foundational/domain knowledge about prompt engineering and LLMs  - which isn't always a safe one.

*However* - if your LLM has a recent training data cuttoff point, I've found they can often bring some creative thinking to the table and help you discover more effective ways of using the tech.

## Example Prompt

Here's a draft configuration for an LLM assistant. Do you think the best way to implement this would be:

1) As a custom assistant
2) As a prompt template
3) Using some other method

Provide both your recommendation and reasoning

---

## Model Configuration (Added As Context)

```text
## Foundational instruction

I'm gathering a list of VS Code extensions that have to do with prompt engineering and working with LLMs.

Here's an example of an extension that's interesting to me:

https://marketplace.visualstudio.com/items?itemName=HuggingFace.huggingface-vscode

To speed up the process, I'd like to establish the following workflow:

1: I'll populate a link into the chat, like:

https://marketplace.visualstudio.com/items?itemName=HuggingFace.huggingface-vscode

2: You will respond with exactly the following, enclosed within a markdown codeblock:

# Extension Name (Publisher Name)

(Shields.io install count badge)

Installation code for command pallette

1 line description

## For example

```
# [llm-vscode (Hugging Face)](https://marketplace.visualstudio.com/items?itemName=HuggingFace.huggingface-vscode)

![Visual Studio Marketplace](https://img.shields.io/visual-studio-marketplace/v/HuggingFace.huggingface-vscode?label=VS%20Code%20Marketplace&logo=visual-studio-code&style=for-the-badge)
![Installs](https://img.shields.io/visual-studio-marketplace/i/HuggingFace.huggingface-vscode?label=Installs&style=for-the-badge)
 
llm-vscode is an extension for all things LLM. It uses llm-ls as its backend.

Install code:
`ext install HuggingFace.huggingface-vscode`
```