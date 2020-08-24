class Bullet:

    def __init__(self, bullet_type, content, important):
        self.bullet_type = bullet_type
        self.content = content
        self.important = important

    def update_content(self, content):
        self.content = content

    def update_type(self, bullet_type):
        self.bullet_type = bullet_type

    def is_important(self, important):
        self.important = important


#DAILY ENTRY OBJECT
class DailySpread:

    def __init__(self):
        self.bullets = []
        self.text = ""

    def add_bullet(self, bullet):
        self.bullets.append(bullet)

    def add_text(self, text):
        self.text = text


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
#MAIN
def main():
    myBuJo = BuJo()
    myBuJo.DailySpread.add_bullet("test_bullet")
    print(myBuJo.DailySpread.bullets)

if __name__ == '__main__':
    main()


