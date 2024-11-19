---
title: "Using LLMs to Generate Prompt Engineering Examples & Lists"
description: "Explore how to use large language models (LLMs) for generating prompt engineering techniques, examples, and structured data. Learn foundational prompts and advanced strategies for better AI interactions."
keywords: 
  - "LLMs"
  - "prompt engineering"
  - "AI techniques"
  - "structured data generation"
  - "GPT-4"
  - "advanced prompting"
author: "Daniel Rosehill"
date: "2024-11-19"
robots: "index, follow"
social:
  cards:
    image: https://docs.bydanielrosehill.com/repos/prompt-library/images/prompt-lab.webp
og_title: "Using LLMs to Generate Prompt Engineering Techniques & Lists"
og_description: "A comprehensive guide on leveraging LLMs to generate prompt engineering examples and structured data. Includes foundational prompts and advanced techniques."
---

# Use-Case: Using LLMs To Generate Prompt Engineering Examples & Lists

![alt text](../../images/prompt-lab.webp)

# Foundational Prompt (Information Gathering)

You can use this prompt - or similar - to try to build your own table of current prompt engineering techniques (this might be especially helpful if - like me - you prefer digesting information in tables and with examples).

As the list of prompt engineering techniques is in flux (and I suspect nobody has a monopoly on it!) it's worth re-running this periodically on a model with a recent training cutoff *or* using a model augmented with real-time information retrieval capabilities. 

# Prompt 1: Generate A Table Of Structured Data

Note: The tabular data targeted here is quite dense so a chunking strategy might be necessary.

Unless you're specifically hoping to use the information you gather in a markdown-native format (like a wiki) you'll probably find that `csv` will be a much more useful target (in which case replace the instruction at the end of the prompt).

> Generate a table of 20 of the most common prompt engineering techniques.
>
> Format your output as a markdown table using the following structure:
>
> - **Column A** - Technique (the name of the technique)
> - **Column B** - Synonyms (any other names the technique is known by. Skip if there are none. Alternatively, use commas to separate the synonyms)
> - **Column C** - Use cases (in up to one sentence the applications for this prompt)
> - **Column D** - An example of the prompt
>
> Order the table alphabetically sorting on 'technique' (from A to Z).
>
> Encapsulate your output within a single continuous codeblock.


# Output 1: A starter list for exploring prompt eng techniques

