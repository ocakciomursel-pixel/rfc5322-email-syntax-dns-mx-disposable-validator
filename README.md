# Rfc5322 Email Syntax Dns Mx Disposable Validator (Powered by B2B Domain Contact, Email, DNS & Tech Stack Enricher)

[![Run on Apify Cloud](https://img.shields.io/badge/Apify_Cloud_Actor-Run_Now_(%240.80%2F1k)-16a34a?style=for-the-badge&logo=apify)](https://apify.com/lucacelli/b2b-domain-contact-tech-enricher)
[![Interactive API Playground](https://img.shields.io/badge/Live_API_Playground-Try_in_Browser-0284c7?style=for-the-badge)](https://ocakciomursel-pixel.github.io/b2b-domain-contact-tech-enricher/)
[![All Apify Actors](https://img.shields.io/badge/Apify_Store-@lucacelli-38bdf8?style=for-the-badge)](https://apify.com/lucacelli)

> **Enrich any list of company domains with verified business emails, phone numbers, LinkedIn/X/Instagram links, MX/SPF/DMARC security policies, 38+ SaaS/Pixel signatures, and personalized cold email icebreakers.**
>
> 🚀 **Live on Apify Store:** **[https://apify.com/lucacelli/b2b-domain-contact-tech-enricher](https://apify.com/lucacelli/b2b-domain-contact-tech-enricher)** — Pay-Per-Result pricing at just **$0.80 per 1,000 domains** (`$0.0008/domain`) with **$0 monthly subscription**.

---

## ⚡ 1-Click Cloud Execution & REST API Quickstart

Run **[Rfc5322 Email Syntax Dns Mx Disposable Validator (Powered by B2B Domain Contact, Email, DNS & Tech Stack Enricher)](https://apify.com/lucacelli/b2b-domain-contact-tech-enricher)** directly in the Apify Console or call it synchronously via REST API, Python, Node.js, **n8n**, **Make.com**, **LangChain**, or **Claude Desktop (MCP)**.

### Option A: Run via cURL (Synchronous JSON Output)

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

### Option B: Run via Python (`apify-client`)

```python
from apify_client import ApifyClient

client = ApifyClient("YOUR_APIFY_TOKEN")
run = client.actor("lucacelli/b2b-domain-contact-tech-enricher").call(run_input={
    "domains": [
        "stripe.com",
        "linear.app",
        "vercel.com"
    ],
    "extractEmails": true,
    "detectTechStack": true
})

for item in client.dataset(run["defaultDatasetId"]).iterate_items():
    print(item)
```

### Option C: Run via Node.js (`apify-client`)

```javascript
import { ApifyClient } from 'apify-client';

const client = new ApifyClient({ token: process.env.APIFY_TOKEN });
const run = await client.actor('lucacelli/b2b-domain-contact-tech-enricher').call({
  "domains": [
    "stripe.com",
    "linear.app",
    "vercel.com"
  ],
  "extractEmails": true,
  "detectTechStack": true
});
const { items } = await client.dataset(run.defaultDatasetId).listItems();
console.log(items);
```

---

## 🌐 All 9 Featured Cloud Actors by [@lucacelli](https://apify.com/lucacelli)

| Cloud Actor | Pricing (Pay-Per-Event) | Apify Store Link |
| :--- | :--- | :--- |
| **Google Maps Scraper: Places, Emails, Contacts & Reviews Pro** | **$1.50 / 1,000 places** | [Run on Apify Cloud →](https://apify.com/lucacelli/google-maps-scraper-places-emails-contacts-reviews) |
| **B2B Domain Contact, Email, DNS & Tech Stack Enricher** | **$0.80 / 1,000 domains** | [Run on Apify Cloud →](https://apify.com/lucacelli/b2b-domain-contact-tech-enricher) |
| **Shopify Store Product, Pricing, Stock & Merchant Contact Spy** | **$0.50 / 1,000 products** | [Run on Apify Cloud →](https://apify.com/lucacelli/shopify-store-product-contact-spy) |
| **Website to Clean Markdown, Vector RAG Chunks & llms.txt** | **$0.50 / 1,000 pages** | [Run on Apify Cloud →](https://apify.com/lucacelli/ai-ready-website-to-markdown-rag-crawler) |
| **Technical SEO, Broken Link, Schema.org & Security Auditor** | **$0.80 / 1,000 pages** | [Run on Apify Cloud →](https://apify.com/lucacelli/seo-technical-audit-broken-link-schema-analyzer) |
| **GitHub Developer, Stargazer & Contributor Lead Enricher** | **$0.80 / 1,000 developers** | [Run on Apify Cloud →](https://apify.com/lucacelli/github-developer-recruiter-lead-enricher) |
| **Greenhouse & Lever Company Job Board & Hiring Signal Scraper** | **$0.50 / 1,000 jobs** | [Run on Apify Cloud →](https://apify.com/lucacelli/ats-job-board-hiring-signal-scraper) |
| **Reddit Subreddit, Buyer Intent & Pain-Point Lead Miner** | **$0.50 / 1,000 posts** | [Run on Apify Cloud →](https://apify.com/lucacelli/reddit-community-pain-point-trend-miner) |
| **WordPress & WooCommerce Theme, Plugin & Agency Lead Spy** | **$0.80 / 1,000 sites** | [Run on Apify Cloud →](https://apify.com/lucacelli/wordpress-woocommerce-site-spy) |

---

## 🔗 Live Interactive Browser Playground

Test live inputs and generate ready-to-paste cURL, Python, Node.js, and n8n HTTP Request payloads in our interactive web playground:

👉 **[Launch Interactive API Playground →](https://ocakciomursel-pixel.github.io/b2b-domain-contact-tech-enricher/)**

## License
MIT © [Lucacelli Cloud Data Engineering](https://apify.com/lucacelli)
