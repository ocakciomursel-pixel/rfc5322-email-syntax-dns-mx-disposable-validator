"""
B2B Domain Contact, Email, DNS & Tech Stack Enricher — Python Quickstart
Official Apify Store Actor: https://apify.com/lucacelli/b2b-domain-contact-tech-enricher ($0.80 / 1,000 domains)
"""
import os
import requests

APIFY_TOKEN = os.getenv("APIFY_TOKEN", "YOUR_APIFY_TOKEN")
ENDPOINT = "https://api.apify.com/v2/acts/lucacelli~b2b-domain-contact-tech-enricher/run-sync-get-dataset-items"

payload = {
    "domains": [
        "stripe.com",
        "linear.app",
        "vercel.com"
    ],
    "extractEmails": True,
    "detectTechStack": True
}

if __name__ == "__main__":
    print(f"Running B2B Domain Contact, Email, DNS & Tech Stack Enricher on Apify Cloud ({ENDPOINT})...")
    response = requests.post(f"{ENDPOINT}?token={APIFY_TOKEN}", json=payload, timeout=300)
    response.raise_for_status()
    data = response.json()
    print(f"Extracted {len(data)} records! Sample:")
    print(data[:3])
