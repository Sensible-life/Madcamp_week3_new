label chapter2:
    hide screen display_likes_ch1
    scene bg_geese with dissolve
    stop music fadeout 1.0
    play music "audio/bgm_daily_7.mp3" fadein 1.0 loop

    voice "audio/ch2/C_001.mp3"
    call show_C_happy from _call_show_C_happy
    C "와, 여기 거위 진짜 많다! 완전 귀여워~!"

    P "너무 가까이 가지 마. 물릴 수도 있다고."

    voice "audio/ch2/C_002.mp3"
    C "에이~ 그런 거였으면 카이스트 사람들이 이미 거위 밥 됐겠지!"

    P "그런 건 아니지만, 그래도 조심하라고..."

    call hide_C_happy from _call_hide_C_happy
    call show_C_surprised from _call_show_C_surprised
    voice "audio/ch2/C_003.mp3"
    C "꺄아아악! 야 [player_name]! 나 거위한테 물릴 뻔했어! 이런 거 미리 말해줬어야지!"

    P "아니, 방금 전에 말했잖아..."

    call hide_C_surprised from _call_hide_C_surprised
    call show_C_angry from _call_show_C_angry
    voice "audio/ch2/C_004.mp3"
    C "몰라! 다 너 때문이야. 어휴, 책임져!"

    voice "audio/ch2/J1_001.mp3"
    call show_J1_happy from _call_show_J1_happy
    Who "안녕~ 오랜만이다, [player_name]."

    P "(이 목소리... 설마!) 너는... 하민이?"

    voice "audio/ch2/J1_002.mp3"
    Who "ㅎㅎ 그래, 나야. 너도 몰캠에 온다고 부모님께 들었는데 진짜였네."

    P "와, 진짜 오랜만이다! 몇 년 만이지? 10년쯤 됐나?"

    voice "audio/ch2/J1_003.mp3" 
    J1 "그 정도 됐나? 시간 참 빠르다. 그런데 옆에 계신 분은 누구야?"

    call hide_C_angry from _call_hide_C_angry
    call show_C_happy from _call_show_C_happy_1
    voice "audio/ch2/C_005.mp3"
    C "저는 침채린이에요. 그런데 그쪽은 누구신데요?"

    voice "audio/ch2/J1_004.mp3"
    J1 "아, 난 주하민이라고 해. [player_name](이)랑 어릴 때부터 친했던 친구야. 반가워."

    voice "audio/ch2/J1_005.mp3"
    J1 "둘이 데이트라도 나온 거야?"

    P "(헉, 뭐야 갑자기!) 아... 아냐아냐... 그런 거 아닌데..."

    call hide_J1_happy from _call_hide_J1_happy
    call show_J1_excited from _call_show_J1_excited
    voice "audio/ch2/J1_006.mp3"
    J1 "뭐 어때. 어차피 오랜만에 만났는데 잠깐 이야기 좀 나눌 수 있을까? 시간 괜찮아?"

    P "어, 어... 괜찮아. 그래, 이야기하자."


    voice "audio/ch2/J1_007.mp3"
    J1 "다행이다! 혹시 무례하게 끼어든 거 아니었나 걱정했거든. ㅎㅎ"

    call hide_C_happy from _call_hide_C_happy_1
    call show_C_angry from _call_show_C_angry_1
    voice "audio/ch2/C_006.mp3"
    C "야!! 너 오늘 나랑 놀기로 했잖아. 왜 네 마음대로 가려고 해?"

    voice "audio/ch2/C_007.mp3"
    C "안 돼. 너 지금 나랑 같이 있어야 해."

    P "아니, 사실 반 억지로 나온 거기도 하고, 오랜만에 친구 본 김에 잠깐..."

    voice "audio/ch2/J1_008.mp3"
    J1 "그럼, [player_name]. 네가 정해. 침채린이랑 계속 놀 거야? 아니면 나랑 이야기할래?"

menu:

    "침채린이랑 놀러 간다.":
        $ like_C += 5
        call hide_J1_excited from _call_hide_J1_excited
        call show_J1_angry from _call_show_J1_angry
        if like_J1 - 5 < 50 and like_J1 >= 50:
            call glitch_J1_angry from _call_glitch_J1_angry
        $ like_J1 -= 5
        jump with_c

    "주하민이랑 놀러 간다.":
        $ like_J1 += 5
        if like_C - 5 < 40 and like_C >= 40:
            call glitch_C_angry from _call_glitch_C_angry
        $ like_C -= 5
        jump with_j1

    "기가 빨렸으니 집에 간다.":
        
        if like_J1 - 5 < 50 and like_J1 >= 50:
            call glitch_J1_excited from _call_glitch_J1_excited
        if like_C - 5 < 40 and like_C >= 40:
            call glitch_C_angry from _call_glitch_C_angry_1
        $ like_J1 -= 5
        $ like_C -= 5
        
        jump going_home


# 침채린 선택 분기
label with_c:
    call hide_C_angry from _call_hide_C_angry_1
    call hide_J1_angry from _call_hide_J1_angry
    call show_J1_sad from _call_show_J1_sad
    call show_C_happy from _call_show_C_happy_2
    voice "audio/ch2/J1_013.mp3"
    J1 "하아... 뭐, 나중에 이야기하자. 할 말이 많았는데 아쉽네."

    call hide_J1_sad from _call_hide_J1_sad
    call hide_C_happy from _call_hide_C_happy_2
    call show_C_excited from _call_show_C_excited
    voice "audio/ch2/C_008.mp3"
    C "역시! 내가 [player_name]을 본 게 얼만데, 네가 날 두고 다른 데 가겠어? ㅎㅎ"

    voice "audio/ch2/C_009.mp3"
    C "자, 거위는 이제 그만 보고 근처 카페나 갈까? 맛있는 거 사줄게~"

    P "아니, 내가 너랑 놀기로 했다고 한 적은 없는데..."
    
    voice "audio/ch2/C_010.mp3"
    C "됐어! 넌 이미 동의했어. 따라와~!"
    # 이후 이벤트 추가 가능
    "(어쩔 수 없이 침채린을 따라가게 되었다)"
    call hide_C_excited from _call_hide_C_excited
    jump date_with_c

