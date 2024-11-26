---
title: "Data retrieval and anlaysis prompt: GHG Emissions"
---

## About The Prompt

This is a complex prompt that uses several steps and is really most suitable for a chaining strategy (the suggested chain: retrieve emissions data; then financials; then compute; then format output).

Like many ambitious prompts, it will hopefuly provide a useful benchmark as models mature and this kind of prompting becomes increasingly feasible and reliable.

## Variables

You can use `LangChain` or (manually) replace the variables. `{ticker}` is there for the purpose of disambiguation.

## Prompt Text

Find the following data for:

{company_name} whose stock market ticker is {ticker}.

### Report Specifics

Retrieve and provide the following details from {company_name}'s latest available sustainability report:

-  Report title
-  Report URL
- Report publication date  

From the sustainability report, extract and output the following, if they are available:

- **GHG emissions (Scope 1)**: Reporting units and quantity
- **GHG emissions (Scope 2)**: Reporting units and quantity
- **GHG emissions (Scope 3)**: Reporting units and quantity

Also note any details about the reporting that are pertinent (for example, scope 1 and 2 are only reported together).

### Computed Fields

Using the extracted data, compute:

1. **Total GHG emissions (all scopes)**: \( \text{Scope 1} + \text{Scope 2} + \text{Scope 3} \)
   - Units: Use the same units as those in which the constituent emissions are reported. If units differ, standardize to a common unit.
2. **Total monetized GHG emissions (all scopes)**: \( (\text{Scope 1} + \text{Scope 2} + \text{Scope 3}) \times 236 \)
   - Units: USD
3. **Total monetized Scope 1 and Scope 2 emissions**: \( (\text{Scope 1} + \text{Scope 2}) \times 236 \)
   - Units: USD

### Additional Financial Data

Retrieve and provide:

- **Price/Earnings (P/E) ratio**:
   - Use the P/E ratio at year-end of the preceding year. If unavailable, provide the latest P/E ratio you can find.
   - Include the P/E ratio source and date.

## Output Formatting

Once all data is retrieved, format your output according to the following template.

### Company (Ticker)

### Sustainability Report

Title:
Publication Date:
URL (print URL, then provide hyperlink)

### Data (Raw)

```csv
Scope,Unit,Quantity,Year
Scope 1,<unit>,<quantity>,<year>
Scope 2,<unit>,<quantity>,<year>
Scope 3,<unit>,<quantity>,<year>
Scope 1+2+3,<unit>,<total_quantity>,<year>
Monetised Emissions,USD,<monetised_total>,<year>

Report URL,<sustainability_report_url>
Report Date,<report_date>
P/E Ratio,<p/e_ratio>
P/E Ratio Date,<p/e_ratio_date>
P/E Ratio Source,<p/e_ratio_source>
GHG Emissions/P/E Ratio (tCO2e/P/E),<ghg_per_pe_ratio>