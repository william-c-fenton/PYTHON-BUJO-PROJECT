from datetime import date
import calendar

class Bullet:

    def __init__(self, bullet_type, content, important):
        #initialize bullet type content and importance
        self.bullet_type = bullet_type
        self.content = content
        self.important = important

    def update_content(self, content):
        self.content = content

    def update_type(self, bullet_type):
        self.bullet_type = bullet_type

    def update_important(self, important):
        self.important = important

    def is_important_str(self):
        if self.important:
            return "*"
        return " "

    def __str__(self):
        if self.bullet_type in ["task", "event", "fact"]:
            return self.is_important_str() + " " + self.bullet_type + ": " + self.content
                    

#DAILY ENTRY OBJECT
class DailySpread:
    title = "Daily Spread"
    
    def __init__(self):
        #initialize the list of bullets and the text
        self.bullets = []
        self.text = ""

    def add_bullet(self, bullet):
        self.bullets.append(bullet)

    def add_text(self, text):
        self.text = text

    def __str__(self):
        bullets_str = ""
        for i in self.bullets:
            bullets_str += (str(i) + "\n")
            
        return bullets_str + " " + self.text

class Habit:
    
    def __init__(self, name, year, month):
        self.name = name
        self.tracker = calendar.TextCalendar().formatmonth(year, month)

    def __str__(self):
        return "    " + self.name + "\n" + self.tracker

    def update(self, day):
        index = self.tracker.find(str(day))
        first_half = self.tracker[:index]
        second_half = self.tracker[index:]

        new = first_half + "*" + second_half
        
        self.tracker = new

    #CALENDAR OBJECT (click on day goes to daily entry)
class MonthSpread:
    title = "Monthly Spread"
    
    
    def __init__(self, habits=[], calendar=calendar.TextCalendar()):
        #initialize habits, calendar, and the current day
        self.habits = habits
        self.calendar = calendar
        self.today = date.today()

        #get the year, month, and day
        self.year = self.today.year
        self.month = self.today.month
        self.day = self.today.day


    def add_habit(self, name):
        self.habits.append(Habit(name, self.year, self.month))
    
    def update_habit(self, name):
        obj = next((x for x in self.habits if x.name == name), None)
        obj.update(self.day)

    def __str__(self):
        habits_text = ""
        for i in self.habits:
            habits_text += str(i) + "\n"
            
        return habits_text

class BuJo:

    #initialize daily and monthly spread pages
    def __init__(self):
        #initialize the monthly and daily spreads
        self.DailySpread = DailySpread()
        self.MonthSpread = MonthSpread()

    
    #Add new bullet to daily spread
    def add_bullet(self):

        #Prompt user for info regarding adding bullets to DAILY SPREAD -- THIS WILL LIKELY CHANGE WHEN GUI GETS ADDED
        bullet_type = None
        while bullet_type not in ["task", "event", "fact"]:
            bullet_type = input("Type (task, event, fact): ").lower()

        #get bullet text
        bullet_text = input("Enter bullet text: ")

        bullet_important = None
        while bullet_important not in ["y", "n"]:
            bullet_important = input("Is important (y/n)? ").lower()
        
        if bullet_important == "y":
            bullet_important = True
        else:
            bullet_important = False

        #add new bullet to daily spread bullet list
        bullet = Bullet(bullet_type, bullet_text, bullet_important)
        self.DailySpread.add_bullet(bullet)

    def add_habit(self):
        #prompt user for info regarding adding habits
        name = input("Name of new habit: ")

        self.MonthSpread.add_habit(name)

    def update_habit(self, name):
        self.MonthSpread.update_habit(name)
    
    def __str__(self):
        return  str(self.MonthSpread) + str(self.DailySpread)
    
#MAIN
##def main():
##    today = str(date.today())
##    
##    
##    myBuJo = BuJo()
##
##    
##    myBuJo.add_bullet()
##    myBuJo.add_habit()
##    name = input("Update which habit? ")
##    myBuJo.update_habit(name)
####    myBuJo.add_bullet()
##
##    
##    print(str(myBuJo))
##
##if __name__ == '__main__':
##    main()


