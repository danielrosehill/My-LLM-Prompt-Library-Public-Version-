---
title: "Github prompting workflow"
---

#  Try it out, get back a GUI template!

## Prompt

Explain how to create the following functionality within a Github repository providing detailed instructions for how to create this:

A Github repository has two folders:

```
/prompts
/outputs
```

Within prompts there are subfolders:

```
/prompts/drafts
/prompts/deployed
```

When a prompt is moved from `/drafts` and into `/deployed` it is sent to the OpenAI API for completion with GPT4o.

The output (the text the API returns) is collected in `/outputs` with the same name as the prompt and written into the markdown file.

### Example

Here's an example to show the desired functionality:

A prompt:

`/prompts/drafts/ask-gpt.md`

Is moved to:

/`prompts/deployed/ask-gpt.md`

The text of that markdown file (the prompt) is sent for completion to OpenAI GPT 4-o via the API. 

When it comes back it's recorded in:

`/outputs/ask-gpt.md`