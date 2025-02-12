﻿# 이 파일에 게임 스크립트를 입력합니다.

# image 문을 사용해 이미지를 정의합니다.
# image eileen happy = "eileen_happy.png"
init python:
    preferences.text_cps = 20

init python:
    def show_C():
        if like_C <= 30:
            renpy.show("C_happy", at="center")
        else:
            renpy.show("C_angry", at="center")

# 게임에서 사용할 캐릭터를 정의합니다.
define P = Character('플레이어', color="#EEEEEE")
define Who = Character('???', color="#eeff91")
define C = Character('침채린', color="#FF7DC1")
define J1 = Character('주하민', color="#FACD89")
define J2 = Character('주유재', color="#7BE68D")
define G = Character('궤하린', color="#CF64E0")
define K = Character('김솔풍', color="#8CCAFF")
default like_C = 50
default like_J1 = 50
default like_J2 = 50
default like_G = 50
default like_K = 50
# default like_C = 100
# default like_J1 = 100
# default like_J2 = 100
# default like_G = 100
# default like_K = 100
default run = False

image bg_N1 = im.Scale("bg_N1.jpeg", config.screen_width, config.screen_height)
image bg_N1_2 = im.Scale("bg_N1_2.jpeg", config.screen_width, config.screen_height)
image bg_N1_117 = im.Scale("bg_N1_117.jpeg", config.screen_width, config.screen_height)
image bg_N1_outside = im.Scale("bg_N1_outside.jpeg", config.screen_width, config.screen_height)
image bg_cafe = im.Scale("bg_cafe.jpeg", config.screen_width, config.screen_height)
image bg_cafeteria = im.Scale("bg_cafeteria.jpeg", config.screen_width, config.screen_height)
image bg_classroom = im.Scale("bg_classroom.jpeg", config.screen_width, config.screen_height)
image bg_computer = im.Scale("bg_computer.jpeg", config.screen_width, config.screen_height)
image bg_dorm = im.Scale("bg_dorm.jpeg", config.screen_width, config.screen_height)
image bg_dorm2 = im.Scale("bg_dorm2.jpeg", config.screen_width, config.screen_height)
image bg_geese = im.Scale ("bg_geese.jpeg", config.screen_width, config.screen_height)
image bg_night = im.Scale("bg_night.jpeg", config.screen_width, config.screen_height)
image bg_night_park = im.Scale("bg_night_park.jpeg", config.screen_width, config.screen_height)
image bg_sunset = im.Scale("bg_sunset.png", config.screen_width, config.screen_height)
image bg_park = im.Scale("bg_park.jpeg", config.screen_width, config.screen_height)
image bg_poster = im.Scale("bg_poster.jpeg", config.screen_width, config.screen_height)
image bg_laboratory  = im.Scale("bg_laboratory.jpeg", config.screen_width, config.screen_height) 
image bg_laboratory_inside = im.Scale("bg_laboratory_inside.jpg", config.screen_width, config.screen_height)
image bg_mole = im.Scale("moleBG.png", config.screen_width, config.screen_height)
image bg_ch1_end = im.Scale("bg_ch1_end.png", config.screen_width, config.screen_height)
image bg_ch2_end = im.Scale("bg_ch2_end.png", config.screen_width, config.screen_height)
image bg_ch3_end = im.Scale("bg_ch3_end.png", config.screen_width, config.screen_height)
image bg_restaurant = im.Scale("bg_restaurant.jpg", config.screen_width, config.screen_height)
image bg_conference = im.Scale("bg_conference.png", config.screen_width, config.screen_height)
image bg_laugh = im.Scale("bg_laugh.png", config.screen_width, config.screen_height)
image bg_car = im.Scale("bg_car.jpeg", config.screen_width, config.screen_height)
###############    엔딩    ###############
image ending_C_1 = im.Scale("ending_C_1.png", config.screen_width, config.screen_height)
image ending_C_2 = im.Scale("ending_C_2.png", config.screen_width, config.screen_height)
image ending_C_3 = im.Scale("ending_C_3.png", config.screen_width, config.screen_height)
image ending_C_4 = im.Scale("ending_C_4.png", config.screen_width, config.screen_height)

image ending_J1_1 = im.Scale("ending_J1_1.png", config.screen_width, config.screen_height)
image ending_J1_2 = im.Scale("ending_J1_2.png", config.screen_width, config.screen_height)
image ending_J1_3 = im.Scale("ending_J1_3.png", config.screen_width, config.screen_height)
image ending_J1_4 = im.Scale("ending_J1_4.png", config.screen_width, config.screen_height)

