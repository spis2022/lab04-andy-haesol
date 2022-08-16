import turtle

weirdTree = turtle.Turtle()
weirdTree.setpos(0, 0)
weirdTree.left(90)

weirdTree.speed(1)


    

def tree(trunk_height, height):
    
    if(height == -1):
        return
    
    
    
    
    weirdTree.forward(trunk_height)
    
    
    weirdTree.right(45)
    tree(trunk_height*(2/3), height - 1)

    weirdTree.left(90)
    tree(trunk_height*(2/3), height - 1)

    weirdTree.right(45)
    weirdTree.backward(trunk_height)
    
    
    
    
    





tree(200,4)
turtle.done()