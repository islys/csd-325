import csv
from datetime import datetime
####---- Changes made ----####, added sys to exit the script
import sys

from matplotlib import pyplot as plt

####---- Changes made ----####, Turned the plot section into a function
def plotter(dates, temps, color, selection):
    # Plot the high temperatures.
    # plt.style.use('seaborn')
    fig, ax = plt.subplots()
    ax.plot(dates, temps, c=color)

    ####---- Changes made ----####, added {selection to the print statements for high/low}
    plt.title(f"Daily {selection} temperatures - 2018", fontsize=24)
    plt.xlabel('', fontsize=16)
    fig.autofmt_xdate()
    plt.ylabel(f"{selection} Temperature (F)", fontsize=16)
    plt.tick_params(axis='both', which='major', labelsize=16)

    plt.show()

filename = 'sitka_weather_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # Get dates and high temperatures from this file.
    ####---- Changes made ----####, added lows
    dates, highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        dates.append(current_date)
        highs.append(int(row[5]))
        lows.append(int(row[6]))

####---- Changes made ----####, Added print statement
print("Welcome to the weather plotter!")

####---- Changes made ----####, added while loop to get user input
while True:
    print("Would you like to plot (h)igh temps? or (l)ow temps? or (e)xit?")
    ####---- Changes made ----####, determines which args are passed to plotter function
    choice = input("> ").upper()
    if choice[0] == "H":
        plotter(dates, highs, 'red', 'high')
    elif choice[0] == "L":
        plotter(dates, lows, 'blue', 'low')
    elif choice[0] == "E":
        print("Goodbye! Thanks for plotting with us!")
        sys.exit()
    else:
        print("Invalid selection")




