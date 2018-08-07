'''import time
print (time.asctime())
import sys
#print (sys.stdin.readline())

def silly_age_joke():
    print('HOW OLD ARE YOU?')
    age=int(sys.stdin.readline())
    if age >=10 and age <= 13:
        print('what is 13+49 +84 + 155+ 97? A headache !')
    else:
        print('Huh?')


silly_age_joke()


def can_we_code ():
    print('Can you code?')
    
    if 'maybe':
        print('atta girl')
    else:
        print(' yesssssss you can')

can_we_code()



"moon weight"
w = 75

for year in range(1,16):
    w = w +1
    m = w * 0.165
    print("Year %s is %s" %(year, m))


def moon_weight(weight, increase, years):
        years = years+1
        for year in range(1,years):
            weight = weight + increase
            moon_weight = weight * 0.165
            print("Year %s is %s " %(year, moon_weight))

moon_weight (35, 0.3, 5)



import sys       
def moon_weight():
    print('What is your weight?')
    weight= float(sys.stdin.readline())
    print('How much will you gain per year eating moon cheese?')
    increase = float(sys.stdin.readline())
    print('how many years are you going to be on the moon ')
    years=int(sys.stdin.readline())
    years = years+1
    for year in range(1,years):
            weight = weight + increase
            moon_weight = weight * 0.165
            print("Year %s is %s " %(year, moon_weight))

moon_weight()'''
    
import sys
def mom_lies():
    print ('does your mom lie')
    answer=str(sys.stdin.readline())
    print('of course she does, how mant times per day')
    day =int(sys.stdin.readline())
    week = (day * 7)
    print('your mom lies %s times per week' % week)

mom_lies()
    
    

