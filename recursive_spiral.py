import turtle

turtle1 = turtle.Turtle()
turtle1.setpos(0,0)
def spiral(initial_length, angle, multiplier):
    
    if(initial_length > 200 or initial_length < 1):
        return
    
    turtle1.forward(initial_length)

    
    
    #below is the base case
    if(multiplier == 1):
        print("Enter a multiplier that is not 1")
    elif(multiplier < 1):
        turtle1.right(angle)       
    elif(multiplier > 1):
         turtle1.left(angle)
         

    spiral(initial_length * multiplier, angle, multiplier)
    


spiral(1, 45, 1.1)
turtle.done()