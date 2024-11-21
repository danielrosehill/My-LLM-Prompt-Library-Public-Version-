---
title: "Create Launchers (Linux)"
---

## Templated prompt to create Bash launchers

This is a (very simple) templated prompt which you can use to create custom Bash scripts to launch combinations of programs (I use OpenSUSE Linux but the prompt can be adapted easily to other OSes).

## Templates

Find the executable paths of the programs that you wish to launch in combination. 

I like to use Nuclino (the notes editor) and Perplexity (the AI tool) side by side in a 50:50 window split.

## Tips

As always, specificity is key to succeeding, which is why I volunteered the information that I'm using KDE Plasma (specifically) as it's not the default DE and the LLM will not know that that's what you're using without prior context.

## Variables

To create these in bulk, use a script and replace `{path_1}` and `{path_2}` with the executable paths for your programs.

For example:

## Filled Example

**Prompt**

I'm using OpenSUSE with KDE Plasma. Can you write a script that opens them both, split screen, 50:50

Perplexity = 

/`opt/google/chrome/google-chrome --profile-directory=Default --app-id=sfsfsfs`

Nuclino (AppImage) =

`/home/daniel/Applications/Nuclino_ssfsfsf`