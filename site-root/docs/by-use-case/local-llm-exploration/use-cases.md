# Can you suggest any new local LLMs I could download?

This simple but effective prompting strategy involves providing an LLM with two pieces of contextual data:

- The list of local LLMs you have installed  
- Your hardware

From those two pieces of data, the LLM can suggest additional models.

---

# Prompt

Here are the local LLMs that I've installed with LM Studio.

I'm trying to cover a few use-cases:

- Python code generation 
- General purpose use
- Cencorship-free usage  

Can you think of any additional models I might wish to run on my local computer which might open up new use-cases?

---

# Contextual Data

Drag and drop:

## 1: Screenshot of LLMs on system:

 ![alt text](../../../Context-Setting/images/llms.png)

## 2: Hardware spec for contextual data:

See `context-docs`

---

## Output

You've already installed a solid set of local LLMs that cover several important use cases, such as Python code generation, general-purpose tasks, and censorship-free usage. Here's a breakdown of your current models:

- **Python Code Generation**: You have models like **WizardCoder-Python-7B** and **CodeLlama-7B**, both of which are strong for coding tasks.
- **General-Purpose Use**: Models like **Llama-2-13B-chat** and **Meta-Llama-3.1-8B-Instruct** are versatile for a wide range of tasks.
- **Censorship-Free Usage**: Models like **Tiger-Gemma-9B** are known for being uncensored and responsive to a wider variety of prompts.

Given your hardware specs (Intel i7, 64GB RAM, AMD Radeon RX 7700 XT with 12GB VRAM), you can comfortably run models up to around 13 billion parameters, especially with quantized versions (e.g., GGUF). Here are some additional models you might want to consider to further expand your use cases:

## Additional Models to Consider

### **1. Starcoder (15B)**
- **Use Case**: Advanced code generation.
- **Why**: Starcoder is specifically designed for code generation and excels in understanding complex programming languages and contexts. It’s a great addition if you want more specialized coding capabilities beyond Python, such as JavaScript or C++.
- **Fit for Hardware**: While it's slightly larger than your current models, you can try using a quantized version (Q4 or Q5) to fit within your hardware limits.

### **2. Mistral 7B or Mixtral 8x7B**
- **Use Case**: General-purpose tasks with strong performance on smaller hardware.
- **Why**: Mistral 7B is known for outperforming other models of similar sizes on benchmarks while being lightweight enough to run efficiently on consumer-grade GPUs. Mixtral 8x7B could be an alternative if you need a mixture of smaller expert models for different tasks.
- **Fit for Hardware**: Mistral's small size makes it highly efficient on your hardware.

### **3. Phind-CodeLlama (34B)**
- **Use Case**: High-level code generation and debugging.
- **Why**: If you're looking for a more advanced model for coding that rivals GPT-4 in terms of reasoning and code generation, Phind-CodeLlama is highly recommended. It’s particularly good at debugging and handling complex programming tasks.
- **Fit for Hardware**: This model might be too large for local use unless heavily quantized, but it's worth testing if you can offload layers to system RAM.

### **4. Xwin-LM (13B)**
- **Use Case**: Uncensored general-purpose tasks.
- **Why**: Xwin-LM is known for being highly uncensored while maintaining high-quality responses across various domains. If you're looking for another censorship-free model that doesn't compromise on quality, this could be useful.
- **Fit for Hardware**: At 13 billion parameters, it should fit well within your current setup, especially with quantization.

### **5. DeepSeek-Coder (33B)**
- **Use Case**: Expert-level code generation and problem solving.
- **Why**: DeepSeek-Coder has been praised for its ability to understand complex coding problems and offer detailed solutions. It’s particularly good at debugging and providing specific insights into code issues.
- **Fit for Hardware**: This model would require significant quantization but may still be feasible with offloading.

### **6. SOLAR 10.7B**
- **Use Case**: General-purpose use with strong instruction-following capabilities.
- **Why**: SOLAR is another strong general-purpose model that performs well across various tasks while being relatively lightweight compared to larger models like GPT4 or Gemini Ultra.
- **Fit for Hardware**: At 10.7 billion parameters, it should run well on your system using GGUF quantization.

## Conclusion

Based on your use cases, here are the additional models I recommend:

1. For more advanced Python and multi-language code generation, try **Starcoder (15B)** or the lighter-weight but still powerful **Mistral 7B/Mixtral 8x7B**.
2. For uncensored general-purpose usage, consider adding **Xwin-LM (13B)** or exploring the highly capable but uncensored versions of models like Tiger-Gemma or DeepSeek-Coder.
3. If you're looking to push the boundaries of local coding assistance without compromising on quality, try testing out larger models like **Phind-CodeLlama (34B)** or the more manageable but still powerful **SOLAR 10.7B**, depending on how much memory you can allocate.

These additions will help you cover even more specialized coding tasks, improve general-purpose interactions, and provide additional censorship-free options while staying within the constraints of your hardware setup.

 