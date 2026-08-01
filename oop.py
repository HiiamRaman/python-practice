# Learning about class


class Book :
    def __init__(self,name):
        self.name =name
        
    def __str__(self):
        return f"self.name"


book1= Book('history')
