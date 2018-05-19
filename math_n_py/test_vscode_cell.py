#%%
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

def sinplot(flip=1):
    x = np.linspace(0, 14, 100)
    for i in range(1, 7):
        plt.plot(x, np.sin(x + i * .5) * (7 - i) * flip)

sns.set_style("ticks")

sinplot()

sns.despine()