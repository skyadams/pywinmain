import inspect
from inspect import *
from OpenGL.GLUT import *

class WinMain:
  @staticmethod
  def __init__(func,*args,**kwargs):
    frm = inspect.stack()[1]
    mod = inspect.getmodule(frm[0])
    if (mod.__name__ == '__main__'):
      func(*args,**kwargs)
      glutMainLoop()
