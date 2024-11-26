---
title: "Useful Docker Compose assistance"
---

## Some more ways LLMs can help with Docker issues

`docker-compose` files can be a lot of information.

Another way that I like to use LLMs to make working with Docker easier is to run prompts against `docker-compose.yml` files.

The methodology here is pretty self-explanatory:

- Drop a `docker compose` into the LLM chat (or IDE copilot or whatever you're using)  
- Ask it questions about it

As I covered in a separate note, you can use LLMs to generate or modify existing docker compose files, like:

> Could you add in this service? 
> Could you change the database used from Postgres to Mongo (assuming it's supported)?  

## Example: which volumes have persistent data?

Something I like to make sure I'm always clear on when working with Docker is understanding which services have persistent mount points on the server and *where* those mount points are (ie, the paths).

Usually, I'll tweak the `docker compose` to set my own.

Providing an LLM with a `docker compose` I might prompt:

> Read this docker compose. Identify which containers have persistent mount points. State where those are.

You can also specify the format you'd like to to output as, like:

Structure your ouput as follows:

## Service (name of the service)
Local mount path  