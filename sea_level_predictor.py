from matplotlib import lines
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')
    x = df["Year"]
    y = df["CSIRO Adjusted Sea Level"]
    
    # Create scatter plot
    plt.scatter(x, y)

    # Create first line of best fit
    res = linregress(x, y)
    last_year = df["Year"].iloc[-1]
    future = range(2050-last_year)
    for i in future:
        i += 1
        new_year = (last_year+i)
        new_y = res.slope*new_year + res.intercept
        df = df.append({"Year": int(new_year), "CSIRO Adjusted Sea Level": new_y}, ignore_index=True)
        
    x_future = df["Year"]
    y_res = res.intercept + res.slope * x_future
    plt.plot(x_future, y_res, 'r', label='fitted line')

    # Create second line of best fit
    x2 = df[(df["Year"] >= 2000) & (df["Year"] <= 2013)]["Year"]
    y2 = df[(df["Year"] >= 2000) & (df["Year"] <= 2013)]["CSIRO Adjusted Sea Level"]
    res2 = linregress(x2, y2)
    
    last_year = 2013
    future = range(2050-last_year)
    for i in future:
        i += 1
        new_year = (last_year+i)
        new_y = res2.slope*new_year + res2.intercept
        df = df.append({"Year": int(new_year), "CSIRO Adjusted Sea Level": new_y}, ignore_index=True)
        
    x_future2 = df[(df["Year"] >= 2000) & (df["Year"] <= 2050)]["Year"]
    y_res2 = res2.intercept + res2.slope * x_future2
    plt.plot(x_future2, y_res2, 'r', label='fitted line')

    # Add labels and title
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.title("Rise in Sea Level")
    
    plt.show()
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()