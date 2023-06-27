import numpy as np
from scipy import stats
import icecream as ic
res = stats.pearsonr([12, 16, 18, 20, 28, 30, 40, 48, 50, 54], [7.2, 7.4, 7, 7.5, 6.6, 6.7, 6, 5.6, 6, 5.5])

print(res)