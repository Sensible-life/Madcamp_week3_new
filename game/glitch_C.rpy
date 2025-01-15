###############    침착맨    ###############
label show_C_happy:
    if like_C >= 40:
        show C_happy at left, fade_in:
            zoom 0.75
    else:
        show ChimChak_happy at left, fade_in:
            zoom 0.75
    return

label hide_C_happy:
    if like_C >= 40:
        hide C_happy
    else:
        hide ChimChak_happy
    return

label show_C_excited:
    if like_C >= 40:
        show C_excited at left, fade_in:
            zoom 0.75
    else:
        show ChimChak_excited at left, fade_in:
            zoom 0.75
    return

label hide_C_excited:
    if like_C >= 40:
        hide C_excited
    else:
        hide ChimChak_excited
    return

label show_C_sad:
    if like_C >= 40:
        show C_sad at left, fade_in:
            zoom 0.75
    else:
        show ChimChak_sad at left, fade_in:
            zoom 0.75
    return

label hide_C_sad:
    if like_C >= 40:
        hide C_sad
    else:
        hide ChimChak_sad
    return

label show_C_angry:
    if like_C >= 40:
        show C_angry at left, fade_in:
            zoom 0.75
    else:
        show ChimChak_angry at left, fade_in:
            zoom 0.75
    return

label hide_C_angry:
    if like_C >= 40:
        hide C_angry
    else:
        hide ChimChak_angry
    
    return

label show_C_surprised:
    if like_C >= 40:
        show C_surprised at left, fade_in:
            zoom 0.75
    else:
        show ChimChak_surprised at left, fade_in:
            zoom 0.75
    return

label hide_C_surprised:
    if like_C >= 40:
        hide C_surprised
    else:
        hide ChimChak_surprised
    return

label show_C_q:
    if like_C >= 40:
        show C_q at left, fade_in:
            zoom 0.75
    else:
        show ChimChak_q at left, fade_in:
            zoom 0.75
    return

label hide_C_q:
    if like_C >= 40:
        hide C_q
    else:
        hide ChimChak_q
    return

label glitch_C_happy:
    call hide_C_happy from _call_hide_C_happy_19
    show glitch_C_happy at left:
        zoom 0.75
    with vpunch  # 화면 흔들림 효과 추가
    pause 0.25  # 지직거림 표시 시간
    hide glitch_C_happy

    show glitch_C_happy at left:
        zoom 0.75
    with vpunch  # 화면 흔들림 효과 추가
    pause 0.25  # 지직거림 표시 시간
    hide glitch_C_happy

    show glitch_ChimChak_happy at left:
        zoom 0.75
    with vpunch  # 화면 흔들림 효과 추가
    pause 0.25  # 지직거림 표시 시간
    hide glitch_ChimChak_happy

    show glitch_ChimChak_happy at left:
        zoom 0.75
    with vpunch  # 화면 흔들림 효과 추가
    pause 0.25  # 지직거림 표시 시간
    hide glitch_ChimChak_happy

    show ChimChak_happy at left, fade_in:
        zoom 0.75
    return

label glitch_C_excited:
    call hide_C_excited from _call_hide_C_excited_7
    show glitch_C_excited at left:
        zoom 0.75
    with vpunch  # 화면 흔들림 효과 추가
    pause 0.25  # 지직거림 표시 시간
    hide glitch_C_excited

    show glitch_C_excited at left:
        zoom 0.75
    with vpunch  # 화면 흔들림 효과 추가
    pause 0.25  # 지직거림 표시 시간
    hide glitch_C_excited

    show glitch_ChimChak_excited at left:
        zoom 0.75
    with vpunch  # 화면 흔들림 효과 추가
    pause 0.25  # 지직거림 표시 시간
    hide glitch_ChimChak_excited

    show glitch_ChimChak_excited at left:
        zoom 0.75
    with vpunch  # 화면 흔들림 효과 추가
    pause 0.25  # 지직거림 표시 시간
    hide glitch_ChimChak_excited

    show ChimChak_excited at left, fade_in:
        zoom 0.75
    return


