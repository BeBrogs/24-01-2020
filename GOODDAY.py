#Python: Brogan McShane's Path to peace:
from datetime import date
today = date.today()
d1 = today.strftime("%B %d, %Y")

broganMcShane = input("Did you wake up on time? ")

def good():
    print("Spring cleaning: ")
    print("\nToday is: " + d1)
    #Takes hour in 00 format
    time = input ("\nWhat hour is it? (/HH/) ")
    time = int(time)
    #Variable determines when I sleep
    idealHoursAwake = 16
    timeTilSleep = (idealHoursAwake -  time)
    print("\n\nYou will rest at " + str(timeTilSleep) + ("PM tonight, (no) IFS ANDS ORS (or) BUTS"))
    offTime = timeTilSleep - 3
    print("\n\nYou will not work on anything that heavily stimulates the left brain past: " + str(offTime))
    print("But you must find balance between relaxing and facing the next day, by planning the day ahead")

def day():
    #Validating its me (only accepting y to continue with if statement
    if broganMcShane == "y":
        print("""\n\nstr(AGoodDay) == ('one with Balance') + ('one that faces ambition and tries to make sanity of it')
        \nGood morning Brogan, look at your notepad... To prepare for your day
        \nFollow through, and reflect on how you've done by ticking off your ambitions to calm any of life's anxiety's
        \n\nBut if you want to find balance on a loop, you must find peace in the loop
        \nAKA if you want to enjoy something, find something to enjoy in what you're doing""")
        print("\nAnd do so with every year, month, week, day, AM, PM or HOUR ")
        print("\n\nOnly then will you have a GOOD day")
        
        
    else:
        print("He didn't wake up.")
        #^Or someone is trying to steal my GOOD day plan

        #End loop and scare them away:
        who = raw_input("What's your name")
        print("Get outta here, " + who + ("\nYou are no match for me"))
        
good()
day()
print("\n\nThat's all for now, but make sure to tick off those ambitions.\nFor that's all anxiety is. Ambition.")


      
        



