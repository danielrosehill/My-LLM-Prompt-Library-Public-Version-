---
title: "Prompting strategies for purchasing: shopping lists & evaluation matrixes"
---

![alt text](../../images/banners/sloth-buying-keyboards.webp)

## Prompting for purchasing: generating shopping lists and matrixes

(Great for high ticket purchasing research or ... agonising over which keyboard to pick out)

You know when you're looking to buy something and it *almost* seems like the perfect *thing* but then it's missing that one thing?

Alongside all life's woes (*I jest*), ChatGPT *et al* can render those a thing of the distant past.

But before we bid a fond goodbye to agonising purchasing decisions, let's see how we can use these tools effectively to do the job of sizing up `Thing A` vs. `Thing B`.

Today's prompting strategy will be:

- Listing our requirements  
- Instructing the LLM to produce a table/matrix with each item evaluated  

In a hopefully not too distant future, LLMs will be good enough that we can just say: *only show me keyboards meeting all these requirements and then retreat back into your AI home*(.)

But my experience has been that their skills *aren't* quite there yet and thus sometimes forcing them to list all the spec requests works better.

In my experience using it so far, this prompting strategy is actually highly effective. You can whittle a huge swamp of potential purchasing options down to a very tidily targeted list with just a little bit of the magic ingredient of prompting: **specficity.**

### Purchasing list prompt skeleton

**Here's the backbone of a prompt we could use to find, per our example, an ergonomic keyboard:**

I'm looking for a keyboard:

These features are essential (group A):

- Ergonomic design (split layout etc)
- Quiet / silent operation
- No RGB or ability to disable RGB

These features are less essential but still important to me (group B):

- Wireless support (dongle ideal)
- Mechanical operation

And finally, these features are less important but also desirable (group C):

- Macro keys

Must be:

- RRP <  $300
- Available for Prime delivery on Amazon.com
  


### Part 2: Add an output instruction to the prompt  

That was the 'core' of my prompt which attempts to set out my requirements in a somewhat logical fashion.

Now, I'm going to attach to that an **output instruction** which will instruct the LLM on *exactly* how I want it to format the output it generates.

I'll show three versions of these to show how you can use small variations in prompt-writing to instruct for very different outputs.

#### V1: Output as a formatted list

**Add this for a formatted list**:

Format your output like this. In the second half of the example, the text in the brackets descrdibe what the variables should represent:

```markdown
# Keyboard Name
## RRP & Manufacturer

Ergonomic: (Does it feature an ergonomic design? If so, which?)  
Wireless: (What kind of wireless does it have? Dongle / Bluetooth / both?)  
Quiet/silent: (How does it operate in a quiet way?)  
Mechanical: (What switch does it use? Or if it's not mechanical what mechanism?)  
Macro keys: (How many macro keys, if any?)
```

The downside is that specifying how you want the LLM to generate the output like this is a bit tedious.  The upside is that when they work they work well: you get a targeted run-through of everything that matters to you about whatever it is that you're buying.

Imagine that instead of buying a keyboard you were buying a new TV or an expensive laptopl. It might be worth the time invested in laying out your requirements very precisely.

![alt text](../../images/posts/keyboard-evals/sloth-shoping2.webp)

#### V2: Output this as an evaluation matrix (ie, table)

If you use a markdown notepad editor, then you can specifically ask the LLM to generate its output as a markdown table that you can copy and paste right into it. Or if you use Google Drive, you can use its markdown integration and do exactly the same thing.

I usually prompt something like and the codefence part is only there because, right now, I'm using Perplexity quite a bit (and it tends to strip them out, rendering the table un-copy-able. Hence, I instruct it explicitly):

> Format your output as a markdown table enclosed within a codefence. The markdown table should list the following parameters: Product | Manufacturer | RRP | Wireless Support 

... you get the idea.

Bear in mind that if we ask for a table with *all* of the variables I asked the LLM to review, it's going to get pretty unwieldly very quickly.

So instead you might want to instruct like this:

> In column 3, include your assessment of all the spec parameters that I provided.

This way, you'll tell the LLM to box of all that part of its output into one section of the table.

![alt text](../../images/posts/keyboard-evals/data-sloths2.webp)

### Targeting a specific data structure in your prompts

In my experience, LLMs aren't particularly picky about how you tell them to lay out tables. 

But many don't know that you actually *can* instruct them to output data in specific arrangements of rows and columns.  This is particularly useful when you're combining multiple outputs into one big data structure (like aggregating prompts generating CSV data that maintains a consistent header row).

As to how to do it ... so far, it seems to be more art than science.

Sometimes, I'll write my request as a narrative:

> In the first column, list the keyboard. In the second, list its RRP. In the third, list a summary of the specs.

In others, I'll use pipe symbols to denote the target layout in a more traditional way:

> Lay out the columns in the table exactly like this: Laptop Name | RRP | Specs

In my experience, there's not much difference in the predictability of the result. 

Both work prety well. But if you're really targeting data consistency, provide an explicit and properly formatted header row and instruct the LLM to output in *exactly* that format.

*(Final formatting tip: if you're doing some more extensive data evaluation and you're hoping to pipe the data into a spreadsheet or database, ask explicitly for CSV or 'raw CSV' and the LLM will output to your chosen format)*.

#### V3: Give me a list, then give me a table

Finally we get to the last permutation of the output instruction which is asking the LLM to do both things with the data it has gathered: ie, give me it as a list, then give it to me as a summary table.

This is a really nice information format that's easy to digest, but it (naturally) runs a greater risk than the preceding approaches of running into output length limits. 

It's easy to forget how capable LLMs are and how much we routinely ask them to do with even simple instructions. In this example, for instance, we're telling the LLM to:

-  Read our prompt (tokenise the words, process their meaning) 
-  Find the top 5 matches (now, search for results against real time data!)    
-  Grade them all according to our spec system  
-  Format that into a list  

So right now, saying: Give me a big long list and then format it into a nice table has (in my experience) mixed success (mixed success might mean that the LLM hits its output limit midway through the generation).

Of course, you can try prompting for it. 

Or you can divide the prompts by using chaining.

E.g, prompt 1:

> Find the keyboards, format that as a list

When you get output 1:

> Take this list and reformat it as a table

Then (if you're really determined) you can just combine the two outputs as one formatted document.
