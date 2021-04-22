class Time:

    def __init__(self,hours,minutes):
        self.hours=hours
        self.minutes=minutes

    def addTime(self,ob2):
        counter=0
        minutes=self.minutes+ob2.minutes
        if minutes>59:
            counter=minutes/60
            minutes=minutes%60
        hours=self.hours+ob2.hours+int(counter)
        print()
        print(hours, "hours",minutes, "minutes")



    def displayTime(self):
        print(self.hours,"hours",self.minutes,"minutes")

    def displayMinute(self):
        x=self.hours*60+self.minutes
        print(x)




ob=Time(1,400)
ob2=Time(3,100)
ob.displayTime()
ob.addTime(ob2)
ob.displayMinute()