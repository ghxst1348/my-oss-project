import os
from openai import OpenAI

# Initialize the OpenAI client
# In production, ensure the OPENAI_API_KEY is set in your environment variables
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY", "your-placeholder-key"))

def summarize_text(text):
    """
    Summarizes long input text using OpenAI API.
    """
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo", # Can be upgraded to newer models with API credits
            messages=[
                {"role": "system", "content": "You are a helpful assistant that summarizes text concisely."},
                {"role": "user", "content": f"Please summarize this:\n\n{text}"}
            ]
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error connecting to OpenAI API: {str(e)}"

if __name__ == "__main__":
    print("--- AI Task Automator CLI ---")
    sample_text = "OpenAI is an AI research and deployment company. Their mission is to ensure that artificial general intelligence benefits all of humanity. OpenAI has released several highly capable language models."
    
    print("\n[Testing Summary Feature...]")
    summary = summarize_text(sample_text)
    print(f"Result:\n{summary}")
