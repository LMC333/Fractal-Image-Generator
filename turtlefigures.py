from turtle import *
import math


#tree
def tree(n, l, pen):
     if n==0 or l<2 :
          return
     #endif
     #recursion
     pen.forward(l)
     pen.left(45)
     tree(n-1, l/2, pen)
     pen.right(90)
     tree(n-1, l/2, pen)
     pen.left(45)
     pen.backward(l)



#binary tree
def tree4(n, l, pen):
    #termination
    if n==0 or l<2:
        return
    
    #endif
    #recursion
    pen.forward(l)
    pen.left(90)
    tree4(n-1, l/2, pen)
    pen.right(60)
    tree4(n-1, l/2, pen)
    pen.right(60)
    tree4(n-1, l/2, pen)
    pen.right(60)
    tree4(n-1, l/2, pen)
    pen.left(90)
    pen.backward(l)
#end tree



def fern(n, l, pen):
    #termination
     if n==0 or l<2:
        return

    #endif

    #recursion
     pen.forward(l/2)
     pen.left(60);fern(n-1, 0.5*l, pen);pen.right(60)
     pen.forward(l/2)
     pen.right(45);fern(n-1, 0.5*l, pen);pen.left(45)
     pen.forward(l)
     pen.right(10);fern(n-1, 0.8*l, pen);pen.left(10)

     pen.backward(2*l)

    #endfern


 #snowflake + antisnowflake
def koch(n, l,  pen):
        #termination
        if n==0 or l<2:
            pen.forward(l)
            return
        
        #endif

        #recursion    
        koch(n-1, l/3, pen)
        pen.left(60)
        koch(n-1, l/3, pen)
        pen.right(120)
        koch(n-1,l/3, pen)
        pen.left(60)
        koch(n-1, l/3, pen)
#endkoch

def flake(n , l,  pen):
    for i in range(3):
        koch(n, l, pen)
        pen.left(120)
        #endfor
#endflake
                    
def flake2(n, l, pen):
    for i in range(3):
        koch(n, l, pen)
        pen.right(120)
        #endfor
   

#endfor

#triangle gasket
def gasket(n, l, pen):
    if n==0 or l<2:
        #equilateral triangle
        for i in range(3):
            pen.forward(l)
            pen.left(120)
        #endfor
        return
    #endif

    #recursion
    for i in range(3):
        gasket(n-1, l/2, pen)
        pen.forward(l)
        pen.left(120)
    #endfor
    #endgasket



# square gaskets
def sqgasket(n, l, pen):
    # termination
    if n==0 or l<2:
        # equilateral quad
        for i in range (4):
            pen.forward(l)
            pen.left(90)
        # end for
        return
    # endif

    # recursion
    for i in range(4):
        sqgasket(n-1, l/3, pen)
        pen.forward(l)
        pen.left(90)
        #end for
        # end gasket
        
     
    '''else:
            for i in range(4):
                s(n-1, l/3)
                pen.forward(l)
                s(n-1, l/3)
                pen.forward(l)
                penforward(l)
                pen.left(90)
            pen._update()
#end'''
        

    #Andrews Cross
def cross(n,l,pen):
        #termination
        if n==0 or l<2:
            pen.forward(l)
            return
        
        #endif

        #recursion    
        koch(n-1, l/3, pen)
        pen.left(90)
        koch(n-1, l/3, pen)
        pen.right(90)
        koch(n-1,l/3, pen)
        pen.right(90)
        koch(n-1, l/3, pen)
        pen.left(90)
        koch(n-1, l/3, pen)
        pen.right(90)
        koch(n-1,l/3, pen)
        pen.right(90)
        koch(n-1, l/3, pen)
        pen.left(90)
        koch(n-1, l/3, pen)
        pen.right(90)
        koch(n-1,l/3, pen)
        pen.right(90)
        koch(n-1, l/3, pen)
        pen.left(90)
        koch(n-1, l/3, pen)
        pen.right(90)
        koch(n-1,l/3, pen)
        pen.right(90)
        koch(n-1, l/3, pen)
        pen.left(90)
        koch(n-1, l/3, pen)

        
#endcross



'''
#flower
def petal(pen,r, n):
     #termination
      if n==0 or l<2:
            pen.forward(l)
            return
        #endif

     #recursion
     pen.forward(50)
     pen.right(150)
     pen.forward (60)
     pen.right (100)
     pen.forward(30)
     pen.right(90)
     #endpetal

def flower(n , l,  pen):
    for i in range(20):
        petal(n, l, pen)
        pen.left(120)
        #endfor
#endflower
'''

'''
def lcircle(n, l, pen):
    #termination
    if n==0 or l<2:
        return

#Linear circle
        pen.penup()
        pen.goto(-75,-75)
        pen.pendown()

#recursion
for i in range(50):
    
    pen.forward(l)
    pen.left(85)

     pen.penup()
     pen.goto(-25,-25)
     pen.pendown()


#Star
def star():

    for i in range(5):

        pen.forward(100)
        pen.right(144)
'''
 
