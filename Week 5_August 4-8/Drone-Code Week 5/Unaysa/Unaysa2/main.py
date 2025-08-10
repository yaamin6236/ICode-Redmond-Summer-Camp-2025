
CampName = input("What is the name of your camp? ")

NumDays = int(input("How many days is {}".format(CampName)))

CurrentDay = int(input("What is the current day of camp: "))

DaysLeft = NumDays - CurrentDay

print("There are {} days left in {}" .format(DaysLeft, CampName))
