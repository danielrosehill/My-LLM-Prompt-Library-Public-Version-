---
title: The Basics
og_image: https://docs.bydanielrosehill.com/repos/prompt-library/images/posts/code-gen/coder-sloth-2.webp
og_title: "How To Use LLMs For Code Generation - Intro"
description: "How to leverage large language models (LLMs) to generate and debug code."

---

![alt text](../../images/posts/code-gen/coder-sloth-2.webp)

## How to prompt LLMs for code generation

In case you didn't get the news:

Large language models (LLMs) can be used effectively to generate (and debug) code.

I can't speak for LLMs' abilities at programming in languages I don't use. 

But I've found LLMs to be **reasonably to highly effective** for all of the following use-cases (and more):

## A (very partial) list of some of the languages LLMs can help with:

### YAML

- Fixing messy indentation issues when you've just about reached the end of your tether!  
- Writing Home Assistant automations

### Python

- You name it, LLMs can at least give it a shot  
- I routinely use LLMs to create GUIs that work perfectly on my (Linux) operating system. I've prompted LLM-generated GUIs to do everything from run backup tasks to extract prompts.

### Linux & Bash Scripting

- LLMs can be used to quickly generate Bash scripts for all manner of automation tasks

### SQL

- Stuck on SQL syntax? Can't remember how to define an M2M relationship? LLMs can generate SQL, debug your queries, and much more

### Javascript

- I could go on, but you get the point. Cool feature: LLMs have enough training data that they can even understand the syntax for well-known frameworks like Astro (or MK Docs, which is what I'm using to write this!)

### HTML, CSS

- You name it, they can do it!  
- You can use LLMs to: debug HTML and CSS; generate it; make sure the HTML & CSS you generate is compliant with whatever framework(s) you're using on your project

### PHP

- Stuck on a Laravel/Wordpress project? You guessed it - LLMs can help!

### Markdown, LateX

- I've gone from hating writing in "code" to actually quite enjoying it thanks almost solely to LLMs. Can't figure out why your markdown isn't rendering correctly? 

### Excel, Google Sheets, Gmail

I also routinely use LLMs to:

- Write advanced Google Search queries (Boolean operators, etc)  
- Write Google Sheet formulae  
- Write Gmail filters to clean my inbox

*Etc, etc*

Contrary to what my somewhat/mega-geeky blog/personality may have you believe, I am **not** a programmer (nor an aspiring one!). 

I *love* watching LLMs write code that I can then study and learn whenever I feel the inclination to do so; but I can access and use the working code iimmediately. Something about the way LLMs explain code feels fluent and intelligible to me. 

If it's a toss-up between trying to write a Python script and doing something else with my time, I'll happily choose the latter and hand the job off to AI.

![alt text](../../images/posts/code-gen/make-me-a-program.webp)

## How do you get LLMs to generate code?

When it comes to prompting LLMs to generate code, context is key. 

A question I've been asking myself (and many others undoubtedly too):

Do I need to pay for (say) Github Copilot *and* (say) ChatGPT?

Even if you're *only* using LLMs for code-generation, I would say "yes"!

- Fine-tuned coding LLMs that live in your repo (and have context of it) will naturally be more helpful than prompting a cloud LLM that doesn't see your codebase

BUT:

- You can totally use a cloud-hosted LLM if you just want to (say) generate a quick GUI/script or even get it to debug a single file (or code snippet) in isolation.

## Sample Python GUI Generation Prompt

Here's one of the prompts I have saved in my library for generating a Python GUI,

As always, the guiding principle is specificity

```text
Could you generate a Python GUI.

Here are the functions I would like incorporated.

The user can enter the text of a prompt. This should be a multi line field
The user can enter the title of the prompt. this should be a single line field.

The user can configure two folders:

The first folder is where the prompts will be stored.
The second folder is where the outputs will be stored.

The user can also enter their OpenAI API key.

The GUI should have the ability to retain these settings between sessions. So these variables can be written to a memory file.

The functionality of the GUI should be as follows

The user enters a prompt text. And when ready to execute it, he clicks a button that says Run Prompt

There is a terminal output display field in the UI where the user can monitor the progress of the jobs which the GUI runs.

When the user executes the prompt, it gets sent to the OpenAI API via its API.

When the API returns with an output, the output should be written to the outputs folder. the file name should be the title that the user entered with hyphens replacing spaces

the prompt should be written to the prompts folder with the same file name

when this process completes successfully the terminal output pane should provide a success message and then the output should clear

After the user sends a prompt for execution, the prompt pane should clear so that the user can use it again to send a new prompt
```

### Or use really simple prompts....

If you just have something to debug, and it's (say) a small YAML file, you can simple copy and paste a code-block into a web UI with something incredibly simple, like:

```
This isn't working. Debug it.
```

Assuming that you're working with a common programming language, the LLM should be able to detect what language you're programming in and will even leverage deeper contextual clues to make determinations like the framework you're using. 

Sometimes I just get sick of trying to fix YAML formatting and say:

```
I've messed up the formatting here. Can you fix it?
```