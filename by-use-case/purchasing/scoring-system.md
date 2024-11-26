---
title: "Scoring system prompt method for purchasing"
---

## Devise a scoring system to choose a purchasing list "winner"

The perfect solution when you're looking for that perfect something but having a hard time picking a winner.

We could prompt like this:

### V1: "Normal" prompt without scoring system

```text
 I'm looking for a keyboard:

These features are essential:

- Ergonomic layout
-  Quiet / silent operation
- No RGB or ability to disable RGB

These features are less essential but still important to me:

- Wireless support (dongle ideal)
- Mechanical operation

And finally, these features are less important but also desirable:

- Macro keys

For each match, list:

- RRP
- If it's available on Amazon

Format the output as a markdown table evaluating the options according to each of these parameters
```

## V2: Deeper evaluation with ranking system

For this version of the prompt I added a  few more parameters to try finally find this keyboard!

### Prompt

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

Find the best 5 matches. Then rank them with this scoring system:

-  For each feature in group A, they get 3 points  
-  For each feature in group B, they get 2 points  
-  For each feature in group C, they get 1 point
-  If it has RGB, it gets deducted 6 points

Finally, format your output like this, as a winner table, using a markdown table:

Product Name |   RRP  |  Total Points