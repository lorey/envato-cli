# Command Line Interface for themeforest (Envato Market)

I love Envato and especially themeforest, so I created envato-cli - a command line interface to fetch and store data
from Envato with the command line. It should work with all Envato Market sites, i.e. themeforest, codecanyon,
videohive, audiojungle, graphicriver, photodune, and 3docean. The tool is written in Python. Its main features are:
* Searching for specific products
* Exporting search results to CSV

## Examples
These are some examples of how to use envato-cli.

### Basic invocation, overview, and help
    ./envato.py --help
Lists all available commands and parameters.

### Listing the best admin templates
    ./envato.py -p 5 -c "site-templates" -s "admin"
Lists the best admin templates (-s "admin") from the "site-template" category on the first five pages (-p 5).

### Storing search results for string "test" as a CSV file
    ./envato.py -p 5 -s test -o "csv" > items.csv
Saves the best templates that contain the word test (-s "test") into `items.csv`.

### Best admin templates
You can see an example csv of the best admin templates at [examples/best-admin-templates.csv](examples/best-admin-templates.csv). It looks like this:

```
link,name,demo,price
https://themeforest.net/item/metronic-responsive-admin-dashboard-template/4021469?s_rank=1,Metronic - Responsive Admin Dashboard Template,https://themeforest.net/item/metronic-responsive-admin-dashboard-template/full_screen_preview/4021469,28
https://themeforest.net/item/angulr-bootstrap-admin-web-app-with-angularjs/8437259?s_rank=2,Angulr - Bootstrap Admin Web App with AngularJS,https://themeforest.net/item/angulr-bootstrap-admin-web-app-with-angularjs/full_screen_preview/8437259,22
https://themeforest.net/item/pages-admin-dashboard-template-web-app/9694847?s_rank=3,Pages - Admin Dashboard Template & Web App,https://themeforest.net/item/pages-admin-dashboard-template-web-app/full_screen_preview/9694847,24
https://themeforest.net/item/constellation-complete-admin-skin/116461?s_rank=4,Constellation complete admin skin,http://preview.themeforest.net/item/constellation-complete-admin-skin/full_screen_preview/116461,22
https://themeforest.net/item/webarch-responsive-admin-dashboard-template/6157416?s_rank=5,Webarch - Responsive Admin Dashboard Template,https://themeforest.net/item/webarch-responsive-admin-dashboard-template/full_screen_preview/6157416,22
```

## Installation
The following Python 3 packages are required:
* bs4
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
