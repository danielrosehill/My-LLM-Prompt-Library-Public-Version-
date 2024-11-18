# Create A PDF From CSV Data

*Use case: event management, document generation*

I used this prompt to successfully generate a PDF guest list and pivot table from CSV data

This prompt worked much more seamlessly than various CSV to PDF API tools I tried and used

It took a few refinements and likely many more could be made

# Prompt

Please generate a PDF from the CSV that I have just uploaded.

Follow my instructions exactly.

# Section 1: Guest List

Here's how you should format the first section:

Name should be bold and in a large font, as if it were a title.
Email and Organisation should be displayed on the next line in normal font.
On the next line display Organisation in bold
Confirmation Code should follow, labeled clearly.
Contact Type should be displayed in a colored bubble (use light blue for 'General' and light green for others).
Party Size should be the last line in the entry.
Each entry should be separated by a blank line. Add a header titled 'IFVI Guest List' at the top of each page and a footer with the page number at the bottom.

Output the guest list in alphabetical order based upon the guest name. 

# Section 2: Organisations Attending

After you have reached the end of the guest list, create another section called Organisations Present 

Display a table of the organisations in the guest list sorted from those with the most attendees to those with the list. 

Follow this format

Organisation (attendee number)
Names of attendees

The first line should be in bold and the next line should be in regular weight font
Leave a space between each 