*Generated with GPT-4o on 19th Nov.*

 
| Technique                    | Synonyms                          | Use cases                                                                                   | An example of the prompt                                                                                           |
|------------------------------|------------------------------------|---------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------|
| Anchoring                    | -                                 | Setting a baseline or reference point for further prompts.                                  | "Assume the user is new to the topic. Start by defining 'machine learning.'"                                       |
| Backward Chaining            | Reverse Prompting                 | Generating intermediate steps from a known outcome.                                         | "Explain the steps that lead to the conclusion: 'AI can revolutionize healthcare.'"                               |
| Brainstorming                | Idea Generation                   | Producing multiple ideas or solutions for a given problem.                                  | "List 10 creative uses for AI in education."                                                                      |
| Chain-of-Thought Prompting   | Logical Reasoning                 | Encouraging step-by-step reasoning for complex queries.                                     | "Explain why the moon appears larger near the horizon, step by step."                                             |
| Clarification                | Reframing                         | Requesting clearer or more specific details on a topic.                                     | "Can you clarify what you mean by 'sustainable farming practices'?"                                               |
| Comparative Reasoning        | -                                 | Comparing two or more items or ideas.                                                       | "Compare the benefits of renewable energy sources to fossil fuels."                                               |
| Conditional Generation       | If-Then Prompting                 | Creating outputs based on specific conditions.                                              | "If the weather is sunny, generate an outdoor activity plan. If it’s rainy, suggest indoor activities."           |
| Context Setting              | Priming                           | Providing context to improve relevance in responses.                                        | "Imagine you are a historian from the 18th century; describe the industrial revolution."                          |
| Counterfactual Prompting     | Hypothetical Prompting            | Exploring 'what if' scenarios.                                                             | "What if humans had evolved to breathe underwater?"                                                               |
| Creative Writing             | Storytelling                     | Generating fictional or imaginative content.                                                | "Write a short story about a robot learning emotions for the first time."                                         |
| Data Extraction              | Information Retrieval             | Pulling structured information from unstructured data.                                       | "Extract all the dates mentioned in the following paragraph."                                                     |
| Debugging                    | Problem Diagnosis                 | Identifying and resolving issues in code or logic.                                          | "Find and fix the error in this Python function."                                                                  |
| Definition                   | Explain Like I’m 5 (ELI5)         | Providing concise explanations or definitions.                                              | "What is quantum computing? Explain in simple terms."                                                             |
| Dialogue Simulation          | Roleplay, Conversation Modeling   | Simulating conversations between individuals or entities.                                   | "Simulate a conversation between a teacher and a student about photosynthesis."                                   |
| Error Analysis               | Fault Identification              | Identifying mistakes or flaws in content or reasoning.                                      | "Analyze the following paragraph for grammatical errors and logical inconsistencies."                              |
| Expansion                    | Elaboration                       | Adding more details or breadth to a topic.                                                 | "Expand on the topic of renewable energy to include its economic impact."                                         |
| Fact Checking                | Verification                      | Verifying the accuracy of a statement or information.                                       | "Fact-check this statement: 'The Great Wall of China is visible from space.'"                                     |
| Formatting                   | Output Styling                    | Presenting information in a specific format or layout.                                      | "Format the following text as a bulleted list."                                                                   |
| Goal-Oriented Prompting      | Task-Specific Prompting           | Designing outputs with a specific objective in mind.                                        | "Generate a 5-step marketing plan for a new app targeting college students."                                      |
| Hypothesis Generation        | -                                 | Proposing possible explanations or theories.                                               | "What could be some reasons for the decline in pollinator populations?"                                           |
| Instruction Following        | Task-Oriented Prompting           | Ensuring outputs adhere to detailed instructions.                                           | "Write a Python function that calculates the factorial of a number."                                              |
| Iterative Refinement         | Incremental Improvement           | Enhancing responses through multiple iterations.                                            | "Revise the following paragraph to make it more concise."                                                         |
| Keyword Highlighting         | Focus Prompting                   | Emphasizing specific terms or concepts in the response.                                     | "Explain the significance of 'neural networks' and 'deep learning' in AI."                                        |
| Knowledge Injection          | Domain Knowledge Integration      | Incorporating specialized knowledge into the output.                                        | "Using your knowledge of astrophysics, explain the concept of dark matter."                                       |
| Language Style Adaptation    | Tone Matching                     | Modifying the tone or style of the output.                                                  | "Rewrite the following paragraph in a formal academic tone."                                                      |
| List Generation              | Enumerative Prompting             | Creating a list of items based on a topic.                                                  | "List the top 10 programming languages in 2024 and their primary use cases."                                       |
| Localization                 | Regional Adaptation               | Adapting content to a specific cultural or geographic context.                              | "Write a travel guide for visiting Kyoto, Japan."                                                                 |
| Meta Prompting               | Prompt Design                     | Asking for the best prompt to solve a given problem.                                        | "What is the best way to prompt for a detailed explanation of quantum mechanics?"                                  |
| Multi-Step Reasoning         | -                                 | Solving problems requiring sequential steps.                                                | "Calculate the distance traveled by a car moving at 60 km/h for 3 hours."                                         |
| Paraphrasing                 | Rewriting                         | Rewording content for clarity or alternative phrasing.                                      | "Paraphrase this sentence: 'The quick brown fox jumps over the lazy dog.'"                                         |
| Prioritization               | Importance Ranking                | Ranking items based on given criteria.                                                     | "Rank these features of a smartphone in order of importance: battery life, camera quality, and price."            |
| Proofreading                 | Grammar and Style Checking        | Correcting errors in grammar, punctuation, or syntax.                                       | "Proofread the following essay for grammatical errors and awkward phrasing."                                       |
| Question Generation          | Query Prompting                   | Creating questions on a given topic.                                                       | "Generate 5 interview questions about renewable energy policies."                                                 |
| Randomization                | -                                 | Introducing randomness into outputs for creativity or variation.                           | "Generate a random motivational quote."                                                                           |
| Relevance Filtering          | Signal-to-Noise Optimization      | Ensuring responses focus only on pertinent details.                                         | "Filter out irrelevant information and summarize the following article."                                           |
| Rephrasing                   | Restating                         | Changing phrasing without altering the meaning.                                             | "Rephrase: 'Artificial intelligence is changing the world in remarkable ways.'"                                   |
| Role-Playing                 | Persona Simulation                | Adopting a specific role or character to provide a perspective.                             | "Act as a doctor and explain how vaccines work."                                                                  |
| Scenario Building            | Situation Simulation              | Creating hypothetical or real-world scenarios.                                              | "Describe a scenario where AI could replace humans in healthcare."                                                |
| Search Optimization          | Query Refinement                  | Improving search engine queries or results.                                                | "Generate keywords for searching information about machine learning applications in finance."                     |
| Sentiment Analysis           | Emotion Detection                 | Identifying or categorizing emotional tones in text.                                        | "Analyze the sentiment of this review: 'The product was amazing and exceeded expectations!'"                      |
| Simplification               | Plain Language Conversion         | Reducing complexity for better understanding.                                              | "Simplify this explanation of relativity for a 10-year-old."                                                      |
| Story Continuation           | Narrative Expansion               | Extending an existing story or narrative.                                                  | "Continue this story: 'The mysterious figure entered the room, holding an ancient key.'"                          |
| Summarization                | Condensing                        | Creating concise versions of longer content.                                               | "Summarize this article in 50 words or less."                                                                     |
| Text Completion              | Fill-in-the-Blank Prompting       | Completing partial sentences or paragraphs.                                                | "Complete this sentence: 'Artificial intelligence has revolutionized many industries, especially in...'"          |
| Tone Adjustment              | Style Shifting                    | Modifying tone to suit a particular audience or purpose.                                    | "Rewrite this feedback in a positive and encouraging tone."                                                       |
| Translation                  | Language Conversion               | Converting text from one language to another.                                              | "Translate this paragraph into French."                                                                           |
| Validation                   | Verification                      | Ensuring outputs meet specified criteria.                                                  | "Verify that this code snippet follows Python's PEP-8 style guide."                                               |
| Visualization Description    | Diagram Prompting                 | Describing visuals or requesting diagrams for understanding.                                | "Describe how to draw a flowchart for an e-commerce website's checkout process."                                   |
| Zero-Shot Prompting          | Zero-Shot Learning                | Generating results without examples or prior demonstrations.                               | "Describe the impact of blockchain on global trade."                                                              |
 
 # Output 2: Give me some weird and obscure prompt engineering techniques

