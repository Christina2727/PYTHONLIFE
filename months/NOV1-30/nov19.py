"""Drunk in the Caribbean"""
"""Figures out how many drinks we would consume in a year"""
my_margarita = 28
cabana_boy_kahluas = 14
spills = 4
drunks = my_margarita
for week in range (1, 53):
    drunks = drunks + cabana_boy_kahluas - spills
    print("Week %s = %s " % (week, drunks))

x = 45
y = 80
while x < 50 and y < 100:
    x = x + 1
    y = y + 1
    print(x, y)


    

for x in range (0,20):
     print('hello %s' % x)
     if x >= 9 or x < 5:
         break


for x in range (3,36, 3):
    print(x)


x = 1
ingredients = ['snails', 'leeches' , 'gorilla', 'caterpillar','centipede']
for i in ingredients:
    print('%s %s' % (x,i))
    x = x + 1

"moon weight"
w = 75

for year in range(1,16):
    w = w +1
    m = w * 0.165
    print("Year %s is %s" %(year, m))
    

    
def testfunc(first, last):
    print('Hello %s %s' % (first, last))

testfunc('Heather' , ' Deloree')
f1= 'Charlie'
f2= 'roberts'

testfunc(f1, f2)

def savings(pocket_money, paper_route, spending):
    return pocket_money + paper_route - spending
print(savings(25,10,5))


another_variable = 100
def variable_test():
    first_variable = 10
    second_variable = 20
    return first_variable * second_variable * another_variable
print(variable_test())


def spaceship_building(cans):
    total_cans=0
    for week in range(1,53):
        total_cans=total_cans + cans
        print ('week %s =%s cans' % (week, total_cans))

spaceship_building(13)

    





   
      

    
