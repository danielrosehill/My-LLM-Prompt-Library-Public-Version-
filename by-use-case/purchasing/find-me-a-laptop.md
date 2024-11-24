---
title: "Buying a new laptop"
ogtitle: "Using ChatGPT To Buy A New Laptop"
ogdescription: "How to use ChatGPT to zone in on a great laptop purchase!"
---

![alt text](../../images/buying-laptop.webp)

24-Nov-24

# Using ChatGPT to buy a new laptop

This prompt template was written for a friend currently visiting the US and looking to buy a new laptop.

Rather than re-send the *result* of the prompt, I'm resending the prompt itself. Or rather, I'm showing how to create it. *Teach a man to fish* and all that.

This is really just a subset of my *general methodology* for using LLMs for targeted purchasing recommendations. But with a few specifics for the type of product that we're looking at (laptops).

We'll also get to look at how some simple prompt chaining can make LLMs exponentially more useful.

## Use-case -> specs -> product 

To use an LLM effectively for this type of purchasing research, I'd proceed like this:

- Firstly, tell the LLM what you need the laptop to *do* (ie, provide it with context)  
- From this, we can get spec recommendations  
- From this, we can get drill down to the level of individual product recommendations

The reason I'd approach the search process like this is because I'm trying to play to the strengths of LLMs in information retrieval.

For real-time product data, Google is has the edge. But using LLMs, we can do something that's much more useful than just fishing through lots of individual results from people trying to sell us stuff: We can understand *what* we need. And then empowered with that information, we can pick out the product in a much more selective (and less annoying) way.

## Specify your software and workflow

![alt text](../../images/purchasing/sloth-working-on-autocad.jpeg)

The key to getting the most out of large language models is to be very *specific* and *detailed* when prompting. 

