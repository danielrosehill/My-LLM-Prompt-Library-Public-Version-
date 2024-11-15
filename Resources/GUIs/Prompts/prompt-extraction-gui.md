I would like you to generate a simple Python GUI for the purpose of saving LLM outputs and extracting the prompts they contain. 

I will describe the functionality that I need. 

Please return the finished code, verifying that it works properly.

The GUI should have three text boxes:

- One for entering a title. This should be a single line field.
- One for entering a prompt. This should be a multiple line field capable of storing 2 paragraphs of text.
- One for saving an output. This should be a multiple line field which can store several paragraphs of rich text preserving its formatting. 

There should also be buttons for saving a few paths:

- A button for saving the prompt storage path in the local filesystem. When the user clicks on this, they should be able to navigate to a folder in the local filesystem.
- A button for saving the output storage path in the local filesystem. When the user clicks on this, they should be able to navigate to a folder in the local filesystem.

It is essential that these paths will persist through a reboot. So please make sure that the app has the ability to use persistent storage. 

Here is the functionality that I would like the GUI to enable:

- The user will enter a title, a prompt, and an output into the text field and click on 'save to library'.

## App Logic

When the user clicks on the save button, the following logic should happen:

- The prompt and output are joined together and saved as a markdown file in the outputs folder which the user selected. The file name will be a prettified version of the title. If the user configured a title of "Top ChatGPT Tips" then the prompt and output should be collected into a file called top-chatgpt-tips.md in the outputs folder. The markdown file generated should follow template 1 which appears below.

- The prompt is also saved as a markdown file in the prompts folder which the user selected. The file name will be a prettified version of the title. If the user configured a title of "Top ChatGPT Tips" then the prompt should be copied and saved to a file called top-chatgpt-tips.md in the prompts folder. The markdown file generated should follow template 2 which appears below.

## File Generation Templates

Template 1:

# Prompt

(The text of the prompt)

# Output

(The text of the output)

Template 2:

# Prompt

(The text of the prompt)

## Action After Saving

After the user saves a prompt and an output:

1: The files should be created as described above
2: A success message should appear. It should say "prompt and output saved"
3: The input fields should clear so that the user can repeat the process and save a new prompt.

## UI Design

Please create an attractive user interface with a modern design. 

