---
title: "Local prompt saving GUI"
---

## Prompt to generate utility for saving prompts to local folder

###

Notes:

- Replace OS (etc) with your own parameters  
- Python will (usually!) require a bit of debugging before it works but ... it usually eventually does  

### Prompt Text

Generate a GUI that can run on OpenSUSE Linux and which will has the following functions:

Note: configurations would need to be able to persist through system reboot (ie, they should be stored in memory)

- The user can specify a folder where they would like to save outputs

The GUI has two text input fields:

- Prompt name
- Prompt text

The user can enter both and hit "send prompt"

When the button is pressed:

- The prompt is sent to OpenAI API for completion 
- The completion is written to the output folder the user specified as a markdown file. Its filename is a truncated version of the prompt name

For example:

The user enters:

- Prompt name: Capital of France
- Prompt text: What's the capital of France?

The output gets saved to the output folder as capital-of-france.md

After the prompt is sent the fields clear so that the user can use the interface again