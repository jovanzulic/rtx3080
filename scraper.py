import requests
import time
import datetime

url_for_rtx_3080 = 'https://www.newegg.com/asus-geforce-rtx-3080-tuf-rtx3080-10g-gaming/p/N82E16814126453?Item=N82E16814126453'
out_of_stock_warning = """<div class="product-inventory"><strong><i class="fas fa-exclamation-triangle"></i> OUT OF STOCK.</strong></div>"""


def get_html_from_newegg():
    page = requests.get(url_for_rtx_3080)
    return page.content.decode()


def check_if_product_out_of_stock(html):
    return out_of_stock_warning in html


def scrape():
    html = get_html_from_newegg()
    product_out_of_stock = check_if_product_out_of_stock(html)
    if product_out_of_stock:
        print("Product out of stock: ", datetime.datetime.now())
        time.sleep(30)
        return True
    return False
