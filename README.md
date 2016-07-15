# Command Line Interface for Envato Market

I love Envato and especially themeforest, so I created envato-cli - a command line interface to fetch and store data
from Envato with the command line. It should work with all Envato Market sites, i.e. themeforest, codecanyon,
videohive, audiojungle, graphicriver, photodune, and 3docean. The tool is written in Python. It's main features are:
* Searching for specific products
* Exporting search results to CSV

## Examples
These are some examples of how to use envato-cli.

### Basic invocation, overview, and help
    python3 envato.py --help

### Listing the best admin templates
    python3 envato.py -p 5 -s admin

### Storing search results for string "test" as a CSV file
    python3 envato.py -p 5 -s test -o "csv" > items.csv

## Installation
envato-cli depends on BeatifulSoup for parsing the HTML files, so please make sure it is installed

## Contributions
Just open a pull request an I will deal with the rest.

## License
MIT