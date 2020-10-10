import datetime


def print_out_of_stock(store):
    print(store, " - Product out of stock: ", datetime.datetime.now())


def print_in_stock(store):
    print("*** ", store, " - Product in stock! ", datetime.datetime.now())


def print_error(store):
    print("*** ERROR during: ", store)