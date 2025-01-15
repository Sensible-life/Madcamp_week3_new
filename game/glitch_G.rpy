label show_G_happy:
    if like_G >= 50:
        show G_happy at right, fade_in:
            zoom 0.75
    else:
        show Gdo_happy at right, fade_in:
            zoom 0.75
    return

label hide_G_happy:
    if like_G >= 50:
        hide G_happy
    else:
        hide Gdo_happy
    return

label show_G_excited:
    if like_G >= 50:
        show G_excited at right, fade_in:
            zoom 0.75
    else:
        show Gdo_excited at right, fade_in:
            zoom 0.75
    return

label hide_G_excited:
    if like_G >= 50:
        hide G_excited
    else:
        hide Gdo_excited
    return

label show_G_sad:
    if like_G >= 50:
        show G_sad at right, fade_in:
            zoom 0.75
    else:
        show Gdo_sad at right, fade_in:
            zoom 0.75
    return

label hide_G_sad:
    if like_G >= 50:
        hide G_sad
    else:
        hide Gdo_sad
    return

label show_G_angry:
    if like_G >= 50:
        show G_angry at right, fade_in:
            zoom 0.75
    else:
        show Gdo_angry at right, fade_in:
            zoom 0.75
    return

label hide_G_angry:
    if like_G >= 50:
        hide G_angry
    else:
        hide Gdo_angry
    
    return

label show_G_outside:
    if like_G >= 50:
        show G_outside at right, fade_in:
            zoom 0.75
    else:
        show Gdo_outside at right, fade_in:
            zoom 0.75
    return

label hide_G_outside:
    if like_G >= 50:
        hide G_outside
    else:
        hide Gdo_outside
    return

label glitch_G_happy:
    call hide_G_happy from _call_hide_G_happy_13
    show glitch_G_happy at right:
        zoom 0.75
    with vpunch  # 화면 흔들림 효과 추가
    pause 0.25  # 지직거림 표시 시간
    hide glitch_G_happy

    show glitch_G_happy at right:
        zoom 0.75
    with vpunch  # 화면 흔들림 효과 추가
    pause 0.25  # 지직거림 표시 시간
    hide glitch_G_happy

    show glitch_Gdo_happy at right:
        zoom 0.75
    with vpunch  # 화면 흔들림 효과 추가
    pause 0.25  # 지직거림 표시 시간
    hide glitch_Gdo_happy

    show glitch_Gdo_happy at right:
        zoom 0.75
    with vpunch  # 화면 흔들림 효과 추가
    pause 0.25  # 지직거림 표시 시간
    hide glitch_Gdo_happy

    show Gdo_happy at right, fade_in:
        zoom 0.75
    return

label glitch_G_excited:
    call hide_G_excited from _call_hide_G_excited_1
    show glitch_G_excited at right:
        zoom 0.75
    with vpunch  # 화면 흔들림 효과 추가
    pause 0.25  # 지직거림 표시 시간
    hide glitch_G_excited

    show glitch_G_excited at right:
        zoom 0.75
    with vpunch  # 화면 흔들림 효과 추가
    pause 0.25  # 지직거림 표시 시간
    hide glitch_G_excited

    show glitch_Gdo_excited at right:
        zoom 0.75
    with vpunch  # 화면 흔들림 효과 추가
    pause 0.25  # 지직거림 표시 시간
    hide glitch_Gdo_excited

    show glitch_Gdo_excited at right:
        zoom 0.75
    with vpunch  # 화면 흔들림 효과 추가
    pause 0.25  # 지직거림 표시 시간
    hide glitch_Gdo_excited

    show Gdo_excited at right, fade_in:
        zoom 0.75
    return


label glitch_G_sad:
    call hide_G_sad from _call_hide_G_sad_4
    show glitch_G_sad at right:
        zoom 0.75
    with vpunch  # 화면 흔들림 효과 추가
    pause 0.25  # 지직거림 표시 시간
    hide glitch_G_sad

    show glitch_G_sad at right:
        zoom 0.75
    with vpunch  # 화면 흔들림 효과 추가
    pause 0.25  # 지직거림 표시 시간
    hide glitch_G_sad

    show glitch_Gdo_sad at right:
        zoom 0.75
    with vpunch  # 화면 흔들림 효과 추가
    pause 0.25  # 지직거림 표시 시간
    hide glitch_Gdo_sad

    show glitch_Gdo_sad at right:
        zoom 0.75
    with vpunch  # 화면 흔들림 효과 추가
    pause 0.25  # 지직거림 표시 시간
    hide glitch_Gdo_sad

    show Gdo_sad at right, fade_in:
        zoom 0.75
    return

label glitch_G_angry:
    call hide_G_angry from _call_hide_G_angry_4
    show glitch_G_angry at right:
        zoom 0.75
    with vpunch  # 화면 흔들림 효과 추가
    pause 0.25  # 지직거림 표시 시간
    hide glitch_G_angry

    show glitch_G_angry at right:
        zoom 0.75
    with vpunch  # 화면 흔들림 효과 추가
    pause 0.25  # 지직거림 표시 시간
    hide glitch_G_angry

    show glitch_Gdo_angry at right:
        zoom 0.75
    with vpunch  # 화면 흔들림 효과 추가
    pause 0.25  # 지직거림 표시 시간
    hide glitch_Gdo_angry

    show glitch_Gdo_angry at right:
        zoom 0.75
    with vpunch  # 화면 흔들림 효과 추가
    pause 0.25  # 지직거림 표시 시간
    hide glitch_Gdo_angry

    show Gdo_angry at right, fade_in:
        zoom 0.75
    return


label glitch_G_outside:
    call hide_G_outside from _call_hide_G_outside_2
    show glitch_G_outside at right:
        zoom 0.75
    with vpunch  # 화면 흔들림 효과 추가
    pause 0.25  # 지직거림 표시 시간
    hide glitch_G_outside

    show glitch_G_outside at right:
        zoom 0.75
    with vpunch  # 화면 흔들림 효과 추가
    pause 0.25  # 지직거림 표시 시간
    hide glitch_G_outside

    show glitch_Gdo_outside at right:
        zoom 0.75
    with vpunch  # 화면 흔들림 효과 추가
    pause 0.25  # 지직거림 표시 시간
    hide glitch_Gdo_outside

    show glitch_Gdo_outside at right:
        zoom 0.75
    with vpunch  # 화면 흔들림 효과 추가
    pause 0.25  # 지직거림 표시 시간
    hide glitch_Gdo_outside

    show Gdo_outside at right, fade_in:
        zoom 0.75
    return