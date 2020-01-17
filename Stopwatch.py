# "Stopwatch: The Game" by Nick Togneri

import simplegui

# define global variables

counter = 0
score1 = 0
tries = 0
is_timer_running = False

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D

def format(t):
    A = t // 600
    B = ((t / 10) % 60) // 10
    C = ((t /10 % 60) % 10)
    D = t % 10

    return str(A) + ':' + str(B) + str(C) + '.' + str(D)
    
# define event handlers for buttons; "Start", "Stop", "Reset"

def timer_handler():
    global counter
    counter += 1
    
def start_handler():
    global is_timer_running
    is_timer_running = True
    timer.start()

def stop_handler():
    global is_timer_running, counter, score1, tries
    if is_timer_running == False:
        timer.stop()
    else:
        is_timer_running = False
        timer.stop()
        if counter % 50 == 0:
            score1 += 1
        tries += 1

def reset_handler():
    global counter, score1, tries
    timer.stop()
    counter = 0
    score1 = 0
    tries = 0
    
# define event handler for timer with 0.1 sec interval

timer = simplegui.create_timer(100, timer_handler)


# define draw handler

def draw_handler(canvas):
    canvas.draw_text(format(counter), (60, 85), 36, 'Yellow')
    canvas.draw_text((str(score1)) + '/' + (str(tries)) , (160, 20), 24, 'Green')
  
# create frame

frame = simplegui.create_frame('Stop Watch', 200, 150)
button_start = frame.add_button('Start', start_handler, 50)
button_stop = frame.add_button('Stop', stop_handler, 50)
button_reset = frame.add_button('Reset', reset_handler, 50)

# register event handlers

frame.set_draw_handler(draw_handler)

# start frame

frame.start()