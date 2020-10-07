from services import console_printer, phone_caller, scraper
import time

check_frequency = 10


def main():
    while True:
        if scraper.scrape():
            console_printer.print_out_of_stock()
        else:
            console_printer.print_in_stock()
            phone_caller.make_call()
        time.sleep(check_frequency)


main()
