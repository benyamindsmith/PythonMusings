# A simple webscraper providing a dataset of all Whitehouse Breifings

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

        title = []
        urls = []
        date = []
        for i in h2_links:
            a_tag = i.find('a')
            urls.append(a_tag.attrs['href'])
            title.append(a_tag.get_text())
        for j in date_links:
            d_tag = j.find('time')
            date.append(d_tag.get_text())

        dt = pd.DataFrame(list(zip(title, date, urls)))

        dat = pd.concat([dat, dt])
    return(dat)
