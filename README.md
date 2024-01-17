Script that downloads files from URLs listed in a table, and then saves them with a specified name from the identifier column, while adding a .pdf prefix, you can use Python. The script will:

Read the table to get the identifier and source-url columns.
Download each file from the source-url.
Save the file with the identifier as its name, adding a .pdf prefix.
First, ensure you have the necessary libraries, like pandas for handling the table and requests for downloading the files. If you don't have them installed, you can install them using pip:

<code>pip install pandas requests</code>

Replace path_to_your_table.csv with the path to your CSV file and path_to_save_pdf with the path where you want to save the PDFs.

**This script assumes that:**
1. Your table is in a CSV format.
2. The identifier column contains valid filenames (no illegal characters for file names).
3. The URLs are direct links to the PDF files.
4. If your table is in a different format (like Excel), you can use pd.read_excel instead of pd.read_csv. Also, this script doesn't handle cases where the URL isn't a direct link to a file or if the link is broken. You might want to add error handling depending on your specific requirements.
