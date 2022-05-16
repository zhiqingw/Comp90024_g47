#!/usr/bin/env bash

python3 read_and_store_couchdb.py
python3 store_result.py
python3 mapreduce.py


