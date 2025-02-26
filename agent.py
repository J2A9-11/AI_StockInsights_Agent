import google.generativeai as genai
from tool import fetch_stock_data

# Load Gemini API key
genai.configure(api_key="your-api-key")

def gemini_agent(ticker):
    """Fetch stock data and generate a response using Gemini."""
    stock_info = fetch_stock_data(ticker)
    response = genai.GenerativeModel("gemini-1.5-pro-latest").generate_content(
        f"Analyze the stock trend and provide insights: {stock_info}"
    )
    return response.text

# User interaction loop
def agent_interaction():
    while True:
        ticker = input("Enter stock ticker (or 'exit' to quit): ").strip().upper()
        if ticker == "EXIT":
            break
        response = gemini_agent(ticker)
        print(response)

if __name__ == "__main__":
    agent_interaction()

