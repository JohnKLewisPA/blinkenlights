import datetime, time

def iplcountdown():
    total = 1
    while (total > 0):
        # taking difference in dates
        current_date = datetime.datetime.now()
        till_date = datetime.datetime(2022, 1, 25, 0, 0, 0, 0)
        difference = till_date - current_date
        total = difference.total_seconds()

        # countdown code
        if (total <= 0):
            print("You're going to Disney World!")
        else:
            # days
            days = difference.days
            # hours
            hours, rest = divmod(difference.seconds, 60 * 60)
            # minutes, seconds
            minutes,seconds_left = divmod(rest, 60)
            countdown = ("WDW in " + str(days) + " Days " + str(hours) + " Hours " + str(minutes) + " Mins " + str(seconds_left) + " seconds.")
            print(countdown + "\r")
            time.sleep(1)
            return (countdown)

iplcountdown()