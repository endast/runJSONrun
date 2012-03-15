# runJSONrun

## What does it do?
runJSONrun converts Runmeter (http://www.abvio.com/runmeter/) CSV exports to JSON.

## Why?
I wanted my runs in JSON.

## Usage
runJSONrun.py -i Runmeter.csv

If you start runJSONrun and only specify a csv file, it will dump the JSON data to standard out

-?				Print help and exit

-i, --input		The runmeter CSV file to read

-o --output		The file you wan't the JSON data to be written to

-V				Print the version and exit

## TODO
* GeoJSON support?
* Remove the need for -i (runJSONrun.py Runmeter.csv)

#JSON format
The header names gets cleaned up:
* Whitespace is removed
* If the column has a typ, for example km/h it gets converted to _kmh
ex:
Average Speed (km/h) -> AverageSpeed_kmh"
Ride Time (secs) -> RideTime_secs
Stopped Time -> StoppedTime