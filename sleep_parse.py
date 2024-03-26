#!/usr/bin/env python3
import json
import csv
import sys
import os

def read_json_reverse(json_file):
    with open(json_file, 'r') as f:
        data = json.load(f)
    
    # Filter out entries with sleepWindowConfirmationType "OFF_WRIST" or "UNCONFIRMED" and reverse the list
    filtered_data = [entry for entry in reversed(data) if entry.get('sleepWindowConfirmationType') not in ["OFF_WRIST", "UNCONFIRMED"]]
    
    return filtered_data

def write_to_csv(data, csv_file):
    with open(csv_file, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)

def main(json_file):
    csv_file = os.path.splitext(os.path.basename(json_file))[0] + ".csv"
    data = read_json_reverse(json_file)
    write_to_csv(data, csv_file)
    print("CSV file '{}' has been generated successfully.".format(csv_file))

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python program.py <json_file>")
        sys.exit(1)
    json_file = sys.argv[1]
    main(json_file)
