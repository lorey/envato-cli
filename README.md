# Command Line Interface for Envato Market

I love Envato and especially themeforest, so I created envato-cli - a command line interface to fetch and store data
from Envato with the command line. It should work with all Envato Market sites, i.e. themeforest, codecanyon,
videohive, audiojungle, graphicriver, photodune, and 3docean. The tool is written in Python. Its main features are:
* Searching for specific products
* Exporting search results to CSV

## Examples
These are some examples of how to use envato-cli.

### Basic invocation, overview, and help
    python3 envato.py --help
Lists all available commands and parameters.

### Listing the best admin templates
    python3 envato.py -p 5 -s "admin"
Lists the best admin templates (-s "admin") from the first five pages (-p 5).

### Storing search results for string "test" as a CSV file
    python3 envato.py -p 5 -s test -o "csv" > items.csv
Saves the best templates that contain the word test (-s "test") into `items.csv`.

## Installation
The following Python 3 packages are required:
* BeautifulSoup
* tabulate
* csv
* optparse
* urllib
* requests
* sys

You should be able to install them via pip if necessary.

## Contributions
Just open a pull request and I will deal with the rest. Keep in mind that I am not a regular Python programmer, so my
code can be messy at times. Help and suggestions always appreciated.

## License
MIT