from services import console_printer, notifier, scraper, yaml_reader
import time

check_frequency = 10


def main():

    stores = yaml_reader.get_data()

    while True:
        for store in stores:
            try:
                if scraper.check_if_product_in_stock(store, stores):
                    console_printer.print_in_stock(store)
                    notifier.notify_by_sms(store)
                    # notifier.notify_by_phone()
                else:
                    console_printer.print_out_of_stock(store)
            except:
                console_printer.print_error(store)

        time.sleep(check_frequency)


if __name__ == '__main__':
    main()
