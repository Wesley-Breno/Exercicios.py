class Solution:
    def convertDateToBinary(self, date: str) -> str:
        date = date.split("-")
        new_date = ""
        for element in date:
            new_date += bin(int(element)).replace("0b", "") + ' '
        return new_date.strip().replace(" ", "-")