label date_with_c:

    scene bg_cafe with dissolve
    stop music fadeout 1.0
    play music "audio/bgm_date_day_1.mp3" fadein 1.0 loop

    "침채린과 [player_name](은)는 근처의 작은 카페로 들어갔다."

    call show_C_happy from _call_show_C_happy_3
    voice "audio/ch2/C_032.mp3"
    C "여기 분위기 진짜 괜찮지 않아? 내가 예전에 우연히 발견했는데, 완전 단골 됐어."

    P "그러네, 생각보다 아늑한데?"

    "침채린이 메뉴판을 보며 신나게 이야기하기 시작했다."

    voice "audio/ch2/C_033.mp3"
    C "음, 나는 초코라떼랑 마카롱 한 세트 먹을래. 너는 뭐 먹을 거야?"

    menu:

        "커피와 케이크를 주문한다.":
            call hide_C_happy from _call_hide_C_happy_3
            call show_C_excited from _call_show_C_excited_1
            $ like_C += 2.5
            P "그럼 나도 커피랑 케이크로 할게. 배도 고프고."

            voice "audio/ch2/C_034.mp3"
            C "오~ 역시 나랑 취향 잘 맞네! 내가 추천한 케이크 완전 맛있어."

            jump cafe_conversation

        "아무거나 주문해달라고 한다.":
            call hide_C_happy from _call_hide_C_happy_4
            call show_C_angry from _call_show_C_angry_2
            if like_C - 5 < 40 and like_C >=40:
                call glitch_C_angry from _call_glitch_C_angry_2
            $ like_C -= 5
            P "아무거나 괜찮아. 네가 추천해줘."

            voice "audio/ch2/C_035.mp3"
            C "아 뭐야~ 재미없게. 그래도 내가 알아서 잘 시켜줄게. 믿어봐!"

            jump cafe_conversation

    label cafe_conversation:

        call hide_C_excited from _call_hide_C_excited_1
        call hide_C_angry from _call_hide_C_angry_2

        call show_C_happy from _call_show_C_happy_4
        "주문한 음료와 디저트가 나왔다."

        voice "audio/ch2/C_036.mp3"
        C "자, 먹어봐! 이 마카롱 진짜 최고야. 내가 먹어본 것 중에서 제일 맛있어."

        P "(한 입 먹으며) 오, 진짜 맛있네. 너가 말한 대로네."

        voice "audio/ch2/C_037.mp3"
        C "그치? 내가 맛있는 거 고르는 건 또 기가 막히지."

        "침채린은 계속해서 몰캠 이야기를 꺼냈다."

        voice "audio/ch2/C_038.mp3"
        C "야, 너 이번 프로젝트 어떡할 거야? 내가 잘 도와줄게, 대신 나중에 보답은 확실히 해라?"

        P "뭐야, 대가성 도움이라니. 그래도 잘 부탁할게."

        call hide_C_happy from _call_hide_C_happy_5
        call show_C_excited from _call_show_C_excited_2
        voice "audio/ch2/C_039.mp3"
        C "오케이~ 그럼 나중에 밥 한 번 사라. 비싼 걸로."

        "둘은 몰캠 생활과 옛 추억에 대해 이야기를 나누며 시간을 보냈다."

    menu:

        "옛날 이야기로 분위기를 부드럽게 만든다.":
            P "근데 너 옛날에 기억나? 동아리에서 나한테 그림 그려주던 거. 그거 은근 잘 그렸었잖아."

            voice "audio/ch2/C_040.mp3"
            C "헉, 너 그거 기억해? 아, 그땐 내가 진짜 순수했는데. 지금은 아니지만 ㅎㅎ"
            call hide_C_excited from _call_hide_C_excited_2
            jump park_walk_c

        "몰캠 프로젝트에 대해 이야기한다.":
            P "그래도 이번 프로젝트는 꽤 재밌는 주제인 것 같아. 너도 기대돼?"

            voice "audio/ch2/C_041.mp3"
            C "응! 근데 너 잘 못 따라올 것 같아서 걱정이야. 내가 많이 도와줘야겠지?"

            P "뭐야, 나 의외로 잘할지도 몰라."
            call hide_C_excited from _call_hide_C_excited_3
            jump park_walk_c

    label park_walk_c:

        scene bg_park with dissolve
        stop music fadeout 1.0
        play music "audio/bgm_date_day_2.mp3" fadein 1.0 loop

        "카페에서 나와 둘은 근처 공원을 산책했다."

        call show_C_happy from _call_show_C_happy_5
        voice "audio/ch2/C_042.mp3"
        C "여기 진짜 좋지 않아? 몰캠 시작하기 전에는 이런 데 한 번도 안 왔거든."

        P "응, 가끔 이렇게 나와서 걷는 것도 나쁘지 않네."

        voice "audio/ch2/C_043.mp3"
        C "야, 나랑 이런 데 걷는 거 영광인 줄 알아라. 너랑은 평생 이런 시간 없을 줄 알았거든."

        P "뭐야, 그게 무슨 소리야. 난 너랑 걷는 거 꽤 괜찮은데?"

        call hide_C_happy from _call_hide_C_happy_6
        call show_C_excited from _call_show_C_excited_3
        voice "audio/ch2/C_044.mp3"
        C "(살짝 웃으며) 그래? 그럼 앞으로 더 자주 같이 다니자. 싫다고는 하지 마라~"

        "둘은 공원을 천천히 걸으며 이야기를 나눴다."
        call hide_C_excited from _call_hide_C_excited_4
        jump goodbye_c

    label goodbye_c:

        scene bg_sunset with dissolve
        stop music fadeout 1.0
        play music "audio/bgm_date_night.mp3" fadein 1.0 loop

        "이제 헤어질 시간이 되었다."

        call show_C_happy from _call_show_C_happy_6
        voice "audio/ch2/C_045.mp3"
        C "오늘 재밌었어. 역시 내가 너 잘 데리고 다녔지?"

        P "뭐, 나쁘지 않았어. 고마워, 재밌었어."

        voice "audio/ch2/C_046.mp3"
        C "오~ 칭찬까지 하네? 좋아, 다음에도 나랑 놀아줄 거지?"

        P "그래, 시간 되면 또 보자."

        voice "audio/ch2/C_047.mp3"
        C "오케이! 그럼 잘 가라, [player_name]~"
        call hide_C_happy from _call_hide_C_happy_7

        "침채린과 헤어진 [player_name](은)는 오늘 하루를 떠올리며 집으로 향했다."

        jump classroom3


