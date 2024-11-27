---
title: "Getting LLMs to be more concise"
---

![alt text](../images/prompt-eng/sleeping-sloth.webp)

LLMs are certainly talkers!

As *large* language models, I guess that's kind of to be expected.

But sometimes you don't want to know every random detail about a subject. 

You just want a summary. Or .... a list.

## Prompt A

Here's a routine prompt that I recently ran:

```text
Generate a list of business sectors. Divide the output into three parts: those usually considered to be poor environmental performers; those usually considered to be mediocre in that respect; and those often considered to outsized performers (high commitment to sustainability)
```

You mightn't expect it to provoke this kind of verbosity, but it did:

Food Retail (energy use for refrigeration and waste generation) 
Manufacturing (varies widely by product type but often involves resource-intensive processes) 
Mining (land degradation and water pollution but essential for raw materials) 
Water Supply (energy-intensive processes for treatment and distribution)

This is actually far from the worst example that I could have picked. But equally, as the output was part of a prompt chain, I didn't want the unrequested explanations in parentheses.

So for Prompt B I made a couple of tweaks, including tightening up the formatting instruction a little to specify that it should output alphabetically within those sections. But it took just two words: **without explanations** to get rid of the appendages that I didn't want:

`Format the list like this, without explanations`

I fleshed out the example to really make clear that I just wanted a list of industries. But it likely wasn't necessary with the addition of the first instruction.

So while `prompt B` looks pretty similar, it actually achieved a far more useful output, at least for my purposes.

In full:

```text
Generate a list of business sectors. Divide the output into three parts: those usually considered to be poor environmental performers; those usually considered to be mediocre in that respect; and those often considered to outsized performers (high commitment to sustainability)

Format the list like this, without explanations. Provide 20 industries in each category. Within each category, order the industries alphabetically.

# Low

Industry 1
Industry 2

# Medium
Industry 1
Industry 2

# High
Industry 1
Industry 2
```

Now we have:

```text
Low Environmental Performers

Agriculture & Food Production

Cement Manufacturing

Chemical Manufacturing

Coal Mining

Construction

Fast Fashion

Fishing Industry

Forestry
```

Etc.