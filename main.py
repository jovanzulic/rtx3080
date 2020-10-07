import scraper
import make_call


def main():
    product_out_of_stock = True

    while product_out_of_stock:
        product_out_of_stock = scraper.scrape()

    print("Product in stock!")
    make_call.make_call()


main()
