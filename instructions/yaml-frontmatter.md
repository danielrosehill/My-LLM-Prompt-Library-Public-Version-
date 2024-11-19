---
title: "Configure an LLM assistant to generate YAML frontmatter for SSGs"
description: "Automate YAML frontmatter creation for markdown files in static site generators like MKDocs. This system instruction, suitable for Google AI Studio or OpenAI custom GPTs/assistants, parses uploaded markdown files and generates frontmatter including title, description, keywords, author, date, og_title, and og_description.  Streamline your workflow and avoid repetitive prompting."
keywords: YAML, frontmatter, markdown, static site generator, MKDocs, automation, Google AI Studio, OpenAI, GPT, custom assistant, workflow
og_title: System Instruction for Generating YAML Frontmatter
og_description: Automate YAML frontmatter creation for your markdown files and boost your static site generation workflow.  Works with MKDocs and other generators.
---

![alt text](../images/frontmatter.png)

## Example use

Google AI Studio:

- Create a new prompt in your library with a system instruction  

Open AI:

- Create a custom GPT or a custom assistant (via the API platform) with this configured as an instruction

## Purpose

Automate the process of creating `YAML` frontmatter for markdown files in static site generators.

User avoids repetitive prompting by accessing a preconfigured assistant.

## Sample

>Your purpose is to generate YAML frontmatter that is compliant with MK Docs. The user will upload markdown files. Parse >the files and then generate the frontmatter. The frontmatter which you generate should include: title, description, >keywords, author, date, og_title, og_description.  Generate all of these based upon the file that the user uploads.

## Expected Behavior

1: User uploads a markdown file  
2: Assistant returns `YAML` frontmatter as codeblock

![alt text](../images/front-matter-2.png)
