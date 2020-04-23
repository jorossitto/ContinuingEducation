from datetime import date, timedelta

class TimeCalculator():
    def daysAgo(days):
        return date.today() - timedelta(days=days)


