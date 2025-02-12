label chapter4:

    hide screen display_likes
    scene bg_dorm2 with fade
    stop music fadeout 1.0
    play music "audio/bgm_daily_7.mp3" fadein 1.0 loop

    "몰입캠프 마지막 날, 해가 뜨기 전에 알람이 울렸다."

    P "(우와... 벌써 마지막 날이야?)"

    P "(진짜 피곤하다... 그래도 이젠 마지막이다. 개발도 힘들었지만, 사람들하고 어울리는 것도 만만치 않았지.)"

    "침대에서 일어나 휴대폰을 확인하니 여러 알림이 와 있다."

    voice "audio/ch4/ch4_C_001.mp3"
    call show_C_happy from _call_show_C_happy_21
    C "일어났냐? 실습실 얼른 와라. 오늘 누님이 하드캐리 해 줌."

    $ renpy.pause(1)

    call hide_C_happy from _call_hide_C_happy_16
    call show_J1_happy from _call_show_J1_happy_16
    voice "audio/ch4/ch4_J1_001.mp3"
    J1 "[player_name]야, 일어났어? 오늘도 화이팅하자!!"

    $ renpy.pause(1)

    call hide_J1_happy from _call_hide_J1_happy_12
    call show_G_happy from _call_show_G_happy_9
    voice "audio/ch4/ch4_G_001.mp3"
    G "케이크는 먹었어? 내 남친? ㅋㅋㅋ (농담이야~)"

    $ renpy.pause(1)

    call hide_G_happy from _call_hide_G_happy_10
    call show_J2_happy from _call_show_J2_happy_8
    voice "audio/ch4/ch4_J2_001.mp3"
    J2 "오빠, 어디야? 나 신상 디저트 사 왔어. 같이 먹자."
    call hide_J2_happy from _call_hide_J2_happy_8

    P "(오늘 하루를 어떻게 보낼지 고민하며 잠시 화면을 응시했다.)"

    P "(마지막 날이니까, 몰캠도 사랑도 모두 쟁취해야지... 안 그러면 후회할지도 몰라!)"

    scene black

    "몰입캠프의 마지막 날에 도착했습니다!! 4.5주간 아주 고생많았어요."

    "하지만 아직 크나 큰 선택의 순간이 기다리고 있습니다."

    "풀리지 않을 것 같은 퍼즐을 맞춰나가세요!"

    "깜짝 미니게임!!"

    "마지막 미니게임: 네모네모로직입니다. (노노그램 ㅋㅋ)"

    "바로 시작합니다."   
    stop music fadeout 1.0
    play music "audio/bgm_minigame_nonogram.mp3" fadein 1.0 loop
    call screen nonogram_game
    stop music fadeout 1.0
    play music "audio/bgm_daily_7.mp3" fadein 1.0 loop

    "오, 노노그램을 성공하셨군요. 10x10은 역시 너무 쉬웠나요~?"

    "이제 엔딩을 향해 달려가 봅시다."

    jump choose

label choose:

    if like_C < 80 and like_J1 < 75 and like_G < 90 and like_J2 < 75 and like_K < 85:
        scene bg_laugh
        stop music fadeout 1.0
        play music "audio/bgm_daily_3.mp3" fadein 1.0 loop
        "앉아서 코딩만 하다보니...뭔가 더 친해지기는 어려웠던 것 같다"

        "결국 연애 시뮬레이션에서도 혼자라니… 코딩만 하면 뭐해!"

        "다음 번엔 '연애의 알고리즘'이라도 짜봐야겠군."

        "혼자라도 괜찮아. 내 PC만 있으면 언제든 새로운 게임을 시작할 수 있으니까!"

        window hide
        jump ending_credits

    else:
        scene black
        stop music fadeout 1.0
        play music "audio/bgm_daily_5.mp3" fadein 1.0 loop
        "몰입캠프의 마지막 날이다...누구와 함께 보낼지 선택해보자."

        menu:

            "침채린":
                if like_C < 80:
                    "침채린의 호감도가 부족합니다. 돌아가주세요."
                    jump choose
                else:
                    jump ending1

            "주하민":
                if like_J1 < 75:
                    "주하민의 호감도가 부족합니다. 돌아가주세요."
                    jump choose
                else:
                    jump ending2
            "궤하린":
                if like_G < 90:
                    "궤하린의 호감도가 부족합니다. 돌아가주세요."
                    jump choose
                else:        
                    jump ending3
            "주유재":
                if like_J2 < 75:
                    "주유재의 호감도가 부족합니다. 돌아가주세요."
                    jump choose
                else:    
                    jump ending4
            "김솔풍": 
                if like_K < 85:
                    "김솔풍의 호감도가 부족합니다. 돌아가주세요."
                    jump choose
                else:    
                    jump ending5

