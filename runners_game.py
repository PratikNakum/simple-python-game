
while True:
    answer = input('would you like to play (yes/no) :')
    
    if answer.lower().strip() == "yes":
        
        answer = input('you reach a cross road now you want to take left turn or right????  :').lower().strip()
        if answer == "left":
            answer = input('you are in front of monster you like to run or attack.  :')
            
            if answer == "attack":
                print('it was not greate idea .........YOU LOST!!!')
                break
            else:
                print('good choise you made it safely...!!!')
                
            answer = input('you see a car and a plane which would you like to take (car/plane)  :')
            
            if answer == "plane":
                print("unfortunetly you don't know how to fly........game over!!!")
                break
            else:
                print("Congratulation you won the game")
                
        elif answer == "right":
            print('you walk aimlessly to the right and fall  on a patch of ice ...you are injured your leg was break!!!')
        
        else:
            print ("That's to bad")
            break	