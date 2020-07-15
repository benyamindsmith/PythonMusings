# A simple webscraper providing a dataset of all Whitehouse Breifings
from bs4 import BeautifulSoup
import requests
import pandas as pd
import re


def get_whitehouse_breifings():
    # Generalize to all pages

    orig_link = requests.get("https://www.whitehouse.gov/briefings-statements/")

    orig_content = orig_link.content

    sp = BeautifulSoup(orig_content, 'lxml')

    pages = sp.find_all('a', {'class': 'page-numbers'})

    the_pages = []

    for pg in pages:
        the_pages.append(pg.get_text())

    # Now make set of links

    the_links = []

    for num in range(1, int(max(the_pages)) + 1):
        the_links.append('https://www.whitehouse.gov/briefings-statements/' + 'page/' + str(num) + '/')

    dat = pd.DataFrame()
    for link in the_links:
        link_content = requests.get(link)
        link_content = link_content.content
        sp = BeautifulSoup(link_content, 'lxml')
        h2_links = sp.find_all('h2')
        date_links = sp.find_all('p', {"class": "meta__date"})
        breif_links = sp.find_all('div', {"class": "briefing-statement__content"})

        title = []
        urls = []
        date = []
        breifing_type = []
        for i in h2_links:
            a_tag = i.find('a')
            urls.append(a_tag.attrs['href'])
            title.append(a_tag.get_text())
        for j in date_links:
            d_tag = j.find('time')
            date.append(d_tag.get_text())
        for k in breif_links:
            b_tag = k.find('p')
            b_tag = b_tag.get_text()
            b_tag = re.sub('\\t', '', b_tag)
            b_tag = re.sub('\\n', '', b_tag)
            breifing_type.append(b_tag)

        dt = pd.DataFrame(list(zip(date, title, urls, breifing_type)))

        dat = pd.concat([dat, dt])

    dat.rename(columns={"Date": date, "Title": title, "URL": urls, "Issue Type": breifing_type})
    return (dat)
