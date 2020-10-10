import datetime


def print_out_of_stock(product):
    print(datetime.datetime.now(), "| Product out of stock |", product)


def print_in_stock(product, stores):
    print(datetime.datetime.now(), "| Product in stock!!!! |", product, stores[product]['url'])


def print_error(product):
    print(datetime.datetime.now(), "Error processing:", product, "*****")