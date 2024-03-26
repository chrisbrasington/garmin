#!/usr/bin/env python

import json
import csv
import sys
import os

def flatten_data(data):
    flat_data = {}
    flat_data.update(data)
    
    # Flatten allDayStress
    all_day_stress = data.get("allDayStress", {}).get("aggregatorList", [])
    for stress_data in all_day_stress:
        prefix = f"STRESS_{stress_data['type']}_"
        for key, value in stress_data.items():
            flat_data[prefix + key] = value
    
    # Remove nested field
    flat_data.pop("allDayStress", None)
    
    return flat_data

def read_json(json_file):
    with open(json_file, 'r') as f:
        data = json.load(f)
    return data

def write_to_csv(data, csv_file):
    fieldnames = set()
    for entry in data:
        fieldnames.update(entry.keys())

    with open(csv_file, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for entry in reversed(data):
            writer.writerow(entry)


def main(json_file):
    data = read_json(json_file)
    flattened_data = [flatten_data(entry) for entry in data]
    
    csv_file = os.path.splitext(os.path.basename(json_file))[0] + ".csv"
    write_to_csv(flattened_data, csv_file)
    print(f"CSV file '{csv_file}' has been generated successfully in the current directory.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python program.py <json_file>")
        sys.exit(1)
    json_file = sys.argv[1]
    main(json_file)
