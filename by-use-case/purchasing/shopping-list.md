# Prompt template for gathering purchasing recommendations

![alt text](../../images/banners/sloth-shopping.webp)

*24-Nov-24*

LLMs can be used for putting together purchasing recommendations.

In this respect, they have an advantage over traditional serach methods (like search engines) and a limitation:

- Advantage: if the training data is selective, they can cut through the reams of highly misleading affiliate marketing that clutters SERPs  

- Disadvantage: as products change frequently, real time information or RAG is almost essential for them to have any utility in this respect

## Example purchasing template

Here's a pretty mundane but illustrative product I'm currently looking for.

I'm trying to find a keyboard that's:

- Ergonomic  
- Wireless  
- Quiet or silent  
- Mechnical

What won't be helpful:

A product that I can't afford.

Oh, and although many keyboard fans seem to dig it, I'm really not into RGB.

Finally, my wife's in the US right now so if it's sold on Amazon that would be really helpful.

## Prompt template

As always, the guiding principle is to be as specific as possible.

The second guiding principle is to break your requirements down into chunks.

The second line (BTW) is to try to subtly nudge the LLM away from recommending products from irreputable FBA companies which might have good keyword performance but whose products I'm not really looking for.

### Keyboard searching prompt

Generate a list of keyboards available for purchase on Amazon.com currently.

Focus on identifying products from reputable, established brands.

The keyboard must be:

- Wireless (Bluetooth or dongle; both is most ideal)  
- Marketed as being "quiet" or "silent"

Include a few options that are ergonomic keyboards.

Attempt to find options which use mechanical switches.

For each option you retrieve, present it as follows, adhering exactly to the template:

```text

# Product Name

Manufacturer  
Average rating on Amazon.com  
RRP in USD  
Mechanical? (yes or no)  
Wireless connectivity: (what type)
Quiet or silent: (how, what method)  
Ergonomic: (is it ergonomic?)
```

## Why the prompt is written like this

I want to make it easy to help the LLM distinguish between my "must-haves" and my "nice to haves."

The end section - where I specify the output format - helps to produce a very consistent output format in a way that I can easily digest.

## Step 2: Chain the output 

After running this prompt, you might come up with a shortlist of 6 great products fitting your criteria.

Let's call them:

```text
Keyboard 1
Keyboard 2
Keyboard 3
Keyboard 4
Keyboard 5
Keyboard 6
```

We can then use prompt chaining to drill down into our shortlist, like this:

### Shortlist matrix

```text
I like:

Keyboard 1 
Keyboard 3 
Keyboard 6

Generate a comparison matrix for those 3 keyboards, formatting your output in markdown.
```