import requests
from bs4 import BeautifulSoup


def get_dom(url):
    response = requests.get(url).content
    return BeautifulSoup(response, 'html.parser')


soup = get_dom('https://en.wikipedia.org/wiki/List_of_World_War_II_battles')
content = soup.select('div#mw-content-text > div.mw-parser-output', limit=1)[0]

soup = get_dom('https://en.wikipedia.org//wiki/Operation_Skorpion')
locator = "table infobox vevent"
page_content = soup.find('table', 'infobox vevent')


def _table_to_dict(table):
    result = {}
    for row in table.find_all('tr'):
        result[row.th.text] = row.td.get_text().strip()
    return result


def _get_main_info(table):
    main = [el for el in table.tbody.find_all('tr', recursive=False) if 'Location' in el.get_text()][0]
    return {'main': _table_to_dict(main)}

def _find_by_header(table,string):
    header = table.tbody.find('tr',text=string)
    if header is not None:
        return header.next_sibling

def _parse_row(row,names=('allies','axis','third party')):
    cells = row.find_all('td',recursive=False)
    if len(cells)==1:
        return {'total':cells[0].get_text().strip()}
    return {name : cell.get_text().strip() for name ,cell in zip(names,cells)}

def _additional(table):
    keywords = (
        'Belligerents',
        'Commanders and leaders',
        'Strength',
        'Casualties and losses',
    )

    result = {}
    for keyword in keywords:
        try:
            data = _find_by_header(table,keyword)
            if data:
                result[keyword] = _parse_row(data)
        except Exception as e:
            raise Exception(keyword,e)
    return result


def parse_battle_page(url):
    try:
        dom = _default_collect(url)
    except Exception as e:
        warnings.warn(str(e))
        return {}

    table = dom.find('table', 'infobox vevent')  # info table
    if table is None:
        return {}
    data = _get_main_info(table)
    data['url'] =url
    additional=_additional(table)
    data.update(additional)
    return data