image ending_J2_1 = im.Scale("ending_J2_1.png", config.screen_width, config.screen_height)
image ending_J2_2 = im.Scale("ending_J2_2.png", config.screen_width, config.screen_height)
image ending_J2_3 = im.Scale("ending_J2_3.png", config.screen_width, config.screen_height)
image ending_J2_4 = im.Scale("ending_J2_4.png", config.screen_width, config.screen_height)  

image ending_G_1 = im.Scale("ending_G_1.png", config.screen_width, config.screen_height)
image ending_G_2 = im.Scale("ending_G_2.png", config.screen_width, config.screen_height)
image ending_G_3 = im.Scale("ending_G_3.png", config.screen_width, config.screen_height)
image ending_G_4 = im.Scale("ending_G_4.png", config.screen_width, config.screen_height)

image ending_K_1 = im.Scale("ending_K_1.png", config.screen_width, config.screen_height)
image ending_K_2 = im.Scale("ending_K_2.png", config.screen_width, config.screen_height)
image ending_K_3 = im.Scale("ending_K_3.png", config.screen_width, config.screen_height)
image ending_K_4 = im.Scale("ending_K_4.png", config.screen_width, config.screen_height)
###############    침착맨    ###############
image C_happy = "침채린_웃음.png"
image C_excited = "침채린_신남.png"
image C_sad = "침채린_당황.png"
image C_angry = "침채린_화남.png"
image C_surprised = "침채린_놀람.png"
image C_q = "침채린_궁금.png"

image glitch_C_happy = "glitch_C_happy.png"
image glitch_ChimChak_happy = "glitch_ChimChak_happy.png"
image glitch_C_excited = "glitch_C_excited.png"
image glitch_ChimChak_excited = "glitch_ChimChak_excited.png"
image glitch_C_sad = "glitch_C_sad.png"
image glitch_ChimChak_sad = "glitch_ChimChak_sad.png"
image glitch_C_angry = "glitch_C_angry.png"
image glitch_ChimChak_angry = "glitch_ChimChak_angry.png"
image glitch_C_surprised = "glitch_C_surprised.png"
image glitch_ChimChak_surprised = "glitch_ChimChak_surprised.png"
image glitch_C_q = "glitch_C_q.png"
image glitch_ChimChak_q = "glitch_ChimChak_q.png"

image ChimChak_happy = "침착맨_웃음.png"
image ChimChak_excited = "침착맨_신남.png"
image ChimChak_sad = "침착맨_당황.png"
image ChimChak_angry = "침착맨_화남.png"
image ChimChak_surprised = "침착맨_놀람.png"
image ChimChak_q = "침착맨_궁금.png"


###############    주호민    ###############
image J1_happy = "주하민_웃음.png"
image J1_excited = "주하민_신남.png"
image J1_sad = "주하민_화남.png"
image J1_angry = "주하민_놀람.png"
image J1_surprised = "주하민_궁금.png"
image J1_q = "주하민_궁금.png"

image glitch_J1_happy = "glitch_J1_happy.png"
image glitch_Jooperl_happy = "glitch_Jooperl_happy.png"
image glitch_J1_excited = "glitch_J1_excited.png"
image glitch_Jooperl_excited = "glitch_Jooperl_excited.png"
image glitch_J1_sad = "glitch_J1_sad.png"
image glitch_Jooperl_sad = "glitch_Jooperl_sad.png"
image glitch_J1_angry = "glitch_J1_angry.png"
image glitch_Jooperl_angry = "glitch_Jooperl_angry.png"
image glitch_J1_surprised = "glitch_J1_surprised.png"
image glitch_Jooperl_surprised = "glitch_Jooperl_surprised.png"
image glitch_J1_q = "glitch_J1_q.png"
image glitch_Jooperl_q = "glitch_Jooperl_q.png"

image Jooperl_happy = "주호민_웃음.png"
image Jooperl_excited = "주호민_신남.png"
image Jooperl_sad = "주호민_당황.png"
image Jooperl_angry = "주호민_화남.png"
image Jooperl_surprised = "주호민_놀람.png"
image Jooperl_q = "주호민_궁금.png"

###############    주우재    ###############

