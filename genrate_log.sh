#!/bin/bash
grep 'sendstr' udping.log > string_encode.csv
grep -v 'sendstr' udping.log > relay.csv

./translation.py relay.csv
./translation.py string_encode.csv