# 주하민 선택 분기
label with_j1:

    call hide_C_angry from _call_hide_C_angry_3
    call show_C_sad from _call_show_C_sad
    voice "audio/ch2/C_012.mp3"
    C "진짜 어이없네... [player_name], 나랑 놀기로 해놓고 딴 사람한테 가다니."

    voice "audio/ch2/C_013.mp3"
    C "(다음엔 절대 양보 안 할 거야. 두고 봐...)"
    
    call hide_C_sad from _call_hide_C_sad
    voice "audio/ch2/J1_009.mp3"
    J1 "ㅎㅎ 진짜 고맙다. 그럼 우리 어디 들어가서 이야기 좀 할까?"

    voice "audio/ch2/J1_010.mp3"
    J1 "너 어릴 때 기억나? 우리 자전거 타다 넘어졌던 거... 그때 너 엄청 울었잖아."

    P "야, 그런 얘기는 여기서 왜 꺼내냐! 10년 만에 만났는데..."

    voice "audio/ch2/J1_011.mp3"
    J1 "ㅎㅎ 그래도 오랜만에 보니까 진짜 반갑다. 잘 지내고 있었어?"
    # 이후 이벤트 추가 가능
    P "응, 뭐 그냥... 바쁘게 지냈지. 너는 어때?"

    voice "audio/ch2/J1_018.mp3"
    J1 "나야 항상 똑같지. 근데 진짜 몰캠에서 너 만날 줄은 몰랐다니까."

    "둘은 근처 카페로 자리를 옮겼다."
    call hide_J1_excited from _call_hide_J1_excited_1

    scene bg_cafe with dissolve
    stop music fadeout 1.0
    play music "audio/bgm_date_day_2.mp3" fadein 1.0 loop

    call show_J1_happy from _call_show_J1_happy_1
    voice "audio/ch2/J1_019.mp3"
    J1 "여기 음료 진짜 맛있다고 소문났는데, 뭐 마실래? 내가 쏠게!"

    P "아니야, 내가 살게. 오랜만에 만난 기념으로 내가 대접할게."

    voice "audio/ch2/J1_020.mp3"
    J1 "에이~ 내가 초대한 거니까 내가 살게. 너는 그냥 고르면 돼!"

    P "그럼... 카페라떼 하나?"

    voice "audio/ch2/J1_021.mp3"
    J1 "오케이~ 그럼 나는 딸기 스무디! 조금만 기다려봐."

    call hide_J1_happy from _call_hide_J1_happy_1
    $ renpy.pause(2)
    call show_J1_happy from _call_show_J1_happy_2
    "주하민이 음료를 들고 자리로 돌아왔다."

    voice "audio/ch2/J1_022.mp3"
    J1 "자, 여기! 어때, 맛있어?"

    P "(한 모금 마시며) 응, 맛있다. 네가 추천한 거니까 믿고 마셨지."

    voice "audio/ch2/J1_023.mp3"
    J1 "ㅎㅎ 역시 내 안목은 틀리지 않지. 그나저나, 너 몰캠 어때? 적응 좀 됐어?"

    P "솔직히 처음엔 많이 어색했는데, 이제 좀 괜찮아졌어. 네가 있어서 더 편한 것 같고."

    call hide_J1_happy from _call_hide_J1_happy_2 
    call show_J1_excited from _call_show_J1_excited_1
    voice "audio/ch2/J1_024.mp3"
    J1 "(살짝 웃으며) 정말? 나 때문에 편하다니 기분 좋은데~"

    "둘은 과거 이야기와 몰캠 생활에 대해 이야기를 나누며 시간을 보냈다."

    "대화가 끝난 후, 주하민이 제안했다."

    voice "audio/ch2/J1_025.mp3"
    J1 "야, 여기 근처에 공원 있거든? 산책이나 좀 할래? 앉아만 있었더니 답답하잖아."

    menu:

        "산책하러 간다.":
            $ like_J1 += 10
            jump park_walk

        "그냥 헤어진다.":
            if like_J1 - 5 < 50 and like_J1 >= 50:
                call glitch_J1_excited from _call_glitch_J1_excited_1
            $ like_J1 -= 5

            jump goodbye_j1

    label park_walk:

        call hide_J1_excited from _call_hide_J1_excited_2

        scene bg_park with dissolve
        stop music fadeout 1.0
        play music "audio/bgm_date_day_1.mp3" fadein 1.0 loop

        "[player_name]와 주하민은 공원을 산책하며 더 많은 이야기를 나누었다."

        call show_J1_excited from _call_show_J1_excited_2
        voice "audio/ch2/J1_026.mp3"
        J1 "여기 진짜 예쁘지 않냐? 어릴 때는 이런 데 올 일이 별로 없었는데, 이제는 이런 시간이 소중하게 느껴져."

        P "그러게. 가끔은 이렇게 쉬어가는 것도 필요한 것 같아."

        voice "audio/ch2/J1_027.mp3"
        J1 "너랑 이렇게 걷는 거, 꽤 괜찮은데? 다음에도 또 같이 오자."

        P "좋아. 나도 재밌었어."

        "둘은 공원 벤치에 잠시 앉아 이야기를 나누며 시간을 보냈다."

        voice "audio/ch2/J1_028.mp3"
        J1 "오늘 진짜 재밌었어. 다음엔 내가 더 맛있는 데 데려가 줄게!"

        P "그래, 기대할게."

        call hide_J1_excited from _call_hide_J1_excited_3
        jump goodbye_j1

    label goodbye_j1:

        scene bg_sunset with dissolve
        stop music fadeout 1.0
        play music "audio/bgm_date_night.mp3" fadein 1.0 loop

        "주하민과 헤어질 시간이 되었다."
        call show_J1_happy from _call_show_J1_happy_3
        voice "audio/ch2/J1_029.mp3"
        J1 "오늘 진짜 즐거웠다. 몰캠 끝날 때까지 종종 보자고!"

        P "나도 재밌었어. 다음에 또 보자."

        voice "audio/ch2/J1_030.mp3"
        J1 "오케이~ 그럼 잘 가! 집 들어가서 푹 쉬고~"

        "주하민과 헤어진 [player_name]는 오늘 하루를 떠올리며 집으로 향했다."

        jump classroom3


