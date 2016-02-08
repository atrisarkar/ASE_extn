'''
Created on 2016-01-26

@author: Atri
'''
import numpy as np
import scipy.stats as sp
import math

def all_true(list):
    for i in list:
        if not i:
            return False
    return True    
    

a = np.array([[1,34.6195898352393],[2,32.8331477185946],[3,31.3720928263893],[4,30.1680518555498],[5,25.7210738118712],[6,23.7259519016034],[7,23.0421812010483],[8,21.2728713292347],[9,20.7563226221117],[10,19.2608584195851],[11,18.9503773752963],[12,19.7959965076262],[13,18.1066916199665],[14,16.2058819771583],[15,14.8048319176054]])
fault_rates = a[:,1]
for i in range(1, len(fault_rates)-1):
    fault_rates[i] = (fault_rates[i-1] + fault_rates[i] + fault_rates[i+1])/3    
a[:,1] = fault_rates

a[:,1] = np.log10(a[:,1])

aa=4.9548
bb=0.024399
r=1
s=64

print(np.exp(2403))
