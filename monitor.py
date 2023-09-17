import datetime

import tushare as ts
import numpy as np
import pandas as pd

from stock import *

USED_COL = ["name", "preclose", "price", "volume", "amount"]


def now():
    return datetime.datetime.now().strftime("%H-%M-%S")


def process_time():
    return int(int(datetime.datetime.now().strftime("%S")) / 3)


if __name__ == "__main__":
    # get today
    today = datetime.datetime.today().strftime("%Y-%m-%d")

    # initialize time settings and origin data
    prev_time = -1
    real_time_data_old = ts.get_realtime_quotes(STOCK_POOL)[USED_COL]

    # start monitoring
    while True:
        if process_time() != prev_time:
            real_time_data_new = ts.get_realtime_quotes(STOCK_POOL)[USED_COL]

            # conditions
            price_rtn = (
                real_time_data_new["price"] - real_time_data_old["price"]
            ) / real_time_data_old["preclose"] - 1
            selected_part = real_time_data_new[price_rtn > 0.005]

            if selected_part.shape[0] > 0:
                # print
                message = "DATETIME {} MONITORING\n".format(now)
                message = message + "==================\n"
                for item in selected_part["name"].values:
                    message = message + item + "\n"
                message = message + "=================="
                print(message)

            real_time_data_old = real_time_data_new.copy()
            prev_time = process_time()
            if now() >= "14-57-00":
                break
        else:
            pass

    # end monitoring
    print(f"{today} Monitoring Ends.")
