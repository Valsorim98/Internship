#!/usr/bin/env python3
# -*- coding: utf8 -*-

from datetime import datetime

class DateTime():
    """Class for date and time.
    """    

    def time_of_execution(self):
        """Method for showing the execution date and time of the program.
        """

        now = datetime.now()
        timestamp = datetime.timestamp(now)
        timestamp = int(timestamp)
        ts = now.strftime("%d %B %Y at %H:%M:%S.%f")

        print(f"Date of execution of the program in timestamp: {timestamp}")
        #print(ts)

        return timestamp
    