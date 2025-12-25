# Crypto Mover Watch

This project fetches the top 100 cryptocurrencies by market capitalization from the CoinGecko API, identifies the top 3 gainers and top 3 losers over the last 24 hours, and generates a daily Markdown report.

## Setup

1.  **Clone the repository (if applicable) or navigate to the project directory:**
    ```bash
    cd crypto-mover-watch
    ```

2.  **Create and activate a Python virtual environment:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Install the required Python packages:**
    ```bash
    pip install -r requirements.txt
    ```

## Usage

To fetch the data and generate the daily report, run the `main.py` script:

```bash
source venv/bin/activate
python main.py
```

This will create a `daily_crypto_movers.md` file in the project directory, containing the report.

## Future Enhancements (Planned)

*   Integration with a Large Language Model (LLM) for "Why" analysis of movers.
*   Automation of daily report generation using cron jobs or similar scheduling tools.
*   Options for publishing the generated content to a static site or blog.
*   Monetization through affiliate links or advertising.