LLMs are getting continually better at being able to store and leverage context (consider, for example, ChatGPT's memory function). But (at least at the time of writing) it's still probably better to play it safe and assume that the LLM you're interacting with is fully context-naive. It knows nothing about you, what you do, or why you need a new laptop. Taking this prompt as a canvas, your job is to fill in the blanks.

*So I might start out with:*

> I'm an architect and I need a new laptop.

That gives the model some clues to start with (architects likely have more demanding graphic workloads than your average user).

But to really dial in the context in a useful way, I'd like to tell the model very specifically what type of programs I use:

> I use my current laptop for 3D modelling. I use Autodesk Revit and AutoCAD.

As I'm not an architect, my ability to really flesh these out is very limited. But if it were a laptop for something I wanted to do, I might go deeper:

> I use my laptop for running local large language models (LLMs). I use OpenSUSE Tumbleweed. Currently, I'm working mostly with Llama 7B. I'm using a quantized model and I'd like to start using more powerful models like Llama 13B.

## What resources do I need?

That was part 1.

Part 2 (our first prompt) is going to be using the LLM to flesh out a ballpark spec for us. 

But before we get to that, I'm going to use this first prompt just to understand *what* I need hardware-wise.

![alt text](../../images/purchasing/spec-identifying.jpeg)

Because we all live on a budget, I'm going to leverage the ability of LLMs to do something else that Google simply can't: 

I'll ask it to give me a few different options for different levels of spec and I can later evaluate these against my budget. 

So I'll prompt:

> Generate a list of the hardware specs that I will likely need in this new laptop. For each spec, give me three options: one for a minimum viable laptop; the next a moderately powerful spec; and finally a high end spec. For example, suggest three CPUs that might fit my needs.

The example here isn't *amazing* but it's always worth including an example because it significantly boosts accuracy.

Finished prompt 1 might look like this:

> I'm an architect who needs a new laptop. I use my laptop primarily for working on client renderings using a mixture of AutoCAD and Revit. My models are typically {size}. I'm looking for a laptop that will handle these jobs comfortably. Generate three sets of specifications: the first for a budget laptop; the second for a moderate laptop; and finally a high end laptop. For each, provide guidelines for what type of hardware I should look for and what parameters might meet my requirements.

## Output 1

As an architect working primarily with AutoCAD and Revit, your laptop needs to handle resource-intensive tasks like 3D modeling, rendering, and multitasking. Below are three sets of specifications tailored to different budget ranges: **Budget**, **Moderate**, and **High-End**.

 ```markdown
## **1. Budget Laptop Specifications**
For light to moderate workloads, such as 2D drafting or small-scale 3D models, a budget laptop can suffice. However, compromises will be made in terms of performance for larger projects.

- **Processor (CPU):** Intel Core i5 (11th or 12th Gen) or AMD Ryzen 5 (4000 or 5000 series) with at least 4 cores and a base clock speed of 2.5 GHz or higher.
- **Graphics (GPU):** NVIDIA GeForce GTX 1650 or GTX 960M (4GB VRAM). Avoid integrated GPUs like Intel Iris Xe.
- **RAM:** Minimum 16GB DDR4.
- **Storage:** 512GB SSD (expandable if possible).
- **Display:** 15.6-inch Full HD (1920x1080) with decent color accuracy.
- **Price Range:** $700–$1,000.

*Example Models:* Lenovo Legion 5i, Acer Predator Helios 300 (entry-level configurations).

---

## **2. Moderate Laptop Specifications**
For architects handling medium to large projects with occasional rendering, a mid-range laptop offers better performance and future-proofing.

- **Processor (CPU):** Intel Core i7 (12th or 13th Gen) or AMD Ryzen 7 (5000 or 7000 series) with at least 6 cores and a turbo boost clock of 4.0 GHz or higher.
- **Graphics (GPU):** NVIDIA GeForce RTX 3060/4060 (6GB–8GB VRAM) or equivalent.
- **RAM:** 32GB DDR4/DDR5.
- **Storage:** 1TB SSD.
- **Display:** 15.6-inch or larger QHD (2560x1440) or Full HD with good color accuracy and brightness.
- **Additional Features:** Thunderbolt ports for external GPU support, good cooling system.
- **Price Range:** $1,200–$1,800.

*Example Models:* MSI Creator M14, Gigabyte Aorus 7, Dell XPS 15.

---

## **3. High-End Laptop Specifications**
For demanding workflows involving large-scale renderings and complex models, a high-end laptop ensures smooth performance without bottlenecks.

- **Processor (CPU):** Intel Core i9 (13th Gen) or AMD Ryzen 9 (7000 series) with at least 8 cores and high turbo boost speeds.
- **Graphics (GPU):** NVIDIA RTX A2000/A3000 (professional-grade) or RTX 4070/4080 with at least 8GB VRAM.
- **RAM:** Minimum of 32GB DDR5; ideally upgradeable to 64GB.
- **Storage:** Dual storage setup with a primary 1TB NVMe SSD and secondary storage option for larger files.
- **Display:** Large screen (16–17 inches), UHD/4K resolution with excellent color accuracy (100% sRGB/AdobeRGB).
- **Additional Features:** ISV certification for software compatibility, advanced cooling systems, long battery life for portability.
- **Price Range:** $2,000–$3,500+.

*Example Models:* Dell Precision 7780, ASUS ProArt StudioBook Pro, MSI CreatorPro M16.

---

## **Key Considerations**
1. **Processor Speed & Cores:** Both AutoCAD and Revit benefit from high single-core performance for modeling but also utilize multi-core processors for rendering tasks.
2. **Graphics Card:** While AutoCAD relies more on the CPU for processing, Revit benefits significantly from a dedicated GPU for smoother model navigation and rendering tasks.
3. **RAM & Storage:** More RAM allows you to handle larger models and multitask efficiently. An SSD ensures faster file access and loading times.
4. **Display Quality:** A high-resolution display with good color accuracy is essential for architectural work to ensure precise detailing in renderings.
```
![alt text](../../images/purchasing/laptop-sloth-3.jpeg)

Personally I have a hard time proessing all that information at once. 

I also didn't want to get specific models just *yet*. I just wanted to use the LLM to make sense of what I need.

So I might iterate on this:

> From the information you provided, generate an evaluation matrix in markdown. Remove the specific product recommendations. Simplify the information. 

Alternatively, you could just as easily switch to a different LLM and prompt:

> Take this data offering recommended specifications for a laptop. Reformat the data into a markdown table. Remove specific product recommendations. Simplify the information.

Then, paste the first output.


Now we have:

### **Laptop Specifications for Architectural Work**

| **Category**       | **Budget Laptop**                       | **Moderate Laptop**                        | **High-End Laptop**                       |
|---------------------|-----------------------------------------|--------------------------------------------|-------------------------------------------|
| **Processor (CPU)** | Intel Core i5 (11th/12th Gen) or AMD Ryzen 5 (4000/5000 series), 4 cores, 2.5 GHz+ | Intel Core i7 (12th/13th Gen) or AMD Ryzen 7 (5000/7000 series), 6 cores, 4.0 GHz+ | Intel Core i9 (13th Gen) or AMD Ryzen 9 (7000 series), 8 cores, high turbo speeds |
| **Graphics (GPU)**  | NVIDIA GTX 1650 or GTX 960M (4GB VRAM) | NVIDIA RTX 3060/4060 (6GB–8GB VRAM)        | NVIDIA RTX A2000/A3000 or RTX 4070/4080 (8GB+ VRAM) |
| **RAM**            | 16GB DDR4                              | 32GB DDR4/DDR5                             | 32GB DDR5 (upgradeable to 64GB)           |
| **Storage**         | 512GB SSD                              | 1TB SSD                                    | Dual storage: 1TB NVMe SSD + secondary option |
| **Display**         | 15.6" Full HD (1920x1080)              | 15.6" QHD (2560x1440) or Full HD with good color accuracy | 16–17" UHD/4K with excellent color accuracy (100% sRGB/AdobeRGB) |
| **Additional Features** | None                                  | Thunderbolt ports, good cooling system     | ISV certification, advanced cooling, long battery life |
| **Price Range**     | $700–$1,000                            | $1,200–$1,800                              | $2,000–$3,500+                             |

### **Key Considerations**
- **Processor Speed & Cores:** High single-core performance is crucial for modeling; multi-core processors are better for rendering.
- **Graphics Card:** Dedicated GPUs improve performance in Revit and ensure smoother navigation/rendering.
- **RAM & Storage:** More RAM supports larger models and multitasking; SSDs provide faster file access.
- **Display Quality:** High-resolution displays with accurate color reproduction are essential for precise architectural detailing.

## Understanding the spec

Laptop specs are kind of overwhelming so this might be a nice opportunity to understand what we're buying and why.

We could again use prompt chaining here. 

For example, we could ask:

> This table represents recommended specifications for a new laptop for an architect. I'm confused about what all the different hardware does. Can you break it down. For each, explain why it would help with my rendering work.

## Finally, from spec to products

![alt text](../../images/purchasing/laptop-4.jpeg)

Although computer specs are themselves time-limited, I think that having a good one is a lot more useful than having some random purchase recommendations. 

The same laptop can have a huge number of variants, leading to more confusion, when sometimes all you need is to have a basic grasp on what you need and how much it's going to cost. 

Now you can provide the spec and prompt something like:

> Suggest 5 laptops that meet the spec outlined in the 'medium' spec recommendation. I'm purchasing a laptop for my business. I work as an architect. 

One benefit of saving prompts is that you can easily re-inject snippets. 

Remember, also, that context is wont to fall out the longer you progress in a single chat with a single LLM which is why sometimes, out of caution, I deliberately repeat prior context (like here, I'm reminding the LLM about the laptop's purpose). 

By the way: this is why saving outputs is also highly useful: you can "inject" one output and a past prompt into a different LLM if (for example) it has better real time ecommerce performance than the LLM you originally used.

If you want to work within context, you can also tack on after-queries, like:

> This laptop is great but it's about $400 than I wanted to spend. Can you suggest a few models that would meet that criteria?

Using these techniques, you can not only get recommendations for specific products, you can also help form a deeper understanding of the hardware that you need which is ultimately much more useful.

