from random import random, randrange


def main():
    print('The Kingdom of Euphoria\n')
    init()
    state()
    
def init():
    print('--initialisation')
    
    global acres
    acres = 1500

    global births
    births = 0
    
    global cropyield
    cropyield = 0

    global naturaldeaths
    naturaldeaths = 0

    global grain_rats
    grain_rats = 0

    global grain_food
    grain_food = 0

    global grain
    grain = 0

    global hire_mercenaries
    hire_mercenaries = 0

    global war_starvation
    war_starvation = 0

    global war_casualties
    war_casualties = 0

    global land_deals
    land_deals = 0

    global looting_victims
    looting_victims = 0

    global input
    input = 0

    global looting_losses
    looting_losses = 0

    global population
    population = 100

    global grain_planted
    grain_planted = 0

    global starvations
    starvations = 0

    global acres_traded
    acres_traded = 0

    global acres_wonlost
    acres_wonlost = 0

    global disease_victims
    disease_victims = 0

    global war_probability
    war_probability = 0

    global crop_yield
    crop_yield = 0

    global year
    year = randrange(6)+1
    
    global fruits_war
    fruits_war = 0


def state():
    print('--state of the kingdom')
    print("Year", int(year/7))
    print("Population", population)

    if (births > 0):
        print(births, "births")

    if (naturaldeaths > 0):
        print(naturaldeaths, "deaths by natural causes")

    if (starvations > 0):
        print(starvations, "deaths by starvation")

    if (war_casualties > 0):
        print(war_casualties, "war casualties")

    if (disease_victims > 0):
        print(disease_victims, "victims of disease")

    if (looting_losses > 0):
        print(looting_losses, "victims of looting")


if __name__ == "__main__":
    main()