# 집으로 가는 선택 분기
label going_home:
    
    P "(아, 오늘 정말 기가 빨린다. 그냥 집에 가서 쉬고 싶어.)"

    P "미안, 둘 다. 난 오늘 좀 피곤해서 먼저 갈게."
    
    voice "audio/ch2/C_011.mp3"
    C "야, [player_name]! 너 뭐야? 나랑 놀기로 해놓고 그냥 간다고?"

    call hide_J1_excited from _call_hide_J1_excited_4
    call show_J1_sad from _call_show_J1_sad_1
    voice "audio/ch2/J1_012.mp3"
    J1 "괜찮아, [player_name]. 무리하지 말고 잘 쉬어."

    P "다음에 다시 보자. 둘 다 미안..."

    P "(진짜 이런 날은 일찍 자는 게 답이다...)"
    # 이후 이벤트 추가 가능
    jump classroom3


label classroom3:

    scene bg_N1_117 with fade
    stop music fadeout 1.0
    play music "audio/bgm_daily_5.mp3" fadein 1.0 loop
    "2주차 강연 시간이 되었다."

    "같은 분반인 침채린과 옆자리에서 강연을 듣게 되었다."

    call show_K_happy from _call_show_K_happy

    voice "audio/ch2/K_001.mp3"
    K "열심히 준비했는데 애들이 재미있어 하면 좋겠다. 특히...[player_name]...아이, 내가 무슨 말을;;"

    "학생들이 강의실로 하나둘 들어온다."

    call show_C_happy from _call_show_C_happy_7
    voice "audio/ch2/C_014.mp3"
    C "조교님, 안녕하세요! 지난번에 밥은 정말 잘 먹었어요!"

    voice "audio/ch2/K_002.mp3"
    K "그래, 안녕. 얼른 자리 잡고 앉아. 오늘 강연은 내가 준비했는데, 잘 맞았으면 좋겠다."

    "강연 시작 30분 후..."

    call hide_K_happy from _call_hide_K_happy
    call hide_C_happy from _call_hide_C_happy_8
    call show_C_angry from _call_show_C_angry_3
    voice "audio/ch2/C_015.mp3"
    C "야, 진짜 재미없지 않냐? 나 더 이상 못 듣겠어. 우리 몰래 나가자."

    P "아니, 그렇긴 한데... 그래도 김솔풍 조교님이 열심히 준비하신 건데 우리가 나가면 좀 그렇잖아. 예의가 아니잖아."

    voice "audio/ch2/C_016.mp3"
    C "(주변을 둘러보며) 야, 저기 옆 애들 안 보이냐? 다 졸고 있잖아. 이 정도면 우리 나가도 문제없지 않냐? 인정? 나가자~"

    call show_K_nervous from _call_show_K_nervous
    "그 순간, 김솔풍과 눈이 마주친다. 김솔풍이 살짝 웃으며 고개를 끄덕인다."
    $ renpy.pause(1)
    menu:
        "침채린과 몰래 나간다":
            $ like_C += 2.5
            if like_K - 5 < 45 and like_K >= 45:
                call glitch_K_nervous from _call_glitch_K_nervous
            $ like_K -= 5
            $ run = True
            jump sneak_out

        "끝까지 강연을 듣는다":
            if like_C - 5 < 40 and like_C >= 40:
                call glitch_C_angry from _call_glitch_C_angry_3
            $ like_C -= 5
            $ like_K += 5
            $ run = False
            jump stay

# 침채린과 몰래 나가는 선택지
label sneak_out:

    scene bg_N1_outside with dissolve
    stop music fadeout 1.0
    play music "audio/bgm_daily_3.mp3" fadein 1.0 loop
    "침채린과 함께 강의실을 몰래 빠져나왔다."

    call show_C_happy from _call_show_C_happy_8
    voice "audio/ch2/C_017.mp3"
    C "봐봐! 내가 너를 제대로 구출한 거야. 나 없었으면 너 이 강의 끝까지 들었겠지? ㅋㅋ"

    P "(살짝 찔리지만... 어쩐지 나도 속이 시원하다.)"

    scene bg_park with dissolve
    stop music fadeout 1.0
    play music "audio/bgm_date_day_1.mp3" fadein 1.0 loop
    "둘은 캠퍼스 한쪽에 있는 작은 벤치에 앉아 가벼운 대화를 나눴다."

    call show_C_happy from _call_show_C_happy_9

    voice "audio/ch2/C_018.mp3"
    C "근데 [player_name], 나중에 우리 몰입캠프 끝나면 뭘 하고 싶어? 난 여행 같은 거 가고 싶은데~"

    P "음... 아직 특별히 생각해본 건 없는데, 몰캠 끝나면 뭔가 배우거나 개발해보고 싶어."

    voice "audio/ch2/C_019.mp3"
    C "흠, 역시 너답다. 그럼 나랑도 놀아줘라. 약속한 거다!"

    "침채린은 활짝 웃으며 손가락을 걸었다. 어쩐지 이런 소소한 시간이 즐겁게 느껴졌다."

    jump end


