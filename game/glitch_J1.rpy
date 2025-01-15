###############    침착맨    ###############
label show_J1_happy:
    if like_J1 >= 50:
        show J1_happy at right, fade_in:
            zoom 0.75
    else:
        show Jooperl_happy at right, fade_in:
            zoom 0.75
    return

label hide_J1_happy:
    if like_J1 >= 50:
        hide J1_happy
    else:
        hide Jooperl_happy
    return

label show_J1_excited:
    if like_J1 >= 50:
        show J1_excited at right, fade_in:
            zoom 0.75
    else:
        show Jooperl_excited at right, fade_in:
            zoom 0.75
    return

label hide_J1_excited:
    if like_J1 >= 50:
        hide J1_excited
    else:
        hide Jooperl_excited
    return

label show_J1_sad:
    if like_J1 >= 50:
        show J1_sad at right, fade_in:
            zoom 0.75
    else:
        show Jooperl_sad at right, fade_in:
            zoom 0.75
    return

label hide_J1_sad:
    if like_J1 >= 50:
        hide J1_sad
    else:
        hide Jooperl_sad
    return

label show_J1_angry:
    if like_J1 >= 50:
        show J1_angry at right, fade_in:
            zoom 0.75
    else:
        show Jooperl_angry at right, fade_in:
            zoom 0.75
    return

label hide_J1_angry:
    if like_J1 >= 50:
        hide J1_angry
    else:
        hide Jooperl_angry
    
    return

label show_J1_surprised:
    if like_J1 >= 50:
        show J1_surprised at right, fade_in:
            zoom 0.75
    else:
        show Jooperl_surprised at right, fade_in:
            zoom 0.75
    return

label hide_J1_surprised:
    if like_J1 >= 50:
        hide J1_surprised
    else:
        hide Jooperl_surprised
    return

label show_J1_q:
    if like_J1 >= 50:
        show J1_q at right, fade_in:
            zoom 0.75
    else:
        show Jooperl_q at right, fade_in:
            zoom 0.75
    return

label hide_J1_q:
    if like_J1 >= 50:
        hide J1_q
    else:
        hide Jooperl_q
    return

label glitch_J1_happy:
    call hide_J1_happy from _call_hide_J1_happy_14
    show glitch_J1_happy at right:
        zoom 0.75
    with vpunch  # 화면 흔들림 효과 추가
    pause 0.25  # 지직거림 표시 시간
    hide glitch_J1_happy

    show glitch_J1_happy at right:
        zoom 0.75
    with vpunch  # 화면 흔들림 효과 추가
    pause 0.25  # 지직거림 표시 시간
    hide glitch_J1_happy

    show glitch_Jooperl_happy at right:
        zoom 0.75
    with vpunch  # 화면 흔들림 효과 추가
    pause 0.25  # 지직거림 표시 시간
    hide glitch_Jooperl_happy

    show glitch_Jooperl_happy at right:
        zoom 0.75
    with vpunch  # 화면 흔들림 효과 추가
    pause 0.25  # 지직거림 표시 시간
    hide glitch_Jooperl_happy

    show Jooperl_happy at right, fade_in:
        zoom 0.75
    return

label glitch_J1_happy_left:
    call hide_J1_happy from _call_hide_J1_happy_15
    show glitch_J1_happy at left:
        zoom 0.75
    with vpunch  # 화면 흔들림 효과 추가
    pause 0.25  # 지직거림 표시 시간
    hide glitch_J1_happy

    show glitch_J1_happy at left:
        zoom 0.75
    with vpunch  # 화면 흔들림 효과 추가
    pause 0.25  # 지직거림 표시 시간
    hide glitch_J1_happy

    show glitch_Jooperl_happy at left:
        zoom 0.75
    with vpunch  # 화면 흔들림 효과 추가
    pause 0.25  # 지직거림 표시 시간
    hide glitch_Jooperl_happy

    show glitch_Jooperl_happy at left:
        zoom 0.75
    with vpunch  # 화면 흔들림 효과 추가
    pause 0.25  # 지직거림 표시 시간
    hide glitch_Jooperl_happy

    show Jooperl_happy at left, fade_in:
        zoom 0.75
    return

