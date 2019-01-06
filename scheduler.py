#!/usr/bin/env python3

import sys
from pandas import read_csv, DataFrame
from datetime import datetime, time, timedelta
from collections import defaultdict

if __name__ == '__main__':
    df = read_csv(sys.argv[1], index_col=0)
    tables = df.columns.values
    print(df.index.values)
    print(df)

    session_length_minutes = 15
    seats = 4

    start_time = datetime.combine(datetime.today(), time(10))
    end_time = datetime.combine(datetime.today(), time(12 + 3))
    current_time = start_time

    times = []
    while current_time < end_time:
        times.append(current_time.isoformat() + '::1')
        times.append(current_time.isoformat() + '::2')
        times.append(current_time.isoformat() + '::3')
        times.append(current_time.isoformat() + '::4')
        current_time += timedelta(minutes=session_length_minutes)

    schedule = DataFrame(index=times, columns=tables)

    seen = defaultdict(lambda: False)

    for table in tables:
        print('filling table' + table)
        col = df.loc[:, table]
        for person_name, enrolled in col.items():
            print(person_name)
            if enrolled == 'y':
                for timeslot, reserved_name in schedule.loc[:, table].items():
                    if seen[timeslot[:-3] + person_name]:
                        continue
                    if not isinstance(reserved_name, str):
                        schedule.at[timeslot, table] = person_name
                        seen[timeslot[:-3] + person_name] = True
                        break





    print(schedule)
