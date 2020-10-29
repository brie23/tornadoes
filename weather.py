import csv
from datetime import datetime

from matplotlib import pyplot as plt

filename = 'tornadoes.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    
    years, tornadoes = [], []
    for row in reader:
        current_year = datetime.strptime(row[0], '%Y%m')
        years.append(current_year)
        tornado = int(row[1])
        tornadoes.append(tornado)
            
        
    # Plots data
    fig, ax = plt.subplots(figsize=(11, 8))
    ax.plot(years, tornadoes, c='blue', alpha=0.5) 
    
    # Format plot
    ax.set_title('U.S. Tornadoes (January-August)', fontsize=20)
    ax.set_xlabel('Year', fontsize=16)
    ax.set_ylabel('Tornado Count', fontsize=16)
    fig.autofmt_xdate()
    ax.tick_params(axis='both', which='major', labelsize=10)
    
    plt.show()
        
        
    
 