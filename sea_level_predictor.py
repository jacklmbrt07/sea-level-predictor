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
    plt.plot(x, y, 'r', label='fitted line')
    


    # Create second line of best fit

    # Add labels and title

    
    plt.show()
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()