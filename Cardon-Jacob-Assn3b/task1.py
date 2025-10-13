# Jacob Cardon
# CS1400 - MWF - 8:30am
import drawly, random
from drawly import set_color, draw, rectangle, text, terminal_output, terminal_input
from time import time

class Game:
    pass

game = Game()
game.SPEED = 10
game.SCREEN_WIDTH = 720
game.SCREEN_HEIGHT = 720
game.SCORE_GOAL = 10
game.POINT_LIST = [5, 4, 3, 2, 1]
game.score = 0


class Meter:
    pass

meter = Meter()
meter.FRAMES = 5
meter.INCR = 12
meter.X = 565
meter.Y = 55
meter.W = 100
meter.H = 600
meter.BG = "white"
meter.CORRECT = "green"
meter.WRONG = "red"
meter.score = 0
meter.top = 0


class Scoreboard:
    pass

sb = Scoreboard()
sb.BG = "white"
sb.FG = "black"
sb.SIZE = 30
sb.X = 55
sb.Y = 55
sb.W = 200
sb.H = 50
sb.TEXT_X = 65
sb.TEXT_Y = 65
sb.score = 0

def update_score(new_score:int=0):
    """
    Updates game.score and changes displayed score instantly on scoreboard
    """
    game.score = new_score
    #scoreboard background
    set_color(sb.BG)
    rectangle(x_pos=sb.X, y_pos=sb.Y, width=sb.W, height=sb.H)
    #scoreboard text
    set_color(sb.FG)
    sb.score = max(0, min(game.score, game.SCORE_GOAL))#keeps scoreboard score within 0-10
    text(x_pos=sb.TEXT_X, y_pos=sb.TEXT_Y, text=f"Score: {sb.score}", size=sb.SIZE)
    draw()


def update_meter(start:int, target:int):
    """
    Takes arguments of where to animate to and from. Then draws animation in 5 frame increments.
    'target' should only be 1 score increase/difference as update_all() will call update_meter() multiple times until new score is met.
    """
    diff = target - start  # Local diff for this step

    for frame in range(1, meter.FRAMES + 1):# frames: 1-5
        # meter background
        set_color(meter.BG)
        rectangle(x_pos=meter.X, y_pos=meter.Y, width=meter.W, height=meter.H)

        frame_slice_modifier = frame / meter.FRAMES# fraction to find the incremental change for each frame update
        animated_score = start + diff * frame_slice_modifier# virtual score to animate for each frame(e.g., 0.2, 0.4, 0.6, 0.8, 1.0)

        # animates score change on meter (green or red) depending on increase or decrease
        if animated_score >= 0:
            green_height = meter.H / game.SCORE_GOAL * animated_score
            top_of_green = meter.Y + meter.H - green_height
            if diff >= 0:
                set_color(meter.CORRECT)
            else:
                set_color(meter.WRONG)
            rectangle(x_pos=meter.X, y_pos=top_of_green, width=meter.W, height=green_height)
            draw()

def update_all(new_score:int=0):
    diff = new_score - game.score

    #initializatin of meter/scoreboard before math questions asked
    if diff == 0:
        start = max(0, min(game.score, game.SCORE_GOAL))
        target = max(0, min(new_score, game.SCORE_GOAL))
        update_score(new_score)
        update_meter(start, target)
    else:
        direction = diff // abs(diff)
        #animates scoreboard and meter one point incriment at a time
        for i in range(abs(diff)):
            start = max(0, min(game.score, game.SCORE_GOAL))
            game.score += direction
            target = max(0, min(game.score, game.SCORE_GOAL))
            update_score(game.score)
            update_meter(start, target)

drawly.start(title="Don't Play With Mathes", dimensions = (720, 720), background="grey", terminal = True, terminal_lines = 5, terminal_line_height=20)
drawly.set_speed(game.SPEED)

#initialization
update_all(0)

terminal_output("DON'T PLAY WITH MATHES")
terminal_output("Earn points for correct answers and lose points for wrong ones.")
terminal_output("Answer quickly to earn (or lose) more points.")
terminal_input("   [Press 'Enter' to Start] ")

#scoreboard
while 0 <= game.score <= game.SCORE_GOAL:

    #generates randome math question
    num1 = random.randint(0, 10)
    num2 = random.randint(0, 10)
    op = random.choice(["+", "-", "*"])
    problem_str = f"{num1} {op} {num2} = "
    if op == "+":
        answer = num1 + num2
    elif op == "-":
        answer = num1 - num2
    elif op == "*":
        answer = num1 * num2

    #asks user to provide answer for math question. Tracks time(seconds) spent to answer and awards points
    # (0 <= sec < 1) = 5 points
    # (1 <= sec < 2) = 4 points
    # (2 <= sec < 3) = 3 points
    # (3 <= sec < 4) = 2 points
    # (4 <= sec) = 1 point
    start = time()
    user_answer = int(terminal_input(problem_str))
    end = time()
    points_awarded = game.POINT_LIST[min(int((end - start) // 1), 4)]

    #checks if correct or inccorect answer and prints message
    if user_answer != answer:
        points_awarded *= -1# points deducted from score if user is incorrect
        terminal_output(f"Incorrect. {points_awarded} points.")
    else:
        terminal_output(f"Correct! {points_awarded} points!")
    
    #updates score and triggers animations
    update_all(game.score + points_awarded)

#win/lose message
if game.score >= game.SCORE_GOAL:
    terminal_output("CONGRATS! YOU WIN!")
if game.score < 0:
    terminal_output("Sorry, you lose!")


drawly.done()