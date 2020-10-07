from services import console_printer, notifier, scraper
import time

check_frequency = 10


def main():
    while True:
        if scraper.scrape():
            console_printer.print_out_of_stock()
        else:
            console_printer.print_in_stock()
            notifier.notify_by_sms()
            # notifier.notify_by_phone()
        time.sleep(check_frequency)


main()
