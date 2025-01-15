init python:
    import random
    hrzpos = [0.2, 0.5, 0.8]
    vrtpos = [0.2, 0.5, 0.7]
    timer_range = 0
    timer_jump = 0
    your_points = 0
    last_x = 0
    last_y = 0
    hit_x = 0
    hit_y = 0
    game_success = [False]

    if isinstance(persistent.hi_score, int):
        hi_score = persistent.hi_score
    else:
        hi_score = 0

    def mole():
        ui.vbox(xalign=which_h, yalign=which_v)
        ui.imagebutton("mole.png", "mole.png", clicked=ui.returns(True))
        ui.close()

    def not_mole():
        ui.vbox(xalign=which_h, yalign=which_v)
        ui.imagebutton("not-mole.png", "not-mole.png", clicked=ui.returns(True))
        ui.close()

    def score():
        ui.vbox(xalign=0.9, yalign=1.0)
        ui.text("Score: [your_points]")
        ui.text("Misses: [misses]")
        ui.close()

        ui.vbox(xalign=0.1, yalign=1.0)
        ui.text("Hi Score: [hi_score]")
        ui.close()

screen countdown:
    timer 0.01 repeat True action If(time > 0, true=SetVariable('time', time - 0.01), false=[Hide('countdown'), Jump(timer_jump)])

screen mole:
    $ mole()

screen not_mole:
    $ not_mole()

screen score:
    $ score()

label start_game:
    # play music "audio/bgm_minigame_mole.mp3" fadein 1.0 loop
    scene bg_mole
    if is_mole:
        hide screen mole
    else:
        hide screen not_mole

    python:
        time = 1.0
        timer_range = time
        timer_jump = 'menu1'
        hit = False
        if your_points > 3:
            mole_or_not = [True, False, False, False]
        elif your_points > 1:
            mole_or_not = [True, False, False]
        else:
            mole_or_not = [True]
        is_mole = random.choice(mole_or_not)

label menu1:
    hide screen countdown
    show screen score
    if is_mole:
        show screen mole
    else:
        show screen not_mole
    python:
        if your_points > 9:
            time = 0.1
            #time = 1
        elif your_points > 4:
            time = 0.4
            #time = 1
        elif your_points > 1:
            time = 0.7
            #time = 1
        else:
            time = 0.9
        while which_v == hit_y and which_h == hit_x:
            which_h = random.choice(hrzpos)
            which_v = random.choice(vrtpos)
        while which_h == last_x and which_v == last_y:
            which_h = random.choice(hrzpos)
            which_v = random.choice(vrtpos)
        last_x = which_h
        last_y = which_v
        timer_jump = 'start_game'

    show screen countdown
    $ hit = ui.interact()
    if hit:
        if is_mole:
            hide screen mole
        else:
            hide screen not_mole
        jump points

label points:
    python:
        hit_x = which_h
        hit_y = which_v
        time = 0.8
        timer_jump = 'menu1'
        hit = False
    if is_mole:
        $ your_points += 1
        voice "audio/yes.mp3"
        if your_points > 9:
            hide screen countdown
            jump win_game
    else:
        voice "audio/smile.wav"
        $ misses -= 1

        if misses < 1:
            jump fail_game
    call screen score
    show screen countdown
    jump menu1

label win_game:
    hide bg field
    hide screen not_mole
    hide screen countdown
    hide screen score
    scene black
    "수고하셨습니다. 얏호~"
    python:
        game_success = True  # Python 블록 내에서 값을 설정
    
    jump correct_guess

label fail_game:
    hide bg field
    hide screen not_mole
    hide screen countdown
    hide screen score
    scene black
    python:
        game_success = False  # Python 블록 내에서 값을 설정

    "아쉽게도 기회를 놓쳤습니다."
    
    jump failed_guess
return
