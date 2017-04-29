import random
from time import sleep

name = input("What is your name? ")
sleep(0.5)
print ("Hello " + name)
sleep(1)

pronoun = input("What is your prefered pronoun? ")

if pronoun == "he":
     possessive_pronoun = "his"
     object_pronoun = "him"
elif pronoun == "she":
     possessive_pronoun = "her"
     object_pronoun = "her"
elif pronoun == "they":
     possessive_pronoun = "their"
     object_pronoun = "them"
     
sleep(1)
print("Hello human person, nice pronouns!")
sleep(1)



places = ["the park", "the zoo", "the museum", "the school library", "the public swimming pool", "the Lego store", "the petshop", "the mall", "the record store", "the beach"]
hobbies = ["reading", "dancing", "traveling", "video games", "listening to music", "Doctor Who", "swimming", "cooking"]
activities = ["flying kytes", "climbing trees", "doing magic tricks", "programming", "board games", "treasure hunts"]
actions = ["slay", "shout at", "pacifically talk to", "scare away", "eat", "vaporise", "reason with", "poison"]
meanies = ["ghost", "giant angry cat", "faceless monster", "TERF", "dinosaur", "Stormtrooper", "werewolf", "red ogre", "gigantic lethal snake"]
books = ["'The Amazing adventures of the chocolate shoe'", "'The Horse that wanted to bark'", "'The Great book of slimy cooking'", "'The Lovely but weird story of the green cat'", "'The Yellow dog who could talk to hummingbirds'", "'Who Let the Meerkats out?'"]
rooms = ["kitchen", "living room", "attic", "basement", "garden", "bedroom"]
drinks = ["hot chocolate", "chai tea", "green tea", "hot milk", "coffee", "lemonade", "ginger ale", "root beer"]



favourite_place = random.choice(places)
favourite_thing = random.choice(hobbies)
monster = random.choice(meanies)
action = random.choice(actions)
book_title = random.choice(books)
favourite_drink = random.choice(drinks)
room = random.choice(rooms)
favourite_activity = random.choice(activities)


story = "Once upon a time, there was a beautiful human person named " + name + " who loved " + favourite_thing + " and " + favourite_activity + ". " + pronoun + " loved spending time at " + favourite_place + "."
continue_story = "one day, there was a " + monster + " and "  + name + " had to find a way to save " + possessive_pronoun + " city! It was up to " + object_pronoun + " or the city would be lost! " + name + " decided to " + action + " the awful monster and it was never seen again."
next_paragraph = "the city was saved, thanks to " + possessive_pronoun + " courage. it was now time to relax. " + name + " went back home to read " + possessive_pronoun + " favourite book, " + book_title + ", in " + possessive_pronoun + " " + room + " with a nice cup of " + favourite_drink + "."
next_morning = "The next morning, " + name + ", went back to " + favourite_place + " where " + pronoun + " hung out with " + possessive_pronoun + " friends. " + name + "'s friends loved " + object_pronoun + " as " + pronoun + " was such a nice person who always went out of " + possessive_pronoun + " way to help other people around " + object_pronoun + "."


print(story)
sleep(0.5)
print (continue_story)
sleep(0.5)
print (next_paragraph)
sleep(0.5)
print(next_morning)





