#!/usr/bin/env python3
# -*- coding: utf8 -*-

import datetime
import math

class DateTime():
    """Class for date and time.
    """    

    def time_of_execution(self):
        """Method for showing the execution date and time of the program.
        """        

        mydate = datetime.datetime.now()
        print(mydate.strftime('Date of execution of the program is: %d %B %Y at %H:%M:%S'))
        print(mydate)

        return mydate
    