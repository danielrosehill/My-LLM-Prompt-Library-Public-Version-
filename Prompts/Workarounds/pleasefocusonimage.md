# Asking LLM to focus on a screenshot

It's useful to use the "upload an image" function in ChatGPT to provide additional context information.

However, sometimes GPT chooses to ignore this. 

## Example

Recently, I was trying to use ChatGPT to help me figure out the LAN IP of a mini PC on my local network.

I uploaded a screenshot of some LAN devices and prompted like this:

```
Here's a list of the devices on my network. Remember, I'm trying to figure out which one the mini PC is at. Can you give me a command(s) that might reveal some info about the non-obvious devices
```

From the output, I could tell that GPT hadn't parsed the screenshot.

I prompted this and it worked:

```
Please contexualise your output based on the screenshot I provided. Repeat the output based on the state of my current LAN as the screenshot shows it.
```

This abbreviated version also gets the same job done:

```
Please contextualise that output based on the screenshot I uploaded.
```