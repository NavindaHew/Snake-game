import turtle as t
import time
import random


playerscore = 0
high_score = 0
score = t.Turtle()
score.speed(0)
score.color('green')
score.penup()
score.hideturtle()
score.goto(0,+250)
score.write('Score:',align='center',font=('Arial',24,'normal'))

delay = 0.1

 
#set up the screen
window=t.Screen()
window.title("Snake Game")
window.bgcolor("black")
window.setup(width=600, height=600)
window.tracer(0)

#create snake head
head=t.Turtle()
head.speed(0)
head.shape("square")
head.color("white")
head.penup()
head.goto(0,0)
head.direction = 'stop'


#food
food=t.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0,100)

#snakebody
segments = []




#functions
def goup():
    if head.direction != 'down':
        head.direction = 'up'

def godown():
    if head.direction != 'up':
        head.direction = 'down'

def goleft():
    if head.direction != 'right':
        head.direction = 'left'

def goright():
    if head.direction != 'left':
        head.direction = 'right'

#keyboard bindings
window.listen()
window.onkeypress(goup,'Up')
window.onkeypress(godown,'Down')
window.onkeypress(goleft,'Left')
window.onkeypress(goright,'Right')

#functions
def move():
    if head.direction == 'up':
        y = head.ycor()
        head.sety(y+20)

    if head.direction == 'down':
        y = head.ycor()
        head.sety(y-20)

    if head.direction == 'left':
        x = head.xcor()
        head.setx(x-20)

    if head.direction == 'right':
        x = head.xcor()
        head.setx(x+20)

#main game loop
while True:
    window.update()

    #collusion with the border
    if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:
        time.sleep(1)
        head.goto(0,0)
        head.direction = 'stop'

        #hide segments
        for segment in segments:
            segment.goto(1000,1000)

        #clear segments
        segments.clear()
        score.clear()
        playerscore = 0

        #time delay
        delay = 0.1

    if head.distance(food) < 15:
        #making the food move into a random place
        x = random.randint(-290,290)
        y = random.randint(-290,290)
        food.goto(x, y)

        #add a segment
        new_segment = t.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("aqua")
        new_segment.penup()
        segments.append(new_segment)

        #shoten delay when snake gets longer
        delay -= 0.001

        
        playerscore += 5
        if playerscore > high_score:
            high_score = playerscore
        score.clear()
        score.write(' Score:{}   High Score: {}'.format(playerscore,high_score),align='center',font=('Arial',24,'normal'))

        
    #move the end segments
    for index in range(len(segments)-1,0,-1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x, y)

    #move segmet 0 to where the head is
    if len(segments) > 0:
        xo = head.xcor()
        yo = head.ycor()
        segments[0].goto(xo,yo)
        
    
    move()

    #collusion with body    
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0,0)
            head.direction = 'stop'

            #hide segments
            for segment in segments:
                segment.goto(1000,1000)

            #clear segments
            segments.clear()
            score.clear()
            playerscore = 0

            delay = 0.1
            
    time.sleep(delay)



window.mainloop()


#first game completed using a youtube video and some were done by me. completed om 8th Sep 2021
#Snake Game 
