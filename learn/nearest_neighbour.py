import numpy as np
import pandas as pd
import pylab as pl
from sklearn.neighbors import KNeighborsClassifier
import StringIO
import random
from tempfile import NamedTemporaryFile
from shutil import copyfileobj
from os import remove

def get_damaged_image(damage_amount):
    data = []
    for i in range(0, 100):
        for j in range(0, 100):
            data.append([i, j])
    
    damage_amount = int(damage_amount)
    if damage_amount > 99:
        damage_amount = 99
    #Remove random pixels 5000 means 50% here
    for i in range(damage_amount*100):
        data.remove(random.choice(data)) 

    df = pd.DataFrame(data, columns=['x', 'y'])
    df['color'] = 'yellow'
     
    # left eye
    idx = ((df['x'] - 30)**2 + (df['y'] - 80)**2 <= 100)
    df['color'] = np.where(idx, 'black', 'yellow')
     
    # right eye
    idx = ((df['x'] - 70)**2 + (df['y'] - 80)**2 <= 100)
    df['color'] = np.where(df['color']!='black', np.where(idx, 'black', 'yellow'), df['color'])
     
    # smile
    idx = ((df['x'] - 50)**2 + (df['y'] - 40)**2 <= 1000)
    idx = idx & (df['y'] < 40)
     
    df['color'] = np.where(df['color']!='black', np.where(idx, 'black', 'yellow'), df['color'])
     
    for color in ['yellow', 'black']:
        #print color
        #print len(df[df.color==color])
        pl.scatter(df[df.color==color].x, df[df.color==color].y, c=color, marker=',', edgecolors='none')
     
    img = StringIO.StringIO()
    
    pl.savefig(img,bbox_inches='tight')
    
    img.seek(0)
    pl.close()
    
    return img


def get_repaired_image():
    data = []
    for i in range(0, 100):
        for j in range(0, 100):
            data.append([i, j])
     
    df = pd.DataFrame(data, columns=['x', 'y'])
    df['color'] = 'yellow'
     
    # left eye
    idx = ((df['x'] - 30)**2 + (df['y'] - 80)**2 <= 100)
    df['color'] = np.where(idx, 'black', 'yellow')
     
    # right eye
    idx = ((df['x'] - 70)**2 + (df['y'] - 80)**2 <= 100)
    df['color'] = np.where(df['color']!='black', np.where(idx, 'black', 'yellow'), df['color'])
     
    # smile
    idx = ((df['x'] - 50)**2 + (df['y'] - 40)**2 <= 1000)
    idx = idx & (df['y'] < 40)
     
    df['color'] = np.where(df['color']!='black', np.where(idx, 'black', 'yellow'), df['color'])
     
    for color in ['yellow', 'black']:
        #print color
        #print len(df[df.color==color])
        pl.scatter(df[df.color==color].x, df[df.color==color].y, c=color, marker=',', edgecolors='none')

    img = StringIO.StringIO()
    
    pl.savefig(img,bbox_inches='tight')
    
    img.seek(0)
    pl.close()
    
    return img

