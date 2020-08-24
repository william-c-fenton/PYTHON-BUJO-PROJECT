class Bullet:

    def __init__(self, bullet_type, content, important):
        self.bullet_type = bullet_type
        self.content = content
        self.important = important

    def update_content(self, content):
        self.content = content

    def update_type(self, bullet_type):
        self.bullet_type = bullet_type

    def update_important(self, important):
        self.important = important

    def is_important(self):
        if self.important:
            return "*"
        return " "

    def __str__(self):
        if self.bullet_type in ["task", "event", "fact"]:
            return self.is_important() + " " + self.bullet_type + ": " + self.content
                    

#DAILY ENTRY OBJECT
class DailySpread:
    title = "Daily Spread"
    
    def __init__(self):
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

#WEEKLY SPREAD OBJECT

#MONTHLY SPREAD OBJECT
    #SHOULD USE:
    #HABITS OBJECT
    #CALENDAR OBJECT (click on day goes to daily entry)
class MonthSpread:
    title = "Monthly Spread"
    
    def __init__(self, habits=None, calendar=None):
        self.habits = habits
        self.calendar = calendar

class BuJo:

    def __init__(self):
        self.DailySpread = DailySpread()
        self.MonthSpread = MonthSpread()

    def
    
    def __str__(self):
        return str(DailySpread)
#MAIN
def main():
    myBuJo = BuJo()
    myBuJo.DailySpread.add_bullet(Bullet("task", "finish BuJo Project", True))
    myBuJo.DailySpread.add_bullet(Bullet("event", "got print working", False))

    myBuJo.DailySpread.add_text("sample text times 1 billion")
    print(str(myBuJo.DailySpread))

if __name__ == '__main__':
    main()


