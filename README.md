
# KWUtils
Utilities for use in Python Apps<br>
by kwoolter :monkey:<br>
:copyright: 2017
# Content

##pick()
```
def pick(object_type: str, objects: list, auto_pick: bool=False)
```
Use to ask the user to select and item from a list or cancel if they decide not to pick one.

####Inputs
- `object_type` - the type of object that you are going to choose from a list e.g. "Weapon"
- `objects` - the list of objects that the user will be asked to pick from
- `auto_pick` - if the list only contains 1 item and auto_pick is `True` then the function automatically returns the only item without user intervention.

####Outputs
Returns the selected object from the list or returns `None` if the user cancelled the selection.

##confirm()
```
def confirm(question : str):
```
Use to get the user to respond to a simple Yes/No question.

####Inputs
- `question` - a string containing the question that you want the user to answer Yes/No to.

####Outputs
Returns `True` if the user picked Yes and `False` if the user picked No

##is_numeric()
```
def is_numeric(s):
```
####Inputs
- `s` - the variable that you want to see is numeric or not

####Outputs
The numeric value of s or `None` if s is not numeric


##Class Colours
```
class Colours:
```
Use to store RGB values of common colours for use in graphics apps.<br>
e.g. `Colours.BLACK`, `Colours.RED`

##Class HighScoreTable
```
class HighScoreTable:
```
Use to track a high score table which can be persisted to file using `save()` and `load()` methods.

###Member Variables
```self.table : []```

Contains a sorted list of (name, score) tuples.  Access this list if you want to display the contents of the high score table yourself.

###Methods
```
def __init__(self, name = "default", max_size = 10)
```
Construct a high score table object.
- `name` : The name of the high score table
- `max_size` : how many score entries do you want to maintain in the table (default is 10)
```
def add(self, name : str, score : float):
```
Add a specified `name` and `score` to the high score table.  Returns `True` if the score made it into the high score table.
```
def is_high_score(self, score):
```
Check to see if a specified score makes it into the current high score table.  Returns `True` is the score is good enough to get into the current table.
```
def save(self):
```
Save the high score table to file called `name+".hst"`.
```
def load(self):
```
Load a high score table from a file called `name+".hst"`.
```
def print(self):
```
Print the high score table.