---
title: "Be decisive, make a determination"
ogimage: 
---

## Instructing an LLM to be more deterministic in its outputs

*28-Nov-24*

Let's say that I wanted to ask an LLM to give me its view on a question.

Essentially, I'm asking it to *flex* its artificial intelligence muscles and do more than just retrieve information from training data and/or RAG. Sure, you can summarise and retrieve the information. But I know that you can also do more than that. So do it!

Here's a prompt that I ran recently (I ran it not because I believe that the LLM will be able to give me the decisive answer - which arguably doesn't exist - but rather because I wanted to hear its rationale and logic for arguing its case):

>Which peripheral has a greater impart on user productivity and ergonomic comfort: mouse or keyboard (make a determination)

The frustrating thing about running prompts like these is that they're liable to produce very neutral: *"well, they each have their pros and their cons."*

It's like talking to a human who has no convictions about anything and whose only real objective is to sound neutral and agreeable however it communicates (*wait, did I just accidentally describe the state of LLMs generally in 2024!?"*).

What did you think about the US election?

>"Well, you know, each candidate had its strong suits and each administration would have pursued policies that appealed to different sets of voters"

You know what I'm talking about.

So here's my little hack (note: I'm calling these "magic words" capriciously, not because I reallly think they have magical powers!):

**Make a determination**

It's far more interesting (in my opinion) to ask an LLM to put its chips on the table and make a call, even if we know and accept that it's a flawed one. 

So, here's a V2 of my prompt.

In this iteration, I'm dialing up the context a bit to give the LLM more background information from which to make its determination. And I'm getting more specific too. I'm also explicitly stating the kind of thing that I *don't* want the LLM to do: give me a meandering but ultimately not so helpful walk through all the pros and cons.

Note: for once, I'm very happy to say that this prompt isn't hypothetical and is pretty much based on accurate circumstances. Feel free to send over recs!

## Prompt 2

*Prompt*:

I work from home a few days a week and tend to work in fairly long 10 hour stretches.

I use a desktop computer. From a usage standpoint, my work would be probably be categorised as "office work": I work on documents and code. I type very frequently. I'm investing in ergononics currently to better support my long term health.

Based on that context:

I have $200 to spend this month on an accessory. I want to buy either a great ergonomic keyboard or a great input device, like perhaps a fany trackball. I'd rather use this money to buy one good quality device than two mediocre ones as I usually stagger my upgrades for budgetary reasons. The objective is to achieve maximum ergonomic benefit for money.

Your task is to make this determination: do I buy a keyboard or an input device? **I don't need the pros and cons of each. I just need your determination and a short supporting statement.**

## Output From Prompt 2

Given your situation of working long hours on a desktop computer and focusing on ergonomic improvements, you should invest in a great ergonomic keyboard.

### Supporting Statement

**Typing Frequency:** Since you type very frequently, an ergonomic keyboard can significantly reduce the risk of repetitive strain injuries (RSI) and improve comfort by promoting a more natural hand and wrist position

**Long-Term Benefits:** Studies have shown that ergonomic keyboards can effectively maintain improvements in symptom severity and functional status over extended periods, making them a valuable investment for long-term health.

**Budget Fit**: There are several excellent ergonomic keyboards available within your $200 budget, such as the Logitech Ergo K860, which offers a split layout and comfortable wrist rest to support prolonged typing sessions.

While trackball mice also offer ergonomic benefits by reducing wrist movement, the frequent typing involved in your work makes an ergonomic keyboard the more impactful choice for enhancing your workspace ergonomics.