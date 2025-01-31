import csv
import re
from dms_conversion import dms_to_decimal

# Function to parse through CSV files and obtain coordinates dynamically
def parse_CSV(file_path):
    points = []
    
    with open(file_path, 'r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        
        # Read the first row (header)
        header = next(reader, None)
        if header is None:
            return points  # Return an empty list if the file is empty

        # Find the indexes of latitude and longitude columns
        try:
            lat_index = header.index("latitude")
            lon_index = header.index("longitude")
        except ValueError:
            print("Error: 'latitude' or 'longitude' column not found in CSV.")
            return points

        # Read the remaining rows
        for row in reader:
            if len(row) <= max(lat_index, lon_index):  # Ensure row has enough columns
                continue

            lat = clean_coordinate(row[lat_index])
            lon = clean_coordinate(row[lon_index])

            if lat is not None and lon is not None:
                points.append((lat, lon))

    return points

# Function to clean coordinate values
def clean_coordinate(coord):
    coord = coord.strip()
    coord = re.sub(r"[^\d.°'\"NSWE-]", "", coord)  # Removing unnecessary characters

    if '°' in coord or "'" in coord or '"' in coord:
        return dms_to_decimal(coord)  # Convert DMS to decimal value
    
    try:
        return float(coord)
    except ValueError:
        return None  # Return None if conversion fails
