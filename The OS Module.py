import os
import shelve
import pprint
import shutil
name = os.name # returns name of operating system
environ = os.environ   # returns environment variables
cwd = os.getcwd()

os.fsencode('C:\\Users\\Ichinga Samuel\\Downloads\\Video\\Interacting With OS')
os.fsdecode(b'C:\\Users\\Ichinga Samuel\\Downloads\\Video\\Interacting With OS')

# print(os.path.abspath('D:\Library\Computer Science\Python\The Python Library Refrence'))

# print(os.path.relpath(r'./Math'))

a = os.listdir('.')
total = 0
for file in a:
    if file.endswith('py'):
        total += os.path.getsize(os.path.join(cwd, file))
print(total)

cats = ['Zophie', 'Pooka', 'Simon']
sf = shelve.open('mydata')
sf['cats'] = cats
sf.close()

d = [{i: i**k for i in range(2, 10)} for k in range(1, 10)]
pprint.pformat(d)
fo = open('newpy.py', 'w')
fo.write('dd = ' + pprint.pformat(d) + '\n')
fo.close()

# shutil.copy(r'./Maths/Change.py', '.')
# shutil.copytree(r'./Maths', r'./Csvs')
shutil.disk_usage()
# shutil.move(r'../../Pluralsights/batch-file - Copy.txt', r'./Maths')

