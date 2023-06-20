# deeplearning-assignment1
Hi Students of ICT303!

This code allows you to download the training and test data for assignment1 into a folder on your google colab.

Simply create a cell at the beginning of your colab notebook, and copy and paste this code there:

```python
try:
    import google.colab
    import requests
    url = 'https://raw.githubusercontent.com/joccing/deeplearning/ICT303-assignment1/config.py'
    r = requests.get(url, allow_redirects=True)
    open('config.py', 'wb').write(r.content)    
except ModuleNotFoundError:
    pass

from config import *
config_data()
```