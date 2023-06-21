import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from scipy.stats import pearsonr 

def scatter_plot(independent_variables, dependent_variables):
    plt.scatter(independent_variables, dependent_variables)

    plt.title('Diagrama de Dispersão Linear')
    plt.xlabel('independent variables')
    plt.ylabel('dependent variables')

    plt.show()
    print()

if __name__ == '__main__':
    
    x = np.array([240, 255, 340, 375, 510, 490, 490, 180, 1125, 1150, 1275]).reshape((-1, 1))
    y = np.array([63, 100, 140, 175, 160, 180, 250, 180, 360, 470, 200])

    #scatter_plot(x,y)
    corr, _ = pearsonr(y, x) 
    print('Pearsons correlation: %.5f' % corr) 


    model = LinearRegression().fit(x, y) 
    
    # Obtain the coefficient of determination by calling the model with the score() function, then print the coefficient:
    r_sq = model.score(x, y)
    print('coefficient of determination:', r_sq)
    print("R² = {}%".format(r_sq*100))
    # Print the Intercept:
    print('intercept:', model.intercept_)
    
    # Print the Slope:
    print('slope:', model.coef_) 
    print("y = {}* x + {}".format(model.coef_, model.intercept_))

    # Predict a Response and print it:
    #y_pred = model.predict(x)
    #print('Predicted response:', y_pred, sep='\n')
