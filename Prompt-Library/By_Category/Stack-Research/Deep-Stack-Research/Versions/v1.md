# Stack Research, Deeper Prompt

## Summary:

Prompt to create a deeper evaluation list (for evaluating tech stacks although other use-cases may be possible).

This prompt was built for a very specific evaluation but could be remodelled for other purposes. 

## Objective:

Create an evaluation longlist, shortlist, and "winner" section. 

## Current version:

1

## Date:

11-08-24

## Iterative Improvement:

Improvements are needed in the third (final) section where more explicit wording is required to identify the "winner" according to the parameters.

## Prompt Text: 


Please provide an overview of 10 SaaS tools for building up a comprehensive knowledge base. 

For every tool that you discover, please output the following details:

- Name of the solution
- Does it have an Android app?
- Does it have a Linux desktop app? 
- Does it have a desktop app for Fedora linux?
- Is it backed by Postgres? If not, what database?
- Does it have native support for markdown?
- Details about the product
- Is it scalable and suitable for enterprise?
- What level of scale can it achieve? How many files?
- Does it allow users to backup their data? If so, how?
- Link to the project
- Price and pricing structure

At the end of the output, please provide a new section called Shortlist

In this section, include a summary of the tools which meet all of these criteria:

- Has an Android app
- Support markdown
- Offers the ability to backup data

Finally, provide a section called Top 3 GPT Recommendations

Recommend 3 solutions from the shortlist and pick whichever one you think is best and offers the best scalability