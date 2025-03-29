from turtle import Turtle

class Scoreboard(Turtle):

      def __init__(self):
          super().__init__()

          self.hideturtle()
          self.score =0
          self.color("White")
          self.penup()
          self.goto(x=0,y=260)
          self.update_score()
      def update_score(self):
          self.write(f"score:{self.score} ", move=False, align='center', font=('Arial', 25, 'normal'))
      def game_over(self):

          self.goto(0,0)
          self.clear()
          self.write("Game Over",False,'center',('courier',24,'normal'))

      def score_inc(self):
          self.score += 1
          self.clear()
          self.update_score()