# 침채린 엔딩
label ending1:

    show bg_classroom
    stop music fadeout 1.0
    play music "audio/bgm_ending_1.mp3" fadein 1.0 loop
    "침채린이 실습실에 앉아, 마지막 프로젝트를 마무리하고 있었다."

    call show_C_happy from _call_show_C_happy_22
    voice "audio/ch4/ch4_C_003.mp3"
    C "야, [player_name]! 오늘은 뭘 그렇게 꾸물거리냐? 빨리 와서 나랑 같이 하자."

    "너는 그녀의 옆에 앉았다. 침채린은 화면에 집중하면서도 말을 걸었다."

    voice "audio/ch4/ch4_C_002.mp3"
    C "[player_name], 너 몰캠 재밌었지? 나 있어서 훨씬 좋았지?"

    P "솔직히 처음엔 좀 무서웠어. 너 중학교 때부터 무섭게 군 기억이 남아서…"

    call hide_C_happy from _call_hide_C_happy_17
    call show_C_sad from _call_show_C_sad_6
    voice "audio/ch4/ch4_C_004.mp3"
    C "아 그거? 어렸을 땐 내가 좀 철이 없었지. 근데 지금은 내가 잘 챙겨줬잖아!"

    P "응. 그래서 점점 너를 좋아하게 된 것 같아."

    "침채린은 갑자기 멈춰서 너를 바라봤다."

    voice "audio/ch4/ch4_C_005.mp3"
    C "야... 그거 진짜야? 아니면 그냥 날 놀리는 거야?"

    P "진심이야. 너랑 함께했던 몰캠이 정말 재밌었어. 너랑 계속 같이 있고 싶어."

    call hide_C_sad from _call_hide_C_sad_5
    call show_C_angry from _call_show_C_angry_10
    voice "audio/ch4/ch4_C_006.mp3"
    C "(얼굴이 빨개지며) …그럼 이제 다른 애들한테 신경 쓰지 마라? 특히 그 주우재!"

    P "응? 다른 사람들? 당연히 안 신경 써. 이제 너만 보면 돼."

    call hide_C_angry from _call_hide_C_angry_15
    call show_C_happy from _call_show_C_happy_23
    voice "audio/ch4/ch4_C_007.mp3"
    C "좋아! 그럼 이제 너, 누나만 믿고 따라와~!"

    P "(웃으며) 네, 누나! ㅋㅋㅋ"
    $ renpy.pause(2)
    call hide_C_happy from _call_hide_C_happy_18

    scene ending_C_1 with fade
    $ renpy.pause(3)
    scene ending_C_2 with fade
    $ renpy.pause(3)
    scene ending_C_3 with fade
    $ renpy.pause(3)
    scene ending_C_4 with fade
    $ renpy.pause(3)
    
    scene black
    $ renpy.pause(2)
    "잘 플레이 하셨나요?"

    "당신의 히로인은 침채린이었군요. 역시 우리 개방장이 짱이죠. 축하합니다."

    "몰임캠프 사랑의 격전지: 4.5 weeks of love 는 멀티 엔딩이 존재하는 게임이므로 여러번 플레이하시는 걸 추천합니다."

    "그럼 감사합니다. 다음에 또 만나요!"

    jump ending_credits

