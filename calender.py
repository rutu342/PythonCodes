import calendar
y=int(input("enter year"))
m=1
print("\n**************CALENDAR**********************")
Cal=calendar.TextCalendar(calendar.SUNDAY)
#An instance of textcalendar class is created and calendar.sunday means that you want to
#start displaying calendar from sunday
i=1
while i<=12:
    Cal.prmonth(y,i)
    i=i+1
#prmonth() is the function of the class that prints the calendar for given month and year
