direction = ""

while direction != "leave":
   direction = input("To enter choose 'start' or 'leave' to exit: ")
   
   if direction == "start":
      print("You have enter the dark room") 
      direction = input("Do you want to head right , left or straight ? ")
      
      if direction == "right":
         print("You have found the medicines to cure any disease")

      elif direction == "left":
         print("You have fall into the pit and got injured ")

      elif direction == "straight":
         print("You have encounter the monsters ")
         action = input("Do you want to 'fight' or 'run'? ").lower()

         if action == "fight":
            print("You have won the hard boss fight against the monsters")
            print("and now gain the ability to fly,cure and teleportation.")

         elif action == "run":
            print("You have escaped unscated and leave that place")

         elif direction == "leave":
            print("You have exited the room ")

         else:
            print("Invalid command , please 'start' or 'leave'. ")
