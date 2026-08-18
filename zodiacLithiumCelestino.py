#Create function for the list and computation of chinese zodiacs
def chinese_zodiac(year):
    #Arrange them in chronological order
    zodiac_animals = ["Rat (鼠 / Shǔ)", "Ox (牛 / Niú)", "Tiger (虎 / Hǔ)", "Rabbit (兔 / Tù)", "Dragon (龙 / Lóng)", "Snake (蛇 / Shé)", "Horse (马 / Mǎ)", "Goat (羊 / Yáng)", "Monkey (猴 / Hóu)", "Rooster (鸡 / Jī)", "Dog (狗 / Gǒu)", "Pig (猪 / Zhū)"]

    remainder = (year - 4) % 12
    return zodiac_animals[remainder]

def main():
    #Create a loop to ensure the user inputs a valid year
    while True:
        #Ask the user's birth year
        birth_year = int(input("Enter your birth year: "))

        #Create an if-else to ensure the input is not lower than 1900
        if birth_year >= 1900:
            break  
        else:
            print("Invalid input. Please enter a year above 1900.")

    #Compute for the user's zodiac sign
    zodiac = chinese_zodiac(birth_year)
    print(f"The year {birth_year} is the Year of the {zodiac}!")
main()   
