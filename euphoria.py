from random import random, randrange
from os import system, name

class State:
    def __init__(self) -> None:
        self.acres = 1500
        self.births = 0
        self.cropyield = -1
        self.deaths = 0
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
        self.yield_acre = 0
        self.year = randrange(6)+1
        self.fruits_war = 0
        self.stop = False

def main():
    kingdom = State()
    init(kingdom)
    while kingdom.stop == False:
        state(kingdom)

def init(kingdom):
    cls()
    print('The Kingdom of Euphoria\n')
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
    cls()

def initPopGrainVectors(kingdom):
    kingdom.births = 0
    kingdom.cropyield = 0
    kingdom.deaths = 0
    kingdom.grain_rats = 0
    kingdom.grain_food = 0
    kingdom.hire_mercenaries = 0
    kingdom.war_casualties = 0
    kingdom.land_deals = 0
    kingdom.looting_victims = 0
    kingdom.looting_losses = 0
    kingdom.grain_planted = 0
    kingdom.starvations = 0
    kingdom.disease_victims = 0
    kingdom.fruits_war = 0

def state(kingdom):
    print("State of the Kingdom\n")
    print("Year", int(kingdom.year / 7))
    print("Population", kingdom.population)

    if (kingdom.births > 0):
        print(kingdom.births, "births")

    if (kingdom.deaths > 0):
        print(kingdom.deaths, "deaths by natural causes")

    if (kingdom.starvations > 0):
        print(kingdom.starvations, "deaths by starvation")

    if (kingdom.war_casualties > 0):
        print(kingdom.war_casualties, "war casualties")

    if (kingdom.disease_victims > 0):
        print(kingdom.disease_victims, "victims of disease")

    if (kingdom.looting_losses > 0):
        print(kingdom.looting_losses, "victims of looting")

    kingdom.deaths = kingdom.deaths + kingdom.starvations + \
        kingdom.war_casualties + kingdom.disease_victims + kingdom.looting_victims
    
    kingdom.population = kingdom.population + \
        kingdom.births - kingdom.deaths

    if kingdom.births + kingdom.deaths > 0:
        print("Total:", kingdom.population)
    
    print("Land (acres):", kingdom.acres)

    if kingdom.acres_traded != 0 or kingdom.acres_wonlost != 0:
        if kingdom.acres_traded > 0:
            print(kingdom.acres_traded, "acres bought")
        if kingdom.acres_traded < 0:
            print(-kingdom.acres_traded, "acres sold")
        if kingdom.acres_wonlost != 0:
            print("Fruits of war:", kingdom.acres_wonlost, "acres")

        kingdom.acres = kingdom.acres + kingdom.acres_traded + kingdom.acres_wonlost

        kingdom.acres_traded = 0
        kingdom.acres_wonlost = 0

        print("Total:", kingdom.acres)

    print("Grain (bushels):", kingdom.grain)

    if kingdom.cropyield < 0:
        initPopGrainVectors(kingdom)
    
    else:
        if kingdom.cropyield != 0:
            r = kingdom.yield_acre
            print("Crop yield", kingdom.cropyield, "at", kingdom.yield_acre, "bushels/acre\n")

        if kingdom.grain_food > 0:
            print(kingdom.grain_food, "bushels used for food")
        if kingdom.grain_planted > 0:
            print(kingdom.grain_planted, "bushels planted")
        if kingdom.land_deals != 0:
            print("Land deals:", kingdom.land_deals, "bushels")
        if kingdom.hire_mercenaries > 0:
            print("Mercenary hire:",kingdom.hire_mercenaries)
        if kingdom.grain_rats > 0:
            print(kingdom.grain_rats, "bushels lost to rats")
        if kingdom.fruits_war != 0:
            print("Fruits of war:", kingdom.fruits_war, "bushels")
        if kingdom.looting_losses > 0:
            print("Looting losses:", kingdom.looting_losses, "bushels")

        kingdom.grain = kingdom.grain + kingdom.cropyield - \
            kingdom.grain_food - kingdom.grain_planted + \
            kingdom.land_deals - kingdom.hire_mercenaries - \
            kingdom.grain_rats + kingdom.fruits_war - kingdom.looting_losses
        
        print("Total:", kingdom.grain)

        initPopGrainVectors(kingdom)

    if kingdom.war_starvation >= 100:
        print("The peasants tire of war and starvation. You are deposed.\n")
        kingdom.stop = True

    if kingdom.population <= 1:
        print("You and the remaining population retire in the Swiss Alps.\n")
        kingdom.stop = True

    if kinggdom.stop == False:

        #make land deals
        grain_price = 23+randrange(8)
        
        ok = False

        while not ok:
            print("How many acres to you want to buy at",
                grain_price, "bushels/acre? ")
            kingdom.acres_traded = int(input())
            if kingdom.acres_traded > 0:
                if grain_price * kingdom.acres_traded <= kingdom.grain:
                    kingdom.land_deals = -grain_price * kingdom.acres_traded
                    ok = True
                else:
                    print("But there is insufficient grain.")
            elif kingdom.acres_traded == 0:
                ok = True

        grain_price = grain_price - 1

        ok = False

        while not ok:
            print("How many acres to you want to sell at",
                grain_price, "bushels/acre? ")
            kingdom.acres_traded = int(input())
            if kingdom.acres_traded > 0:
                if kingdom.acres_traded <= kingdom.acres:
                    if kingdom.acres_traded < int(kingdom.acres / 10):
                        kingdom.acres_traded = -kingdom.acres_traded
                        kingdom.land_deals = -grain_price * kingdom.acres_traded
                        ok = True
                else:
                    print("But there is insufficient land.")
            elif kingdom.acres_traded == 0:
                ok = True
        
        ok = False

        while not ok:
            print("How many acres to you want to plant?")
            kingdom.grain_planted = int(input())
            if kingdom.grain_planted > 0:
                if kingdom.grain_planted <= kingdom.acres + kingdom.acres_traded:
                    if kingdom.grain_planted <= kingdom.population * 10:
                        ok = True
                else:
                    print("But there are insufficient people.")
            elif kingdom.grain_planted == 0:
                ok = True

        ok = False

        while not ok:
            print("How many bushels to you wish to use as food?")
            kingdom.grain_food = int(input())
            if kingdom.grain_food > 0:
                if kingdom.grain + kingdom.land_deals - kingdom.grain_planted - kingdom.grain_food >= 0:
                    if kingdom.grain_food <= 40 * kingdom.population:
                        kingdom.starvations = kingdom.population - int(kingdom.grain_food/40)
                        kingdom.war_starvation = kingdom.war_starvation + kingdom.starvations
                        ok = True

        kingdom.yield_acre = 5 + randrange(4)

        if int(kingdom.year/7) - int(kingdom.year/49*7) == kingdom.year:
            kingdom.yield_acre = int(kingdom.yield_acre / 2)

        ok = False

        while not ok:
            kingdom.cropyield = kingdom.yield_acre * kingdom.grain_planted

            if kingdom.grain + kingdom.land_deals - kingdom.grain_planted - \
                kingdom.grain_food + kingdom.cropyield >=0:
                if randrange(99) < 25:
                    kingdom.grain_rats = int((kingdom.grain + kingdom.land_deals - \
                        kingdom.grain_food + kingdom.cropyield) / 10)
                    ok = True
            else:
                kingdom.yield_acre = int((32767 - kingdom.grain - kingdom.land_deals + \
                    kingdom.grain_planted + kingdom.grain_food) / kingdom.grain_planted)

        if randrange(99) <= 15:
            kingdom.war_probability = 25
            print("A nearby kingdom threatens war.")


            key = ""
            while key != "Y" and key != "N":
                key = input("Do you wish to make a pre-emptive strike? ")

            if key == "Y": 
                kingdom.war_probability = 100
                kingdom.war_starvation = kingdom.war_starvation + 5
            
            ok = False

            while not ok:
                kingdom.input = input("How many mercenaries will you hire at 80 bushels each? ")
                if int(kingdom.input) >= 0: ok = True

            kingdom.naturaldeaths = kingdom.grain * \
                kingdom.land_deals - kingdom.grain_planted - kingdom.grain_food * \
                    kingdom.cropyield - kingdom.grain_rats
            
            if randrange(99) >= kingdom.war_probability:
                print("Peace negotiations succeed.")
            
            else:
                if kingdom.war_probability == 25:
                    kingdom.war_probability = 150
                
                num = kingdom.population - kingdom.starvations
                if kingdom.input <= num / 10:
                    num = 3 * kingdom.war_probability / 5 * kingdom.input * kingdom.input / num * 100 / num
                else:
                    num = 3 * kingdom.war_probability / 5 * kingdom.input * 100 / num
                    kingdom.war_casualties = int((kingdom.population - kingdom.starvations) / 2)
                    kingdom.acres_wonlost = -int((kingdom.acres + acres_traded) / 2)
                    kingdom.fruits_war = -int(kingdom.naturaldeaths / 2)

                    if randrange(99) > cnt:
                        print("You have lost the war.")
                        kingdom.war_starvation = int(kingdom.war_starvation + 5000 / kingdom.war_probability)
                    else:
                        print("You have won the war.")
                        kingdom.war_casualties = int(kingdom.war_casualties / 2)
                        kingdom.acres_wonlost = -kingdom.acres_wonlost
                        kingdom.fruits_war = int(kingdom.naturaldeaths / 4)

            if kingdom.input * 80 > kingdom.naturaldeaths + kingdom.fruits_war:
                print("There is insufficient grain to pay the mercenaries")
                kingdom.looting_victims = int(3 * (kingdom.population - kingdom.starvations - kingdom.war_casualties) / 4)
                kingdom.looting_losses = int(3 * (num + kingdom.fruits_war) / 4)
            else:
                kingdom.hire_mercenaries = kingdom.input * 80
            
        kingdom.input = kingdom.population - kingdom.starvations - kingdom.war_casualities - kingdom.looting_victims

        if randrange(99) < 4:
            print("The black plague strikes.")
            print kingdom.disease_victims = int(kingdom.input / 2)
        elif randrange(99) < 20:
            print("A pox epidemic breaks out.")
            kingdom.disease_victims = int(kingdom.input / 20)
            kingdom.input = kingdom.input - kingdom.disease_victims

        kingdom.births = int((kingdom.input * randrange(5) + 9) / 100) + 1
        kingdom.naturaldeaths = int((kingdom.input * randrange(3) + 4) / 100)

        if kingdom.year % 7 == 0:
            print("Seven year locusts reduce crop yield.")
        
        if kingdom.grain_rats > 0:
            print("Rats infest your silos.")


def cls():

    # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

if __name__ == "__main__":
    main()
