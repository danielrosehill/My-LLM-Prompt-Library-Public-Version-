---
title: "Using LLMs for ... movie recommendations!"
---

## Using LLMs to find movies, TV, documentaries (etc)

![alt text](../../images/misc/sloth-in-cinema.webp)

# Movie, TV and documentary preferences

If you're looking for something good to watch on Netflix tonight (or elsewhere) try the following prompt-and-context template.

This is (another) great use-case for the context-snippet idea which you can use as a low-tech surrogate for RAG (or try what I'm attempting to set up: have a context repository that serves as a pipeline to a RAG setup!).

The idea is as follows:

- You jot down your movie preferences once and save that as a template file like `daniels-movie-preferences.md`. 
- Then, you reuse that tiny text snippet to prompt to get targeted movie recommendations, even if the LLM is totally context-"naive"  

A model context snippet is below. Because where we are based in the world affects the choice of entertainment available to us, I've included a little note of where the user is located.

## Prompt model

**You could prompt something like this:**

Any movies I might enjoy from this year? 

Here are my preferences

`(insert context snippet)`

## How you add the context snippet

If you're using a web UI youc an simply drag and drop the file.

Manual method: copy and paste.

## Example context snippet recording your general entertainment preferences

```text
Interests:

- Space Exploration  
- Nature and Wildlife  
- Crime Thrillers  
- Sports and Adventure  
- Political Dramas  

## What I don't like

- Reality TV shows  
- Romantic comedies  
- Movies that are overly long  

Topics, types, genres:

- Space exploration stories  
- Fictional accounts of historical events  
- Documentaries about nature  
- Political intrigue  

## Limitations

I live in Canada. You can recommend content that isn't in Netflix's Canada library, but if you do, flag it.
```