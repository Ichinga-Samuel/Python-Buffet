import sys
#sys.stderr.write('What is Happening Here\n')
#sys.stdout.write('Out of where\n')
#sys.stderr.write('what is stderr\n')
#sys.stderr.flush()

if len(sys.argv) > 1:
    print(float(sys.argv[1])*5)

def pr(x, t, y):
    return y**(x*t)

if len(sys.argv) > 3:
    print(pr(float(sys.argv[1]), float(sys.argv[2]),float(sys.argv[3])))


