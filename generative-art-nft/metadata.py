#!/usr/bin/env python
# coding: utf-8
# 0xgio dev notes: edited line 132. [added "+1" to index (idx)]
#                  edited line 135. [removed '/']

import pandas as pd
import numpy as np
import time
import os
from progressbar import progressbar
import json
from copy import deepcopy

import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)


# Base metadata. MUST BE EDITED.
BASE_IMAGE_URL = ""
BASE_NAME = "Sol Traveler #"

BASE_JSON = {
    "name": BASE_NAME,
    "symbol": "TVP",
    "description": "The Sol Travelers, a unique collection with access to discounted flights.",
    "image": BASE_IMAGE_URL,
    "seller_fee_basis_points": 750,
    "external_url": "https://travelpad.app/",
    "attributes": [
    ],
    
    "properties": {
        "files": [
            
        ],
        "category": "image",
         "creators": [{"address": "2bFR4scUACqx7rov2vxbBFxe7vra4YJPXAAWvpzgijEn", "share": 100}],
    }
}


# Get metadata and JSON files path based on edition
def generate_paths(edition_name):
    edition_path = os.path.join('output', 'edition ' + str(edition_name))
    metadata_path = os.path.join(edition_path, 'metadata.csv')
    json_path = os.path.join(edition_path, 'json')

    return edition_path, metadata_path, json_path

# Function to convert snake case to sentence case
def clean_attributes(attr_name):
    
    clean_name = attr_name.replace('_', ' ')
    clean_name = list(clean_name)
    
    for idx, ltr in enumerate(clean_name):
        if (idx == 0) or (idx > 0 and clean_name[idx - 1] == ' '):
            clean_name[idx] = clean_name[idx].upper()
    
    clean_name = ''.join(clean_name)
   
    return clean_name


# Function to get attribure metadata
def get_attribute_metadata(metadata_path):

    # Read attribute data from metadata file 
    df = pd.read_csv(metadata_path)
    df = df.drop('Unnamed: 0', axis = 1)
    df.columns = [clean_attributes(col) for col in df.columns]

    # Get zfill count based on number of images generated
    # -1 according to nft.py. Otherwise not working for 100 NFTs, 1000 NTFs, 10000 NFTs and so on
    zfill_count = len(str(df.shape[0]-1))

    return df, zfill_count

# Main function that generates the JSON metadata
def main():

    # Get edition name
    print("Enter edition you want to generate metadata for: ")
    while True:
        edition_name = input()
        edition_path, metadata_path, json_path = generate_paths(edition_name)

        if os.path.exists(edition_path):
            print("Edition exists! Generating JSON metadata...")
            break
        else:
            print("Oops! Looks like this edition doesn't exist! Check your output folder to see what editions exist.")
            print("Enter edition you want to generate metadata for: ")
            continue
    
    # Make json folder
    if not os.path.exists(json_path):
        os.makedirs(json_path)
    
    # Get attribute data and zfill count
    df, zfill_count = get_attribute_metadata(metadata_path)
    
    for idx, row in progressbar(df.iterrows()):    
    
        # Get a copy of the base JSON (python dict)
        item_json = deepcopy(BASE_JSON)
        
        # Append number to base name
        item_json['name'] = item_json['name'] + str(idx + 1)

        # Append image PNG file name to base image path (add / to '' for path)
        item_json['image'] = item_json['image'] + '' + str(idx) + '.png'
  
        # Convert pandas series to dictionary
        attr_dict = dict(row)
        
        # Add all existing traits to attributes dictionary
        for attr in attr_dict:
            
            if attr_dict[attr] != 'none':
                item_json['attributes'].append({ 'trait_type': attr, 'value': attr_dict[attr] })


        #item_json['properties']['files'][0] = "asd"
        temp = item_json['properties']['files']
        #print("temp is: ",  temp)
        temp.append({
            "uri": item_json['image'],
            "type": "image/png"
            },)
        #print("AGAIN: ", temp)
        item_json['properties']['files'] = temp
        #print("final form: ", item_json['properties']['files'])
        
        # Write file to json folder
        #Use format(idx, "03d") instead of str(idx) to name json files starting with 000 instead of 0
        item_json_path = os.path.join(json_path, str(idx))
        #print(str(format(idx, "03d")))

        item_json_path = item_json_path + ".json"
        #print(item_json_path)
        with open(item_json_path, 'w') as f:
            json.dump(item_json, f)
            #print(f)

# Run the main function
main()
