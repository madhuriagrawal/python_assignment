import time
import pyttsx3
class ElevatorSystemDesign:

     #Assuming a simple Elevator design


    def elevatorButtonPressed(self,currentFloor):
        engine = pyttsx3.init();
        engine.setProperty('rate', 175)
        engine.setProperty('volume', 1.0)



        print("Door is opening!")
        engine.say("Door is opening!")
        engine.runAndWait();
        print("Welcome to the floor Number",currentFloor)
        text="Welcome to the floor Number",currentFloor
        engine.say(text)
        engine.runAndWait();

        engine.say("Enter the floor number you want to go")
        engine.runAndWait();
        floorToGo=int(input("Enter the floor number you want to go:"))

        if currentFloor>floorToGo:
            for i in range(currentFloor, floorToGo, -1):
                print(i)
                time.sleep(2)

        else:
            for i in range(currentFloor,floorToGo):
                print(i)
                time.sleep(2)




        print("you reached at floor Number",floorToGo)
        text="you reached at floor Number",floorToGo
        engine.say(text)
        engine.runAndWait();
        print("Door is closing now! Bye")
        engine.say("Door is closing now! Bye")
        engine.runAndWait();




x = ElevatorSystemDesign()
x.elevatorButtonPressed(4)


