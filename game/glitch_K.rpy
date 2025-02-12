label show_K_happy:
    if like_K >= 45:
        show K_happy at right, fade_in:
            zoom 0.75
    else:
        show KPoong_happy at right, fade_in:
            zoom 0.75
    return

label hide_K_happy:
    if like_K >= 45:
        hide K_happy
    else:
        hide KPoong_happy
    return

label show_K_excited:
    if like_K >= 45:
        show K_excited at right, fade_in:
            zoom 0.75
    else:
        show KPoong_excited at right, fade_in:
            zoom 0.75
    return

label hide_K_excited:
    if like_K >= 45:
        hide K_excited
    else:
        hide KPoong_excited
    return

label show_K_nervous:
    if like_K >= 45:
        show K_nervous at right, fade_in:
            zoom 0.75
    else:
        show KPoong_nervous at right, fade_in:
            zoom 0.75
    return

label hide_K_nervous:
    if like_K >= 45:
        hide K_nervous
    else:
        hide KPoong_nervous
    return

label glitch_K_happy:
    call hide_K_happy from _call_hide_K_happy_13
    show glitch_K_happy at right:
        zoom 0.75
    with vpunch  # 화면 흔들림 효과 추가
    pause 0.25  # 지직거림 표시 시간
    hide glitch_K_happy

    show glitch_K_happy at right:
        zoom 0.75
    with vpunch  # 화면 흔들림 효과 추가
    pause 0.25  # 지직거림 표시 시간
    hide glitch_K_happy

    show glitch_KPoong_happy at right:
        zoom 0.75
    with vpunch  # 화면 흔들림 효과 추가
    pause 0.25  # 지직거림 표시 시간
    hide glitch_KPoong_happy

    show glitch_KPoong_happy at right:
        zoom 0.75
    with vpunch  # 화면 흔들림 효과 추가
    pause 0.25  # 지직거림 표시 시간
    hide glitch_KPoong_happy

    show KPoong_happy at right, fade_in:
        zoom 0.75
    return

label glitch_K_excited:
    call hide_K_excited from _call_hide_K_excited_4
    show glitch_K_excited at right:
        zoom 0.75
    with vpunch  # 화면 흔들림 효과 추가
    pause 0.25  # 지직거림 표시 시간
    hide glitch_K_excited

    show glitch_K_excited at right:
        zoom 0.75
    with vpunch  # 화면 흔들림 효과 추가
    pause 0.25  # 지직거림 표시 시간
    hide glitch_K_excited
    
    show glitch_KPoong_excited at right:
        zoom 0.75
    with vpunch  # 화면 흔들림 효과 추가
    pause 0.25  # 지직거림 표시 시간
    hide glitch_KPoong_excited

    show glitch_KPoong_excited at right:
        zoom 0.75
    with vpunch  # 화면 흔들림 효과 추가
    pause 0.25  # 지직거림 표시 시간
    hide glitch_KPoong_excited

    show KPoong_excited at right, fade_in:
        zoom 0.75
    return

label glitch_K_nervous:
    call hide_K_nervous from _call_hide_K_nervous_5
    show glitch_K_nervous at right:
        zoom 0.75
    with vpunch  # 화면 흔들림 효과 추가
    pause 0.25  # 지직거림 표시 시간
    hide glitch_K_nervous
    
    show glitch_K_nervous at right:
        zoom 0.75
    with vpunch  # 화면 흔들림 효과 추가
    pause 0.25  # 지직거림 표시 시간
    hide glitch_K_nervous

    show glitch_KPoong_nervous at right:
        zoom 0.75
    with vpunch  # 화면 흔들림 효과 추가
    pause 0.25  # 지직거림 표시 시간
    hide glitch_KPoong_nervous

    show glitch_KPoong_nervous at right:
        zoom 0.75
    with vpunch  # 화면 흔들림 효과 추가
    pause 0.25  # 지직거림 표시 시간
    hide glitch_KPoong_nervous

    show KPoong_nervous at right, fade_in:
        zoom 0.75
    return

