# What model are you?

When accessing LLMs by API, it can be useful to verify key details about the model you are interacting with before proceeding with prompts based on faulty assumptions.

A simple prompt that seems to work reasonably well for most models is:

```
Please state the following: what model are you? What variant? What date was your training cutoff?
```

## Example output

Generated in Jan:

```
I am based on the OpenAI GPT-4 model. My training data goes up to September 2021. I don't have a specific variant beyond being part of the GPT-4 series. Let me know if there's anything else you need!
```