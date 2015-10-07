#!/bin/bash

find data -name NOTES -delete

mkdir cleaned_data

mv data/* cleaned_data

for name in cleaned_data/*/*; do mv $name $name.txt; done
