# Suggest a local instructional LLM

## Notes

This prompt is designed to use a powerful cloud LLM with recent training data to suggest some open-source LLMs which can be locally hosted.

The purpose of the examples is to be specific and help steer the LLM's recommendations in the right direction (as examples reliably do). Without explicitly adding these, I found that the LLM jumped to the faulty assumption that I wanted a code-generation LLM.

The purpose of providing the hardware data is, as always, to make sure that the recommendations are tailored to your hardware. Otherwise, it will naturally suggest high parameter models which might not be viable. 

## Contextual Data

Desktop specs

## Prompt Text

My desktop specs are attached.

I use LM Studio to run local LLMs.

Suggest the most capable instructional LLM that I can run for the following example purposes:

- I have a CSV that I want to reformat as a markdown document. I want the rows in the CSV to be grouped into logical groups. 
- I have a long PDF. I would like to extract the text from it and ignore the formatting elements. 
- I would like to extract data elements like tables from a 10 page PDF report. 

Recommend an LLM that will be as efficient as possible without exceeding the capabilities of my hardware.