# 끝까지 강연을 듣는 선택지
label stay:

    scene bg_N1_outside with dissolve
    stop music fadeout 1.0
    play music "audio/bgm_daily_3.mp3" fadein 1.0 loop
    "강연이 끝나고, 학생들이 하나둘 강의실을 빠져나갔다. 자리에서 일어나니 김솔풍과 주하민이 강의실 뒤쪽에서 다가오는 것이 보인다."

    call show_K_excited from _call_show_K_excited
    if like_J1 >= 50:
        show J1_happy at left, fade_in:
            zoom 0.75
    else:
        show Jooperl_happy at left, fade_in:
            zoom 0.75
    
    #위치 겹쳐서 얘는 따로 넣음
    voice "audio/ch2/K_003.mp3"
    K "끝까지 들어줘서 고마워, [player_name]. 오늘 강연 어땠어? 솔직하게 말해도 괜찮아!"

    "주하민이 옆에서 흥미로운 표정으로 내 대답을 기다리고 있었다."

    menu:
        
        "논리정연하게 강연에 대한 단점을 말한다":
            if like_K - 10 < 45 and like_K >= 45:
                call glitch_K_excited from _call_glitch_K_excited_1
            $ like_K -= 10
            

            P "조교님, 강연은 전체적으로 좋았는데 몇몇 부분에서 내용이 조금 어려웠던 것 같아요. 예를 들면 사례가 부족해서 공감하기 어려웠다고 느꼈어요."

            call hide_K_excited from _call_hide_K_excited
            call show_K_nervous from _call_show_K_nervous_1
            voice "audio/ch2/K_004.mp3"
            K "(살짝 당황한 표정) 아, 그런가? 다음엔 좀 더 쉽게 설명할 수 있도록 노력해야겠네. 피드백 고마워."

            call hide_J1_happy from _call_hide_J1_happy_3
            $ like_J1 += 10
            if like_J1 >= 50:
                show J1_excited at left, fade_in:
                    zoom 0.75
            else:
                show Jooperl_excited at left, fade_in:
                    zoom 0.75
            voice "audio/ch2/J1_014.mp3"
            J1 "와, [player_name] 네가 이런 걸 말할 줄이야. 역시 성실한 모습은 여전하네."

            "김솔풍은 살짝 아쉬운 표정을 지었지만, 진지하게 경청하는 모습이었다."

            jump end

        "눈치보며 마지못해 좋았다고 말한다.":
            $ like_K += 5

            if like_J1 - 10 < 50 and like_J1 >= 50:
                call glitch_J1_happy_left from _call_glitch_J1_happy_left
            $ like_J1 -= 10

            P "아, 네! 정말 좋았어요. 특히 마지막 정리 부분이 기억에 남아요."

            voice "audio/ch2/K_005.mp3"
            K "정말? 다행이다! 다음에도 재미있고 유익한 강연을 준비할게."

            call hide_J1_happy from _call_hide_J1_happy_4
            if like_J1 >= 50:
                show J1_sad at left:
                    zoom 0.75
            else:
                show Jooperl_sad at left:
                    zoom 0.75
            voice "audio/ch2/J1_015.mp3"
            J1 "(작은 목소리로) 음, 네 대답 너무 의례적인 거 아니냐? 뭐, 네가 그럴 수도 있지."

            "김솔풍은 미소를 지으며 만족스러워 보였고, 주하민은 살짝 의심스러운 표정이었다."

            jump end


# 강연 후 공통 파트
label end:

    scene bg_poster with dissolve

    stop music fadeout 1.0
    play music "audio/bgm_daily_7.mp3" fadein 1.0 loop
    "강연이 끝난 후, 강의실을 나서다 복도 벽면에 붙어 있는 연구실 홍보 포스터를 발견했다."

    if run == True:

        call show_C_happy from _call_show_C_happy_10
        voice "audio/ch2/C_020.mp3"
        C "야, [player_name]! 이거 봐봐! 연구실에서 뭔가 엄청 재미있는 거 하는 것 같은데, 우리도 한번 구경 가볼래?"

        P "음... 신청 안 하고 가도 되는 건가?"

        voice "audio/ch2/C_021.mp3"
        C "여기 써 있잖아. 누구나 환영한다고. 다음주에 시간 맞춰서 한번 가보자!"

        P "(침채린이 이렇게 적극적인 모습이라니, 나름 새롭다. 한번 가보는 것도 좋을 것 같다.)"

    else:

        call show_J1_happy from _call_show_J1_happy_4
        voice "audio/ch2/J1_016.mp3"
        J1 "어, 이거 봐. 너 어릴 때부터 이런 거 관심 많았잖아. 다음주에 한다는데, 한번 가보자."

        P "어? 진짜? 좋아, 나도 이런 쪽은 항상 흥미가 있었어. 같이 가자!"

        voice "audio/ch2/J1_017.mp3"
        J1 "좋아, 역시 [player_name] 너는 이런 게 딱이야."

        P "(주하민과 이런 기회로 연결될 줄은 몰랐는데... 기대된다.)"

    "연구실 포스터를 본 뒤, 네 마음엔 새롭게 무언가에 도전하고 싶은 의욕이 생겨났다."

    "그렇게 몰입캠프의 하루가 마무리되어 갔다."

label restaurant_event:

    scene bg_restaurant with dissolve
    stop music fadeout 1.0
    play music "audio/bgm_daily_2.mp3" fadein 1.0 loop

    "[player_name](은)는 주말에 식당 알바를 하고 있다. 평소처럼 조용한 날이었다."

    "그러다 갑작스럽게 들려오는 다소 격한 대화 소리. 고개를 돌리자 싸우고 있는 커플이 눈에 들어온다."

    "직업적인 책임감에 다가가 상황을 확인하려는 순간, 남자가 화장실로 향하며 자리를 비운다."

    "[player_name](은)는 이 틈을 타 여자를 향해 조심스럽게 말을 건다."

    P "저기, 혹시 무슨 일이신가요? 다른 손님들께서 불편해하셔서 목소리를 조금만 낮춰주시면 감사하겠습니다."

    call show_G_sad from _call_show_G_sad
    voice "audio/ch2/G_001.mp3"
    G "(미안한 표정으로) 아... 죄송해요. 개인적인 일이 있어서요."

    P "(얼핏 보니 이 사람... 저번에 학교에서 본 포스터 속의 궤하린 교수 아닌가?) 왜 이런 곳에서 싸우고 계신 거지...?"

    voice "audio/ch2/G_002.mp3"
    G "(주저하며) 그런데... 혹시 저 좀 도와주실 수 있나요?"

    P "네? 어떤 일인지 말씀해 주시면…"

    voice "audio/ch2/G_003.mp3"
    G "아까 화장실에 간 남자가, 얼마 전에 이별한 전 남자친구인데요. 지금까지 괴롭히고 있어서요... 부탁드릴게요."

    "그때 남자가 화장실에서 돌아왔다. 상황이 한층 긴장감으로 가득 찬다."

    voice "audio/ch2/M_001.mp3"
    "남자 1" "이봐, 당신 뭐야? 왜 여기 서 있는 거야?"

    P "(침착하게) 다른 손님들께서 시끄럽다고 컴플레인이 들어와서요. 목소리를 조금 낮춰주시면 감사하겠습니다."

    voice "audio/ch2/G_004.mp3"
    G "(남자를 향해) 제 남자친구예요. 이미 말했잖아요. 남자친구 있다고. 오늘 여기까지 나와 달라고 한 이유도 그걸 증명하려고 해서예요."

    voice "audio/ch2/M_002.mp3"
    "남자 1" "뭐? 이렇게 어린애가 네 남자친구라고? 웃기지 마라."

    voice "audio/ch2/M_003.mp3"
    "남자 1" "야, 알바생. 네가 말해봐. 진짜 네 여자친구냐?"

    "궤하린 교수가 간절한 눈빛으로 [player_name]를 바라본다."

