import pandas as pd

# Updated function to handle headers correctly
def read_and_parse_dat_automation(filepath):
    with open(filepath, 'r', encoding='utf-8-sig') as file:
        raw_text = file.read()

    # Split the text into lines
    lines = raw_text.splitlines()

    # Process the lines manually to create a structured DataFrame
    data = []
    for line in lines[3:]:  # Skip the first three lines to avoid the header
        parts = line.split(';')
        # Remove quotes and replace commas with dots for float conversion
        parts[1] = float(parts[1].replace(',', '.').replace('"', ''))
        parts[0] = parts[0].replace('"', '')
        data.append(parts)

    # Convert the list of lists into a DataFrame
    df = pd.DataFrame(data, columns=["Country", "Risk of Automation"])

    return df

