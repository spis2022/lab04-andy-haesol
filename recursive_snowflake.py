import turtle

snow = turtle.Turtle()
snow.penup()
snow.setpos(-100,0)
snow.pendown()

def snowflake(side_length, levels):
    snowflake_side(side_length, levels)
    snow.right(120)
    snowflake_side(side_length, levels)
    snow.right(120)
    snowflake_side(side_length, levels)
    
 




def snowflake_side(side_length, levels):
    
    if(levels == 0):
        snow.forward(side_length*(1/3))
        return

   
    if(levels > 0):
        snowflake_side(side_length, levels - 1)
        snow.left(60)
        snowflake_side(side_length, levels - 1)
        snow.right(120)
        snowflake_side(side_length, levels - 1)
        snow.left(60)
        snowflake_side(side_length, levels - 1)
    
    


snowflake(25, 3)
turtle.done()