# Rfc5322 Email Syntax Dns Mx Disposable Validator (n8n, Claude MCP & Cloud API)

[![Run on Apify Cloud](https://img.shields.io/badge/Apify_Cloud_Actor-Run_Now_(%240.80%2F1k)-16a34a?style=for-the-badge&logo=apify)](https://apify.com/lucacelli/b2b-domain-contact-tech-enricher)
[![Interactive API Playground](https://img.shields.io/badge/Live_API_Playground-Try_in_Browser-0284c7?style=for-the-badge)](https://ocakciomursel-pixel.github.io/b2b-domain-contact-tech-enricher/)
[![Claude MCP Ready](https://img.shields.io/badge/Claude_&_Cursor_MCP-Ready-7c3aed?style=for-the-badge)](https://apify.com/lucacelli/b2b-domain-contact-tech-enricher)
[![n8n & Make Blueprints](https://img.shields.io/badge/n8n_&_Make.com-Blueprints_Included-ea580c?style=for-the-badge)](./workflows/n8n-workflow.json)

> **Enrich any list of company domains with verified business emails, phone numbers, LinkedIn/X/Instagram links, MX/SPF/DMARC security policies, 38+ SaaS/Pixel signatures, and personalized cold email icebreakers.**
>
> 💡 **Why pay Apollo.io / BuiltWith / Hunter ($99–$295/mo) when you can run on-demand in the cloud for just `$0.80 per 1,000 domains` (`$0.0008/domain`) with $0 monthly subscription?**
> *(Every Apify account includes **$5.00 in free monthly usage credits** — meaning you can extract up to **3,300–10,000 records every month for $0!**)*
>
> 👉 **[Launch B2B Domain Contact, Email, DNS & Tech Stack Enricher on Apify Cloud →](https://apify.com/lucacelli/b2b-domain-contact-tech-enricher)**

---

## 🎁 Ready-to-Import Automation Blueprints Included in This Repo

We have pre-packaged turnkey templates in this repository so you can plug **[lucacelli/b2b-domain-contact-tech-enricher](https://apify.com/lucacelli/b2b-domain-contact-tech-enricher)** directly into your AI agents and automation pipelines in 30 seconds:

1. **⚡ [1-Click n8n Workflow (`workflows/n8n-workflow.json`)](./workflows/n8n-workflow.json)** — Import directly into **n8n**; pre-wired to `https://api.apify.com/v2/acts/lucacelli~b2b-domain-contact-tech-enricher/run-sync-get-dataset-items`.
2. **🟣 [Make.com Scenario Blueprint (`workflows/make-com-blueprint.json`)](./workflows/make-com-blueprint.json)** — Import directly into **Make.com**.
3. **🤖 [Claude Desktop / Cursor MCP Server Config (`mcp/claude_desktop_config.json`)](./mcp/claude_desktop_config.json)** — Let Claude, Cursor, or Windsurf call this scraper autonomously via Model Context Protocol!
4. **🐍 [Python Quickstart (`python_quickstart.py`)](./python_quickstart.py)** & **🟢 [Node.js CLI (`index.js`)](./index.js)**.

---

## 🤖 Use as an AI Agent Tool (Claude Desktop, Cursor, Windsurf MCP)

Add this block to your `claude_desktop_config.json` or Cursor MCP settings to let your AI assistant run **[B2B Domain Contact, Email, DNS & Tech Stack Enricher](https://apify.com/lucacelli/b2b-domain-contact-tech-enricher)** on demand:

```json
{
  "mcpServers": {
    "lucacelli-b2b-domain-contact-tech-enricher": {
      "command": "npx",
      "args": [
        "-y",
        "@apify/actors-mcp-server",
        "--actors",
        "lucacelli/b2b-domain-contact-tech-enricher"
      ],
      "env": {
        "APIFY_TOKEN": "YOUR_APIFY_TOKEN_HERE"
      }
    }
  }
}
```

---

## ⚡ Synchronous REST API, Python & Node.js Quickstart

### 1. Run via cURL (Returns JSON Dataset Directly)

```bash
curl -X POST "https://api.apify.com/v2/acts/lucacelli~b2b-domain-contact-tech-enricher/run-sync-get-dataset-items?token=YOUR_APIFY_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
  "domains": [
    "stripe.com",
    "linear.app",
    "vercel.com"
  ],
  "extractEmails": true,
  "detectTechStack": true
}'
```

### 2. Run via Node.js CLI (Included in Repo)

```bash
git clone https://github.com/ocakciomursel-pixel/b2b-domain-contact-tech-enricher.git
cd b2b-domain-contact-tech-enricher
APIFY_TOKEN="your_apify_token" node index.js
```

---

## 📊 Price & Capability Comparison vs. Legacy SaaS Tools

| Feature | **[Lucacelli Apify Actor](https://apify.com/lucacelli/b2b-domain-contact-tech-enricher)** | **Apollo.io / BuiltWith / Hunter ($99–$295/mo)** | **Self-Hosted Puppeteer/Playwright** |
| :--- | :--- | :--- | :--- |
| **Cost per 1,000 domains** | **$0.80 / 1k** (Pay-as-you-go) | $49–$299/mo mandatory subscription | $40+/mo VPS + residential proxy costs |
| **Free Monthly Tier** | **Yes ($5/mo free Apify credit)** | Credit card / trial wall | None |
| **Anti-Bot & Proxy Rotation** | **Included automatically** | Extra credit charges | Manual maintenance |
| **n8n / Make / Claude MCP** | **Native 1-Click Templates Included** | Paid Enterprise API tier only | Requires custom webhook server |

---

## 🔥 Complete Suite of 14 Live Cloud Actors by [@lucacelli](https://apify.com/lucacelli)

| Cloud Actor | Price | Legacy Competitor Replaced | Run in Cloud |
| :--- | :--- | :--- | :--- |
| **[Google Maps Scraper: Places, Emails, Contacts & Reviews Pro](https://apify.com/lucacelli/google-maps-scraper-places-emails-contacts-reviews)** | **$1.50 / 1k places** | Replaces *Outscraper / PhantomBuster ($49–$199/mo)* | [🚀 Run on Apify →](https://apify.com/lucacelli/google-maps-scraper-places-emails-contacts-reviews) |
| **[B2B Domain Contact, Email, DNS & Tech Stack Enricher](https://apify.com/lucacelli/b2b-domain-contact-tech-enricher)** | **$0.80 / 1k domains** | Replaces *Apollo.io / BuiltWith / Hunter ($99–$295/mo)* | [🚀 Run on Apify →](https://apify.com/lucacelli/b2b-domain-contact-tech-enricher) |
| **[Shopify Store Product, Pricing, Stock & Merchant Contact Spy](https://apify.com/lucacelli/shopify-store-product-contact-spy)** | **$0.50 / 1k products** | Replaces *Koala Inspector / Commerce Inspector ($49–$99/mo)* | [🚀 Run on Apify →](https://apify.com/lucacelli/shopify-store-product-contact-spy) |
| **[Website to Clean Markdown, Vector RAG Chunks & llms.txt](https://apify.com/lucacelli/ai-ready-website-to-markdown-rag-crawler)** | **$0.50 / 1k pages** | Replaces *Firecrawl / Jina Reader API ($19–$99/mo)* | [🚀 Run on Apify →](https://apify.com/lucacelli/ai-ready-website-to-markdown-rag-crawler) |
| **[Technical SEO, Broken Link, Schema.org & Security Auditor](https://apify.com/lucacelli/seo-technical-audit-broken-link-schema-analyzer)** | **$0.80 / 1k pages** | Replaces *Screaming Frog / Ahrefs Site Audit ($99–$249/mo)* | [🚀 Run on Apify →](https://apify.com/lucacelli/seo-technical-audit-broken-link-schema-analyzer) |
| **[GitHub Developer, Stargazer & Contributor Lead Enricher](https://apify.com/lucacelli/github-developer-recruiter-lead-enricher)** | **$0.80 / 1k developers** | Replaces *SeekOut / Gem / Clay ($149–$499/mo)* | [🚀 Run on Apify →](https://apify.com/lucacelli/github-developer-recruiter-lead-enricher) |
| **[Greenhouse & Lever Company Job Board & Hiring Signal Scraper](https://apify.com/lucacelli/ats-job-board-hiring-signal-scraper)** | **$0.50 / 1k jobs** | Replaces *Clay Hiring Signals / LoneScale ($149+/mo)* | [🚀 Run on Apify →](https://apify.com/lucacelli/ats-job-board-hiring-signal-scraper) |
| **[Reddit Subreddit, Buyer Intent & Pain-Point Lead Miner](https://apify.com/lucacelli/reddit-community-pain-point-trend-miner)** | **$0.50 / 1k posts** | Replaces *GummySearch / Syften ($29–$79/mo)* | [🚀 Run on Apify →](https://apify.com/lucacelli/reddit-community-pain-point-trend-miner) |
| **[WordPress & WooCommerce Theme, Plugin & Agency Lead Spy](https://apify.com/lucacelli/wordpress-woocommerce-site-spy)** | **$0.80 / 1k sites** | Replaces *Wappalyzer / BuiltWith ($99+/mo)* | [🚀 Run on Apify →](https://apify.com/lucacelli/wordpress-woocommerce-site-spy) |
| **[Hacker News Launch, Show HN & Tech Founder Lead Monitor](https://apify.com/lucacelli/hackernews-tech-launch-lead-monitor)** | **$0.50 / 1k storys** | Replaces *Harmonic.ai / PitchBook Alerts ($200+/mo)* | [🚀 Run on Apify →](https://apify.com/lucacelli/hackernews-tech-launch-lead-monitor) |
| **[XML Sitemap URL Inventory, SEO Freshness & Content Auditor](https://apify.com/lucacelli/sitemap-url-inventory-content-freshness-auditor)** | **$0.50 / 1k URLs** | Replaces *Visualping / Screaming Frog ($49+/mo)* | [🚀 Run on Apify →](https://apify.com/lucacelli/sitemap-url-inventory-content-freshness-auditor) |
| **[SaaS Pricing Page, Plan Tiers & Competitor Feature Spy](https://apify.com/lucacelli/saas-pricing-page-tier-feature-extractor)** | **$0.80 / 1k pages** | Replaces *Klue / Crayon ($500+/mo)* | [🚀 Run on Apify →](https://apify.com/lucacelli/saas-pricing-page-tier-feature-extractor) |
| **[ClinicalTrials.gov & OpenFDA Biotech / Pharma Lead Enricher](https://apify.com/lucacelli/clinical-trials-fda-drug-safety-intel)** | **$0.80 / 1k trials** | Replaces *Citeline / GlobalData Pharma ($500+/mo)* | [🚀 Run on Apify →](https://apify.com/lucacelli/clinical-trials-fda-drug-safety-intel) |
| **[Scientific Paper, Author Email & Lab Research Lead Miner](https://apify.com/lucacelli/scientific-literature-citation-author-lead-miner)** | **$0.50 / 1k papers** | Replaces *Dimensions.ai / SciLeads ($300+/mo)* | [🚀 Run on Apify →](https://apify.com/lucacelli/scientific-literature-citation-author-lead-miner) |

---

## 🌐 Live Browser Playground & Code Generator
Test live inputs and generate cURL, Python, Node.js, n8n, and MCP configs directly in your browser:
👉 **[https://ocakciomursel-pixel.github.io/b2b-domain-contact-tech-enricher/](https://ocakciomursel-pixel.github.io/b2b-domain-contact-tech-enricher/)**
