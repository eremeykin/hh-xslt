#!/usr/bin/env python3

import requests
import sys
import os.path
from lxml import etree
from lxml.html.soupparser import parse

GITHUB_URL = "https://github.com"
DEFAULT_URL = "https://github.com/facebook/create-react-app/pulls?q=is%3Apr"
PULL_PAGE = "homework/pull#{id}.html"
PULLS_HTML = 'homework/pulls.html'
PULLS_VALID_HTML = 'homework/pulls-valid.html'


def load_html(url, file_name):
    print('Loading HTML file: {0} ...'.format(url))
    req = requests.get(url)
    text = req.text
    with open(file_name, 'w') as outfile:
        outfile.writelines(text)


if __name__ == "__main__":
    if not os.path.isfile(PULLS_HTML):
        url = sys.argv[1] if len(sys.argv) > 2 else DEFAULT_URL
        load_html(url, PULLS_HTML)
    print('HTML file is ok')
    root = parse(PULLS_HTML)
    panel_div = root.findall(".//div[@class='js-navigation-container js-active-navigation-container']")[0]
    valid_html = '<html>\n<head>\n</head>\n<body>\n{}\n</body>\n</html>' \
        .format(etree.tostring(panel_div, pretty_print=True).decode('UTF-8'))
    with open(PULLS_VALID_HTML, 'w') as valid_html_file:
        valid_html_file.writelines(valid_html)
    links = root.xpath("//div[contains(@class, 'Box-row')]//a[contains(@id,'issue_')]")
    for link in links:
        link_ref = link.get("href")
        pull_id = str(link_ref.split("/")[-1])
        page_file_name = PULL_PAGE.format(id=pull_id)
        if not os.path.isfile(page_file_name):
            load_html(GITHUB_URL + link_ref, page_file_name)
