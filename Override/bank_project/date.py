from datetime import date

class Date():
    """Create class Date.
    """    

    def today_date(self):
        """Create method today_date.
        """        

        today = date.today()
        d1 = today.strftime("%d/%m/%Y")     #day/month/year format
        print("Today's date: ", d1)
