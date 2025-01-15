label show_J2_happy:
    if like_J2 >= 40:
        show J2_happy at left, fade_in:
            zoom 0.75
    else:
        show JooWoo_happy at left, fade_in:
            zoom 0.75
    return

label hide_J2_happy:
    if like_J2 >= 40:
        hide J2_happy
    else:
        hide JooWoo_happy
    return

label show_J2_excited:
    if like_J2 >= 40:
        show J2_excited at left, fade_in:
            zoom 0.75
    else:
        show JooWoo_excited at left, fade_in:
            zoom 0.75
    return

label hide_J2_excited:
    if like_J2 >= 40:
        hide J2_excited
    else:
        hide JooWoo_excited
    return

label show_J2_sad:
    if like_J2 >= 40:
        show J2_sad at left, fade_in:
            zoom 0.75
    else:
        show JooWoo_sad at left, fade_in:
            zoom 0.75
    return

label hide_J2_sad:
    if like_J2 >= 40:
        hide J2_sad
    else:
        hide JooWoo_sad
    return

label show_J2_surprised:
    if like_J2 >= 40:
        show J2_surprised at left, fade_in:
            zoom 0.75
    else:
        show JooWoo_surprised at left, fade_in:
            zoom 0.75
    return

label hide_J2_surprised:
    if like_J2 >= 40:
        hide J2_surprised
    else:
        hide JooWoo_surprised
    return

label show_J2_q:
    if like_J2 >= 40:
        show J2_q at left, fade_in:
            zoom 0.75
    else:
        show JooWoo_q at left, fade_in:
            zoom 0.75
    return

label hide_J2_q:
    if like_J2 >= 40:
        hide J2_q
    else:
        hide JooWoo_q
    return

label glitch_J2_happy:
    call hide_J2_happy from _call_hide_J2_happy_9
    show glitch_J2_happy at left:
        zoom 0.75
    with vpunch  # 화면 흔들림 효과 추가
    pause 0.25  # 지직거림 표시 시간
    hide glitch_J2_happy

    show glitch_J2_happy at left:
        zoom 0.75
    with vpunch  # 화면 흔들림 효과 추가
    pause 0.25  # 지직거림 표시 시간
    hide glitch_J2_happy

    show glitch_JooWoo_happy at left:
        zoom 0.75
    with vpunch  # 화면 흔들림 효과 추가
    pause 0.25  # 지직거림 표시 시간
    hide glitch_JooWoo_happy

    show glitch_JooWoo_happy at left:
        zoom 0.75
    with vpunch  # 화면 흔들림 효과 추가
    pause 0.25  # 지직거림 표시 시간
    hide glitch_JooWoo_happy

    show JooWoo_happy at left, fade_in:
        zoom 0.75
    return

label glitch_J2_excited:
    call hide_J2_excited from _call_hide_J2_excited_5
    show glitch_J2_excited at left:
        zoom 0.75
    with vpunch  # 화면 흔들림 효과 추가
    pause 0.25  # 지직거림 표시 시간
    hide glitch_J2_excited

    show glitch_J2_excited at left:
        zoom 0.75
    with vpunch  # 화면 흔들림 효과 추가
    pause 0.25  # 지직거림 표시 시간
    hide glitch_J2_excited

    show glitch_JooWoo_excited at left:
        zoom 0.75
    with vpunch  # 화면 흔들림 효과 추가
    pause 0.25  # 지직거림 표시 시간
    hide glitch_JooWoo_excited

    show glitch_JooWoo_excited at left:
        zoom 0.75
    with vpunch  # 화면 흔들림 효과 추가
    pause 0.25  # 지직거림 표시 시간
    hide glitch_JooWoo_excited

    show JooWoo_excited at left, fade_in:
        zoom 0.75
    return


label glitch_J2_sad:
    call hide_J2_sad from _call_hide_J2_sad_7
    show glitch_J2_sad at left:
        zoom 0.75
    with vpunch  # 화면 흔들림 효과 추가
    pause 0.25  # 지직거림 표시 시간
    hide glitch_J2_sad

    show glitch_J2_sad at left:
        zoom 0.75
    with vpunch  # 화면 흔들림 효과 추가
    pause 0.25  # 지직거림 표시 시간
    hide glitch_J2_sad

    show glitch_JooWoo_sad at left:
        zoom 0.75
    with vpunch  # 화면 흔들림 효과 추가
    pause 0.25  # 지직거림 표시 시간
    hide glitch_JooWoo_sad

    show glitch_JooWoo_sad at left:
        zoom 0.75
    with vpunch  # 화면 흔들림 효과 추가
    pause 0.25  # 지직거림 표시 시간
    hide glitch_JooWoo_sad

    show JooWoo_sad at left, fade_in:
        zoom 0.75
    return

label glitch_J2_surprised:
    call hide_J2_surprised from _call_hide_J2_surprised
    show glitch_J2_surprised at left:
        zoom 0.75
    with vpunch  # 화면 흔들림 효과 추가
    pause 0.25  # 지직거림 표시 시간
    hide glitch_J2_surprised

    show glitch_J2_surprised at left:
        zoom 0.75
    with vpunch  # 화면 흔들림 효과 추가
    pause 0.25  # 지직거림 표시 시간
    hide glitch_J2_surprised

    show glitch_JooWoo_surprised at left:
        zoom 0.75
    with vpunch  # 화면 흔들림 효과 추가
    pause 0.25  # 지직거림 표시 시간
    hide glitch_JooWoo_surprised

    show glitch_JooWoo_surprised at left:
        zoom 0.75
    with vpunch  # 화면 흔들림 효과 추가
    pause 0.25  # 지직거림 표시 시간
    hide glitch_JooWoo_surprised

    show JooWoo_surprised at left, fade_in:
        zoom 0.75
    return

label glitch_J2_q:
    call hide_J2_q from _call_hide_J2_q
    show glitch_J2_q at left:
        zoom 0.75
    with vpunch  # 화면 흔들림 효과 추가
    pause 0.25  # 지직거림 표시 시간
    hide glitch_J2_q

    show glitch_J2_q at left:
        zoom 0.75
    with vpunch  # 화면 흔들림 효과 추가
    pause 0.25  # 지직거림 표시 시간
    hide glitch_J2_q

    show glitch_JooWoo_q at left:
        zoom 0.75
    with vpunch  # 화면 흔들림 효과 추가
    pause 0.25  # 지직거림 표시 시간
    hide glitch_JooWoo_q

    show glitch_JooWoo_q at left:
        zoom 0.75
    with vpunch  # 화면 흔들림 효과 추가
    pause 0.25  # 지직거림 표시 시간
    hide glitch_JooWoo_q

    show JooWoo_q at left, fade_in:
        zoom 0.75
    return