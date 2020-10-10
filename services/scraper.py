import requests


def get_html(url):
    headers = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36'}
    page = requests.get(url, headers=headers)
    return page.content.decode()


def check_if_product_in_stock(product, products):
    indicator = products[product]['indicator']
    url = products[product]['url']
    return indicator in get_html(url)
