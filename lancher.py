import os
import sys

filename = sys.argv[1]

os.system("python3 projet_maker.py " + str(filename) + ".json")
os.system("python3 converter.py " + str(filename) + ".json " + str(filename) + ".csv")
os.system("python3 viewer.py " + str(filename) + ".csv")
