#13.4 to 13.6 and some fun stuff

from datetime import date, timedelta, datetime

bday = date(1967, 5, 12)
print("Birthday:\n\t", bday)
fmt = "%A, %B %d, %Y"
print("\t", bday.strftime(fmt))

one_day = timedelta(days=1)
print("Birthday + 10,000 days:\n\t", (bday + one_day*10000).strftime(fmt))

print("-------")
today = date.today()
print("Today:", today)

print("-------")
days = today - bday
print("Current age days:", days)
print("Reverse age date:", bday - days)
print("Current age date:", bday + days)
