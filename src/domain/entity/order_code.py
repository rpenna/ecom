from datetime import datetime

class OrderCode:
    def __init__(self, issue_date: datetime, year_count: int):
        self.__value = '%s%s' % (issue_date.year, str(year_count).zfill(8))

    @property
    def value(self):
        return self.__value