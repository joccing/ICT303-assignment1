# ICT303 Assignment1
Hi Students of ICT303!

This code allows you to download the training and test data for **Assignment 1** into a folder on your google colab.

Simply create a cell at the beginning of your colab notebook, and copy and paste this code there:

```python
import os
import importlib

def install_package(package):
    try:
        importlib.import_module(package)
    except ImportError:
        import sys
        !{sys.executable} -m pip install {package}

def is_running_in_colab():
    try:
        from google.colab import _ipython as ip
        return True
    except ImportError:
        return False

def is_running_in_jupyter():
    try:
        shell = get_ipython().__class__.__name__
        if shell == 'ZMQInteractiveShell':
            return True
        else:
            return False
    except NameError:
        return False

def is_running_in_vscode():
    return 'VSCODE_PID' in os.environ

try:
  if is_running_in_colab():
    print("Running in Google Colab")
  elif is_running_in_jupyter():
    if is_running_in_vscode():
      print("Running in Jupyter Notebook within VSCode")
    else:
      print("Running in Jupyter Notebook (not in VSCode)")

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
try:
    import pandas as pd
except ImportError:
    # If pandas is not installed, install it
    install_package('pandas')
    import pandas as pd

train_data = pd.read_csv('data/train.csv')
test_data  = pd.read_csv('data/test.csv')
assert train_data.shape == (1460,81)
assert test_data.shape == (1459, 80)
print('Loaded and verified data!')
```