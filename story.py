

print("There is a vampire cyclops chasing you into the forest!")
direction= input("Do you want to turn LEFT or RIGHT?")
direction= direction.lower()

if direction == "left":
    print("There was a large tree hiding in the shadows and its branches tripped you, resutling in the monster dragging you away to your doom!")
    print("try again!")

elif direction == "right":
    print("You found boulder waiting right around the corner, you hid behind it and due to his single, eye the cyclops didn't see you! Now you see a opening to the field that was next to the forest.")
    field= input("Do you want to wander into the field?")
    field = field.lower()

    if field == "yes":
        print("This was the wrong choice. The meadow is crawling with poisonous catepillars which will bite your ankles, soon their venom will seep into your veins!")
        print("try again!")


    elif field == "no":
        print("The forest provided shelter to you from the evils of the field. Now as you walk through the forest, you fall into a pit of quicksand!")
        struggle= input("Do you want to try and get out of the quicksand yourself?")
        struggle= struggle.lower()

        if struggle == "yes":
            print("Struggling only made yous sink into the quicksand faster, resutling in no possible escape from its grasp.")


        elif struggle == "no":
            print("Your resistance to struggle and loud screams, attracted the attention of a handsom young man, who came to the rescue. He carried you out of the quicksand and to a beautiful waterfall. He insists you take a drink from the fresh water since you were so parched.")
            water= input("Do you trust him and drink the water?")
            water = water.lower()

            if water == "yes":
                print("Phew, that water was fresh and delicious, thank god it was not bad for you! Now you and the man are going to part ways.")
                home= input("Do you go home or follow the man and leave your old life forever?")
                home = home.lower()

                if home == "go home":
                    print("You finally get to go home safely! Tell your family that you are OK, and go watch some netflix. Relax, you ar finally safe!")

                elif home == "follow the man":
                    print("This is where we lose you! Never follow a man you don't know!!! Whatever happens now is your own fault, BEWARE!")
                    print("try again!")


                else:
                    print("This is an incorrect answer. Try a new answer or typing it a differnt way.")
                    home= input("Do you go home or follow the man and leave your old life forever")
                    home = home.lower()

            elif water == "no":
                print("Uh Oh! You had gone too long without water and your dehardation will be the end of you! make sure to always hydrate!")
                print("try again!")
                

            else:
                print("This is an incorrect answer. Try a new answer or typing it a differnt way.")
                water= input("Do you trust him and drink the water?")
                water = water.lower()

        else:
            print("This is an incorrect answer. Try a new answer or typing it a differnt way.")
            struggle= input("Do you want to try and get out of the quicksand yourself?")
            struggle = struggle.lower()
    else:
        print("This is an incorrect answer. Try a new answer or typing it a differnt way.")
        field= input("Do you want to wander into the field?")
        field = field.lower()

else:
    print("This is an incorrect answer. Try new answer or typing it a differnt way.")
    direction= input("Do you want to turn LEFT or RIGHT?")
    direction= direction.lower()
