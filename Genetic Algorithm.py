import random
import sys
sys.setrecursionlimit(2500)

class UFDS:
    def __init__(self,d):
        a=list(d.keys())
        c=[i.split('-') for i in a]
        s=set()
        for i in c:
            s.update(i)
        b=list(s)
        self.u=[{i} for i in b]
               
    
    def find(self,x):
        for i in self.u:
            if x in i:
                return i
                
    
    
    def union(self,x,y):
        self.u.remove(x)
        self.u.remove(y)
        a=x|y
        self.u.append(a)
        return self.u

def testing_solution(c,d):
    o=UFDS(d)
    for i in c:
        x,y=i.split('-')
        j=o.find(x)
        k=o.find(y)
        if j!=k:
            o.union(j,k)
        else:
            return False
    else:
        return True

def create_random_chromosme(d,s,e):
    o=UFDS(d)
    random.shuffle(s)
    a=[]
    for i in s:
        x,y=i.split('-')
        j=o.find(x)
        k=o.find(y)
        if j!=k:
            a.append(i)
            o.union(j,k)
        else:
            pass
        
        if len(a)==e:
            return a
        
    

def create_parent_solutions(d,s,n,e):
    p=[create_random_chromosme(d,s,e) for i in range(n)]
    return p
        

def computing_fitness_value(d,c):
    s=[d[i] for i in c]
    f=sum(s)
    return round(f,2)
    

def selecting_parent_solutions(d,s,n,e):
    p=create_parent_solutions(d,s,n,e)
    p.sort(key= lambda x:computing_fitness_value(d,x))
    ps=p[0:2]
    return ps


def crossover(d,a,e):
    ''' a is gotten from the selecting_parent_solutions function '''
    u=set(a[0])|set(a[1])
    o=list(u)
    try:
        c=create_random_chromosme(d,o,e)
        assert computing_fitness_value(d,c)<computing_fitness_value(d,a[0])
    except RecursionError:
        return a[0]
    except AssertionError:
        return crossover(d,a,e)
    else:
        return c



def mutation(d,s,e,b):
    ''' b is gotten from the crossover function '''
    r=random.random()
    if r<0.15:
        try:
            c=create_random_chromosme(d,s,e)
            assert computing_fitness_value(d,c)<computing_fitness_value(d,b)
        except AssertionError:
            return mutation(d,s,e,b)
        except RecursionError:
            return b,computing_fitness_value(d,b)
        else:
            return c,computing_fitness_value(d,c)
    else:
        return b,computing_fitness_value(d,b)

def ga(d,g,e):
    s=list(d.keys())
    offsprings=[]
    a=selecting_parent_solutions(d,s,4,e)
    h=crossover(d,a,e)
    f= mutation(d,s,e,h)
    offsprings.append(f)
    for i in range(g):
        try:
            a=selecting_parent_solutions(d,s,4,e)
            a=[offsprings[0][0],a[0]]
            h=crossover(d,a,e)
            f= mutation(d,s,e,h)
            offsprings.sort(key=lambda x: x[1])
            offsprings=offsprings[:1]
            if offsprings[0][1]>f[1]:
                print('The total distance after {} iterations is {}'.format(i, offsprings[0][1]))
            offsprings.append(f)
        except RecursionError:
            solution=offsprings[0]
            print(solution)
    else:
        print(f' total distance after {g} iterations is {offsprings[0][1]}')
        solution = offsprings[0][0]
        print(solution)
        for edge in solution:
            print(f'{edge} \t {d[edge]}')

network = {'1-2': 853.4, '2-3': 160, '2-23': 933.9, '3-4': 170, '3-5': 158.7, '5-6': 142.8, '4-8': 256.7, '6-7': 68.7,
           '7-8': 27.2, '8-9': 142.7, '7-10': 36.8, '10-11': 27.2, '8-11': 36.8, '11-12': 126, '12-13': 208.2,
           '12-14': 363.6, '14-15': 118, '13-16': 328.2, '15-16': 150, '14-17': 100, '15-18': 100, '18-19': 100,
           '18-17': 118, '16-19': 115, '20-21': 166.4, '18-21': 152.8, '21-26': 170, '26-25': 84.2, '26-27': 130,
           '27-28': 170, '28-35': 115, '35-34': 170, '27-34': 115, '34-36': 235, '36-33': 72, '33-26': 574,
           '25-24': 140, '24-23': 100, '23-22': 100, '22-31': 371.35, '24-30': 100, '23-29': 100, '29-30': 100,
           '29-32': 170, '32-33': 285, '32-31': 100, '17-20': 115}


ga(network, 23, 35)