Much of the fun in trying out prompts is in writing moonshot prompts that you know probably won't yield what you've looking for but .... the chance that they might keeps you hacking away writing weird queries.

Who wouldn't want to have a few little known tricks up their sleeve?!

The great thing about recording your prompts: you can save yourself a lot of repetition by reusing prompts you previously wrote!

For prompt 2, I made a couple of light touch edits to the first prompt, dialling down the number of outputs a little to make the info more digestible.

> Generate a table of 10 obscure or little known prompt engineering techniques. These should be prompt engineering techniques that are relatively obscure even among prompt engineering enthusiasts.
>
> Format your output as a markdown table using the following structure:
>
> - **Column A** - Technique (the name of the technique)
> - **Column B** - What's known about the prompt and what LLMs it's typically used with
> - **Column C** - Strengths and weaknesses of this prompting strategy
>
> Order the table alphabetically sorting on 'technique' (from A to Z).
>
> Encapsulate your output within a single continuous codeblock.

And this got me:

| Technique                   | What's Known About the Prompt and What LLMs It's Typically Used With | Strengths and Weaknesses                                                                                   |
|-----------------------------|----------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------|
| Adaptive Framing           | A technique where prompts are iteratively reframed to suit the LLM's responses. Works well with GPT models and Claude. | **Strengths**: Encourages flexibility and adaptation; improves outcomes for ambiguous tasks. **Weaknesses**: Time-intensive; requires user input. |
| Ambiguity Injection        | Purposefully introduces ambiguity in prompts to assess the LLM's inferential capabilities. Used with GPT and PaLM models. | **Strengths**: Tests reasoning and creativity. **Weaknesses**: Results can be unpredictable and context-dependent.                          |
| Cascading Prompts          | Involves feeding progressively detailed prompts in a sequence to refine outputs. Compatible with most advanced LLMs. | **Strengths**: Gradual improvement of responses. **Weaknesses**: Demands user oversight; increases latency.                                  |
| Constraint Anchoring       | Provides fixed constraints to guide the response generation. Effective with Codex and GPT models.                    | **Strengths**: Ensures specific boundaries are maintained. **Weaknesses**: Overly restrictive; may stifle creativity.                      |
| Cross-Domain Embedding     | Combines language and domain-specific embeddings in the prompt. Best with models that support embeddings (e.g., GPT-4). | **Strengths**: Enhances domain relevance. **Weaknesses**: Requires understanding of embedding manipulation; complex setup.                 |
| Fallback Enumeration       | Lists fallback instructions in case of failure to perform the primary task. Useful with GPT models.                 | **Strengths**: Improves reliability for multi-step tasks. **Weaknesses**: Can confuse the model if poorly structured.                      |
| Input Chunking             | Divides large inputs into manageable chunks to bypass token limits. Works with most LLMs with token constraints.    | **Strengths**: Handles larger datasets effectively. **Weaknesses**: Requires preprocessing; risks losing context between chunks.           |
| Latent Intent Extraction   | Prompts designed to infer unspoken user intents. Effective with GPT-4 and Claude for nuanced queries.               | **Strengths**: Captures implicit information. **Weaknesses**: Prone to misinterpretation if intent signals are weak.                       |
| Multi-Turn Context Stitching| Combines multiple conversation histories into a single context prompt. Works best with conversational models.       | **Strengths**: Preserves continuity across sessions. **Weaknesses**: Can exceed token limits or confuse model if context overlaps.         |
| Self-Critique Invocation   | Asks the model to critique its own response before finalizing. Effective with GPT-4 and Claude.                     | **Strengths**: Improves accuracy and coherence. **Weaknesses**: Slower response times; depends on model’s ability to self-assess.          |

## Of course, the real point of all this...

![alt text](../../images/sloth-grading-paper.webp)

*I need a couple of lines to use the next time I'm at a meeting when somebody says they know a thing or two about prompt engineering. The purpose of these lines should be to reference an obscure prompt engineering technique in a way that makes it seem as complicated and unfathomable as possible. Emphasise how this technique is only used by veteran prompting experts and beyond the grasp of most beginners to the craft.*

Output:

>"Ah, prompt engineering? That’s fascinating. Have you delved into recursive meta-contextual layering yet? It’s >where you embed a self-referential prompt loop within a dynamic hierarchical framework to iteratively refine AI >reasoning chains. It’s not something most people grasp right away—definitely not beginner territory. It really >separates the veterans from those just dabbling in the basics."