from datetime import datetime


class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        weeks_day = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        return weeks_day[datetime(year, month, day).weekday()]
