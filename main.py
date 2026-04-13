# import pandas as pd
# from scraper import fetch_page_html, parse_reviews
# from llm_processor import summarize_review
# import time

# def main():
#     target_url = "https://www.amazon.in/gp/help/customer/display.html?nodeId=G3UA5WC5S5UUKB5G"
#     print(f"Fetching reviews from {target_url}...")
    
#     html = fetch_page_html(target_url)
#     if not html:
#         print("Failed to retrieve HTML. Exiting.")
#         return

#     reviews = parse_reviews(html)
#     print(f"Extracted {len(reviews)} reviews. Starting LLM processing...")

#     # Process through LLM
#     for review in reviews:
#         print(f"Processing review by {review['Author']}...")
#         try:
#             llm_output = summarize_review(review['Original_Text'])
#             review['LLM_Summary_and_Sentiment'] = llm_output
#         except Exception as e:
#             print(f"Failed to process review with LLM: {e}")
#             review['LLM_Summary_and_Sentiment'] = "Error during processing"
            
#         # Slight pause to be polite to the API, though tenacity handles hard limits
#         time.sleep(0.5) 

#     # Save to CSV
#     df = pd.DataFrame(reviews)
#     output_file = "output/processed_reviews.csv"
#     df.to_csv(output_file, index=False)
#     print(f"Done! Saved results to {output_file}")

# if __name__ == "__main__":
#     main()




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