image J2_happy = "주유재_신남.png"
image J2_excited = "주유재_매우신남.png"
image J2_sad = "주유재_당황.png"
image J2_surprised = "주유재_궁금.png"
image J2_q = "주유재_궁금.png"

image glitch_J2_happy = "glitch_J2_happy.png"   
image glitch_JooWoo_happy = "glitch_JooWoo_happy.png"
image glitch_J2_excited = "glitch_J2_excited.png"
image glitch_JooWoo_excited = "glitch_JooWoo_excited.png"
image glitch_J2_sad = "glitch_J2_sad.png"
image glitch_JooWoo_sad = "glitch_JooWoo_sad.png"
image glitch_J2_surprised = "glitch_J2_surprised.png"
image glitch_JooWoo_surprised = "glitch_JooWoo_surprised.png"
image glitch_J2_q = "glitch_J2_q.png"
image glitch_JooWoo_q = "glitch_JooWoo_q.png"

image JooWoo_happy = "주우재_웃음.png"
image JooWoo_excited = "주우재_신남.png"
image JooWoo_sad = "주우재_당황.png"
image JooWoo_surprised = "주우재_놀람.png"
image JooWoo_q = "주우재_궁금.png"

###############    궤도    ###############

image G_happy = "궤하린_웃음.png"
image G_sad = "궤하린_놀람.png"
image G_angry = "궤하린_당황.png"
image G_excited = "궤하린_신남.png"
image G_outside = "궤하린_외출.png"

image glitch_G_happy = "glitch_G_happy.png"
image glitch_Gdo_happy = "glitch_Gdo_happy.png"
image glitch_G_sad = "glitch_G_sad.png"
image glitch_Gdo_sad = "glitch_Gdo_sad.png"
image glitch_G_angry = "glitch_G_angry.png"
image glitch_Gdo_angry = "glitch_Gdo_angry.png"
image glitch_G_excited = "glitch_G_excited.png"
image glitch_Gdo_excited = "glitch_Gdo_excited.png"
image glitch_G_outside = "glitch_G_outside.png"
image glitch_Gdo_outside = "glitch_Gdo_outside.png"

image Gdo_happy = "궤도_웃음.png"
image Gdo_sad = "궤도_놀람.png"
image Gdo_angry = "궤도_화남.png"
image Gdo_excited = "궤도_신남.png"
image Gdo_outside = "궤도_외출.png"

###############    김풍    ###############

image K_happy = "김솔풍_웃음.png"
image K_excited = "김솔풍_신남.png"
image K_nervous = "김솔풍_당황.png"

image glitch_K_happy = "glitch_K_happy.png"
image glitch_KPoong_happy = "glitch_KPoong_happy.png"
image glitch_K_excited = "glitch_K_excited.png"
image glitch_KPoong_excited = "glitch_KPoong_excited.png"
image glitch_K_nervous = "glitch_K_nervous.png"
image glitch_KPoong_nervous = "glitch_KPoong_nervous.png"

image KPoong_happy = "김풍_웃음.png"
image KPoong_excited = "김풍_신남.png"
image KPoong_nervous = "김풍_당황.png"

image flashing:
    Solid("#FFFFFF")
    alpha 0.0
    linear 0.1 alpha 1.0
    linear 0.1 alpha 0.0
    repeat

transform fade_in:
    alpha 0.0
    linear 0.5 alpha 1.0  # 1초 동안 투명 -> 불투명

transform fade_out:
    alpha 1.0
    linear 0.5 alpha 0.0

screen display_likes_ch1:
    # like_C 값을 왼쪽 상단에 표시
    text "호감도: [like_C]" xpos 646 ypos 590 color "#000000" size 50 font "Pretendard-Bold.ttf"
    text "호감도: [like_K]" xpos 1076 ypos 590 color "#000000" size 50 font "Pretendard-Bold.ttf"

screen display_likes_ch2:
    # like_C 값을 왼쪽 상단에 표시
    text "호감도: [like_C]" xpos 216 ypos 590 color "#000000" size 50 font "Pretendard-Bold.ttf"
    text "호감도: [like_K]" xpos 1076 ypos 590 color "#000000" size 50 font "Pretendard-Bold.ttf"
    text "호감도: [like_C]" xpos 646 ypos 590 color "#000000" size 50 font "Pretendard-Bold.ttf"
    text "호감도: [like_K]" xpos 1506 ypos 590 color "#000000" size 50 font "Pretendard-Bold.ttf"

