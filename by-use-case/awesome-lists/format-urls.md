---
title: "Format URLs for an Awesome list (etc)"
---

# Foundational prompt for formatting URLs for Awesome list 

Could be reconfigured slightly so that it's the configuration instruction for an agent/assistant.


## Foundational instruction

I'm gathering a list of VS Code extensions that have to do with prompt engineering and working with LLMs.

Here's an example of an extension that's interesting to me:

`https://marketplace.visualstudio.com/items?itemName=HuggingFace.huggingface-vscode`

To speed up the process, I'd like to establish the following workflow:

1: I'll populate a link into the chat, like:

`https://marketplace.visualstudio.com/items?itemName=HuggingFace.huggingface-vscode`

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

## Usage

If the configuration instruction worked, you should be able to just paste a URL and get exactly the desired template back in a codeblock for easy population into your markdown file.

## Delimeters

For custom agents supporting dynamic prompting and limited real time search retrieval, you can limit search activity to this URI:

`marketplace.visualstudio.com`
