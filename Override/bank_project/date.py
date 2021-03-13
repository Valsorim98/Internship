from datetime import date

class Date():

    def today_date(self):

        today = date.today()
        d1 = today.strftime("%d/%m/%Y")     #day/month/year format
        print("Today's date: ", d1)
