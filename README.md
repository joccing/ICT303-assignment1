# ICT303 Assignment1
Hi Students of ICT303!

This code allows you to download the training and test data for **Assignment 1** into a folder on your google colab.

Simply create a cell at the beginning of your colab notebook, and copy and paste this code there:

```python
try:
    import google.colab
    import requests
    url = 'https://raw.githubusercontent.com/joccing/ICT303-assignment1/master/config.py'
    r = requests.get(url, allow_redirects=True)
    open('config.py', 'wb').write(r.content)    
except ModuleNotFoundError:
    pass

from config import *
config_data()
```

Run the code using Shift-Return on the above cell.
After doing this, in another cell, copy and paste the following:

```python
import pandas as pd
train_data = pd.read_csv('data/train.csv')
test_data  = pd.read_csv('data/test.csv')
```

Run it using Shift-Return on the cell.

Validation:  When you run the following

```
print(train_data.shape)
print(test_data.shape)
```

You should get

(1460, 81)
(1459, 80)