screen display_likes:
    # like_C 값을 왼쪽 상단에 표시
    text "호감도: [like_C]" xpos 522 ypos 693 color "#000000" size 40 font "Pretendard-Bold.ttf"
    text "호감도: [like_J1]" xpos 174 ypos 433 color "#000000" size 40 font "Pretendard-Bold.ttf"
    text "호감도: [like_J2]" xpos 1578 ypos 433 color "#000000" size 40 font "Pretendard-Bold.ttf"
    text "호감도: [like_G]" xpos 1220 ypos 693 color "#000000" size 40 font "Pretendard-Bold.ttf"
    text "호감도: [like_K]" xpos 881 ypos 433 color "#000000" size 40 font "Pretendard-Bold.ttf"

# 여기에서부터 게임이 시작합니다.
label start:
    
    # 이름 입력 (최대 길이 12자)
    $ player_name = renpy.input("당신의 이름을 입력하세요. (최대 12자)", length=12) or "공진우"

    # 이름이 공백일 경우 기본값 설정
    if player_name.strip() == "":
        $ player_name = "공진우"

    # 이름 확인
    "안녕하세요, [player_name]님. 게임에 오신 것을 환영합니다!"

    # 캐릭터 생성
    $ P = Character(player_name, color="#FFFFFF")

    P "이제 제 이야기를 시작해볼까요?"


    # show screen display_likes
    # jump chapter4
    # show screen display_likes_ch1

    scene bg_dorm with fade

    stop music fadeout 1.0
    play music "audio/bgm_intro.mp3" fadein 1.0 loop

    P "이 캠프는 나에게 큰 기회다. 어떻게 따낸 건데... 첫날부터 지각생으로 찍히면 안 돼!"
    
    P "몰입캠프에서 개발만 한다고? 아니, 연애도 많이 한다던데... 혹시 나에게도 그런 일이 생길 수 있을까?"

    scene bg_N1 with fade
    
    P "아냐, 무슨. 연애라니. 나 같은 녀석이? 손도 못 잡아 본 주제에, 에휴... 꿈도 크다."

    play sound "audio/ch1/crash.mp3"
    show black
    P "...!!!"
    $ renpy.pause(3)
    hide black
    show flashing
    $ renpy.pause(2)
    hide flashing

    voice "audio/ch1/ch1_C_001.mp3"
    
    call show_C_angry from _call_show_C_angry_11
    Who "꺄악! 뭐야 너!! 앞 좀 보고 다녀!!"

    P "으윽... 뭐지? 뭐랑 부딪힌 거 같은데... 머리야… 아프다."

    voice "audio/ch1/ch1_C_002.mp3" 
    Who "킥보드 타는 거 처음이야? 앞 좀 보고 다녀야지! 에휴, 다 왔는데 이게 뭐야!!"

    P "죄, 죄송합니다! 제가 잠깐... 딴생각을 하느라… 정말 죄송합니다!"

    voice "audio/ch1/ch1_C_003.mp3" 
    $ preferences.text_cps = 20
    Who "됐어요! 신경 꺼요!"

    P "네? 뭐라고요?"

    call hide_C_angry from _call_hide_C_angry_17

    call show_C_happy from _call_show_C_happy_24
    voice "audio/ch1/ch1_C_004.mp3"
    Who "어? 뭐야. 너 설마 [player_name] 아니야? ㅋㅋㅋ"

    P "네? [player_name](이)요? 저를 아세요?"

    voice "audio/ch1/ch1_C_005.mp3"
    Who "야, 나 침채린이야! 기억 안 나? 중학교 때 같은 반이었잖아!"

    P "아… 그, 그랬었지. (이런, 잊고 싶었던 기억이 되살아난다.)"

    "중학교 내내 날 괴롭히던 그 녀석. 침채린. 설마 여기까지 와서 다시 보게 될 줄이야. 그런데 여긴 카이스트 아닌가?"

    voice "audio/ch1/ch1_C_006.mp3"
    C "왜 그래? 갑자기 멍 때리고 있네? 하긴 오랜만이긴 하지. ㅋㅋ"

    voice "audio/ch1/ch1_C_007.mp3"
    C "보아하니 너도 몰입캠프 왔나 보네? 잘 부탁해, [player_name]~"

    P "(같은 반 아니겠지? 아니야, 단톡방에서 저 녀석 이름 본 적 없는데... 제발.)"