menu:

    "궤하린 교수를 돕는다.":
        $ like_G += 5
        jump professorHelp

    "상황에 끼어들지 않는다.":
        if like_G - 5 < 50 and like_G >= 50:
            call glitch_G_sad from _call_glitch_G_sad
        $ like_G -= 5
        jump ignore_situation

label professorHelp:

    P "맞...맞습니다. 제가 그녀의 남자친구입니다. 아직 부족하지만, 정말 소중한 사람입니다."

    P "그러니 그만 가주세요. 지금 당장 가지 않으시면 경찰에 신고하겠습니다."

    "남자는 한동안 침묵하더니, 결국 화난 얼굴로 자리를 떠났다."

    voice "audio/ch2/M_004.mp3"
    "남자 1" "에이, 재수가 없으려니까. 그래 간다 가."

    call hide_G_sad from _call_hide_G_sad
    call show_G_happy from _call_show_G_happy
    voice "audio/ch2/G_005.mp3"
    G "(안도의 한숨을 내쉬며) 정말 감사합니다. 덕분에 큰일 날 뻔한 상황을 막았네요."

    P "아니에요. 제가 잘했는지는 모르겠지만, 도움이 되셨다니 다행이에요."

    voice "audio/ch2/G_006.mp3"
    G "그런데... 혹시 다음에도 도와줄 수 있을까요? 15일에 또 만날 일이 있을 것 같아서요."

    menu:

        "도와주겠다고 약속한다.":
            $ like_G += 5
            P "아... 알겠습니다. 도와드릴게요."
            jump car

        "도움 대신 연구실 구경을 요청한다.":
            $ like_G += 10
            P "그럼, 제가 도와드리는 대신 교수님 연구실을 구경해도 될까요?"

            call hide_G_happy from _call_hide_G_happy
            call show_G_sad from _call_show_G_sad_1
            voice "audio/ch2/G_007.mp3"
            G "(놀란 표정) 어? 그걸 어떻게 알았죠? 혹시 우리 학교 학생인가요?"

            P "네... 사실 캠퍼스에서 포스터를 보고 교수님을 알게 되었어요."

            voice "audio/ch2/G_008.mp3"
            G "(고민하며) 알겠어요. 하지만 다른 사람들에게는 비밀이에요. 약속해요."

            jump car

label ignore_situation:

    P "(상황이 너무 복잡하다. 괜히 끼어들었다간 더 큰 일이 생길지도 모른다.)"

    "남자는 돌아왔지만, 궤하린 교수는 침착하게 대응했다. 결국 몇 분 후 남자는 자리를 떠났다."

    call show_G_sad from _call_show_G_sad_2
    "궤하린 교수는 약간의 실망스러운 표정으로 [player_name]에게 감사 인사를 건넸다."

    voice "audio/ch2/G_009.mp3"
    G "그래도 다행이에요. 신경 써주셔서 감사합니다."

    P "아니에요. 도움이 많이 되지 못해 죄송해요."

    jump lab_visit

label car:

    call hide_G_sad from _call_hide_G_sad_1
    call show_G_happy from _call_show_G_happy_1
    voice "audio/ch2/G_010.mp3"
    G "오늘은 제가 차로 학교까지 데려다 줄게요. 이왕 도와주셨으니 제가 감사 표시라도 해야죠."

    P "정말요? 괜찮으시다면... 감사합니다."

    scene bg_car with dissolve
    "학교로 향하는 길, 궤하린 교수는 조심스럽게 자신의 이야기를 조금씩 꺼내기 시작했다."
    # 차 안 사진 추가 필요
    
    call show_G_happy from _call_show_G_happy_2
    voice "audio/ch2/G_011.mp3"
    G "솔직히 말하면, 오늘 당신 덕분에 정말 큰 도움을 받았어요. 다음에도 부탁드릴게요."

    P "네, 교수님. 저도 언제든 돕겠습니다."

    jump lab_visit

