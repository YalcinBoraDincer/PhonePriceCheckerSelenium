# 📱 Price Comparison Tool for Phones

## 🌟 Overview

Welcome to the Price Comparison Tool for Phones! This Python-based application uses Selenium to scrape phone prices from Amazon and Trendyol, processes the data, and displays it in a user-friendly format using Tkinter. It provides an efficient way to compare phone prices across different platforms.

## 🚀 Features

- **Web Scraping:** Automatically fetches phone product names and prices from Amazon and Trendyol.
- **Data Processing:** Cleans and processes the scraped data, ensuring accurate price comparisons.
- **Comparison Display:** Presents the comparison results in a Tkinter-based GUI.
- **Excel Export:** Saves the scraped data from both platforms into Excel files for further analysis.

## 🛠 Technologies Used

- **Python Libraries:**
  - `Selenium`: For web scraping
  - `pandas`: For data manipulation
  - `Tkinter`: For creating the GUI
  - `webdriver_manager`: For managing browser drivers
- **Websites Scraped:**
  - [Amazon](https://www.amazon.com.tr)
  - [Trendyol](https://www.trendyol.com)

## 🔑 Setup Instructions

1. **Install Dependencies:**

   Make sure you have Python installed, then install the required libraries using pip:

   ```bash
   pip install selenium pandas openpyxl webdriver_manager
   
2. **Download Web Drivers:**

      The script uses 'webdriver_manager' to handle ChromeDriver automatically, so no manual download is needed.

3. **Run the Scraping Script:**

   ```bash
   Execute the main.py script to start the scraping process and compare prices:
  This will fetch the data, process it, and display the results in a Tkinter GUI.

4.**Check the Results:**
- **amazon_products.xlsx:** Contains phone data scraped from Amazon.
- **trendyol_products.xlsx:** Contains phone data scraped from Trendyol.
- The Tkinter GUI will display the comparison of prices for phones found on both platforms.

5.**View the GUI:**

The application will open a Tkinter window showing a comparison of phone prices between Amazon and Trendyol. You can review and analyze the data directly within this GUI.