label classroom:

    stop music fadeout 1.0
    play music "audio/bgm_daily_1.mp3" fadein 1.0 loop
    scene bg_classroom with fade

    "반 실습실에 들어가자 분반 조교의 안내로 캠프가 시작된다."

    call show_K_happy from _call_show_K_happy_10
    voice "audio/ch1/ch1_K_001.mp3"
    K "안녕하세요, 여러분. 저는 4분반 조교 김솔풍입니다. 몰입캠프 기간 동안 잘 부탁드려요. 궁금한 점 있으시면 언제든 편하게 질문해주세요~!"

    P "\'와... 엄청난 미인! 이게 몰입캠프구나... 열심히 해야겠다!\'"

    call show_C_happy from _call_show_C_happy_25
    voice "audio/ch1/ch1_C_008.mp3"
    C "야, [player_name]! 우리 같은 반, 같은 팀이네~ 대박! 중학교 때 생각나고 좋다~ 너는 좋겠다~ 나같이 예쁜 사람이랑 같은 팀이라~"

    P "(으으… 침채린이라니… 어쩌다 또 얽힌 거야…)"

    P "하하, 그런가…?"

    voice "audio/ch1/ch1_K_002.mp3"
    K "어머, 두 분이 아는 사이였구나? 일부러 접점이 없을 것 같은 사람끼리 배정했는데 이런 우연이 있네요~ㅎㅎ"

    voice "audio/ch1/ch1_K_003.mp3"
    K "혹시 오늘 첫날이니까, 다 같이 점심 먹으러 갈래요? 분반 사람들 한 번씩 다 사주려고 했는데, 너희가 첫 번째로 당첨됐어!"

    voice "audio/ch1/ch1_C_009.mp3"
    C "와! 진짜요? 완전 좋아요!! [player_name], 너도 가자~!"

    menu:
        "같이 점심 먹으러 간다":
            
            $ like_C += 2.5
            $ like_K += 2.5
            P "아… 네, 감사합니다. 같이 갈게요."
            $ renpy.pause(0.5)

            call hide_C_happy from _call_hide_C_happy_20
            call hide_K_happy from _call_hide_K_happy_14
            jump cafeteria

        "바쁘다고 핑계대고 가지 않는다":

            if like_C - 5 < 40 and like_C >= 40:
                call glitch_C_happy from _call_glitch_C_happy_2
            $ like_C -= 5
            
            if like_K - 10 < 45 and like_K >= 45:
                call glitch_K_happy from _call_glitch_K_happy_2
            $ like_K -= 10
            P "죄송해요, 오늘은 조금 바빠서 다음에 꼭 갈게요!"

            jump skip_lunch_scene

label cafeteria:

    scene bg_cafeteria with dissolve
    stop music fadeout 1.0
    play music "audio/bgm_daily_7.mp3" fadein 1.0 loop
    call show_K_happy from _call_show_K_happy_11
    voice "audio/ch1/ch1_K_004.mp3"
    K "먹고 싶은 거 마음껏 골라. 오늘은 내가 쏜다~"

    call show_C_happy from _call_show_C_happy_26
    voice "audio/ch1/ch1_C_010.mp3"
    C "와~ 뭐 먹지? 야, [player_name]. 너 뭐 먹을 거야? 먹고 싶은 거 없으면 라구 파스타 시켜. 내가 뺏어먹게~ㅋㅋ"

    P "으음… 저는 함박스테이크로 할게요."

    voice "audio/ch1/ch1_C_011.mp3"
    C "진짜? 역시 이름값 하네. 아주 찐~한 선택이다. ㅋㅋ"

    voice "audio/ch1/ch1_K_005.mp3"
    K "얘들아, 싸우지 말고 각자 먹고 싶은 거 시켜. 점심은 즐겁게 먹자~"

    voice "audio/ch1/ch1_C_012.mp3"
    C "조교님 덕분에 잘 먹겠습니다! [player_name], 너도 감사해해라."

    voice "audio/ch1/ch1_K_006.mp3"
    K "근데, [player_name]. 혹시 연애 해본 적 있어?"

    voice "audio/ch1/ch1_C_013.mp3"
    C "얘가요? ㅋㅋㅋ 있을 리가요. 중학교 때도 완전 찐따였는데 뭐 ㅋㅋㅋ"

    P "(침채린 저 녀석... 꼭 안 해도 될 말만 골라서 하네...)"

    voice "audio/ch1/ch1_K_007.mp3"
    K "ㅎㅎ 그래도 연애는 안 해봤어도 이상형 정도는 있을 거 아니야. 궁금한데~ 우리 둘 중에 누가 더 이상형에 가까워?"

    menu: 
        "침채린이... 더 나은 것 같아요":
            $ like_C += 5
            if like_K - 10 < 45 and like_K >= 45:
                call glitch_K_happy from _call_glitch_K_happy_3
            $ like_K -= 10
            P "음... 그래도 침채린 쪽이 좀 더 가까운 것 같아요."
            voice "audio/ch1/ch1_C_014.mp3"
            C "ㅋㅋㅋ 내가 그럴 줄 알았다. 역시 안목은 있네, [player_name]!"
            voice "audio/ch1/ch1_K_008.mp3"
            K "(살짝 웃으며) 둘이 은근 잘 어울리네."
            jump team_project

        "풍 조교님이 훨씬 예쁘죠":

            call hide_C_happy from _call_hide_C_happy_21
            call show_C_angry from _call_show_C_angry_12

            $ like_K += 10
        
            P "음... 저는 조교님 쪽이 더 이상형에 가까운 것 같아요."
            voice "audio/ch1/ch1_K_009.mp3"
            K "어머~ 고마워, [player_name]. 뭔가 기분 좋은데~?"
            

            if like_C - 5 < 40 and like_C >= 40:
                call glitch_C_angry from _call_glitch_C_angry_8
            $ like_C -= 5

            voice "audio/ch1/ch1_C_015.mp3"
            C "뭐야, 나 무시하는 거야? 아, 몰라. 내 라구 파스타나 먹어야지!"
            jump team_project


