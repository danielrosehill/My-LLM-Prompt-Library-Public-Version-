---
title: "GHG Emissions & Social Cost Of Carbon Prompts (Data Retrieval)"
---

## Templatable Values

Use `{company-name}`.

This prompt can be templated and used with LangChain (etc).

# Prompt Text

## Scope 1 & 2 GHG Emissions x Social Cost Of Carbon

Find the 2023 sustainability report for: {company-name}

From that report, retrieve each of the following:

- Total scope 1 emissions  
- Total scope 2 emissions  
  
For each, provide both the value and the measurement unit and then list the source (name, URL)

## Data selection

- If emissions are reported on an equity-basis or an operational basis, choose the operational basis data.

- If scope 2 emissions are reported on a location-based or market-based basis, choose the location-based data.

Provide the units in both a written form and their unit of measurement.

Then:

- Calculate the sum of scope 1 and scope 2 emissions. State this as: Scope 1 and 2 (combined).

Then:

- Multiply that value (scope 1 and 2 combined) by 236,000,000 and report that value in $. 

Format this value as: 

- Monetised scope 1 and 2 emissions. 
- Express it firstly as a number and then in billions, correct to two decimal places.

Here's an example showing the requested format. 

Note: the data in parantheses in the header is the company stock ticker and exchange.

# GHG Emissions Data For Shell (LON:SHEL)

Data source:
2023 Sustainability Report
shell.com/sustainability

Scope 1 Emissions:
50 mt2coe

Scope 2 Emissions:
40 mtco2e

Scope 1+ 2 Emissions (Combined):
90 mtco2e.

Monetised scope 1 and 2 emissions: $21240000000 ($21.24)

Units:
Millions of tonnes of carbon dioxide equivalent.

Source:
shell.com/sustainability


## GHG Emissions Data Sourcing Prompt, V2

Find {company}'s latest sustainability report - 2023 if possible.

From that report, retrieve each of the following:

- Total scope 1 emissions  
- Total scope 2 emissions  
- Total scope 3 emissions

For scope 3 emissions, you can use an additional data source.

For each, provide both the value and the measurement unit and then list the source (name, URL)

If emissions are reported on an equity-basis or an operational basis, choose the operational basis data.

If scope 2 emissions are reported on a location-based or market-based basis, choose the location-based data.

Provide the units in both a written form and their unit of measurement.

Find the product of scope 1, 2, and 3 emissions and report it here as the "all scope" emissions number.

Here's an example:

Shell
2023 Sustainability Report
shell.com/sustainability

Scope 1 Emissions:
50 mt2coe

Scope 2 Emissions:
40 mtco2e

Scope 3 emissions:
30 mtco2e.

All scope emissions:
120 mtco2e.

Units:
Millions of tonnes of carbon dioxide equivalent.

Source:
shell.com/sustainability