label lab_visit:

    scene bg_laboratory with dissolve
    stop music fadeout 1.0
    play music "audio/bgm_daily_7.mp3" fadein 1.0 loop

    "며칠 뒤, 침채린과 주하민의 권유로 궤하린 교수의 연구실 탐방을 함께 가기로 했다."

    "셋은 캠퍼스 한쪽에 위치한 연구실 앞에서 발걸음을 멈췄다."

    call show_C_happy from _call_show_C_happy_11
    call show_J1_happy from _call_show_J1_happy_5
    voice "audio/ch2/C_022.mp3"
    C "어, 여기다! 궤하린 교수의 뼈 치킨 연구실! 이름 진짜 독특하지 않아?"

    voice "audio/ch2/J1_031.mp3"
    J1 "그러게. [player_name], 얼른 가보자. 이런 연구실 체험은 진짜 흔치 않은 기회야."
    call hide_C_happy from _call_hide_C_happy_9
    call hide_J1_happy from _call_hide_J1_happy_5
    "문을 두드리자 안에서 발소리가 들려왔다. 문이 열리고 궤하린 교수가 얼굴을 내밀었다."
    
    if like_G >= 50:
        show G_sad at center, fade_in:
            zoom 0.75
    else:
        show Gdo_sad at center, fade_in:
            zoom 0.75
    
    # center는 정의가 안 되어 있어서 이대로 추가함
    voice "audio/ch2/G_012.mp3"
    G "(살짝 놀란 표정으로) 어? [player_name]...? 여긴 어쩐 일이야?"

    P "(살짝 당황하며) 아, 친구들이 연구실 구경하고 싶다고 해서... 저도 같이 오게 됐어요."

    call show_C_angry from _call_show_C_angry_4
    voice "audio/ch2/C_023.mp3"
    C "(눈을 가늘게 뜨며) 근데 교수님, 왜 [player_name] 보고 웃으세요? 둘이 아는 사이예요?"

    call show_J1_surprised from _call_show_J1_surprised
    voice "audio/ch2/J1_032.mp3"
    J1 "흠... 그러게. [player_name], 너 궤하린 교수님 처음 뵙는 거 아니야?"

    P "(속마음) 차마 교수님의 전 남친 퇴치에 동원됐다고 말할 순 없지. 얘네가 알면 평생 놀릴 게 뻔하잖아."

    P "(겉으로는 태연하게) 아, 뭐... 그냥 반가운 미소겠지. 저도 처음 뵙는 것 같아요."

    call hide_G_sad from _call_hide_G_sad_2
    if like_G >= 50:
        show G_happy at center:
            zoom 0.75
    else:
        show Gdo_happy at center:
            zoom 0.75
    call hide_C_angry from _call_hide_C_angry_4
    if like_C >= 40:
        show C_happy at left:
            zoom 0.75
    else:
        show ChimChak_happy at left:
            zoom 0.75
    "궤하린 교수는 대답 대신 미소를 지으며 셋을 연구실 안으로 안내했다."

    show bg_laboratory_inside with dissolve
    stop music fadeout 1.0
    play music "audio/bgm_daily_5.mp3" fadein 1.0 loop

    "연구실 안은 최신 장비들로 가득했고, 김솔풍 조교가 책상에서 서류를 정리하고 있었다."
    call hide_G_happy from _call_hide_G_happy_1
    call hide_J1_surprised from _call_hide_J1_surprised
    call hide_C_happy from _call_hide_C_happy_10
    call show_K_happy from _call_show_K_happy_1
    K "어? 너희들 여긴 어쩐 일이야? [player_name] 너는 여기까지 구경 오다니 의외네~"

    P "(어색한 미소를 지으며) 아, 그냥 친구들이 오자고 해서요."

    if like_G >= 50:
        show G_happy at center, fade_in:
            zoom 0.75
    else:
        show Gdo_happy at center, fade_in:
            zoom 0.75
    voice "audio/ch2/G_013.mp3"
    G "(미소) 마침 시간 괜찮으니 구경하면서 질문 있으면 편하게 해."

    call show_C_happy from _call_show_C_happy_12
    voice "audio/ch2/C_024.mp3"
    C "교수님, 연구실 이름이 뼈 치킨이라니... 진짜 치킨 연구하시는 거예요?"

    voice "audio/ch2/G_014.mp3"
    G "(웃으며) 아니야. AI와 로봇 자동화 관련 프로젝트를 진행 중이야. 이름은 단순히 내부 유머일 뿐이야."

    "김솔풍이 열정적으로 연구실의 주요 프로젝트를 설명했다."

    K "이 프로젝트는 제가 맡고 있는데, 나중에 너희도 참여할 기회가 있을지도 몰라. 기대해 봐!"

    menu:

        "궤하린 교수와 대화를 나눈다.":
            
            call hide_K_happy from _call_hide_K_happy_1
            call hide_G_happy from _call_hide_G_happy_2
            $ like_G += 7.5
            call show_G_happy from _call_show_G_happy_3
            P "교수님, 아까 말씀하신 프로젝트 정말 흥미로워요. 나중에 참여할 방법이 있을까요?"

            voice "audio/ch2/G_015.mp3"
            G "(살짝 놀라며) 그래? 네가 관심이 있다면 충분히 기회가 있을 거야. 자세한 건 차차 얘기하자."

            call show_C_happy from _call_show_C_happy_13
            voice "audio/ch2/C_025.mp3"
            C "뭐야~ [player_name] 너 교수님한테 아부하는 거야?"

            P "(웃으며) 아부라니, 진심이야. 연구 주제가 정말 멋지잖아."

            jump after_lab

        "김솔풍 조교에게 질문한다.":
            call hide_C_happy from _call_hide_C_happy_11
            if like_G >= 50:
                show G_happy at left, fade_in:
                    zoom 0.75
            else:
                show Gdo_happy at left, fade_in:
                    zoom 0.75
            $ like_K += 5
            P "조교님, 아까 말씀하신 프로젝트 정말 멋져 보였어요. 저도 나중에 참여할 수 있을까요?"

            K "(환한 미소로) 그럼! 너처럼 열정 있는 학생이라면 언제든 환영이야."

            voice "audio/ch2/G_016.mp3"
            G "(옆에서) 풍이가 너를 굉장히 높게 평가하는 것 같네. 기대된다."

            jump after_lab

        "침채린과 주하민과 대화를 나눈다.":
            $ like_C += 2.5
            $ like_J1 += 2.5
            if like_G >= 50:
                show G_happy at center, fade_out:
                    zoom 0.75
            else:
                show Gdo_happy at center, fade_out:
                    zoom 0.75
            call hide_K_happy from _call_hide_K_happy_2
            call show_C_happy from _call_show_C_happy_14
            call show_J1_happy from _call_show_J1_happy_6
            voice "audio/ch2/C_026.mp3"
            C "[player_name], 봤지? 나랑 너 진짜 연구실에서 완벽한 팀이 될 수 있을 것 같아!"

            voice "audio/ch2/J1_033.mp3"
            J1 "뭐래~ [player_name](은)는 나랑 더 잘 맞을걸. [player_name], 나중에 같이 프로젝트 하면 재밌겠다, 그치?"

            P "(둘의 티격태격을 보며 웃는다) 그래, 나중에 다 같이 하면 재밌을 것 같아."

            jump after_lab

label after_lab:

    stop music fadeout 1.0
    scene bg_laboratory with dissolve
    play music "audio/bgm_daily_7.mp3" fadein 1.0 loop
    "탐방이 끝난 후, 궤하린 교수와 김솔풍은 너희를 배웅하며 따뜻한 인사를 건넸다."

    if like_K >= 45:
        show K_happy at left, fade_in:
            zoom 0.75
    else:
        show KPoong_happy at left, fade_in:
            zoom 0.75
    # 여기도 예외처리 둘 다 오른쪽임
    call show_G_happy from _call_show_G_happy_4
    voice "audio/ch2/G_017.mp3"
    G "오늘 와줘서 고마워. 다음에 또 기회 되면 놀러 와."

    K "맞아! 우리 연구실은 언제든 열려 있으니까 부담 갖지 말고~"

    "연구실을 나서며 너는 궤하린 교수와 김솔풍 조교의 연구와 열정에 대해 다시 한번 생각하게 되었다."

    call hide_K_happy from _call_hide_K_happy_3
    call hide_G_happy from _call_hide_G_happy_3
    call show_C_happy from _call_show_C_happy_15
    call show_J1_happy from _call_show_J1_happy_7
    voice "audio/ch2/C_027.mp3"
    C "야 [player_name], 오늘 진짜 재밌지 않았냐? 나중에 우리도 저런 멋진 연구 하면 좋겠다!"

    voice "audio/ch2/J1_034.mp3"
    J1 "그러게. [player_name], 나중에 우리 연구실 한 번 들어가 보는 것도 좋을 것 같아. 네가 잘 어울릴 것 같아."

    P "(미소를 지으며) 그래. 오늘은 정말 많은 걸 배우고 느낀 날이었어."

    jump presentation_prep

