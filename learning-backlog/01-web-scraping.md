# Phase 1 — Web Scraping & Data Extraction

## Research & Planning

- [ ] Identify target real estate platforms (Finca Raíz, Metrocuadrado, etc.)
- [ ] Understand the difference between API-based and HTML-based scraping
- [ ] Inspect a listing page: identify the HTML elements that hold price, area (m²), neighbourhood, date
- [ ] Review `robots.txt` and terms of service — understand legal and ethical boundaries

## HTTP Fundamentals

- [ ] How HTTP requests work: methods (GET, POST), headers, status codes (200, 403, 429, 500)
- [ ] The `requests` library: making a GET request, reading the response, handling errors
- [ ] Request headers: `User-Agent`, why it matters, setting custom headers
- [ ] Rate limiting: what it is, why it exists, how to respect it

## HTML Parsing

- [ ] HTML structure: tags, attributes, nesting
- [ ] `BeautifulSoup`: parse HTML, navigate the tree, extract text and attributes
- [ ] CSS selectors vs `find()`/`find_all()` — when to use each
- [ ] Extract structured data from a single listing page into a Python dict

## Building the Scraper

- [ ] Handle pagination: detect next page, loop through all pages
- [ ] Error handling: retries with exponential backoff for transient failures
- [ ] Output scraped data as structured JSON (one file per run, per source)
- [ ] Validate extracted data: check for missing fields, unexpected types
- [ ] Make the scraper idempotent — running it twice does not produce duplicates

## Design Patterns Applied

- [ ] Strategy pattern: different scraping logic per source site behind a common interface
- [ ] Factory pattern: instantiate the right scraper based on configuration

## Notes

<!-- Space for observations about the student's progress -->
