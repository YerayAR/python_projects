import tkinter as tk
import time as tm
import random

class Pong(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Pong")
        self.canvas = tk.Canvas(self, width=800, height=400, bg="black")
        self.canvas.pack()
        self.balls = [Ball(self.canvas, self, 50//4, "white")]
        self.player_paddle = Paddle(self.canvas, "white", 750)
        self.auto_paddle = AutoPaddle(self.canvas, "white", 50)
        self.bind_all("<Key>", self.keypress)
        self.player_score = 0
        self.auto_score = 0
        self.player_score_text = self.canvas.create_text(200, 20, fill="white", font="Times 20 italic bold", text="Player: 0")
        self.auto_score_text = self.canvas.create_text(600, 20, fill="white", font="Times 20 italic bold", text="AI: 0")
        self.game_over_text = self.canvas.create_text(400, 200, fill="white", font="Times 40 italic bold", text="")
        self.reset_button = tk.Button(self, text="Reset", command=self.reset)
        self.reset_button.pack()
        self.game_over = False
        self.animate()

    def reset(self):
        self.game_over = False
        self.player_score = 0
        self.auto_score = 0
        self.canvas.itemconfigure(self.player_score_text, text="Player: 0")
        self.canvas.itemconfigure(self.auto_score_text, text="AI: 0")
        self.canvas.itemconfigure(self.game_over_text, text="")
        # Delete all balls from the canvas
        for ball in self.balls:
            self.canvas.delete(ball.id)
        # Reset the balls list
        self.balls = [Ball(self.canvas, self, 50//4, "white")]

    def keypress(self, event):
        if event.keysym == "Up":
            self.player_paddle.move(-12)
        elif event.keysym == "Down":
            self.player_paddle.move(12)

    def update_score(self, player_scored):
        if self.game_over:
            return

        if player_scored:
            self.player_score += 1
            self.canvas.itemconfigure(self.player_score_text, text=f"Player: {self.player_score}")
        else:
            self.auto_score += 1
            self.canvas.itemconfigure(self.auto_score_text, text=f"AI: {self.auto_score-1}")

        if self.player_score >= 5:
            self.game_over = True
            self.canvas.itemconfigure(self.game_over_text, text="Player Wins")
        elif self.auto_score >= 6:
            self.game_over = True
            self.canvas.itemconfigure(self.game_over_text, text="AI Wins")

    def animate(self):
        while True:
            for ball in self.balls:
                ball.move(self.player_paddle, self.auto_paddle)
            self.auto_paddle.manage_movement(self.balls[0].y, tm.time())
            self.update_idletasks()
            self.update()
            tm.sleep(0.01)

class Ball:
    def __init__(self, canvas, game, size, color):
        self.canvas = canvas
        self.game = game
        self.id = canvas.create_oval(20, 20, size, size, fill=color)
        self.canvas.move(self.id, 245, 100)
        self.xspeed = 3
        self.yspeed = 3
        self.y = 100
                 
    def move(self, player_paddle, auto_paddle):
        self.canvas.move(self.id, self.xspeed, self.yspeed)
        pos = self.canvas.coords(self.id)
        width = self.canvas.winfo_width()
        height = self.canvas.winfo_height()

        if pos[1] <= 0 or pos[3] >= height:
            self.yspeed = -self.yspeed

        if self.hit_paddle(pos, player_paddle):
            if not self.game.game_over:
                self.xspeed = -self.xspeed
            else:
                if random.random() > 0.8:
                    self.game.balls.append(Ball(self.canvas, self.game, 50//4, "white"))
        elif self.hit_paddle(pos, auto_paddle):
            if not self.game.game_over:
                self.xspeed = -self.xspeed
            else:
                if random.random() > 0.8:
                    self.game.balls.append(Ball(self.canvas, self.game, 50//4, "white"))
        elif pos[0] <= 0:
            self.xspeed = -self.xspeed
            self.game.update_score(True)
        elif pos[2] >= width:
            self.xspeed = -self.xspeed
            self.game.update_score(False)

        self.y = (pos[1] + pos[3]) // 2  # update the vertical center of the ball


    def hit_paddle(self, pos, paddle):
        paddle_pos = self.canvas.coords(paddle.id)
        if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:
            if pos[3] >= paddle_pos[1] and pos[1] <= paddle_pos[3]:
                return True
        return False

class Paddle:
    def __init__(self, canvas, color, x_position):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0, 0, 30//4, 175//4, fill=color)
        self.canvas.move(self.id, x_position, 150)

    def move(self, amount):
        pos = self.canvas.coords(self.id)
        height = self.canvas.winfo_height()

        if pos[1] + amount >= 0 and pos[3] + amount <= height:
            self.canvas.move(self.id, 0, amount)
    
    def move_to(self, y):
        pos = self.canvas.coords(self.id)
        current_y = (pos[1] + pos[3]) // 2
        if y > current_y:
            self.move(3)
        elif y < current_y:
            self.move(-3)

class AutoPaddle(Paddle):
    def __init__(self, canvas, color, x_position):
        super().__init__(canvas, color, x_position)
        self.random_movement_end = tm.time()
        self.random_direction = 3

    def move(self, amount):
        pos = self.canvas.coords(self.id)
        height = self.canvas.winfo_height()

        if pos[1] + amount >= 0 and pos[3] + amount <= height:
            self.canvas.move(self.id, 0, amount)
        else:
            self.random_direction *= -1

    def manage_movement(self, ball_y, current_time):
        if current_time < self.random_movement_end:
            self.move(self.random_direction)
        else:
            self.move_to(ball_y)
            if random.random() < 0.01:
                self.random_movement_end = current_time + random.randint(3, 4)
                self.random_direction = random.choice([-3, 3])

if __name__ == "__main__":
    Pong()
