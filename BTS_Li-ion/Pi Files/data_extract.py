import csv
import numpy as np

with open('w1.csv', 'rb') as f:
    reader = csv.reader(f)
    w1 = float(list(reader))

with open('w2.csv', 'rb') as f:
    reader = csv.reader(f)
    w2 = float(list(reader))

with open('b1.csv', 'rb') as f:
    reader = csv.reader(f)
    b1 = float(list(reader))

with open('b2.csv', 'rb') as f:
    reader = csv.reader(f)
    b2 = float(list(reader))
    
n1 = np.tanh(w1*x + b1)