# 주하민 엔딩
label ending2:

    show bg_classroom
    stop music fadeout 1.0
    play music "audio/bgm_ending_3.mp3" fadein 1.0 loop
    "주하민과 실습실에서 마지막 날을 정리하고 있다."

    call show_J1_q from _call_show_J1_q_5
    voice "audio/ch4/ch4_J1_002.mp3"
    J1 "[player_name]야, 오늘 캠프 끝나고 뭐 해? 혹시 시간 있어?"

    P "응? 아니. 특별히 정해둔 건 없는데 왜?"

    call hide_J1_q from _call_hide_J1_q_6
    call show_J1_excited from _call_show_J1_excited_5
    voice "audio/ch4/ch4_J1_003.mp3"
    J1 "다행이다. 사실 너랑 하고 싶은 말이 있어."

    "그녀는 살짝 부끄러운 얼굴로 말을 이어갔다."

    call hide_J1_excited from _call_hide_J1_excited_5
    call show_J1_happy from _call_show_J1_happy_17
    voice "audio/ch4/ch4_J1_004.mp3"
    J1 "그동안 너랑 이야기 나누면서 느꼈어. 우리가 정말 잘 맞는다는 거…"
    $ renpy.pause(3)

    voice "audio/ch4/ch4_J1_005.mp3"
    J1 "[player_name]야, 나 너 좋아해. 사귀자!"

    "너는 순간 놀랐지만 곧 미소를 지으며 대답했다."

    P "사실 나도 너 좋아했어. 먼저 말해줘서 고마워."

    call hide_J1_happy from _call_hide_J1_happy_13
    call show_J1_excited from _call_show_J1_excited_6
    voice "audio/ch4/ch4_J1_006.mp3"
    J1 "정말? 진짜로? 근데 내가 먼저 말할 줄은 몰랐다. 너도 그렇게 생각하고 있었다니!"

    P "그래. 우리 이제부터 1일이다?"

    voice "audio/ch4/ch4_J1_007.mp3"
    J1 "응! 1일이야!!"

    call hide_J1_excited from _call_hide_J1_excited_6
    $ renpy.pause(2)

    scene ending_J1_1 with fade
    $ renpy.pause(3)
    scene ending_J1_2 with fade
    $ renpy.pause(3)
    scene ending_J1_3 with fade
    $ renpy.pause(3)
    scene ending_J1_4 with fade
    $ renpy.pause(3)

    scene black
    $ renpy.pause(2)
    "잘 플레이 하셨나요?"

    "당신의 히로인은 주하민이었군요. 축하합니다."

    "몰임캠프 사랑의 격전지: 4.5 weeks of love 는 멀티 엔딩이 존재하는 게임이므로 여러번 플레이하시는 걸 추천합니다."

    "그럼 감사합니다. 다음에 또 만나요!"

    jump ending_credits