label skip_lunch_scene:

    scene bg_classroom with dissolve
    stop music fadeout 1.0
    play music "audio/bgm_daily_1.mp3" fadein 1.0 loop
    "분반 조교와 침채린의 점심 제안을 거절하고, 혼자 실습실로 돌아왔다."

    P "(점심을 같이 먹는 것도 좋았을 텐데… 하지만 첫날부터 너무 친해지려는 건 부담스러워.)"

    P "(혼자서 정리할 시간도 필요하니까, 나만의 시간을 보내는 것도 나쁘진 않아.)"

    "실습실에서 노트북을 켜고, 몰입캠프 첫 과제 자료를 다시 살펴보기 시작했다."

    "그렇게 시간을 보내던 중, 침채린과 분반 조교가 실습실로 돌아왔다."

    call show_C_happy from _call_show_C_happy_27
    call show_K_happy from _call_show_K_happy_12

    voice "audio/ch1/ch1_C_016.mp3"
    C "[player_name]~ 너 점심 먹으러 진짜 안 오더라? 우리끼리 신나게 먹고 왔어. 너 빠지니까 재미가 덜했어~!"

    P "아… 좀 정리할 게 많아서... 그래도 재밌게 먹었다니 다행이네."

    voice "audio/ch1/ch1_K_010.mp3"
    K "괜찮아. 다음에 같이 먹자! [player_name]도 나름 진지하게 준비하는 것 같네."

    voice "audio/ch1/ch1_C_017.mp3"
    C "근데 너 그거 알아? 조교님이 너한테 아까... '생각보다 성실한 친구네'라고 했어! 완전 칭찬이지?"

    voice "audio/ch1/ch1_K_011.mp3"
    K "(웃음) 맞아. 그래도 혼자만 너무 무리하지 마."

    P "(칭찬인가? 아니면 걱정인가?)"

    P "(어쨌든, 다음엔 같이 가는 게 나을지도… 혼자선 조금 허전하네.)"

    "그렇게 첫날은 조용히 지나갔다."

    jump team_project

