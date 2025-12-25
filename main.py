import requests
import json
import os
from datetime import datetime
import google.generativeai as genai
import time

COINGECKO_API_URL = "https://api.coingecko.com/api/v3/coins/markets"

def configure_genai():
    """Configures the Google Generative AI API."""
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        print("Warning: GEMINI_API_KEY environment variable not set. Skipping AI analysis.")
        return False
    genai.configure(api_key=api_key)
    return True

def fetch_crypto_data():
    """
    Fetches cryptocurrency data from the CoinGecko API.
    Returns a list of dictionaries, each representing a cryptocurrency.
    """
    params = {
        "vs_currency": "usd",
        "order": "market_cap_desc",
        "per_page": 100,
        "page": 1,
        "sparkline": "false",
        "price_change_percentage": "24h"
    }
    try:
        response = requests.get(COINGECKO_API_URL, params=params)
        response.raise_for_status() # Raise an exception for HTTP errors
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from CoinGecko API: {e}")
        return None

def analyze_mover(name, symbol, change, is_configured):
    """
    Uses Gemini to analyze why a crypto moved.
    """
    if not is_configured:
        return "Analysis unavailable (API key missing)."

    model = genai.GenerativeModel('gemini-2.5-flash')
    direction = "up" if change > 0 else "down"
    prompt = (
        f"The cryptocurrency {name} ({symbol}) is {direction} by {abs(change):.2f}% in the last 24 hours. "
        f"Provide a single, concise sentence explaining the most likely reason for this price movement based on recent news or market trends. "
        f"If there is no specific news, mention that it follows general market volatility."
    )
    
    try:
        response = model.generate_content(prompt)
        # Add a small delay to avoid hitting rate limits too quickly
        time.sleep(1) 
        return response.text.strip()
    except Exception as e:
        print(f"Error analyzing {name}: {e}")
        return "Analysis unavailable due to error."

def generate_markdown_report(gainers, losers, gainers_analysis, losers_analysis):
    """
    Generates a Markdown formatted report of top gainers and losers.
    """
    report_date = datetime.now().strftime("%Y-%m-%d")
    report = f"# Daily Crypto Movers - {report_date}\n\n"
    
    report += "## Top 3 Gainers (24h)\n"
    for i, crypto in enumerate(gainers):
        report += (f"### {i+1}. {crypto['name']} ({crypto['symbol'].upper()})\n"
                   f"- **Price:** ${crypto['current_price']:.2f}\n"
                   f"- **Change:** +{crypto['price_change_percentage_24h']:.2f}%\n"
                   f"- **Analysis:** {gainers_analysis[i]}\n\n")

    report += "## Top 3 Losers (24h)\n"
    for i, crypto in enumerate(losers):
        report += (f"### {i+1}. {crypto['name']} ({crypto['symbol'].upper()})\n"
                   f"- **Price:** ${crypto['current_price']:.2f}\n"
                   f"- **Change:** {crypto['price_change_percentage_24h']:.2f}%\n"
                   f"- **Analysis:** {losers_analysis[i]}\n\n")
    return report

def main():
    is_genai_configured = configure_genai()
    crypto_data = fetch_crypto_data()
    
    if crypto_data:
        # Filter out cryptos without 24h price change data
        filtered_data = [
            c for c in crypto_data
            if c.get('price_change_percentage_24h') is not None
        ]

        if not filtered_data:
            print("No crypto data with 24h price change available.")
            return

        # Sort by 24h price change percentage
        sorted_by_change = sorted(
            filtered_data,
            key=lambda x: x['price_change_percentage_24h'],
            reverse=True
        )

        top_gainers = sorted_by_change[:3]
        top_losers = sorted_by_change[-3:]

        print("Analyzing top gainers...")
        gainers_analysis = []
        for crypto in top_gainers:
            print(f"  - Analyzing {crypto['name']}...")
            analysis = analyze_mover(
                crypto['name'], 
                crypto['symbol'], 
                crypto['price_change_percentage_24h'], 
                is_genai_configured
            )
            gainers_analysis.append(analysis)

        print("Analyzing top losers...")
        losers_analysis = []
        for crypto in top_losers:
            print(f"  - Analyzing {crypto['name']}...")
            analysis = analyze_mover(
                crypto['name'], 
                crypto['symbol'], 
                crypto['price_change_percentage_24h'], 
                is_genai_configured
            )
            losers_analysis.append(analysis)
        
        report_content = generate_markdown_report(
            top_gainers, top_losers, gainers_analysis, losers_analysis
        )
        
        with open("daily_crypto_movers.md", "w") as f:
            f.write(report_content)
        print("\nDaily crypto movers report saved to daily_crypto_movers.md")

    else:
        print("Failed to fetch crypto data.")

if __name__ == "__main__":
    main()
