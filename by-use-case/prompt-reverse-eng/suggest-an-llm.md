---
title: "Here's a prompt, suggest a good LLM"
---

## Can LLMs altruistically recommend the competition?

This prompting strategy is actually pretty intriguing to try out because its success is very much predicated on the idea that LLMs can be benign guides through the LLM universe, charitably pointing you in the direction of the slightly better model just down the street. 

But much like walking into a pizza shop and asking the owner whether it can recommend a *better* place to buy pizza, you can't go into this strategy expecting fantastic results from the get-go.

This strategy also provides an interesting insight into the extent to which any given LLM is inherently self-biased.

From experience:

- If you ask any of the OpenAI LLMs which is the best LLM for (your use case) they recommend OpenAI LLMs with astounding regularity  
- Ditto for Anthropic & Claude  

## Now my conspiracy theory...

This is probably only that, but my inkling is that cloud LLMs are more kindly disposed towards recommending open-source and self-hostable LLMs.

Another workaround to mitigate their bias:

Specify that you're wondering if there might be a `fine-tune` that could do a better job for generating a useful output than a generic LLM.

## Example prompt

At the very least, it doesn't hurt to try.

So the next time you're wondering whether there might be a better model for this task, try asking:

```text
Here's my prompt: {prompt}

Recommend an LLM that you think would generate the best output.

For the purpose of this prompt, "best" means: most useful and valuable to producing the type of information you can infer I'm looking for from my prompt.
```

## Image generation

Another experiment worth trying out is seeing whether a textual LLM (or a multimodal LLM) can guide you towards a good image generation LLM based upon the prompt.

Example usage:

> Which image generation AI tool do you think would produce the best output for the following prompt: