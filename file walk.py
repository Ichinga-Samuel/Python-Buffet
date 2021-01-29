
import os

os.chdir('C:\\Users\Ichinga Samuel\WebstormProjects\GadMws')

files = []
for f, j, k in os.walk('.'):
    files.append(k)

print(files)