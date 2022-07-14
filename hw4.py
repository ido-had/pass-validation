class Date:
    def __init__(self,day,month,year):
        """
        constructor for Date object
        """
        if isinstance(day,int) and isinstance(month,int) and isinstance(year,int):
            self._day=day
            self._month=month
            self._year=year
        else:
            print("invalid Date parameters- must be integers")
            self._day=1
            self._month=1
            self._year=1990





    def __str__(self)->str:
        """
        allows the Date class to be printed
        :return: strings contains Date parameters
        """
        s=f"{self._day}\{ self._month}\{self._year}"
        return s

    def isValid(self)->bool:
        """
        Checks if the current instance Date parameters represents a valid date
        :return:
        """
        if self._day<1 or self._day>31 or self._month>12 or self._month<1 or self._year<1 \
            or self._year>9999:
            return False
        days_month_dic={1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
        days_month_dic_leap={1:31,2:29,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
        if Date.isLeapyear(self._year):
            if Date.daysExceed(self._day,self._month,days_month_dic_leap):
                return False
            else:
                return True
        else:
            if Date.daysExceed(self._day,self._month,days_month_dic):
                return False
            else:
                return True

    @staticmethod
    def isLeapyear(year)->bool:
        """
        determine if 'year' is leaped
        :param year:
        :return: true if leaped false otherwise
        """
        if (year%4==0 and year%100!=0) or (year%400==0):
            return True
        else:
            return False

    @staticmethod
    def daysExceed(day,month,dict)->bool:
        """
        determines if passed value day exceed max monthly available
        :return: true if days passed the limit.false otherwise
        """
        if day>dict.get(month):
            return True
        else:
            return False


    def getNextDay(self)->object:
        """
        calculates next day
        :return:Date object
        """
        tmpDate=Date(self._day+1,self._month,self._year)
        if tmpDate.isValid():
            return tmpDate
        else:
            if self._month==12: #last day of the year
                return Date(1,1,self._year+1)
            else: #last day of the month
                return Date(1,self._month+1,self._year)


    def getNextDays(self,dayToAdd)->object:
        """
        calculates current stored date + n days forward
        :param dayToAdd: amount of days to add
        :return: new Date object with calculated date
        """
        if not isinstance(dayToAdd,int):
            print("Invalid argument.must be int type")
            return self
        if dayToAdd<0:
            print("Parameter must be positive int")
            return self
        tmp_date=self
        for i in range(dayToAdd):
            tmp_date=tmp_date.getNextDay()
        return tmp_date


    def __eq__(self, other)->bool:
        """
        compares two Date objects
        :return: true if identical,false otherwise
        """
        if isinstance(other,Date):
            return self._year==other._year and self._month==other._month and self._day==other._day
        else:
            print("cannot compare Date type to:",type(other))

    def __ne__(self, other)->bool:
        """
        compares two date object
        :return: true if different,false otherwise
        """
        return not self==other


    def __lt__(self, other)->bool:
        """
        compares two Date objects
        :return: true if this < than other,false otherwise
        """
        if self._year>other._year: #checks in this order year-month-day
            return False
        else:
            if self._year==other._year:
                if self._month>other._month:
                    return False
                else:
                    if self._month==other._month:
                        if self._day<other._day:
                            return True
                        else:
                            return False #this.day>other.day
                    else:
                        return True #this.month<other.month
            else:
                return True #this.year<other.year


    def __gt__(self, other)->bool:
        """
        compares two Date objects
        :return: true if this > other,false otherwise
        """
        if self==other:
            return False
        else:
            return not self<other

    def __ge__(self, other)->bool:
        """
        compares two Date object
        :param other:date object to be compared
        :return: true if>= false otherwise
        """
        return self>other or self==other

    def __le__(self, other)->bool:
        """
        compares two date object
        :return: true if this <= other,false otherwise
        """
        return self<other or self==other

    @staticmethod
    def calculate(before,after)->int:
        """
        Calculate days between two given dates
        :param before: Start date
        :param after:  end date
        :return: number of days
        """
        tmpDays=0
        tmpdate=before
        while tmpdate!=after:
            tmpdate=tmpdate.getNextDay()
            tmpDays+=1
        return tmpDays

    def sub(self,date)->int:
        """
        return difference in days between two dates
        :return: number of days
        """
        if self==date: #same date
            return 0
        elif self<date: #self is start date other is end date
            return Date.calculate(self,date)
        else:           #self is latter
            return Date.calculate(date,self)






dt=Date(15,2,2006)
print(dt.isValid())
dt11=dt
dt2=dt.getNextDay()
dt3=dt.getNextDays(200)
print(dt3)
print(dt11<dt2)
print(dt!=dt11)
print(dt3<dt)
print(dt3>=dt)
print(dt2)
print(dt3)
print(dt3.sub(dt))
print(dt.sub(dt3))
