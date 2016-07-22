# see http://www.ibm.com/developerworks/aix/library/au-pythocli/index.html
import csv
import optparse
import urllib
from urllib.parse import urljoin

import requests
import sys
from bs4 import BeautifulSoup, NavigableString
from tabulate import tabulate


def main():
    p = optparse.OptionParser()

    p.add_option('--category', '-c', default='',
                 help="The category to choose (site-templates, wordpress, psd-templates, marketing, ecommerce, "
                      + "cms-themes, muse-templates, blogging, courses, sketch-templates, forums, "
                      + "static-site-generators, typeengine-themes)")
    p.add_option('--pages', '-p', default=1, help="Number of pages to fetch")
    p.add_option('--search', '-s', default='', help="Term to search for")
    p.add_option('--output', '-o', default='table', help="The output format (csv or table)")

    options, arguments = p.parse_args()

    # extract options
    category = options.category
    max_page_count = int(options.pages)
    search_term = options.search
    output_format = options.output

    # fetch pages
    pages = fetch_html_pages(max_page_count, search_term, category)

    # extract items
    items = extract_items(pages)

    # generate ouput
    if output_format == 'table':
        output_table(items)
    elif output_format == 'csv':
        output_csv(items)
    else:
        exit('Unknown output format')


def extract_items(pages):
    items = []
    for page in pages:
        soup = BeautifulSoup(page, 'html.parser')

        product_list = soup.findAll(attrs={'class': 'product-list'})[0]
        for li in product_list.contents:
            if not isinstance(li, NavigableString):
                items.append(extract_item(li))

    return items


def fetch_html_pages(page_count, search_term, category):
    pages = []
    for page_number in range(1, page_count + 1):
        url = get_url(page_number, term=search_term, category=category)
        r = requests.get(url)

        if r.status_code == 302:
            # 302 means last page was exceeded
            # -> exit loop
            break
        elif r.status_code != 200:
            # unexpected status code
            exit('HTTP code is ' + str(r.status))

        # only save text to save space
        pages.append(r.text)

    return pages


def output_csv(items):
    list_writer = csv.DictWriter(
        sys.stdout,
        fieldnames=items[0].keys(),
        delimiter=';',
        quotechar='"',
        quoting=csv.QUOTE_MINIMAL
    )
    list_writer.writeheader()
    for a in items:
        list_writer.writerow(a)


def output_table(items):
    table = tabulate(items, headers='keys')
    print(table)


def get_url(page=1, term='', category=''):
    # https://docs.python.org/3/library/urllib.parse.html#urllib.parse.urlencode
    query = {
        'page': page,
        'utf8': '✓',
        'term': term,
        'referrer': 'search',
        # grid
        'view': 'list',
        # empty (is newest), sales, rating, price-asc, price-desc
        'sort': 'sales',
        # this-year, this-month, this-week, this-day
        'date': '',
        # site-templates, wordpress, psd-templates, marketing, ecommerce, cms-themes, muse-templates, blogging,
        #  courses, sketch-templates, forums, static-site-generators, typeengine-themes
        'category': category,
        # int
        'price_min': '',
        # int
        'price_max': '',
        # rank-0 (no sales) to rank-4 (top sellers)
        'sales': '',
        # empty, 1 to 4
        'rating_min': '',
    }
    return 'https://themeforest.net/search?' + urllib.parse.urlencode(query, True)


def extract_item(li):
    template = {}

    # heading
    heading = li.findAll("h3")[0]
    template['name'] = heading.text.strip()

    # template url
    template_link_relative = heading.a['href']
    template['link'] = make_link_absolute(template_link_relative)

    # price
    template['price'] = li.findAll(attrs={'class': 'product-list__price'})[0].text.strip().replace('$', '')

    # demo url
    if len(li.findAll(attrs={'class': 'item-thumbnail__preview'})) == 1:
        template_demo_relative = li.findAll(attrs={'class': 'item-thumbnail__preview'})[0].a['href']
        template['demo'] = make_link_absolute(template_demo_relative)

    return template


def make_link_absolute(url):
    return urljoin('https://themeforest.net/', url)


if __name__ == '__main__':
    main()
