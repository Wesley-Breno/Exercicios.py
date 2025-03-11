from datetime import datetime


class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        d1 = datetime.strptime(date1, "%Y-%m-%d").date()
        d2 = datetime.strptime(date2, "%Y-%m-%d").date()

        diff = abs((d2 - d1).days)
        return diff