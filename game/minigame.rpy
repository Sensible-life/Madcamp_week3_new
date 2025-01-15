init:
    $ found1_left = False
    $ found2_left = False
    $ found3_left = False
    $ found4_left = False
    $ found5_left = False
    $ found1_right = False
    $ found2_right = False
    $ found3_right = False
    $ found4_right = False
    $ found5_right = False

screen differences:
    imagemap:
        ground "images/difference1.png"
        
        # 첫 번째 차이점 (왼쪽 이미지)
        hotspot (92, 185, 100, 100) action [SetVariable("found1_left", True), SetVariable("found1_right", True)]
        # 첫 번째 차이점 (오른쪽 이미지)
        hotspot (1052, 185, 100, 100) action [SetVariable("found1_left", True), SetVariable("found1_right", True)]
        
        # 두 번째 차이점 (왼쪽 이미지)
        hotspot (443, 198, 74, 74) action [SetVariable("found2_left", True), SetVariable("found2_right", True)]
        # 두 번째 차이점 (오른쪽 이미지)
        hotspot (1403, 198, 74, 74) action [SetVariable("found2_left", True), SetVariable("found2_right", True)]

        # 세 번째 차이점 (왼쪽 이미지)
        hotspot (422, 861, 116, 218) action [SetVariable("found3_left", True), SetVariable("found3_right", True)]
        # 세 번째 차이점 (오른쪽 이미지)
        hotspot (1382, 861, 116, 218) action [SetVariable("found3_left", True), SetVariable("found3_right", True)]

        # 네 번째 차이점 (왼쪽 이미지)
        hotspot (108, 1006, 74, 73) action [SetVariable("found4_left", True), SetVariable("found4_right", True)]
        # 네 번째 차이점 (오른쪽 이미지)
        hotspot (1068, 1006, 74, 73) action [SetVariable("found4_left", True), SetVariable("found4_right", True)]

        # 다섯 번째 차이점 (왼쪽 이미지)
        hotspot (774, 967, 74, 74) action [SetVariable("found5_left", True), SetVariable("found5_right", True)]
        # 다섯 번째 차이점 (오른쪽 이미지)
        hotspot (1734, 967, 74, 74) action [SetVariable("found5_left", True), SetVariable("found5_right", True)]
    
    # 첫 번째 차이점 발견 (왼쪽 및 오른쪽 모두)
    if found1_left:
        add "images/circle.png" xpos 92 ypos 185 xsize 100 ysize 100
    if found1_right:
        add "images/circle.png" xpos 1052 ypos 185 xsize 100 ysize 100
    
    # 두 번째 차이점 발견 (왼쪽 및 오른쪽 모두)
    if found2_left:
        add "images/circle.png" xpos 443 ypos 198 xsize 74 ysize 74
    if found2_right:
        add "images/circle.png" xpos 1403 ypos 198 xsize 74 ysize 74

    if found3_left:
        add "images/circle.png" xpos 422 ypos 861 xsize 116 ysize 218
    if found3_right:
        add "images/circle.png" xpos 1382 ypos 861 xsize 116 ysize 218
 
    if found4_left:
        add "images/circle.png" xpos 108 ypos 1020 xsize 74 ysize 73
    if found4_right:
        add "images/circle.png" xpos 1068 ypos 1020 xsize 74 ysize 73

    if found5_left:
        add "images/circle.png" xpos 774 ypos 967 xsize 74 ysize 74
    if found5_right:
        add "images/circle.png" xpos 1734 ypos 967 xsize 74 ysize 74

label minigame:
    # 대사 창 숨기기
    window hide
    show screen differences
    stop music fadeout 1.0
    play music "audio/bgm_minigame_mole.mp3" fadein 1.0 loop
    $ time_left = 90
    $ success = False  # 기본값은 실패로 설정

    while time_left > 0:
        $ renpy.pause(1.0)  # 1초마다 감소
        $ time_left -= 1
        # 모든 차이점을 발견했는지 확인
        if (found1_left and found2_left and found3_left and found4_left and found5_left and
            found1_right and found2_right and found3_right and found4_right and found5_right):
            $ success = True  # 성공으로 변경
            "축하합니다! 모든 차이점을 찾았습니다!"
            window show
            hide screen differences
            return  # 미니게임 종료 후 반환

    # 제한 시간 초과 시 실패 처리
    hide screen differences
    "시간이 초과되었습니다. 다음 기회에 도전하세요!"
    $ success = False  # 실패로 유지
    window show
    return