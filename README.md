# runJSONrun

## What does it do?
runJSONrun converts Runmeter (http://www.abvio.com/runmeter/) CSV exports to JSON.

## Usage
runJSONrun.py -i Runmeter.csv

If you start runJSONrun and only specify a csv file, it will dump the JSON data to standard out

-?				Print help and exit

-i, --input		The runmeter CSV file to read

-o --output		The file you wan't the JSON data to be written to

-V				Print the version and exit

## TODO
* GeoJSON support?