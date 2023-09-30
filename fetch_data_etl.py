#!/usr/bin/env python
# coding: utf-8

# In[2]:


import requests
import json
import csv
import os

url = 'https://raw.githubusercontent.com/Niek/tesla-superchargers/main/superchargers.json'

response = requests.get(url)

response = requests.get(json_url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the JSON content
    json_data = response.json()

    # Define the CSV file name and path to save it on your desktop
    desktop_path = os.path.expanduser("C://Users/Admin/Downloads/")
    csv_filename = os.path.join(desktop_path, 'output2.csv')

    # Define the fields you want to extract from the JSON data
    desired_fields = ["location.latitude", "location.longitude", "name", "power", "type", "stalls"]

    # Write the JSON data to a CSV file with 'utf-8' encoding
    with open(csv_filename, 'w', newline='', encoding='utf-8') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=desired_fields)

        # Write the header row with column names
        writer.writeheader()

        # Extract and write the data rows
        for item in json_data.values():
            data_to_write = {
                "location.latitude": item["location"]["latitude"],
                "location.longitude": item["location"]["longitude"],
                "name": item.get("name", ""),
                "power": item.get("power", ""),
                "type": item.get("type", ""),
                "stalls": item.get("stalls", "")
            }
            writer.writerow(data_to_write)

    print(f'CSV file "{csv_filename}" created successfully on your desktop.')
else:
    print(f'Failed to fetch JSON data. Status code: {response.status_code}')


# In[ ]:




