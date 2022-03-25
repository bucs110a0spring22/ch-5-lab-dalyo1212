'''
Estimates pi using Monte Carlo simulation

Virtual Dartboard has area 2 X 2 to accommodate unit circle
Total area is 4
Therefore, since area of unit circle = pi * radius^2 (and radius of 1 squared
  is 1), ratio of area of unit circle to area of board should be pi/4
  Theoretically, if you fill the entire board with darts, counting
  the number of darts that fall within the circle divided by the
  total number of darts thrown should give us that ratio (i.e., 1/4 * pi)
  Therefore, multiplying that result by 4 should give us an approx. of pi

Output to monitor:
  approximation of pi (float)
Output to window:
  colored dots that simulate unit circle on 2x2 square
Functions you must implement:
  drawSquare(myturtle=None, width=0, top_left_x=0, top_left_y=0) - to outline dartboard
  drawLine(myturtle=None, x_start=0, y_start=0, x_end=0, y_end=0) - to draw axes
  drawCircle(myturtle=None, radius=0) - to draw the circle
  setUpDartboard(myscreen=None, myturtle=None) - to set up the board using the above functions
  isInCircle(myturtle=None, circle_center_x=0, circle_center_y=0, radius=0) - determine if dot is in circle
  throwDart(myturtle=None)
  playDarts(myturtle=None) - a simulated game of darts between two players
  montePi(myturtle=None, num_darts=0) - simulation algorithm returns the approximation of pi
'''
import turtle
import random
import time

#########################################################
#                   Your Code Goes Below                #
#########################################################

def drawSquare(darty, width, top_left_x, top_left_y):
  darty.up()
  darty.goto(top_left_x, top_left_y)
  darty.down()
  for i in range(4):
    darty.forward(width)
    darty.right(90)

def drawLine(darty, x_start, y_start, x_end, y_end):
  darty.up()
  darty.goto(x_start, y_start)
  darty.down()
  darty.goto(x_end, y_end)
  
def drawCircle(darty, radius):
  darty.up()
  darty.goto(0, -radius)
  darty.down()
  darty.circle(radius,steps=360)
  

def setUpDartboard(window, darty):
  window.setworldcoordinates(-2, -2, 2, 2)
  drawSquare(darty, 2, -1, 1)
  drawLine(darty, -1, 0, 1, 0)      
  drawLine(darty, 0, -1, 0, 1)
  drawCircle(darty, -1)


def throwDart(darty):
  x_coordinate=random.uniform(-1, 1)
  y_coordinate=random.unifrom(-1, 1)
  darty.up()
  darty.goto(x_coordinate, y_coordinate)
  if darty.distance(0, 0)<1:
    darty.color("blue")
  elif darty.distance(0, 0)>1:
    darty.color("Black")
  darty.dot()
  darty.color("Red")


def drawSquareisInCircle(darty):
  if darty.distance(0, 0)<1:
    return True
  elif darty.distance(0, 0)>1:
    return False

def playDarts(darty): 
  player1score = 0
  player2score = 0
  player1 = throwDart
  player2 = throwDart
  for i in range(10):
    player1(darty)
    if darty.isInCircle(darty):
      player1score += 1
    player2(darty)
    if darty.isInCircle(darty):
      player2score += 1 
    print("Player 1 Score:" + str(player1score))
    print("Player 2 Score:" + str(player2score))
  if player1score > player2score:
    print("Player 1 Wins!")
  if player2score > player1score:
    print("Player 2 Wins!")
  elif player1score == player2score:
    print("Tie! GAME OVER!")

  
def montePi(darty, number_darts):
  pi = throwDart
  pi_num = 0
  for i in range(number_darts):
    pi(darty)
    if darty.isInCircle(darty):
      pi_num += 1
  return (pi_num/number_darts*4)






#########################################################
#         Do not alter any code below here              #
#       Your code must work with the main proivided     #
#########################################################
def main():
    print("This is a program that simulates throwing darts at a dartboard\n" \
        "in order to approximate pi: The ratio of darts in a unit circle\n"\
        "to the total number of darts in a 2X2 square should be\n"\
        "approximately  equal to pi/4")
    print("=========== Part A ===========")

    #Create window, turtle, set up window as dartboard
    window = turtle.Screen()
    darty = turtle.Turtle()
    darty.speed(0) 
    setUpDartboard(window, darty)

    for i in range(10):
        throwDart(darty)
    print("\tPart A Complete...")
    print("=========== Part B ===========")
    darty.clear()
    setUpDartboard(window, darty)
    playDarts(darty)
    print("\tPart B Complete...")
    print("=========== Part C ===========")
    darty.clear()
    setUpDartboard(window, darty)
    

    BATCH_OF_DARTS = 5000
    window.tracer(BATCH_OF_DARTS)

    
    number_darts = int(input("\nPlease input the number of darts to be thrown in the simulation:  "))
    approx_pi = montePi(darty, number_darts)
    print("\nThe estimation of pi using "+str(number_darts)+" virtual darts is " + str(approx_pi))
    print("\tPart C Complete...")
    window.exitonclick()

main()
