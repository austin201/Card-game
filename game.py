def ask_yes_no(question):
    """Ask a yes or no question."""
    response = None
    while response not in ("y", "n"):
        try:
            response = input(question).lower()
        except:
            print("Not a valid response")
    return response

def ask_number(question, low, high):
    """Ask for a number within a range."""
    response = None
    while response not in range(low, high):
        try:
            response = int(input(question))
        except:
            print("Not a valid number")
    return response

def get_name(question):
    name = ""
    while name == "":
        try:
            name = input(question)
        except:
            print("Something went wrong")
    return name
class Player(object):
    """A player for a game. """
    def __init__(self, name, score = 0):
        self.name = name
        self.score = score

    def __str__(self):
        rep = self.name + ":\t" + str(self.score)
        return rep
class trys(object):
    """How many trys you get to have."""
    def __init__(self, tr):
        self.tr = tr
    def __str__(self):
        rep = "You have "+str(self.tr)+" tries left."
        return rep
class response(object):
    """If the response given is correct or incorrect."""
    def __init__(self, cor, incor):
        self.cor = cor
        self.incor = incor
    def __str__(self):
        rep = "You have gotten"+str(self.cor)+" right.\nYou have gotten "+str(self.incor)+" wrong."
        return rep
class pictures(object):
    """The pictures you can have in your program."""
    def __init__(self, approp, inapprop):
        self.approp = approp
        self.inapprop = inapprop
    def __str__(self):
        rep = "I you have good pictures you may use them but no inappropriate pictures."

