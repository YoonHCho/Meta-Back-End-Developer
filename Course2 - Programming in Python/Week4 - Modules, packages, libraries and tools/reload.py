# import importlib
# import sample
# # import sample # will not print Hello World from sample.py
# # import sample # will not print Hello World from sample.py

# importlib.reload(sample) # will print Hello World from sample.py
# importlib.reload(sample) # will print Hello World from sample.py
# importlib.reload(sample) # will print Hello World from sample.py

import importlib
import filechanges

def changes():
    try:
        importlib.reload(filechanges)
        filechanges.print_changes()
    except:
        pass

for i in range(3):
    changes()
    input('Hit enter to reload...')