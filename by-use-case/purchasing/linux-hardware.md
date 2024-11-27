---
title: "Finding Linux compatible hardware with LLMs"
---

# Finding Linux compatible hardware with the help of LLMs

## The Problem

While Linux is amazing, finding hardware that's *compatible* with Linux isn't always such a glorious experience.

## Databases help up to a point

While there are *some* Linux databases that list compatible hardware, Reddit threads, etc, especially when dealing in the murky world of Aliexpress hardware, it's still not always easy to find products that stand a better chance of working out of the box - especially when who makes them (!) isn't always as clear as might be hoped.

Also: there are many distros and even if a product says it "supports Linux" given how many variations on the Linux OS there are, that's not always even a guarantee it will work.

## Why would it work or not work?

The approach I've tried with some success instead is to try to understand why a specific piece of hardware *would* or *would not* work. Ie, is there an open source driver that - if it exists - will probably help or vice versa.

**My prompting template is something like*::

I use OpenSUSE Tumbleweed.

I'm looking for a macropad.

What specifications should I look for that would increase the likelihood that this will work on this distro?

What specifications would indicate that there is a lesser chance that this will work?

## Pair with a direct prompt

If you're fortunate enought to have regular access to something like Amazon, you can use a dual-pronged research approach:

1 - Ask for specific product recommendations  
2 - If you feel like branching out a bit, try to get a sense, as well, for how general compatibility might be achieved

## My backup approach

Sometimes, ordering hardware for Linux is just a bit of a gamble.

If it's a not-inconsequential amount of money at stake, I sometimes try to figure out if - worst case scenario - there are workarounds.

Like:

> I'm looking at this macropad. If it's not detected on Linux, is there any way to program it on Windows in a way that it will store the configurations?

The great thing about prompting LLMs: unlike posting on Reddit communities, you don't have to worry about being judged extremely hardshly for asking a question that's deemed "stupid."

The robot has no strong feelings about you or your question. So ask whatever you think might bring clarity to your search.