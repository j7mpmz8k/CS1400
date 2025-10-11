# Jacob Cardon
# CS1400 - MWF - 8:30am
import drawly, random
from drawly import set_color, draw, rectangle, text
from time import time

def update_score(new_score:int=0):
    game.score = new_score
    #scoreboard background
    set_color(sb.BG)
    rectangle(x_pos=sb.X, y_pos=sb.Y, width=sb.W, height=sb.H)
    #scoreboard text
    set_color(sb.FG)
    sb.score = max(0, min(game.score, game.SCORE_GOAL))
    text(x_pos=sb.TEXT_X, y_pos=sb.TEXT_Y, text=f"Score: {sb.score}", size=sb.SIZE)
    draw()


def update_meter(start: int, target: int):
    diff = target - start

    for frame in range(1, meter.FRAMES + 1):
        # meter background
        set_color(meter.BG)
        rectangle(x_pos=meter.X, y_pos=meter.Y, width=meter.W, height=meter.H)

        # frame_slice_modifier finds fraction to incrementally change animation per frame (e.g., 0.2, 0.4, 0.6, 0.8, 1.0)
        frame_slice_modifier = frame / meter.FRAMES

        # animated_score extracts current set of slices from the difference of change in scores
        # ...then adds the sliced difference of change to the start
        animated_score = start + diff * frame_slice_modifier

        if animated_score >= 0:
            green_height = meter.H / game.SCORE_GOAL * animated_score
            top_of_green = meter.Y + meter.H - green_height
            if game.score - game.prev_score >= 0:
                set_color(meter.CORRECT)
            else:
                set_color(meter.WRONG)
            rectangle(x_pos=meter.X, y_pos=top_of_green, width=meter.W, height=green_height)
            draw()

def update_all(new_score: int = 0):
    game.prev_score = game.score
    diff = int(new_score - game.prev_score)
    counter = game.prev_score
    if diff == 0:
        current_start = max(0, min(counter, game.SCORE_GOAL))
        current_target = max(0, min(new_score, game.SCORE_GOAL))
        update_score(new_score)
        update_meter(current_start, current_target)
        return  # Exit early to skip the loop
    for increment in range(abs(diff)):
        current_start = max(0, min(counter, game.SCORE_GOAL))
        counter += diff // abs(diff)
        current_target = max(0, min(counter, game.SCORE_GOAL))
        update_score(counter)
        update_meter(current_start, current_target)
        game.prev_score = counter


class Game:
    pass

game = Game()
game.SPEED = 10
game.SCREEN_WIDTH = 720
game.SCREEN_HEIGHT = 720
game.SCORE_GOAL = 10
game.POINT_LIST = [5, 4, 3, 2, 1]
game.score = 0
game.prev_score = 0  # Added to track previous score for animation


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

drawly.start(title="Don't Play With Mathes", dimensions = (720, 720), background="grey", terminal = True, terminal_lines = 5, terminal_line_height=20)
drawly.set_speed(game.SPEED)

#initialization
update_all(0)

drawly.terminal_output("DON'T PLAY WITH MATHES")
drawly.terminal_output("Earn points for correct answers and lose points for wrong ones.")
drawly.terminal_output("Answer quickly to earn (or lose) more points.")
drawly.terminal_input("   [Press 'Enter' to Start] ")

#scoreboard
while 0 <= game.score <= game.SCORE_GOAL:

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

    start = time()
    user_answer = int(drawly.terminal_input(problem_str))  # Renamed variable for clarity
    end = time()
    points_awarded = game.POINT_LIST[min(int((end - start) // 1), 4)]
    if user_answer != answer:
        points_awarded *= -1
        drawly.terminal_output(f"Incorrect. {points_awarded} points.")
    else:
        drawly.terminal_output(f"Correct! {points_awarded} points!")
    print(game.score, points_awarded)
    update_all(game.score + points_awarded)

if game.score >= game.SCORE_GOAL:
    drawly.terminal_output("CONGRATS! YOU WIN!")
if game.score < 0:
    drawly.terminal_output("Sorry, you lose!")


drawly.done()