# 궤도 엔딩
label ending3:
    #TODO 연구실 앞 사진
    scene bg_laboratory
    stop music fadeout 1.0
    play music "audio/bgm_ending_2.mp3" fadein 1.0 loop
    "궤하린 교수는 몰캠 마지막 날에도 여전히 바쁘게 움직이고 있었다."

    call show_G_happy from _call_show_G_happy_10
    voice "audio/ch4/ch4_G_002.mp3"
    G "어? [player_name]? 네가 여기까지 웬일이야?"

    P "교수님, 잠깐 시간 괜찮으세요? 드릴 말씀이 있어서요."

    call hide_G_happy from _call_hide_G_happy_11
    call show_G_sad from _call_show_G_sad_3
    voice "audio/ch4/ch4_G_003.mp3"
    G "(살짝 놀라며) 그래. 무슨 일이야?"

    P "사실... 계속 고민했는데… 아무래도 교수님을 좋아하게 된 것 같아요."
    $ renpy.pause(2)
    "궤하린 교수는 순간 멈칫하더니 조용히 너를 바라봤다."

    voice "audio/ch4/ch4_G_004.mp3"
    G "[player_name]야… 그건 굉장히 중요한 말인데… 진심이야?"

    P "네. 진심이에요. 교수님과 함께한 모든 순간이 너무 소중했어요."

    $ renpy.pause(3)
    voice "audio/ch4/ch4_G_005.mp3"
    G "(잠시 침묵하다가) 나도 사실… 너에게 특별한 감정을 느꼈어. 하지만 내가 교수라는 게 신경 쓰였어."

    call hide_G_sad from _call_hide_G_sad_3
    call show_G_happy from _call_show_G_happy_11
    voice "audio/ch4/ch4_G_006.mp3"
    G "그래도… 너라면… 괜찮을지도 모르겠어."

    P "정말요? 교수님… 아니, 이제부터는 궤도야. 우리 시작하자."
    voice "audio/ch4/ch4_G_007.mp3"
    G "ㅎㅎ 좋아. [player_name], 아니, 이제부턴 나만의 침착맨."

    call hide_G_happy from _call_hide_G_happy_12
    $ renpy.pause(2)

    scene ending_G_1 with fade
    $ renpy.pause(3)
    scene ending_G_2 with fade
    $ renpy.pause(3)
    scene ending_G_3 with fade
    $ renpy.pause(3)
    scene ending_G_4 with fade
    $ renpy.pause(3)

    scene black
    $ renpy.pause(2)
    "잘 플레이 하셨나요?"

    "당신의 히로인은 궤하린이었군요. 축하합니다."

    "몰임캠프 사랑의 격전지: 4.5 weeks of love 는 멀티 엔딩이 존재하는 게임이므로 여러번 플레이하시는 걸 추천합니다."

    "그럼 감사합니다. 다음에 또 만나요!"

    jump ending_credits

# 주우재 엔딩
label ending4:

    show bg_classroom
    stop music fadeout 1.0
    play music "audio/bgm_ending_3.mp3" fadein 1.0 loop
    "주우재는 실습실 문 앞에서 기다리고 있었다."

    call show_J2_excited from _call_show_J2_excited_6
    voice "audio/ch4/ch4_J2_002.mp3"
    J2 "오빠! 드디어 끝났네. 이제 내 차례야."

    P "응? 무슨 차례?"

    voice "audio/ch4/ch4_J2_003.mp3"
    J2 "(꽃다발을 건네며) 나랑 사귀자! 오빠도 나 좋아하잖아."

    P "(놀란 얼굴로) 갑자기? 너… 진심이야?"

    voice "audio/ch4/ch4_J2_004.mp3"
    J2 "응! 나 진심이지. 슈퍼스타가 고백하는데, 오빠가 거절할 리 없잖아."

    P "(웃으며) 그건 그렇지… 좋아. 우리 사귀자."

    voice "audio/ch4/ch4_J2_005.mp3"
    J2 "좋아! 그럼 바로 디저트 먹으러 가자! 내가 쏠게~"

    P "그래그래 알았어"
    call hide_J2_excited from _call_hide_J2_excited_4
    $ renpy.pause(2)

    scene ending_J2_1 with fade
    $ renpy.pause(3)
    scene ending_J2_2 with fade
    $ renpy.pause(3)
    scene ending_J2_3 with fade
    $ renpy.pause(3)
    scene ending_J2_4 with fade
    $ renpy.pause(3)

    scene black

    $ renpy.pause(2)    
    "잘 플레이 하셨나요?"

    "당신의 히로인은 주유재였군요. 축하합니다."

    "몰임캠프 사랑의 격전지: 4.5 weeks of love 는 멀티 엔딩이 존재하는 게임이므로 여러번 플레이하시는 걸 추천합니다."

    "그럼 감사합니다. 다음에 또 만나요!"

    jump ending_credits

