import pandas as pd
import requests
from pathlib import Path

# Load the table (assuming it's a CSV file)
table = pd.read_csv('path_to_your_table.csv')

# Directory where the PDFs will be saved
output_dir = Path('path_to_save_pdf')
output_dir.mkdir(exist_ok=True)

for _, row in table.iterrows():
    identifier = row['identifier']
    url = row['source-url']

    try:
        response = requests.get(url)
        response.raise_for_status()  # Check if the download was successful

        file_path = output_dir / f"{identifier}.pdf"
        with open(file_path, 'wb') as file:
            file.write(response.content)
        print(f"Downloaded and saved: {file_path}")
    except requests.RequestException as e:
        print(f"Failed to download {url}: {e}")