label team_project:


    stop music fadeout 1.0
    scene bg_computer with dissolve
    play music "audio/bgm_daily_4.mp3" fadein 1.0 loop

    "1주차 프로젝트 과제를 진행하던 중, 실습실에서 문제가 발생했다."

    P "(헉, 갑자기 이 오류는 뭐지...? 어제까지는 잘 돌아갔던 것 같은데.)"

    "그때 침채린과 김솔풍 조교가 실습실로 다가온다."

    call show_C_happy from _call_show_C_happy_28

    call show_K_happy from _call_show_K_happy_13
    voice "audio/ch1/ch1_C_018.mp3"
    C "야, [player_name]. 뭐 해? 완전 멍 때리고 있네. 혹시 문제 생겼어?"

    P "어… 코딩하다가 갑자기 오류가 나서, 뭘 잘못한 건지 모르겠어."

    voice "audio/ch1/ch1_K_012.mp3"
    K "음, 같이 한번 볼까? 팀 프로젝트니까 다 같이 도와야지!"

    "김솔풍 조교와 침채린이 주인공을 도우며 과제를 해결하기 위해 나선다."
    
    menu:
        "침채린에게 도움을 요청한다":

            $ like_C += 2.5
            if like_K - 2.5 < 45 and like_K >= 45:
                call glitch_K_happy from _call_glitch_K_happy_4
            $ like_K -= 2.5

            call hide_K_happy from _call_hide_K_happy_15
            $ renpy.pause(1.5)
            jump help_by_C 

        "김솔풍 조교에게 도움을 요청한다":

            if like_C - 2.5 < 40 and like_C >= 40:
                call glitch_C_happy from _call_glitch_C_happy_3
            $ like_C -= 2.5

            $ like_K += 2.5

            call hide_C_happy from _call_hide_C_happy_22
            $ renpy.pause(1.5)
            jump help_by_K

label help_by_C:

    voice "audio/ch1/ch1_C_019.mp3"
    C "야, 코딩은 내가 별로지만 그래도 넌 나보다 더 못하잖아. 잘 봐, 내가 한번 해결해볼게."

    "침채린이 키보드를 두드리며 오류를 고치려고 노력한다. 하지만 더 복잡한 문제가 발생했다."

    "깜짝 미니게임~~!!"

    "이 게임을 플레이하는 당신, 기본적인 코드는 읽으실 수 있겠죠?"

    "미니게임: 프로그래밍 퀴즈를 시작합니다."

    "총 5문제로 이루어져 있으며 난이도는 \"Super Easy\" 그 자체!!"

    "바로 시작합니다."

    call programming_quiz from _call_programming_quiz
    scene bg_computer
    stop music fadeout 1.0
    play music "audio/bgm_daily_4.mp3" fadein 1.0 loop
    P "(으으… 그래도 침채린이 도와주려고 하니 기분은 나쁘지 않네.)"

    "둘이 함께 열심히 오류를 찾으며 친해졌다."
    
    call hide_C_happy from _call_hide_C_happy_23

    $ like_C += 5

    jump classroom2

label help_by_K:

    voice "audio/ch1/ch1_K_013.mp3"
    K "음, 이건 논리적 오류 같네. 여길 수정하면 될 것 같아. 내가 한번 해볼게."

    "김솔풍 조교가 차분하게 오류를 분석하고 고쳐준다."

    "깜짝 미니게임~~!!"

    "이 게임을 플레이하는 당신, 기본적인 코드는 읽으실 수 있겠죠?"

    "미니게임: 프로그래밍 퀴즈를 시작합니다."

    "총 5문제로 이루어져 있으며 난이도는 \"Super Easy\" 그 자체!!"

    "바로 시작합니다."

    call programming_quiz from _call_programming_quiz_1
    scene bg_computer
    stop music fadeout 1.0
    play music "audio/bgm_daily_4.mp3" fadein 1.0 loop

    P "(역시 조교님은 실력이 대단하다... 나도 이렇게 되고 싶다.)"

    "김솔풍 조교의 도움으로 문제를 해결하며, 주인공의 호감이 상승했다."

    call hide_K_happy from _call_hide_K_happy_16
    $ like_K += 5
    jump classroom2

label classroom2:

    scene bg_classroom with fade
    stop music fadeout 1.0
    play music "audio/bgm_daily_6.mp3" fadein 1.0 loop

    "1주차 분반 발표를 앞둔 3시간 전."

    P "드디어 첫 발표 날이다. 침채린한테 일주일 동안 시달렸는데 그래도 이제 거의 다 끝났네. 휴우…"

    "그런데 갑자기 침채린에게 보이스톡이 걸려왔다."

    P "(얘가 왜 갑자기 나한테 전화를 하지? 받아야 하나... 안 받으면 더 난리 날 텐데...)"

    "(결국 전화를 받았다.)"

    call show_C_sad from _call_show_C_sad_7
    voice "audio/ch1/ch1_C_020.mp3"
    C "야, [player_name]. 너 실습실이지?"

    P "응… 그런데 무슨 일이야? 목소리가 왜 그래? (침채린답지 않게 축 처진 목소리다.)"

    voice "audio/ch1/ch1_C_021.mp3"
    C "그게... 나... 어떡하지..."

    voice "audio/ch1/ch1_C_022.mp3"
    C "방금 혼자 저녁 먹으러 나왔다가 돌아오는 길에... 버스랑 부딪혀서 다쳤어."

    P "(뭐?! 버스랑 부딪혔다고?!)"

    voice "audio/ch1/ch1_C_023.mp3"
    C "근데... 도저히 혼자 못 가겠어. 아... 아니다. 미안. 그냥 끊을게."

    menu: 

        "침채린을 데리러 간다":
            $ like_C += 5
            jump gotFetchC

        "그냥 발표를 준비한다":

            if like_C - 10 < 40 and like_C >= 40:
                call glitch_C_sad from _call_glitch_C_sad
            $ like_C -= 10
            
            jump present

