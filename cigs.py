from datetime import datetime, date, time
from anniversary import celebrate

if __name__ == "__main__":

    quit_datetime = datetime.combine(date(2009, 11, 03), time(8, 30))
    celebrate(quit_datetime)
