class Solution:
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

    def reformatDate(self, date: str) -> str:
        day, month, year = date.split()

        day = ''.join([digit for digit in day if digit.isdigit()])
        day = day if len(day) > 1 else '0' + day

        month = str(self.months.index(month) + 1)
        month = month if len(month) > 1 else '0' + month

        return f'{year}-{month}-{day}'
