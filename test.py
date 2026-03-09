import requests
from bs4 import BeautifulSoup
import csv

# URL of the results page
url = "https://results.amcgroup.edu.in/student/result"

# Send a GET request to the results page
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# Find the table with class 'result-table'
table = soup.find("table", class_="result-table")

if table:
    # Extract all rows from the table
    rows = table.find_all("tr")

    # Extract headers
    headers = [header.get_text(strip=True) for header in rows[0].find_all("th")]

    # Extract data rows
    data = []
    for row in rows[1:]:
        cells = [cell.get_text(strip=True) for cell in row.find_all("td")]
        data.append(cells)

    # Save data to CSV file
    with open("student_results.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(headers)
        writer.writerows(data)

    print("✅ Data saved to 'student_results.csv'")
else:
    print("❌ No table found. Check the HTML structure or try a different payload.")