label gotFetchC:

    P "잠깐! 끊지 마! 내가 갈게. 어디야?"

    voice "audio/ch1/ch1_C_024.mp3"
    C "어? 너가 온다고? 됐어, 괜찮아. 다른 사람한테 부탁하면 돼."

    P "아니, 너 지금 아는 사람 나밖에 없잖아. 내가 갈게. 위치 찍어줘."

    voice "audio/ch1/ch1_C_025.mp3"
    C "그... 그래. 알았어. 고마워... 위치 보낼게."

    "침채린이 보낸 위치를 확인한 후, 주인공은 급히 실습실을 나섰다."

    jump hulala1

label present:

    P "그럼... 발표는 내가 혼자 맡을게. 너 빨리 병원 갔다 와."

    voice "audio/ch1/ch1_C_026.mp3"
    C "그래... 미안하고 고마워. 발표 잘 해."

    "침채린과의 통화를 마친 주인공은 혼자 발표 준비를 시작했다."

    jump hulala2

label hulala1:

    scene bg_night with dissolve

    call show_C_happy from _call_show_C_happy_29
    stop music fadeout 1.0
    play music "audio/bgm_date_night.mp3" fadein 1.0 loop
    "침채린을 데리고 실습실로 돌아오는 길."

    P "괜찮아? 많이 아팠겠네… 병원은 꼭 가봐야 하지 않을까?"

    voice "audio/ch1/ch1_C_027.mp3"
    C "괜찮아. 그냥 놀랐던 거야. 너 덕분에 무사히 돌아올 수 있었어. 고마워, [player_name]."

    P "아냐, 내가 당연히 해야 할 일인데 뭐. 그런데 말이야… 여기 거위가 많다던데 내일 같이 보러 갈래?"

    voice "audio/ch1/ch1_C_028.mp3"
    C "(살짝 웃으며) 거위...? 그래, 거위 보러 가자. 너도 참 이상하다니까."

    "침채린은 피곤한 듯 미소를 지으며 고개를 끄덕였다."

    jump chapter1_end

label hulala2:

    scene bg_classroom with dissolve
    stop music fadeout 1.0
    play music "audio/bgm_date_night.mp3" fadein 1.0 loop
    
    "발표를 마친 후, 침채린과 실습실에서 다시 마주쳤다."

    call show_C_angry from _call_show_C_angry_13
    voice "audio/ch1/ch1_C_029.mp3"
    C "(술에 취한 듯한 상태로) 야! 너 아까 왜 안 왔어. 예전에는 말 잘 듣더니 이제는 진짜…"

    P "너가 괜찮다고 했잖아… 그래서 발표 준비했지…"

    voice "audio/ch1/ch1_C_030.mp3"
    C "내가 부축해달라고 꼭 말해야 돼?"

    "침채린이 살짝 고개를 돌리며 투덜댔다."

    voice "audio/ch1/ch1_C_031.mp3"
    C "됐어. 대신 벌로 내일 나랑 거위 보러 가. 알았지?"

    P "거위...? 갑자기?"

    voice "audio/ch1/ch1_C_032.mp3"
    C "아 몰라. 내 말 들어. 어쨌든 거위 보러 가야 돼. 끝."

    jump chapter1_end

label chapter1_end:
    hide bg_classroom
    hide bg_night
    hide C_happy at fade_out
    hide K at fade_out
    show bg_ch1_end with fade

    # 스크린 표시
    show screen display_likes_ch1
    "챕터의 마지막에는 지금까지 등장한 캐릭터들의 호감도를 알려줍니다."

    "사랑을 얻으려면 전략도 필요한 법!! 파이팅입니다~!!"
    jump chapter2
