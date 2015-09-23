import numpy as np
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection
from sklearn.linear_model import LinearRegression
from sklearn.isotonic import IsotonicRegression
from sklearn.utils import check_random_state
from sklearn.linear_model import LinearRegression
from sklearn.datasets import load_boston
import StringIO



def get_data():

    data = load_boston()

    clf = LinearRegression()

    clf.fit(data.data, data.target)

    predicted = clf.predict(data.data)

    plt.figure(num=None, figsize=(14, 6), dpi=80, facecolor='w', edgecolor='k')
    
    plt.scatter(data.target, predicted)
    
    plt.plot([0, 50], [0, 50], '--k')
    
    plt.axis('tight')
    
    plt.xlabel('True price of Houses ($1000s)')
    
    plt.ylabel('Predicted price of Houses ($1000s)')
        
    img = StringIO.StringIO()
    
    plt.savefig(img,bbox_inches='tight')
    
    img.seek(0)
    
    plt.close()

    return img
    