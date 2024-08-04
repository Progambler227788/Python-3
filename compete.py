# TASK 2
class Competitor:
    points = 0
    color = ""
    def situation(self):
        print( f"I'm {self.color} and I've {self.points} points!")
    
    def score(self):
        self.points+= 1
        
first = Competitor()
first.color ="blue"
first.score()
first.situation()