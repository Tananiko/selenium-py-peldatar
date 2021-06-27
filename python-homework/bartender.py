# Kérd be a felhasználó életkorát, és kérdezd meg, mit iszik.
# Kétféle italt ismerünk: sör és kóla.
# Ha a felhasználó kiskorú, és sört kér, akkor közöld vele, hogy sajnos nem adhatsz neki.
# Ha a felhasználó 60 feletti, és kólát kér, akkor közöld vele, hogy a koffein megemelheti a vérnyomását.
# Ha ismeretlen italt adott meg, akkor írd ki, hogy csak sört és kólát tudunk adni.
# Minden más esetben szolgáld ki. (Írd ki pl. "Parancsoljon, a söre." vagy "Parancsoljon,a kólája.")

drink_preferences = ("Beer", "Coke")
age= int(input("Please, submit your age!: "))
drink_of_choice = input("What would you like to drink?: ")

if (age<18 and drink_of_choice == "Beer"):
        print("I am afraid, you are not going to be served as consumption of alcoholic drinks "
          "for young people under 18 is not legal. You can order a Coke only")
elif age >= 61 and drink_of_choice == "Coke":
        print("Please consider, that caffein may harm and increase your bloodpressure.")
elif drink_of_choice not in drink_preferences:
    print("I am afraid, we can only serve you with Beer or Coke")

else:
    print(f"Thank you, you are eligable to order! My pleasure, here is your {drink_of_choice}.Enjoy!")

