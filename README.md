# KSL Vehicle Scraper

This Python script (`main.py`) scrapes vehicle listings from KSL Classifieds and stores the results in JSON format. It utilizes Selenium for web scraping and BeautifulSoup for HTML parsing.

## Project Overview

The script performs the following tasks:

1. **Construct URL**: Constructs the URL based on the vehicle details provided (make, model, and price range).

2. **Scrape Data**: Utilizes Selenium to open the URL in a browser, waits for JavaScript execution, retrieves the HTML content, and then parses it using BeautifulSoup.

3. **Extract Information**: Extracts vehicle details such as year, trim, price, mileage, and link from the parsed HTML.

4. **Update Results**: Compares the newly scraped results with existing results stored in `results.json`, identifies new vehicles, and saves them to `new_results.json`. All results are saved to `results.json`.

5. **Display Results**: Displays the scraped vehicle details, including any new vehicles found.

## Dependencies

Ensure you have the following dependencies installed:

- `json`
- `os`
- `selenium`
- `beautifulsoup4`

You can install the dependencies using pip:

```bash
pip install selenium beautifulsoup4
```

## Usage

1. **Configure Vehicle Details**: Modify the `vehicle` dictionary in the script with the desired vehicle make, model, and price range.

2. **Run the Script**: Execute the script by running the following command in your terminal:

    ```bash
    python main.py
    ```

3. **View Results**: The scraped vehicle details will be displayed in the terminal. Any new vehicles found will be saved in `new_results.json`, and all results will be saved in `results.json`.

## Note

- Ensure you have the appropriate web driver for Selenium (e.g., ChromeDriver) installed and added to your system's PATH.
- Adjust the `implicitly_wait` duration in the script based on the page load time.
- This script is provided for educational purposes and may require adjustments to work with different websites or environments.

---

*Disclaimer: This project is not affiliated with or endorsed by KSL Classifieds. Use at your own risk.*