label presentation_prep:

    scene bg_classroom with dissolve
    stop music fadeout 1.0
    play music "audio/bgm_daily_1.mp3" fadein 1.0 loop

    "2주차 발표를 위해 팀원들이 실습실에 모였다."

    call show_C_q from _call_show_C_q
    call show_J1_q from _call_show_J1_q
    voice "audio/ch2/C_028.mp3"
    C "야 [player_name], 우리가 주제를 정하긴 했는데 자료가 너무 부족하지 않냐?"

    voice "audio/ch2/J1_035.mp3"
    J1 "맞아. 우리가 준비한 내용은 아직 너무 추상적이야. 좀 더 구체적으로 정리해야 해."

    P "그래. 그러면 각자 생각나는 아이디어를 모아서 다시 정리해 보자. 뭔가 재미있고 독창적인 걸 넣으면 좋을 것 같은데."

    "팀원들이 서로 의견을 주고받으며 발표 자료를 준비하기 시작했다."

    voice "audio/ch2/C_029.mp3"
    C "근데 이렇게 하면 시간이 너무 오래 걸릴 것 같아. [player_name], 네가 정리 좀 해줄래?"

    voice "audio/ch2/J1_036.mp3"
    J1 "좋아. 그러면 [player_name]가 정리하는 동안, 우리는 추가 자료를 찾아볼게."

    "발표 자료를 정리하는 과정에서, 카드 뒤집기 미니게임이 시작된다."

    jump card_game_start

label card_game_start:

    call hide_J1_q from _call_hide_J1_q
    call hide_C_q from _call_hide_C_q
    "발표 자료를 정리하려면 아이디어 카드를 매칭해야 한다."

    "카드는 총 16장으로 구성되어 있으며, 같은 내용의 카드를 두 개씩 매칭하면 완료된다."

    stop music fadeout 1.0
    play music "audio/bgm_minigame_card.mp3" fadein 1.0 loop
    call memoria_game from _call_memoria_game
    stop music fadeout 1.0
    play music "audio/bgm_daily_1.mp3" fadein 1.0 loop
    # 미니게임 구현
    # 카드 뒤집기 로직을 여기에 추가합니다. 간단히 성공/실패 여부로 결정.
    # minigame_success = renpy.random.choice([True, False])  # 랜덤으로 성공/실패 (테스트용)

    if minigame_success:
        "카드를 모두 맞췄다! 발표 자료가 훨씬 완성도 높아졌다."

    else:
        "카드 매칭에 실패했다. 자료가 약간 어수선하게 정리되었다."

    "발표 자료 정리가 끝났다. 팀원들이 준비 상황을 확인하기 위해 모였다."

    jump presentation_day

label presentation_day:

    scene bg_N1_117 with fade
    stop music fadeout 1.0
    play music "audio/bgm_daily_7.mp3" fadein 1.0 loop

    "드디어 2주차 발표 날이 되었다. 팀원들은 긴장된 표정으로 발표를 준비했다."

    call show_C_sad from _call_show_C_sad_1
    call show_J1_sad from _call_show_J1_sad_2
    voice "audio/ch2/C_030.mp3"
    C "야 [player_name], 우리 발표 진짜 잘해야 돼. 금픽으로 뽑히기에는 엄청 까다롭다는 소문 들었지?"

    voice "audio/ch2/J1_037.mp3"
    J1 "맞아. 하지만 우리 준비 많이 했잖아. 침착하게 하면 잘할 수 있을 거야."

    "팀원들이 무대에 올라 발표를 시작했다."

    if minigame_success:
        "발표가 성공적으로 진행되었다! 교수님들과 학생들이 박수를 보낸다."
        P "(뿌듯한 미소로) 우리가 해냈어!"
        "발표가 끝난 후 팀원들은 실습실로 돌아갔다."

        call hide_C_sad from _call_hide_C_sad_1
        call hide_J1_sad from _call_hide_J1_sad_1

        $ like_C += 5
        $ like_J1 += 5
    else:
        "발표 도중 약간의 실수가 있었지만, 큰 문제 없이 마무리되었다."
        P "(아쉬운 표정으로) 다음엔 더 잘할 수 있을 거야..."
        call hide_C_sad from _call_hide_C_sad_2
        call hide_J1_sad from _call_hide_J1_sad_2
        if like_C - 5 < 40 and like_C >= 40:
            call glitch_C_happy from _call_glitch_C_happy
        if like_J1 - 5 < 50 and like_J1 >= 50:
            call glitch_J1_happy from _call_glitch_J1_happy

        "발표가 끝난 후 팀원들은 실습실로 돌아갔다."

        $ like_C -= 5
        $ like_J1 -= 5

    
    call show_C_excited from _call_show_C_excited_4
    call show_J1_excited from _call_show_J1_excited_3
    voice "audio/ch2/C_031.mp3"
    C "야~ 그래도 우리 꽤 괜찮게 하지 않았냐? 다음엔 더 잘할 수 있을 거야!"

    voice "audio/ch2/J1_038.mp3"
    J1 "응, 이번 경험을 바탕으로 다음 발표는 더 완벽하게 준비하자."

    P "(오늘 하루도 많은 걸 배웠다. 다음주가 더 기대된다.)"

    jump chapter2_end

label chapter2_end:
    scene bg_ch2_end with fade

    # 스크린 표시
    show screen display_likes_ch2
    
    "두번째 챕터가 마무리되었습니다"

    "남은 챕터도 잘 진행해보세요."
    jump chapter3
