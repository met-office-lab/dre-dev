#! /usr/bin/env python
"""
Adds the test data to the Mongo DB

"""

import json
import boto3
import os

import sys
sys.path.append("..")
from database import *


def upsert_configs(file_path, table_name):
    with open(file_path, "r") as f:
        conf = encode_floats(json.loads(f.read()))
    print "Upserting", file_name
    table = get_table(table_name)
    table.put_item(Item=conf)


if __name__ == "__main__":
    base = os.path.split(__file__)[0]
    for file_name in os.listdir(base):
        path = os.path.join(base, file_name)
        if "activities" in file_name:
            upsert_configs(path, "dre-default-values")
        elif "time_slot" in file_name:
            upsert_configs(path, "dre-default-timeslot-values")
        elif "speech" in file_name:
            upsert_configs(path, "dre-speech-configs")
        else:
            print "Passing", file_name