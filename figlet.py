import random
import sys
from pyfiglet import Figlet
figlet = Figlet()
font = figlet.getFonts()
definedFont = figlet.setFont()
if len(sys.argv) == 1:
    figlet.setFont(font = random.choice(font))
    text = input("Input: ")
    print("Output: " + figlet.renderText(text)) 
elif sys.argv[1] == "-f" or sys.argv[1] == "--font":
    figlet.setFont(font=sys.argv[2])
    text = input("Input: ")
    print("Output: " + "\n" + figlet.renderText(text))
else:
    print("Invalid usage")   