label glitch_J1_excited:
    call hide_J1_excited from _call_hide_J1_excited_7
    show glitch_J1_excited at right:
        zoom 0.75
    with vpunch  # 화면 흔들림 효과 추가
    pause 0.25  # 지직거림 표시 시간
    hide glitch_J1_excited

    show glitch_J1_excited at right:
        zoom 0.75
    with vpunch  # 화면 흔들림 효과 추가
    pause 0.25  # 지직거림 표시 시간
    hide glitch_J1_excited

    show glitch_Jooperl_excited at right:
        zoom 0.75
    with vpunch  # 화면 흔들림 효과 추가
    pause 0.25  # 지직거림 표시 시간
    hide glitch_Jooperl_excited

    show glitch_Jooperl_excited at right:
        zoom 0.75
    with vpunch  # 화면 흔들림 효과 추가
    pause 0.25  # 지직거림 표시 시간
    hide glitch_Jooperl_excited

    show Jooperl_excited at right, fade_in:
        zoom 0.75
    return


label glitch_J1_sad:
    call hide_J1_sad from _call_hide_J1_sad_4
    show glitch_J1_sad at right:
        zoom 0.75
    with vpunch  # 화면 흔들림 효과 추가
    pause 0.25  # 지직거림 표시 시간
    hide glitch_J1_sad

    show glitch_J1_sad at right:
        zoom 0.75
    with vpunch  # 화면 흔들림 효과 추가
    pause 0.25  # 지직거림 표시 시간
    hide glitch_J1_sad

    show glitch_Jooperl_sad at right:
        zoom 0.75
    with vpunch  # 화면 흔들림 효과 추가
    pause 0.25  # 지직거림 표시 시간
    hide glitch_Jooperl_sad

    show glitch_Jooperl_sad at right:
        zoom 0.75
    with vpunch  # 화면 흔들림 효과 추가
    pause 0.25  # 지직거림 표시 시간
    hide glitch_Jooperl_sad

    show Jooperl_sad at right, fade_in:
        zoom 0.75
    return

label glitch_J1_angry:
    call hide_J1_angry from _call_hide_J1_angry_5
    show glitch_J1_angry at right:
        zoom 0.75
    with vpunch  # 화면 흔들림 효과 추가
    pause 0.25  # 지직거림 표시 시간
    hide glitch_J1_angry

    show glitch_J1_angry at right:
        zoom 0.75
    with vpunch  # 화면 흔들림 효과 추가
    pause 0.25  # 지직거림 표시 시간
    hide glitch_J1_angry

    show glitch_Jooperl_angry at right:
        zoom 0.75
    with vpunch  # 화면 흔들림 효과 추가
    pause 0.25  # 지직거림 표시 시간
    hide glitch_Jooperl_angry

    show glitch_Jooperl_angry at right:
        zoom 0.75
    with vpunch  # 화면 흔들림 효과 추가
    pause 0.25  # 지직거림 표시 시간
    hide glitch_Jooperl_angry

    show Jooperl_angry at right, fade_in:
        zoom 0.75
    return

label glitch_J1_surprised:
    call hide_J1_surprised from _call_hide_J1_surprised_1
    show glitch_J1_surprised at right:
        zoom 0.75
    with vpunch  # 화면 흔들림 효과 추가
    pause 0.25  # 지직거림 표시 시간
    hide glitch_J1_surprised

    show glitch_J1_surprised at right:
        zoom 0.75
    with vpunch  # 화면 흔들림 효과 추가
    pause 0.25  # 지직거림 표시 시간
    hide glitch_J1_surprised

    show glitch_Jooperl_surprised at right:
        zoom 0.75
    with vpunch  # 화면 흔들림 효과 추가
    pause 0.25  # 지직거림 표시 시간
    hide glitch_Jooperl_surprised

    show glitch_Jooperl_surprised at right:
        zoom 0.75
    with vpunch  # 화면 흔들림 효과 추가
    pause 0.25  # 지직거림 표시 시간
    hide glitch_Jooperl_surprised

    show Jooperl_surprised at right, fade_in:
        zoom 0.75
    return

label glitch_J1_q:
    call hide_J1_q from _call_hide_J1_q_7
    show glitch_J1_q at right:
        zoom 0.75
    with vpunch  # 화면 흔들림 효과 추가
    pause 0.25  # 지직거림 표시 시간
    hide glitch_J1_q

    show glitch_J1_q at right:
        zoom 0.75
    with vpunch  # 화면 흔들림 효과 추가
    pause 0.25  # 지직거림 표시 시간
    hide glitch_J1_q

    show glitch_Jooperl_q at right:
        zoom 0.75
    with vpunch  # 화면 흔들림 효과 추가
    pause 0.25  # 지직거림 표시 시간
    hide glitch_Jooperl_q

    show glitch_Jooperl_q at right:
        zoom 0.75
    with vpunch  # 화면 흔들림 효과 추가
    pause 0.25  # 지직거림 표시 시간
    hide glitch_Jooperl_q

    show Jooperl_q at right, fade_in:
        zoom 0.75
    return