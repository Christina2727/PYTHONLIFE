#sillysentencer.py
#Heather Loree and Christina
#Dec 21

"""this program prints silly sentences by mapping random words
into a formatting template"""

#import
import random
sample_list = [x for x in range(10)]
random.choice(sample_list)


#constant               
template = "%s %s the %s %s."
BASE_SENTENCE = "My Python teacher wrote the Python book."
persons = ["My Python teacher","Christina","Charlie","Heather"]
verbs = ["wrote", "drank", "cried", "ran", "threw up", "pistol whipped"]
adjectives = ["Python", "fancy", "shiny", "rich", "funny", "naughty",
              "sparkly"]
nouns = ["book", "boat", "bloody mary", "house", "plane", "mixed drink"]


#Main Section
if __name__ == "__main__":
    person= random.choice(persons)
    verb = random.choice(verbs)
    adjective = random.choice(adjectives)
    noun = random.choice(nouns)

    format_values = (person, verb, adjective, noun)

#print(BASE_SENTENCE)
print(template%format_values)
print(BASE_SENTENCE == template%format_values)