# 주우재 엔딩
label ending5:

    show bg_laboratory
    stop music fadeout 1.0
    play music "audio/bgm_ending_1.mp3" fadein 1.0 loop
    "김솔풍을 만나기 위해 연구실 앞으로 향했다."

    P "똑똑똑, 조교님 계시나요?"

    "잠시 뒤 김솔풍이 연구실 앞으로 나왔다."

    call show_K_happy from _call_show_K_happy_8
    voice "audio/ch4/ch4_K_001.mp3"
    K "응? [player_name]. 캠프 끝났는데 아직 안 갔어?"

    P "그 그게 하고 싶은 말이 있어서요."

    "김솔풍은 무언가를 직감한 듯 침을 삼켰다."

    call hide_K_happy from _call_hide_K_happy_11
    call show_K_nervous from _call_show_K_nervous_3
    voice "audio/ch4/ch4_K_002.mp3"
    K "하고 싶은 말? 뭐... 뭐 뭔데?"

    P "저 조교님을 좋아해요!!"

    voice "audio/ch4/ch4_K_003.mp3"
    K "(얼굴이 빨개지며) 뭐.. 뭐라고?"

    P "좋아한다고요. 김솔풍 조교님이랑 연애. 하고 싶어요!"

    P "이번 캠프 동안 정말 친절하게 대해주시고, 제가 성장할 수 있도록 묵묵히 도와주시는 모습이 너무 멋졌어요."

    P "앞으로 조교님과 함께하면 뭐든 할 수 있을 것 같은 기분이 들었어요.."

    voice "audio/ch4/ch4_K_004.mp3"
    K "아..."

    voice "audio/ch4/ch4_K_005.mp3"
    K "그랬구나... [player_name]"

    voice "audio/ch4/ch4_K_006.mp3"
    K "나도 너에게 말 안 했던게 있는데"

    call hide_K_nervous from _call_hide_K_nervous_4
    call show_K_happy from _call_show_K_happy_9
    voice "audio/ch4/ch4_K_007.mp3"
    K "사실 나도 너를 좋아하고 있었어"

    voice "audio/ch4/ch4_K_008.mp3"
    K "처음 경험하는 이 몰입캠프에서 항상 멋지게 해내는 모습을 보고나서 부터 너를 좋아하게 된 것 같아"

    call hide_K_happy from _call_hide_K_happy_12
    call show_K_excited from _call_show_K_excited_5
    voice "audio/ch4/ch4_K_009.mp3"
    K "너만 괜찮다면... 우리 연애할까..?"

    P "정말요? 당연하죠!!!"
    call hide_K_excited from _call_hide_K_excited_3
    $ renpy.pause(2)

    scene ending_K_1 with fade
    $ renpy.pause(3)
    scene ending_K_2 with fade
    $ renpy.pause(3)
    scene ending_K_3 with fade
    $ renpy.pause(3)
    scene ending_K_4 with fade
    $ renpy.pause(3)

    scene black
    $ renpy.pause(2)
    "잘 플레이 하셨나요?"

    "당신의 히로인은 김솔풍이었군요. 축하합니다."

    "몰임캠프 사랑의 격전지: 4.5 weeks of love 는 멀티 엔딩이 존재하는 게임이므로 여러번 플레이하시는 걸 추천합니다."

    "그럼 감사합니다. 다음에 또 만나요!"

    jump ending_credits

label ending_credits:
    window hide
    # 화면 배경색 설정
    scene black with fade
    play music "audio/bgm_ending_1.mp3" fadein 1.0 loop

    # 크레딧 시작 시 바로 스크롤 시작
    show text """
    제작자\n\n\n
    프로그래머     조성원\n
    프로그래머     최주찬\n
    디자이너     조성원\n
    디자이너     최주찬\n
    음향감독     조성원\n
    음향감독     최주찬\n
    미술감독     조성원\n
    미술감독     최주찬\n

    \n\n
    출연진\n\n\n
    침착맨/침채린     이병견\n
    주펄/주하민     주호민\n
    주우재/주유지     주우재\n
    궤도/궤하린     궤도\n
    김풍/김솔풍     김풍\n


    특별 감사\n\n\n
    madcamp 24W\n
    게임을 플레이해주신 당신!\n\n\n

    감사합니다!

    """ at Move((0.39, 1.0), (0.39, -2.0), 15.0)  # 느리게 중앙에서 시작하고 위로 이동

    # 크레딧이 끝날 때까지 대기
    $ renpy.pause(50.0)
    return

