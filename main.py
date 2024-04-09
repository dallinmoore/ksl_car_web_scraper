import json
import os
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.common.exceptions import WebDriverException

def print_vehicle_details(vehicle):
    print("-" * 50)
    print("Year:", vehicle["Year"])
    print("Trim:", vehicle["Trim"])
    print("Price:", "${:,}".format(vehicle["Price"]))
    print("Mileage:", "{:,}".format(vehicle["Mileage"]))
    print("Link:", vehicle["Link"])

vehicle = {"make" : "Lexus",
           "model" : "GX",
           "priceTo" : "10500"}
# Construct the URL
url_parts = [f"{key}/{value}" for key, value in vehicle.items()]
url = "https://cars.ksl.com/search/" + "/".join(url_parts)

# File to store results in JSON format
json_file_path = 'results.json'
new_json_file_path = 'new_results.json'

# Create lists to store the results
results = []
new_results = [] 

try:
    # Use a non-headless browser (in this case, Chrome)
    options = webdriver.ChromeOptions()
    # options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)

    # Open the URL in the browser
    driver.get(url)

    # Wait for the JavaScript to execute and update the DOM
    driver.implicitly_wait(10)  # Adjust the wait time based on your needs

    # Get the updated HTML content
    html = driver.page_source

    # Close the browser
    driver.quit()

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(html, 'html.parser')

    # Find all <a> elements with the specified class for titles
    title_elements = soup.find_all('a', class_='Typography__variantProp-sc-5cwz35-0 fUvrwF listing-title')

    # Find all <p> elements with the specified class for prices
    price_elements = soup.find_all('p', class_='Typography__variantProp-sc-5cwz35-0 eaOVFJ')

    # Find all <p> elements with the specified class for mileage
    mileage_elements = soup.find_all('p', class_='Typography__variantProp-sc-5cwz35-0 kMOSqH')

    # Extract and print the text of each title, price, mileage, and link
    for title_element, price_element, mileage_element in zip(title_elements, price_elements, mileage_elements):
        year = int(title_element.text.strip()[0:4])
        trim = title_element.text.lstrip()[14:]
        price = int(price_element.text.strip().replace('$', '').replace(',', ''))
        mileage = int(mileage_element.text.strip().replace(',', '').split()[0])  # Strip 'Miles' and convert to integer
        link = title_element['href']  # Extract the 'href' attribute for the link

        # Append the result to the list
        results.append({
            "Year": year,
            "Trim": trim,
            "Price": price,
            "Mileage": mileage,
            "Link": link
        })

    # Load existing results from the JSON file if available
    existing_results = []
    if os.path.exists(json_file_path):
        with open(json_file_path, 'r', encoding='utf-8') as json_file:
            existing_results = json.load(json_file)

    # Check for new results and save them to new_ksl_results.json
    new_results = [result for result in results if result not in existing_results]
    if new_results:
        print("\nNew Vehicles:")
        for new_result in new_results:
            # Print vehicle details
            print_vehicle_details(new_result)

        with open(new_json_file_path, 'w', encoding='utf-8') as new_json_file:
            json.dump(new_results, new_json_file, indent=2)
        print("\nNew results saved to", new_json_file_path)
    else:
        print("\nNo new vehicles.")

        # Save an empty list to new_ksl_results.json
        with open(new_json_file_path, 'w', encoding='utf-8') as new_json_file:
            json.dump([], new_json_file, indent=2)
        print("New results file saved as", new_json_file_path)

    # Save all results to ksl_results.json
    with open(json_file_path, 'w', encoding='utf-8') as json_file:
        json.dump(results, json_file, indent=2)
    print("All results saved to", json_file_path)

except WebDriverException as e:
    print("Error:", e)
    print("Failed to update results from the website.")

# Load and display results from ksl_results.json
if os.path.exists(json_file_path):
    with open(json_file_path, 'r', encoding='utf-8') as json_file:
        results = json.load(json_file)

    if new_results:
        print("\nRemaining Vehicles:")
        # Display the results from ksl_results.json that are not in new_results
        for result in results:
            if result not in new_results:
                # Print vehicle details
                print_vehicle_details(result)
    else:
        print("\nAll Vehicles:")

        # Display all results from ksl_results.json
        for result in results:
            # Print vehicle details
            print_vehicle_details(result)