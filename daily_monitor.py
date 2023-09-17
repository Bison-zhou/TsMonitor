import tushare as ts
import datetime
import numpy as np
import pandas as pd

USED_COL = ["name", "price", "volume", "amount"]

if __name__ == "__main__":
    today = datetime.datetime.today().strftime("%Y-%m-%d")
    pool_list

    prev_time = "0000"
    real_time_data_old = ts.get_realtime_quotes(bond_list)[USED_COL]
    while True:
        if now().strftime("%H%M%S") != prev_time:
            print(now().strftime("%H%M%S"))
            real_time_data_new = ts.get_realtime_quotes(bond_list)[USED_COL]
            diff = real_time_data_new.copy()
            diff[USED_COL[1:]] = real_time_data_new[USED_COL[1:]].astype(
                float
            ) - real_time_data_old[USED_COL[1:]].astype(float)
            selected_part = diff[diff["amount"] > 1.5 * 1e7]

            if selected_part.shape[0] > 0:
                # print
                message = "DATETIME {} 转债监控\n".format(now().strftime("%m/%d-%H:%M"))
                message = message + "==================\n"
                for item in selected_part["name"].values:
                    message = message + item + "\n"
                message = message + "=================="
                send_text(message, key="4e6d2ba7-3dc1-408b-87d5-a0b32dc912c8")

            real_time_data_old = real_time_data_new.copy()
            prev_time = now().strftime("%H%M")
            if prev_time >= "1501":
                break
        else:
            pass

    send_text(f"{today} 监控结束.", key="4e6d2ba7-3dc1-408b-87d5-a0b32dc912c8")
