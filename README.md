# PyWinMain

### Motivation
I've never liked the python accepted practice of using:
```sh
if __name__=='__main__':
   #do something
```

When creating a GUI, I thought it would look nicer to create a simple module so one could write code like this:

```sh
@WinMain
def main():
   #do something
```

Of course the function above, "main" could also take variables such as "sys.args".

### Usage
To get started with PyWinMain, one needs only do install the package and perform the following in the python script:
```sh
import sys
from pywinmain import WinMain

@WinMain
def main( argv = sys.args[1:] ):
   #do something
```

And Voila! You are there!

### Caveats
* It will not run in python's interactive mode
