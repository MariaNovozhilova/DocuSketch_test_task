import pandas as pd
import matplotlib.pyplot as plt
import os


url = "https://ai-process-sandy.s3.eu-west-1.amazonaws.com/purge/deviation.json"


class PlotDrawer:

    def __init__(self, df, *columns):
        self.df = df
        self.columns = columns

    def plot(self): 
        source_series = []
        for column in self.columns:
            source_series.append(self.df[column])
       
        plt.plot(*source_series)


def draw_plots(url, *columns):
    df = pd.read_json(url)
    drawer = PlotDrawer(df, *columns)    
    drawer.plot()   

    results_dir = 'plots'
    
    if not os.path.exists(results_dir):
        plot_counter = 0
        os.makedirs(results_dir)

    plot_counter = len([name for name in os.listdir('plots')])
    plot_file_name = str(plot_counter)
   
    plt.savefig(os.path.join(results_dir, plot_file_name))

  

draw_plots(url, 'max', 'mean', 'min')