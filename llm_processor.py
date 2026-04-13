import os
from openai import OpenAI
from tenacity import retry, wait_random_exponential, stop_after_attempt
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# This decorator automatically retries the function if it hits a rate limit or network error
@retry(wait=wait_random_exponential(min=1, max=60), stop=stop_after_attempt(5))
def summarize_review(review_text):
    # Preprocessing: Basic truncation if review is absurdly long to save tokens
    # (In a production app, you might use tiktoken to chunk precisely)
    if len(review_text) > 4000: 
        review_text = review_text[:4000] + "..."

    prompt = f"""
    Analyze the following product review. 
    Provide a 1-sentence summary of the main point, and classify the sentiment as POSITIVE, NEUTRAL, or NEGATIVE.
    Format your response exactly as: [Sentiment] - [Summary]
    
    Review: {review_text}
    """

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful e-commerce data analyst."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.3, # Low temperature for more deterministic output
        max_tokens=60
    )
    
    return response.choices[0].message.content.strip()