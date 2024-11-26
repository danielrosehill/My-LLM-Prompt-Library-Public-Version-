---
title: "Write me a Docker Compose"
---

## Using LLMs to generate custom docker compose files

A great use for LLMs is asking them to write custom `docker-compose.yml` files in case you're looking to deploy something but there isn't *quite* an exact match for your needs already out there.

`yml` being super picky about syntax, an LLM takes all the inconvenience away from manually defining services.

I've found that even when a `docker-compose.yml` *does* exist in documentation, an LLM can make little adjustments.

## Prompt variations

I've tried a few approaches, all have worked pretty well.

One is just taking the lazy approach of asking it to generate a `docker compose` even if you're pretty sure that one exists.

I just prompted, for example:

>I'd like to installed LangFuse and Postgres on this server. Please generate a docker compose

## Adding context

If you use the excellent Portainer, then another approachthat I've found useful is this:

- Screenshot your containr list so that the LLM can "see" what ports are currently occupied  
- Ask it to generate the `docker compose` ensuring that there are no port conflicts

The variations are pretty much endless.

For example, if you know that a project can work with MongoDB but there isn't a `docker compose` template in existence, try:

> This Docker Compose provides Postgres. Modify it so that the database is MongoDB.