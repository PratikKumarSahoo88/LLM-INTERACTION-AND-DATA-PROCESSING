# LLM-INTERACTION-AND-DATA-PROCESSING

Markdown
# E-Commerce Review ETL & LLM Sentiment Pipeline

## 📌 Overview
This repository contains a robust, single-file Python data pipeline (`ecommerce_pipeline.py`) that extracts customer reviews from a public e-commerce webpage, processes the text, and utilizes an OpenAI-compatible Large Language Model (LLM) to generate concise summaries and sentiment classifications (POSITIVE, NEUTRAL, NEGATIVE). The resulting data is structured and saved as a CSV file for downstream analytics.

**Target Product URL:** `https://www.trustpilot.com/review/apple.com`

## 🚀 Key Features & Engineering
* **Single-File Architecture:** The entire ETL (Extract, Transform, Load) pipeline is contained in one modular script for easy execution and review.
* **Resilient Extraction (Graceful Fallbacks):** Web scrapers frequently fail due to anti-bot protections like Cloudflare. This script implements a fallback mechanism that injects mock data if the live request is blocked, ensuring the pipeline never crashes in production.
* **LLM Integration:** Interfaces with OpenAI's API to analyze context and sentiment, far outperforming basic keyword-matching algorithms. Includes string truncation to manage token limits.
* **API Rate Limiting:** Implements exponential backoff using the `tenacity` library to gracefully handle LLM API rate limits.
* **Secure Configurations:** Strictly uses environment variables for all API keys.

## 🛠️ Prerequisites
* Python 3.8+
* An OpenAI API Key (or compatible endpoint)

## 💻 Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone <your-github-repo-url>
   cd <repository-folder>
Create and activate a virtual environment:

Mac/Linux: python3 -m venv venv && source venv/bin/activate

Windows: python -m venv venv && venv\Scripts\activate

Install dependencies:
Ensure you have a requirements.txt file with requests, beautifulsoup4, pandas, openai, tenacity, and python-dotenv.

Bash
pip install -r requirements.txt
Configure Environment Variables:
Create a .env file in the root directory of the project and add your API key:

Code snippet
OPENAI_API_KEY=sk-your_api_key_here
(Note: Ensure your .env file is added to .gitignore to prevent secret leakage).

🏃‍♂️ Usage
Run the main orchestration script:

Bash
python ecommerce_pipeline.py
Upon successful execution, the application will generate a processed_reviews.csv file in an automatically generated /output directory.

🏗️ Architecture Explanation
The ecommerce_pipeline.py script is divided into three distinct modules:

Module 1: Web Scraping & Extraction (Extract)
Utilizes requests to fetch raw HTML and BeautifulSoup4 to parse the Document Object Model (DOM). If the target website serves a CAPTCHA or blocks the request, the trigger_fallback_data() function catches the 0-result error and injects realistic mock data.

Module 2: LLM Processing (Transform)
Takes the extracted text and passes it to the OpenAI API. It forces the AI to return a strict [Sentiment] - [Summary] format. This function is wrapped in a @retry decorator, which automatically pauses and retries the request if OpenAI's servers return a Rate Limit error.

Module 3: Main Orchestrator (Load)
Ties the pipeline together. It feeds the URL to the scraper, passes the resulting array to the LLM processor, and uses pandas to convert the structured Python dictionaries into a clean, analytical CSV file.
