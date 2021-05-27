#!/usr/bin/env python3
import json
import argparse

def get_args():
    parser = argparse.ArgumentParser(description='Converting Json file to CSV.')
    parser.add_argument('-s', dest='jsonf', help='Source Json file', required=True)
    parser.add_argument('-d', dest='csvf', help='filename to write csv data  REQUIRED', required=True)
    args = parser.parse_args()
    return args
def convertJson2Csv(jsonf, csvf):
     capfields = ["src_address", "dst_address", "src_port", "dst_port", "proto"]
     with open(jsonf) as json_file:
         data = json.load(json_file)
     # now we will open a file for writing
     csv_file = open(csvf, 'w')
     csv_file.write(','.join([str(x) for x in capfields])) 
     csv_file.write("\n")
     for item in data:
          values = ",".join([item[x] for x in capfields])
          csv_file.write(values)
          csv_file.write("\n")
     csv_file.close()
     json_file.close()


if __name__ == "__main__":
    # Get arguments from command line.

    args = get_args()
    convertJson2Csv(args.jsonf, args.csvf)