label glitch_C_sad:
    call hide_C_sad from _call_hide_C_sad_6
    show glitch_C_sad at left:
        zoom 0.75
    with vpunch  # 화면 흔들림 효과 추가
    pause 0.25  # 지직거림 표시 시간
    hide glitch_C_sad

    show glitch_C_sad at left:
        zoom 0.75
    with vpunch  # 화면 흔들림 효과 추가
    pause 0.25  # 지직거림 표시 시간
    hide glitch_C_sad

    show glitch_ChimChak_sad at left:
        zoom 0.75
    with vpunch  # 화면 흔들림 효과 추가
    pause 0.25  # 지직거림 표시 시간
    hide glitch_ChimChak_sad

    show glitch_ChimChak_sad at left:
        zoom 0.75
    with vpunch  # 화면 흔들림 효과 추가
    pause 0.25  # 지직거림 표시 시간
    hide glitch_ChimChak_sad

    show ChimChak_sad at left, fade_in:
        zoom 0.75
    return

label glitch_C_angry:
    call hide_C_angry from _call_hide_C_angry_16
    show glitch_C_angry at left:
        zoom 0.75
    with vpunch  # 화면 흔들림 효과 추가
    pause 0.25  # 지직거림 표시 시간
    hide glitch_C_angry

    show glitch_C_angry at left:
        zoom 0.75
    with vpunch  # 화면 흔들림 효과 추가
    pause 0.25  # 지직거림 표시 시간
    hide glitch_C_angry

    show glitch_ChimChak_angry at left:
        zoom 0.75
    with vpunch  # 화면 흔들림 효과 추가
    pause 0.25  # 지직거림 표시 시간
    hide glitch_ChimChak_angry

    show glitch_ChimChak_angry at left:
        zoom 0.75
    with vpunch  # 화면 흔들림 효과 추가
    pause 0.25  # 지직거림 표시 시간
    hide glitch_ChimChak_angry

    show ChimChak_angry at left, fade_in:
        zoom 0.75
    return

label glitch_C_surprised:
    call hide_C_surprised from _call_hide_C_surprised_2
    show glitch_C_surprised at left:
        zoom 0.75
    with vpunch  # 화면 흔들림 효과 추가
    pause 0.25  # 지직거림 표시 시간
    hide glitch_C_surprised

    show glitch_C_surprised at left:
        zoom 0.75
    with vpunch  # 화면 흔들림 효과 추가
    pause 0.25  # 지직거림 표시 시간
    hide glitch_C_surprised

    show glitch_ChimChak_surprised at left:
        zoom 0.75
    with vpunch  # 화면 흔들림 효과 추가
    pause 0.25  # 지직거림 표시 시간
    hide glitch_ChimChak_surprised

    show glitch_ChimChak_surprised at left:
        zoom 0.75
    with vpunch  # 화면 흔들림 효과 추가
    pause 0.25  # 지직거림 표시 시간
    hide glitch_ChimChak_surprised

    show ChimChak_surprised at left, fade_in:
        zoom 0.75
    return

label glitch_C_q:
    call hide_C_q from _call_hide_C_q_4
    show glitch_C_q at left:
        zoom 0.75
    with vpunch  # 화면 흔들림 효과 추가
    pause 0.25  # 지직거림 표시 시간
    hide glitch_C_q

    show glitch_C_q at left:
        zoom 0.75
    with vpunch  # 화면 흔들림 효과 추가
    pause 0.25  # 지직거림 표시 시간
    hide glitch_C_q

    show glitch_ChimChak_q at left:
        zoom 0.75
    with vpunch  # 화면 흔들림 효과 추가
    pause 0.25  # 지직거림 표시 시간
    hide glitch_ChimChak_q

    show glitch_ChimChak_q at left:
        zoom 0.75
    with vpunch  # 화면 흔들림 효과 추가
    pause 0.25  # 지직거림 표시 시간
    hide glitch_ChimChak_q

    show ChimChak_q at left, fade_in:
        zoom 0.75
    return