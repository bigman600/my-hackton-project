import flet
from flet import *
from functools import partial
import time

class navigation_bar(UserControl):
   def __init__(self):
      super().__init__()
   def build(self):
      return Container(content=None)

#main function
def main(page: Page):
   # title
   page.title ='flet modern sidebar'
   
   #alignement
   
   page.vertical_alignment = 'center'
   page.horizontal_alignment = 'center'

   add class to page
   