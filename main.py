from services import console_printer, notifier, scraper, yaml_reader
import time

check_frequency = 10


def main():

    products = yaml_reader.get_data()

    while True:
        for product in products:
            try:
                if scraper.check_if_product_in_stock(product, products):
                    console_printer.print_in_stock(product, products)
                    notifier.notify_by_sms(product, products)
                    # notifier.notify_by_phone()
                else:
                    console_printer.print_out_of_stock(product)
            except:
                console_printer.print_error(product)

        time.sleep(check_frequency)


if __name__ == '__main__':
    main()
