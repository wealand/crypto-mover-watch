# Handover Notes: Crypto Mover Watch Project

This document outlines the final steps you need to take to get your `crypto-mover-watch` project fully automated and deployed using GitHub Pages.

## Your Tasks:

1.  **Create a New GitHub Repository:**
    *   Go to [github.com/new](https://github.com/new).
    *   Name your repository (e.g., `crypto-mover-watch`).
    *   Choose your desired visibility (Public is required for GitHub Pages).
    *   **Do NOT initialize with a README, .gitignore, or license** (we already have these locally).
    *   Click "Create repository".

2.  **Add Your Gemini API Key as a GitHub Secret:**
    *   On your newly created GitHub repository page, navigate to **Settings** (usually in the top menu).
    *   In the left sidebar, click on **Secrets and variables** > **Actions**.
    *   Click the **"New repository secret"** button.
    *   For **Name**, enter: `GEMINI_API_KEY` (It must match exactly).
    *   For **Secret**, paste your actual Gemini API key (the string starting with `AIza...`).
    *   Click "Add secret".

3.  **Push Your Local Code to GitHub:**
    *   Open your terminal.
    *   Navigate to your project directory: `cd crypto-mover-watch`
    *   Add all local files to git: `git add .`
    *   Commit your changes: `git commit -m "Initial commit: Crypto Mover Watch with Gemini integration"`
    *   Set the remote origin (replace `YOUR_USERNAME` with your GitHub username):
        `git remote add origin https://github.com/YOUR_USERNAME/crypto-mover-watch.git`
    *   Push your code to the `main` branch: `git push -u origin main`

4.  **Enable GitHub Pages:**
    *   On your GitHub repository page, navigate to **Settings** (top menu).
    *   In the left sidebar, click on **Pages**.
    *   Under "Build and deployment", for "Source", select `Deploy from a branch`.
    *   For "Branch", select `main` and `/ (root)` for the folder.
    *   Click the **"Save"** button.

## What will happen next?

*   GitHub Actions will automatically detect the workflow file (`.github/workflows/daily_update.yml`).
*   It will run the first time, and then every day at 08:00 UTC.
*   The workflow will:
    *   Checkout your code.
    *   Install Python dependencies.
    *   Run `main.py` (using your `GEMINI_API_KEY` secret).
    *   Generate `daily_crypto_movers.md`.
    *   Copy `daily_crypto_movers.md` to `index.md`.
    *   Commit these changes back to your `main` branch.
    *   GitHub Pages will then automatically publish the `index.md` as your website.

Your live report will be accessible at: `https://YOUR_USERNAME.github.io/crypto-mover-watch/` (replace `YOUR_USERNAME`).

## Next Steps (Optional, as per our original plan):

*   **Monetization**: Once the site is live, you can explore adding affiliate links to crypto exchanges within your Markdown report.
*   **Refinement**: Improve the LLM prompts for more specific analysis.
*   **Further Automation**: Explore other publishing options beyond GitHub Pages if you want more advanced features.

Good luck, and enjoy your new passive income stream!