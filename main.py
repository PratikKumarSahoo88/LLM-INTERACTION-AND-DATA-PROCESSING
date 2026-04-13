
import pandas as pd
import os
from scraper import fetch_page_html, parse_reviews

def main():
    target_url = "https://www.trustpilot.com/review/apple.com"
    print(f"Fetching reviews from {target_url}...")
    
    html = fetch_page_html(target_url)
    reviews = parse_reviews(html)
    
    print(f"Extracted {len(reviews)} reviews.")

    if len(reviews) == 0:
        print("0 reviews extracted. Check scraper.py!")
        return

    print("Bypassing OpenAI for testing...")
    
    # Give it fake LLM data just to test the CSV creation
    for review in reviews:
        review['LLM_Summary_and_Sentiment'] = "TESTING - AI TURNED OFF"

    # Check if output folder exists
    if not os.path.exists('output'):
        print("Creating output folder...")
        os.makedirs('output')
        
    # Save to CSV
    df = pd.DataFrame(reviews)
    output_file = "output/processed_reviews.csv"
    df.to_csv(output_file, index=False)
    
    print(f"SUCCESS! Saved results to {output_file}")

if __name__ == "__main__":
    main()
