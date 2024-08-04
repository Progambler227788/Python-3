# Task 3
class Competitor:
    """Competitor: contains points and color"""
    points = 0
    color = ""
    
    # Constructor
    def __init__(self):
        self.color = input("Give me a color: ")
    
    # Function to print data members
    def situation(self):
        print( f"I'm {self.color} and I've {self.points} points!")
    
    # Function to increment score
    def score(self):
        self.points+= 1

# First create objects     
first  = Competitor()
second = Competitor()

# Then call situation function to print color name and points
first.situation()
second.situation()

print(first.__doc__) # first, second and class name Competitor can be used here

