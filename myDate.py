class MyDate:
    MONTHS = ["Yanvar", "Fevral", "Mart", "Aprel", "May", "Iyun", "Iyul", "Avgust", "Sentabr", "Oktabr", "Noyabr", "Dekabr"]
    DAY_IN_MONTHS = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    def __init__(self, day, month, year):
        self.__year = year
        self.__month = month
        self.__day = day

    def IsLeapYear(self, year):
        return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

    def isValidDate(self, day, month, year):
        if year < 1 or year > 9999:
            return False
        if month < 1 or month > 12:
            return False
        if day < 1 or day > self.DAY_IN_MONTHS[month - 1]:
            if month == 2 and day == 29 and self.IsLeapYear(year):
                return True
            return False
        return True

    def setDate(self, day, month, year):
        if self.isValidDate(day, month, year):
            self.__year = year
            self.__month = month
            self.__day = day
        else:
            print("Yil, oy yoki kun noto'g'ri kiritildi")

    def setYear(self, year):
        if self.isValidDate(self.__day, self.__month, year):
            self.__year = year
        else:
            print("Kiritilgan yil noto'g'ri!")

    def setMonth(self, month):
        if self.isValidDate(self.__day, month, self.__year):
            self.__month = month
        else:
            print("Kiritilgan oy noto'g'ri!")

    def setDay(self, day):
        if self.isValidDate(day, self.__month, self.__year):
            self.__day = day
        else:
            print("Kiritilgan kun noto'g'ri!")

    def getYear(self):
        return self.__year

    def getMonth(self):
        return self.MONTHS[self.__month - 1]

    def getDay(self):
        return self.__day

    def __str__(self):
        return f"{self.__day}-{self.MONTHS[self.__month - 1]}-{self.__year} yil"

    def nextDay(self):
        if self.__day < self.DAY_IN_MONTHS[self.__month - 1]:
            self.__day += 1
        else:
            self.__day = 1
            if self.__month == 12:
                self.__month = 1
                self.__year += 1
            else:
                self.__month += 1
        return self.__str__()

    def nextMonth(self):
        if self.__month == 12:
            self.__month = 1
            self.__year += 1
        else:
            self.__month += 1
        return self.__str__()

    def nextYear(self):
        self.__year += 1
        return self.__str__()

    def previousDay(self):
        if self.__day > 1:
            self.__day -= 1
        else:
            if self.__month == 1:
                self.__month = 12
                self.__year -= 1
            else:
                self.__month -= 1
            self.__day = self.DAY_IN_MONTHS[self.__month - 1]
        return self.__str__()

    def previousMonth(self):
        if self.__month == 1:
            self.__month = 12
            self.__year -= 1
        else:
            self.__month -= 1
        return self.__str__()

    def previousYear(self):
        self.__year -= 1
        return self.__str__()

print("Tast --> 1")
d1 = MyDate(28, 2, 2012)
print(d1)
print(d1.nextDay())
print(d1.nextMonth())
print(d1.nextYear())
print(d1.nextYear())

print("Tast --> 2")
d2 = MyDate(2, 1, 2012)
print(d2)
print(d2.previousDay())
print(d2.previousDay())
print(d2.previousMonth())
print(d2.previousYear())
