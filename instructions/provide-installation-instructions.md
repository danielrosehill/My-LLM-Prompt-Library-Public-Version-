---
title: "Provide installation instructions"
---

## Recommend tools, provide installation instructions

If you're a Linux user using LLMs to quickly see what options are out there for your distro, then most probably you don't just want a list, if one sounds good, you'd like to know how to install it too. 

The solution I've found is - after specifying what you're looking for - prompt something like:

`for every tool that you recommend, specify the installation command`

... or something similar.

The installation commands are not always accurate, but a decent amount of the time they are, especially if the package is in the standard repository of a popular distro (etc).

## Prompt

Here's my workflow: import webp into GIMP for editing, crop, export. I'm using OpenSUSE and have a batch of about 200 images to do. Note: I want to crop them visually and not programatically. Any better tools for doing this? If you have a tool to recommend, **please provide installation instructions**

## Example Output (GPT-4o, 28-Nov-24)

For visually cropping a large batch of images, you might find it more efficient to use a tool with a streamlined interface specifically designed for simple tasks like cropping. Since you're on OpenSUSE, here are a few tools you might consider:

### 1. **XNView MP**

XNView MP is a versatile image viewer that also has some basic editing capabilities, including cropping. It supports batch processing, which can help manage multiple files more easily. 

**Installation:**

1. Download the XNView MP package for Linux from the official [XNView website](https://www.xnview.com/en/xnviewmp/).
2. Open a terminal and navigate to the directory where you downloaded the package.
3. Extract the downloaded archive:
   ```bash
   tar -xvf XnViewMP-linux-x64.tgz
   ```
4. Navigate into the extracted directory:
   ```bash
   cd XnView
   ```
5. Run the program:
   ```bash
   ./xnview.sh
   ```

### 2. **digiKam**

digiKam is a powerful photo management application that includes a number of editing features. It’s well-suited for managing and editing large collections of images.

**Installation:**

1. Open a terminal.
2. Install digiKam using the OpenSUSE package manager:
   ```bash
   sudo zypper install digikam
   ```
3. Launch digiKam from your applications menu once the installation is complete.

### 3. **Shotwell**

Shotwell is a simple photo manager that includes basic editing features such as cropping. It's lightweight and easy to use.

**Installation:**

1. Open a terminal.
2. Install Shotwell using the OpenSUSE package manager:
   ```bash
   sudo zypper install shotwell
   ```
3. Launch Shotwell from your applications menu.

### 4. **GIMP with Batch Processing**

If you prefer to stick with GIMP but want to streamline the process, you could use GIMP for the cropping and then automate the export with a script. Although this won't help with the manual cropping part, it can help with batch exporting.

### Workflow Recommendation:

Given your requirement to visually crop each image, XNView MP or digiKam might offer the best combination of speed and simplicity. Both allow you to quickly open, crop, and save images without the overhead of heavier tools like GIMP.

Remember to always back up your images before starting the batch processing to avoid any accidental data loss.
