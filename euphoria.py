from random import random, randrange

class State:
    def __init__(self) -> None:
        self.acres = 1500
        self.births = 0
        self.cropyield = -1
        self.naturaldeaths = 0
        self.grain_rats = 0
        self.grain_food = 0
        self.grain = 5000
        self.hire_mercenaries = 0
        self.war_starvation = 0
        self.war_casualties = 0
        self.land_deals = 0
        self.looting_victims = 0
        self.input = 0
        self.looting_losses = 0
        self.population = 100
        self.grain_planted = 0
        self.starvations = 0
        self.acres_traded = 0
        self.acres_wonlost = 0
        self.disease_victims = 0
        self.war_probability = 0
        self.crop_yield = 0
        self.year = randrange(6)+1
        self.fruits_war = 0

def main():
    print('The Kingdom of Euphoria\n')
    kingdom = State()
    init(kingdom)
    state(kingdom)

def init(kingdom):
    print("You have inherited the throne to the medieval")
    print("kingdom of Euphoria, somewhere in Europe.\n")
    print("At this time it is about", kingdom.acres, "acres in size,")
    print("with", kingdom.population, "loyal peasants to serve you.")
    print("In your royal silos you have", kingdom.grain, "bushels of")
    print("nutritious grain with which to feed the people")
    print("and transact international trade.\n")
    print("Close by your side are jealous neighboring")
    print("kingdoms, but you can protect yourself by")
    print("hiring evil mercenaries.\n")
    print("Each year your ministers will present you with")
    print("a summary of your current status, and then ask")
    print("you for decisions on what to do for the next")
    print("year. Please type Y or N for yes or no, or a")
    print("whole number for numeric answers.\n")

    key = ""
    while key != "Y":
        key = input("Are you ready, your highness? ")
    
def state(kingdom):
    print('--state of the kingdom')
    print("Year", int(kingdom.year/7))
    print("Population", kingdom.population)

    if (kingdom.births > 0):
        print(kingdom.births, "births")

    if (kingdom.naturaldeaths > 0):
        print(kingdom.naturaldeaths, "deaths by natural causes")

    if (kingdom.starvations > 0):
        print(kingdom.starvations, "deaths by starvation")

    if (kingdom.war_casualties > 0):
        print(kingdom.war_casualties, "war casualties")

    if (kingdom.disease_victims > 0):
        print(kingdom.disease_victims, "victims of disease")

    if (kingdom.looting_losses > 0):
        print(kingdom.looting_losses, "victims of looting")

    kingdom.naturaldeaths = kingdom.naturaldeaths + kingdom.starvations + \
        kingdom.war_casualties + kingdom.disease_victims + kingdom.looting_victims
    
    kingdom.population = kingdom.population + \
        kingdom.births - kingdom.naturaldeaths

if __name__ == "__main__":
    main()
