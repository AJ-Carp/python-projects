def chooser():
  import random

  def food_chooser():
    food = ["Burger King", "McDonalds", "Taco Bell", "Chick-Fil-A"]

    choice = random.choice(food)
    print(choice)

  def color_chooser():
    color = ["black", "red", "blue", "pink"]

    choice = random.choice(color)
    print(choice)

  def mood_chooser():
    mood = ["happy", "sad", "angry",]

    choice = random.choice(mood)
    print(choice)
  print("\n")
  print("I can help you choose your mood, color, and food for the day.")
  answer = input("What can I help you choose? ").lower()

  if "food" in answer and "mood" in answer and "color" in answer: 
    mood_chooser()
    food_chooser()
    color_chooser()
  elif "food" in answer and "mood" in answer:
    food_chooser() 
    mood_chooser()
  elif "food" in answer and "color" in answer:
    food_chooser()
    color_chooser()
  elif "mood" in answer and "color" in answer:
    mood_chooser()
    color_chooser()
  elif "food" in answer:
    food_chooser()
  elif "color" in answer:
    color_chooser()
  elif "mood" in answer:
    mood_chooser()
  print("\n")
  answer = input("Is there anything else? ").lower()
  if answer == "yes" or answer == "yeah" or answer == "ye" or answer == "ya":
    chooser()
  else:
  
    print("Ok")
    quit()

chooser()

