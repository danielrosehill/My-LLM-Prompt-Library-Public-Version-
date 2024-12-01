---
title: "Generate an LLM summary"
---

Works best on models with real time data RAG (given the fast pace of developments etc).

Outputs can be surprisingly rich given that this is a relatively short prompt:

## Basic prompt template

For this LLM: 

`{llm-name}`

Provide the following:

- Release date
- End of training period
- Strengths
- Weaknesses
- Preceded by
- Performance on benchmarks
- Comparable to

## With Markdown Formatting Insturction

For this LLM: 

`{llm-name}`

Retrieve the following:

- Release date
- End of training period
- Strengths
- Weaknesses
- Preceded by
- Performance on benchmarks
- Comparable to

Format the output as a markdown table:

## With CSV Formatting Instruction

For this LLM: 

`{llm-name}`

Retrieve the following:

- Release date
- End of training period
- Strengths
- Weaknesses
- Preceded by
- Performance on benchmarks
- Comparable to

Format the output as CSV with this header row:

`{header-row-for-consistency}`

## More Extensive Version With Section Formatting Instructions

```text
For this LLM: 

`{llm-name}`

Provide the following and use the following markdown formatting headers as your model to follow in how you structure your output.

# Basic Parameters

## Release date

(When was the LLM released)

## Training period & data

(What is known about the training period it underwent )

## Release Date

(When the model was released)

# Reception

## Benchmark performance

## Critical reception 
```

