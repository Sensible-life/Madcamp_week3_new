label chapter3:
    hide screen display_likes_ch2
    stop music fadeout 1.0
    play music "audio/bgm_daily_6.mp3" fadein 1.0 loop
    scene bg_classroom with dissolve

    "3주차 발표 전 날 아침... 실습실로 향하고 있다."

    "실습실 문 앞을 보니 주하민이 군것질거리들을 들고 기웃거리고 있다."

    call show_J1_q from _call_show_J1_q_1
    P "호민아, 안녕! 우리 반에는 무슨 일이야?"

    voice "audio/ch3/J1_001.mp3"
    J1 "아, 그게... 사실 이 반에 내 사촌 동생이 있어서 간식 좀 가져다주려고."

    voice "audio/ch3/J1_002.mp3"
    J1 "얘가 입이 좀 짧아서 밥은 잘 안 먹고 과자만 먹거든."

    P "사촌 동생? 누군데?"

    voice "audio/ch3/J1_003.mp3"
    J1 "흐음, 네가 직접 맞춰볼래? 네 반 친구들 중 한 명이야!"
    
    P "(우리 반 친구들 중 한 명이라니... 도대체 누굴까?)"

    # 미니게임 시작
    # 두더지 게임
    "깜짝 미니게임!! 혼란한 상황에서 하민이의 사촌동생을 찾아보세요!"

    "바로 시작합니다."

    python:
        _game_menu_screen = None
        your_points = 0
        which_h = 0
        which_v = 0
        misses = 3
        is_mole = True
        mole_or_not = [True]
        game_success = [False]

    play music "audio/bgm_minigame_mole.mp3" fadein 1.0 loop
    call start_game from _call_start_game


label correct_guess:
    scene bg_classroom with dissolve
    stop music fadeout 1.0
    play music "audio/bgm_daily_6.mp3" fadein 1.0 loop
    call hide_J1_q from _call_hide_J1_q_1
    call show_J1_happy from _call_show_J1_happy_8
    voice "audio/ch3/J1_004.mp3"
    J1 "정답이야! 역시 [player_name], 넌 눈치가 빠르구나."

    P "와, 진짜 유재가 너 사촌동생이었다니. 왜 이제야 말한 거야?"

    call show_J2_happy from _call_show_J2_happy
    voice "audio/ch3/J2_001.mp3"
    J2 "ㅎㅎ 제가 숨기려고 한 건 아니에요. 그냥 사람들이 잘 모르길래..."

    P "그렇구나. 어쨌든 알아서 다행이다."

    $ like_J2 += 10
    jump after_guess

label failed_guess:
    scene bg_classroom with dissolve
    stop music fadeout 1.0
    play music "audio/bgm_daily_6.mp3" fadein 1.0 loop
    call hide_J1_q from _call_hide_J1_q_2
    call show_J1_happy from _call_show_J1_happy_9
    voice "audio/ch3/J1_005.mp3"
    J1 "아쉽다, [player_name]. 정답은 주유재였어."

    P "진짜? 난 전혀 몰랐는데... 다음엔 더 잘 맞춰볼게."

    call show_J2_happy from _call_show_J2_happy_1
    voice "audio/ch3/J2_002.mp3"
    J2 "오빠, 다음엔 더 잘 부탁해요!"

    if like_J2 - 10 < 40 and like_J2 >= 40:
        call glitch_J2_happy from _call_glitch_J2_happy
    $ like_J2 -= 10
    jump after_guess

label after_guess:


    if game_success:
        "미니게임에서 성공하며 주유재와 친밀감을 쌓았다!"
    else:
        "미니게임에서 실패했지만, 주유재가 너의 노력에 고마움을 느꼈다."

    "모두가 웃으며 점심시간을 함께 보내기로 한다."

    P "(유재가 주하민의 사촌동생이라는 걸 알게 되다니... 이 캠프는 정말 특별하다.)"

    jump cafe

label cafe:

    scene bg_cafeteria with dissolve
    stop music fadeout 1.0
    play music "audio/bgm_daily_2.mp3" fadein 1.0 loop

    call show_J1_happy from _call_show_J1_happy_10
    call show_J2_happy from _call_show_J2_happy_2
    P "아, 잘 먹었다~ 정말 배부르네."

    voice "audio/ch3/J1_006.mp3"
    J1 "그러게, [player_name]가 사서 그런지 더 맛있는 것 같아. 히힛~!"

    P "하핫...! 다음에는 내가 아닌 네가 사는 걸로 하자."

    voice "audio/ch3/J2_003.mp3"
    J2 "잘 먹었습니다."

    P "(반도 안 먹었는데 잘 먹었다니... 역시 듣던 대로 입이 짧구나.)"

    voice "audio/ch3/J1_007.mp3"
    J1 "그럼 밥도 먹었겠다, 이제 다시 개발하러 가볼까?"

    voice "audio/ch3/J1_008.mp3"
    J1 "난 이만 가볼게~ 너희 둘은 같은 반이니까 같이 들어가! 가는 김에 대화도 좀 하고~"

    P "응, 그래. 잘 가 호민아!"

    call hide_J1_happy from _call_hide_J1_happy_6
    "호민이 떠나고 실습실로 가는 길에 둘만 남았다."

    voice "audio/ch3/J2_004.mp3"
    J2 "혹시 카페 잠깐 가실래요? 밥 얻어먹었는데, 이번엔 제가 사야죠."

    P "네? 아, 괜찮아요. 오늘은 제가 일이 있어서요."

    call hide_J2_happy from _call_hide_J2_happy
    call show_J2_sad from _call_show_J2_sad
    voice "audio/ch3/J2_005.mp3"
    J2 "(조금 실망한 표정) 아, 그렇군요. 알겠습니다."

    "그때 핸드폰이 울린다. 궤하린 교수님이다. 아, 맞다! 오늘이 15일이구나!"

menu:

    "주유재와 카페에 간다":
        $ like_J2 += 10
        if like_G - 10 < 50 and like_G >=50:
            call glitch_G_sad from _call_glitch_G_sad_1
        $ like_G -= 10
        jump cafe2

    "궤하린 교수님과의 선약을 지키러 간다":
        if like_J2 - 10 < 40 and like_J2 >=40:
            call glitch_J2_sad from _call_glitch_J2_sad
        $ like_J2 -= 10
        $ like_G += 10
        jump laboratory2

label cafe2:

    scene bg_cafe with dissolve
    stop music fadeout 1.0
    play music "audio/bgm_date_day_1.mp3" fadein 1.0 loop
    "주유재와 함께 근처 카페에 들어갔다. 창가 자리로 안내받아 앉자 유재가 메뉴를 건넨다."

    call show_J2_happy from _call_show_J2_happy_3
    voice "audio/ch3/J2_006.mp3"
    J2 "오빠, 제가 자주 오는 곳이에요. 여기 디저트도 진짜 맛있어요!"

    P "그래? 그럼 네가 추천하는 걸로 주문해볼게. 네가 좋아하는 거 궁금하기도 하고."

    call hide_J2_happy from _call_hide_J2_happy_1
    call show_J2_excited from _call_show_J2_excited
    voice "audio/ch3/J2_007.mp3"
    J2 "(미소 지으며) 역시 오빠는 센스가 있어요. 그러면 제가 제일 좋아하는 케이크랑 음료로 주문할게요."

    call hide_J2_excited from _call_hide_J2_excited
    "잠시 후, 유재가 주문한 디저트와 음료가 테이블에 놓인다. 보기만 해도 군침이 도는 비주얼이다."

    call show_J2_excited from _call_show_J2_excited_1
    voice "audio/ch3/J2_008.mp3"
    J2 "어때요? 맛있나요? 제가 좋아하는 메뉴인데 오빠 입맛에 맞을지 모르겠어요."

    P "아, 엄청 맛있다! 네가 자주 먹어서 그런지, 추천도 잘하는데?"

    voice "audio/ch3/J2_009.mp3"
    J2 "(장난스럽게) 네? 뭐라고요? 제가 자주 먹어서요?"

    P "(당황하며) 아, 아니야! 그런 뜻이 아니라... 그냥 맛있다는 얘기였어!"

    voice "audio/ch3/J2_010.mp3"
    J2 "(웃으며) 다행이에요. 사실 오빠랑 이렇게 단둘이 있는 것도 처음이라, 좀 긴장되네요."

    P "긴장할 필요 없어. 나도 네가 편하게 느낄 수 있도록 노력할게."

    "유재는 손끝으로 컵을 만지작거리며 잠시 머뭇거린다. 뭔가 하고 싶은 말이 있는 듯했다."

    P "그나저나, 아까 할 말이 있다고 했잖아? 무슨 얘긴데?"

    call hide_J2_excited from _call_hide_J2_excited_1
    call show_J2_sad from _call_show_J2_sad_1
    voice "audio/ch3/J2_011.mp3"
    J2 "아... 사실 대단한 건 아니고요. 그냥... 오빠랑 좀 더 친해지고 싶어요."

    P "(음료를 흘릴 뻔하며) 네? 친해진다고? 물론이지! 나도 그러고 싶어."

    "유재는 얼굴이 조금 붉어진 듯 보였지만, 금세 밝은 표정으로 웃으며 고개를 끄덕였다."

    P "(너무 유명한 사람이라 친해지고 싶어도 말을 못 했는데... 이런 기회를 주다니!)"

    P "그럼 이제 말 편하게 놓을까? 어때?"

    call hide_J2_sad from _call_hide_J2_sad
    call show_J2_happy from _call_show_J2_happy_4
    voice "audio/ch3/J2_012.mp3"
    J2 "좋아요, 오빠 ㅎㅎ 그런데 먼저 놓으세요. 오빠가 나이 많으니까."

    P "(장난스럽게) 아, 내가 많긴 하지. 하지만 너도 이젠 성인이잖아?"

    voice "audio/ch3/J2_013.mp3"
    J2 "(웃으며) 맞아요. 성인인데 왜 자꾸 애 취급하세요? 어쨌든 이제부터는 말 놓을게요, 오빠~"

    "대화가 자연스레 이어지면서 두 사람 사이의 거리도 조금씩 가까워지는 듯했다."

    voice "audio/ch3/J2_014.mp3"
    J2 "오빠, 사실 오늘 진짜 만나고 싶었어요. 원래는 그냥 밥만 먹으려 했는데..."

    P "그래? 왜? 뭔가 특별한 이유라도 있어?"

    voice "audio/ch3/J2_015.mp3"
    J2 "그냥... 오빠랑 얘기하면 뭔가 편하고 좋더라고요. 그래서 이렇게라도 시간을 내고 싶었어요."

    P "고맙다. 사실 나도 너랑 더 얘기하고 싶었어. 네가 워낙 유명해서 처음엔 좀 부담스러웠는데..."

    call hide_J2_happy from _call_hide_J2_happy_2
    call show_J2_excited from _call_show_J2_excited_2
    voice "audio/ch3/J2_016.mp3"
    J2 "(장난스럽게) 부담스러웠다니, 그건 내 잘못인가요?"

    P "아니, 그게 아니라... 네가 워낙 빛나니까 그런 거지."

    "유재는 얼굴을 살짝 붉히며 컵을 들어 음료를 마셨다. 그녀의 행동 하나하나가 자연스레 눈길을 끌었다."

    "시간이 흐르는 것도 모를 만큼 대화가 이어지고, 두 사람은 카페에서 나왔다."

    "밖으로 나오니 시원한 바람이 두 사람의 얼굴을 스쳤다."

    voice "audio/ch3/J2_017.mp3"
    J2 "오빠, 오늘 정말 재밌었어요. 다음에도 또 같이 놀아요, 네?"

    P "당연하지. 언제든 불러줘."

    voice "audio/ch3/J2_018.mp3"
    J2 "(작은 목소리로) 그럼... 다음번엔 내가 진짜 좋아하는 곳에 데려갈게요. 비밀이에요."

    P "그래, 기대할게. 그럼 이제 실습실로 돌아갈까?"

    voice "audio/ch3/J2_019.mp3"
    J2 "네~ 오빠 따라갈게요!"

    "두 사람은 나란히 걸어가며 한층 더 가까워진 관계를 느꼈다."
    call hide_J2_excited from _call_hide_J2_excited_2

    jump going_back


label going_back:

    scene bg_N1_2 with fade
    stop music fadeout 1.0
    play music "audio/bgm_daily_7.mp3" fadein 1.0 loop

    "돌아가는 길에 침채린과 마주쳤다."

    call show_C_angry from _call_show_C_angry_5
    if like_J2 > 40:
        show J2_happy at right, fade_in:
            zoom 0.75
    else:
        show JooWoo_happy at right, fade_in:
            zoom 0.75
    
    voice "audio/ch3/C_001.mp3"
    C "어, [player_name]? 어디 갔다 왔어? 찾고 있었는데! 그리고 옆에 있는 건...?"

    voice "audio/ch3/C_002.mp3"
    C "(귓속말) 우리 반 그 애기 아니야? 너 왜 쟤랑 같이 있어?"

    P "아, 호민이 사촌 동생이더라고. 셋이서 밥 먹고 돌아오는 길이야."

    voice "audio/ch3/J2_020.mp3"
    J2 "안녕하시렵니까~"

    voice "audio/ch3/C_003.mp3"
    C "요즘 애들은 인사법이 특이하네. 나 때는 안 이랬는데."

    voice "audio/ch3/C_004.mp3"
    C "근데 왜 둘만 와? 호민이는 어디 가고?"

    P "호민이는 자기 반에 일이 있어서 먼저 갔어."

    voice "audio/ch3/J2_021.mp3"
    J2 "그리고 제가 카페 가자고 했어요."

    call hide_C_angry from _call_hide_C_angry_5
    call show_C_q from _call_show_C_q_1
    voice "audio/ch3/C_005.mp3"
    C "응? 카페? 둘이서만?"

    call hide_J2_happy from _call_hide_J2_happy_3
    if like_J2 > 40:
        show J2_q at right, fade_in:
            zoom 0.75
    else:
        show JooWoo_q at right, fade_in:
            zoom 0.75
    voice "audio/ch3/J2_022.mp3"
    J2 "네, 그런데요? 왜요? 혹시 [player_name]오빠 좋아하세요?"

    call hide_C_q from _call_hide_C_q_1
    call show_C_sad from _call_show_C_sad_2
    voice "audio/ch3/C_006.mp3"
    C "(갑자기 얼굴이 빨개지며) 내가? 얘를? 아니, 그런 거 아니거든!"

    voice "audio/ch3/C_007.mp3"
    C "몰라, 몰라. 얼른 가자! [player_name], 내가 할 말이 있으니까!"

    jump choice

label laboratory2:

    scene bg_classroom with fade
    stop music fadeout 1.0
    play music "audio/bgm_daily_5.mp3" fadein 1.0 loop

    P "네, 교수님! 전화 받았습니다."

    call show_G_outside from _call_show_G_outside
    voice "audio/ch3/G_001.mp3"
    G "혹시 아직 오는 길이니? 언제쯤 도착해?"

    P "아, 이제 출발하려고요. 근처에 점심 먹으러 왔어서 금방 도착해요."

    voice "audio/ch3/G_002.mp3"
    G "그래, 좀 이따 보자. 혹시 모르니 위치 다시 한 번 찍어서 보낼게."

    "[player_name]는 핸드폰으로 위치를 확인한다."

    P "(여긴 어디지? 학회장 근처 같은데...?)"

    "[player_name]는 궁금함을 안고 택시를 타고 교수님이 보낸 장소로 향했다."

    scene bg_conference with fade

    "택시를 타고 도착한 곳은 바로 대형 학회가 열리고 있는 장소였다."

    "멀리서 궤하린 교수가 손을 흔들며 [player_name]를 맞이하고 있었다."

    call show_G_outside from _call_show_G_outside_1

    P "(1km 밖에서도 눈에 띌 만큼 화려한 외모... 이런 사람과 함께 있다니, 실감이 안 나네.)"

    voice "audio/ch3/G_003.mp3"
    G "(밝게 웃으며) [player_name]~ 어서 와, 오느라 수고했어."

    P "교수님! 안녕하세요. 그런데 여긴...?"

    voice "audio/ch3/G_004.mp3"
    G "나중에 설명해줄게. 그리고 여기서는 반모! 알지?"

    P "네? 반모요? 교수님께 반말을 하라고요?"

    voice "audio/ch3/G_005.mp3"
    G "ㅎㅎ 어색하긴. 그래도 여기서만큼은 그냥 편하게 해봐. [player_name]~"

    P "그럼... 그래, 궤하린야. 어색하지만 한 번 해볼게."

    "학회장으로 들어서자 분위기가 달라졌다. 전문적이고 고급스러운 분위기가 감돌았다."

    "그때 전에 식당에서 보았던 궤하린 교수의 전남친으로 보이는 남자가 시야에 들어왔다."

    P "(저 사람... 식당에서 싸우던 그 남자잖아. 여기서 또 보게 될 줄이야...)"

    "궤하린 교수는 그를 본 듯하지만, 담담한 표정으로 학회장을 둘러보며 [player_name]를 안내했다."

    voice "audio/ch3/G_006.mp3"
    G "(웃으며) 이쪽이야. 내 교수님들이 많이 계셔. 긴장하지 말고 따라와."

    "교수 1" "오, 궤하린 교수! 오랜만이야. 잘 지냈어?"

    "교수 2" "저번 논문 정말 잘 읽었어. 역시 궤하린 교수답더라구."

    "교수 3" "근데 옆에 있는 청년은 누구야? 꽤 젊어 보이는데?"

    voice "audio/ch3/G_007.mp3"
    G "(미소 지으며) 아, 제 남자친구에요. 멋있죠?"

    P "(갑작스러운 말에 심장이 멎을 뻔했다.) 네?! 남자친구라고?!"

    "교수 1" "남자친구? 그럼... 정 사장은 어떻게 된 거야?"

    "교수 2" "맞아. 정 사장님이랑 잘 되고 있는 줄 알았는데..."

    voice "audio/ch3/G_008.mp3"
    G "(눈빛이 단단해지며) 정 사장님이랑은 끝난 지 오래예요."

    voice "audio/ch3/G_009.mp3"
    G "바람은 자기가 피워 놓고 오히려 제 탓을 하더라고요. 그래서 정리했어요."

    "교수 3" "어머, 그런 힘든 일이 있었다니...!"

    "교수 1" "그런 놈은 그냥 두면 안 되겠어! 우리가 손 좀 봐줄까?"

    "교수 2" "맞아! 정 사장은 우리 손으로 정리해야지."

    "분위기가 다소 묘해질 때, [player_name]가 입을 열었다."

    P "(장난스럽게) 정 사장은 바람둥이다~ 불륜남이다~!"

    "갑작스러운 외침에 궤하린 교수는 터져 나오는 웃음을 참지 못했다."

    voice "audio/ch3/G_010.mp3"
    G "(웃음을 터트리며) 푸흡...하하하하하하! [player_name], 너 정말...!"

    voice "audio/ch3/G_011.mp3"
    G "그만해, ㅋㅋㅋ 여기서 웃음 터지면 이미지 다 날아가겠어."

    P "아, 죄송합니다. 그냥... 교수님이 너무 멋있어서요."

    voice "audio/ch3/G_012.mp3"
    G "(눈웃음 지으며) 정말? 그럼 이번엔 내가 너를 구해준 셈이네."

    "그렇게 웃음이 오가는 가운데 학회는 점점 분위기를 띄워갔다."

    jump back_at_school


label back_at_school:

    scene bg_N1 with dissolve
    stop music fadeout 1.0
    play music "audio/bgm_daily_4.mp3" fadein 1.0 loop
    "학교에 다시 도착했다."

    call show_J1_q from _call_show_J1_q_2
    voice "audio/ch3/J1_009.mp3"
    J1 "어, [player_name]. 어디 갔다 오는 길이야?"

    P "아, 궤하린 교수님이랑 일이 있어서 잠깐 다녀왔어."

    voice "audio/ch3/J1_010.mp3"
    J1 "궤하린 교수님? 교수님이랑 무슨 일?"

    "그때 궤하린 교수가 걸어와 인사를 건넨다."

    if like_G >= 50:
        show G_outside at left, fade_in:
            zoom 0.75
    else:
        show Gdo_outside at left, fade_in:
            zoom 0.75
    voice "audio/ch3/G_013.mp3"
    G "아직 안 갔구나, [player_name]. 오늘 덕분에 정말 고마웠어."

    "궤하린 교수는 [player_name]에게 작은 상자를 건넨다. 정교하게 포장된 케이크였다."

    voice "audio/ch3/G_014.mp3"
    G "맛있게 먹어, 하지만 꼭 혼자 먹어야 해. 알겠지? 그리고... 옆에 있는 호민 씨? 너도 손 대면 안 돼~"

    "주하민은 장난스럽게 케이크를 쳐다보며 말했다."
    call hide_G_outside from _call_hide_G_outside
    call hide_J1_q from _call_hide_J1_q_3
    call show_J1_happy from _call_show_J1_happy_11
    voice "audio/ch3/J1_011.mp3"
    J1 "너 케이크 안 좋아하잖아. 어차피 나 주면 되지 않나?"

    P "(피식 웃으며) 어, 그치. 옛날엔 안 좋아했었는데, 그걸 잘 기억하네."

    voice "audio/ch3/J1_012.mp3"
    J1 "(자신감 넘치며) 당연하지~ 내가 기억력 하나는 진짜 끝내주잖아~!"

    P "역시 호민이야. 누구랑 다르게 얼굴만 예쁜 게 아니라니까."

    "호민은 어깨를 으쓱이며 웃는다."

    if like_G >= 50:
        show G_outside at left, fade_in:
            zoom 0.75
    else:
        show Gdo_outside at left, fade_in:
            zoom 0.75
    voice "audio/ch3/G_015.mp3"
    G "그럼 난 이만 가볼게. [player_name], 다음에 또 보자. 잘 쉬고!"

    "궤하린 교수는 떠나면서 살짝 손을 흔들었다. [player_name]는 잠시 그녀의 뒷모습을 바라봤다."

    call hide_G_outside from _call_hide_G_outside_1
    call hide_J1_happy from _call_hide_J1_happy_7
    call show_J1_q from _call_show_J1_q_3
    voice "audio/ch3/J1_013.mp3"
    J1 "(작은 목소리로) 너랑 궤하린 교수님, 좀 수상한데? 뭔가 있는 거 아냐?"

    P "뭐? 무슨 소리야! 그냥 도와드린 거였다고!"

    voice "audio/ch3/J1_014.mp3"
    J1 "그래~ 뭐 그렇다고 치자. 근데 너 오늘 케이크 먹으면서 생각 좀 해봐."

    P "생각? 무슨 생각?"

    voice "audio/ch3/J1_015.mp3"
    J1 "네가 요즘 인기가 많다는 생각 말이야. 네 주변에 왜 이렇게 예쁜 사람들이 많아졌냐고."

    P "(당황하며) 아, 아니 그건 그냥 우연이지..."

    "둘은 실습실 쪽으로 걸음을 옮기며 이야기를 이어갔다."

    call hide_J1_q from _call_hide_J1_q_4
    call show_J1_happy from _call_show_J1_happy_12
    voice "audio/ch3/J1_016.mp3"
    J1 "아무튼 오늘 고생 많았어. 내가 케이크 좀 나눠줄까 싶지만, 너 혼자 먹으라는 교수님 말을 따라야겠지?"

    P "(장난스럽게) 어, 혼자 다 먹어야지. 너 뺏어 먹지 마라!"

    "주하민은 장난스럽게 웃으며 손을 들어 보였다."

    voice "audio/ch3/J1_017.mp3"
    J1 "알겠어, 알겠어. 그럼 실습실에서 보자."

    P "응, 그래. 고마워, 호민아."

    "[player_name]는 케이크 상자를 품에 안고 천천히 실습실로 걸음을 옮겼다."

    jump choice


label choice:

    scene bg_classroom with dissolve
    stop music fadeout 1.0
    play music "audio/bgm_daily_6.mp3" fadein 1.0 loop

    "다음 날, 실습실에 늦게 도착하였더니, 침채린과 주유재가 이야기하고 있다."

    call show_C_angry from _call_show_C_angry_6
    if like_J2 >= 50:
        show J2_sad at right, fade_in:
            zoom 0.75
    else:
        show JooWoo_sad at right, fade_in:
            zoom 0.75
    voice "audio/ch3/C_008.mp3"
    C "어, [player_name]! 너 어디 갔다 왔어? 우리 기다렸잖아."

    voice "audio/ch3/J2_023.mp3"
    J2 "(토라진 표정으로) 맞아 오빠. 나 디저트 먹으려고 기다렸는데, 밥도 못 먹었어."

    P "(당황하며) 어? 둘이 왜 기다렸어? 그리고 유재 너는 밥 잘 안 먹잖아."

    voice "audio/ch3/J2_024.mp3"
    J2 "(뾰로통하며) 아니에요, 디저트는 다르다고요! 오빠 진짜...!"

    voice "audio/ch3/C_009.mp3"
    C "(어깨를 으쓱하며) 아무튼, 너랑 할 얘기 좀 하려고 했지. 근데 왜 이렇게 늦게 와?"

    P "(혼란스러워하며) 아, 미안... 오늘 좀 바빠서..."

    "침채린은 살짝 찌릿한 눈빛을 보내고, 주유재는 입을 삐죽 내밀며 앉아 있다."

    voice "audio/ch3/C_010.mp3"
    C "우린 이제 가려고 했는데, 너도 같이 갈래? 아니면 여기서 혼자 좀 더 있을 거야?"

    voice "audio/ch3/J2_025.mp3"
    J2 "오빠는 저랑 같이 가야죠. 딱 봐도 같이 가고 싶어 보이는데?"

    P "(머리를 긁적이며) 아, 글쎄... 나는 조금 더 있다가 가려고."

    "[player_name]는 마음속으로 복잡한 생각을 정리하기 시작했다."

    P "(아, 이게 무슨 일이야. 왜 내 주변에 이렇게 사람들이 몰리는 거지?)"

    P "(특히 이렇게 다들 나한테 관심 있는 것 같아 보이는데... 나, 대체 뭘 어떻게 해야 하지?)"
    call hide_C_angry from _call_hide_C_angry_6
    call hide_J2_sad from _call_hide_J2_sad_1

menu:

    "주하민을 선택한다":
        if like_C - 7.5 < 40 and like_C >= 40:
            call glitch_C_angry from _call_glitch_C_angry_4
        $ like_C -= 7.5
        call hide_C_angry from _call_hide_C_angry_7
        $ like_J1 += 10
        if like_J2 - 15 < 40 and like_J2 >= 40:
            call glitch_J2_sad from _call_glitch_J2_sad_1
        $ like_J2 -= 15
        call hide_J2_sad from _call_hide_J2_sad_2
        if like_G - 2.5 < 50 and like_G >= 50:
            call glitch_G_angry from _call_glitch_G_angry
        $ like_G -= 2.5
        call hide_G_angry from _call_hide_G_angry
        if like_K - 10 < 45 and like_K >= 45:
            call glitch_K_nervous from _call_glitch_K_nervous_2
        $ like_K -= 10
        call hide_K_nervous from _call_hide_K_nervous
        P "(그래, 이런 상황일 땐 호민이가 가장 믿음직스럽지.)"
        P "호민아, 같이 가자. 너랑 얘기 좀 더 하고 싶어."
        jump date_with_J1

    "주유재를 선택한다":
        if like_C - 7.5 < 40 and like_C >= 40:
            call glitch_C_angry from _call_glitch_C_angry_5
        $ like_C -= 7.5
        call hide_C_angry from _call_hide_C_angry_8
        if like_J1 - 2.5 < 50 and like_J1 >= 50:
            call glitch_J1_angry from _call_glitch_J1_angry_1
        $ like_J1 -= 2.5
        call hide_J1_angry from _call_hide_J1_angry_1
        $ like_J2 += 15
        if like_G - 2.5 < 50 and like_G >= 50:
            call glitch_G_angry from _call_glitch_G_angry_1
        $ like_G -= 2.5
        call hide_G_angry from _call_hide_G_angry_1
        if like_K - 10 < 45 and like_K >= 45:
            call glitch_K_nervous from _call_glitch_K_nervous_3
        $ like_K -= 10
        call hide_K_nervous from _call_hide_K_nervous_1
        P "(유재가 나를 기다렸다고 했으니, 이번엔 유재한테 신경 써주는 게 좋겠지.)"
        P "유재야, 같이 가자. 네가 기다렸으니 내가 디저트라도 사줄게."
        jump date_with_J2

    "침채린을 선택한다":
        $ like_C += 7.5
        if like_J1 - 2.5 < 50 and like_J1 >= 50:
            call glitch_J1_angry from _call_glitch_J1_angry_2
        $ like_J1 -= 2.5
        call hide_J1_angry from _call_hide_J1_angry_2
        if like_J2 - 15 < 40 and like_J2 >= 40:
            call glitch_J2_sad from _call_glitch_J2_sad_2
        $ like_J2 -= 15
        call hide_J2_sad from _call_hide_J2_sad_3
        if like_G - 2.5 < 50 and like_G >= 50:
            call glitch_G_angry from _call_glitch_G_angry_2
        $ like_G -= 2.5
        call hide_G_angry from _call_hide_G_angry_2
        if like_K - 10 < 45 and like_K >= 45:
            call glitch_K_nervous from _call_glitch_K_nervous_4
        $ like_K -= 10
        call hide_K_nervous from _call_hide_K_nervous_2
        P "(침채린이 나한테 뭔가 할 말이 있는 것 같아. 이번엔 침채린을 따라가야겠다.)"
        P "침채린, 같이 가자. 너 할 말 있다며."
        jump date_with_C

    "교수님을 선택한다":
        if like_C - 7.5 < 40 and like_C >= 40:
            call glitch_C_angry from _call_glitch_C_angry_6
        $ like_C -= 7.5
        call hide_C_angry from _call_hide_C_angry_9
        if like_J1 - 2.5 < 50 and like_J1 >= 50:
            call glitch_J1_angry from _call_glitch_J1_angry_3
        $ like_J1 -= 2.5
        call hide_J1_angry from _call_hide_J1_angry_3
        if like_J2 - 15 < 40 and like_J2 >= 40:
            call glitch_J2_sad from _call_glitch_J2_sad_3
        $ like_J2 -= 15
        call hide_J2_sad from _call_hide_J2_sad_4
        $ like_G += 2.5
        if like_K - 10 < 45 and like_K >= 45:
            call glitch_K_nervous from _call_glitch_K_nervous_5
        $ like_K -= 10
        call hide_K_nervous from _call_hide_K_nervous_3
        P "(궤하린 교수님이 오늘도 나한테 도움을 주셨는데, 그 고마움을 표현해야겠어.)"
        P "미안, 다들. 난 교수님한테 들러야 할 일이 있어. 다음에 봐!"
        jump date_with_G

    "김솔풍 조교님을 선택한다":
        if like_C - 7.5 < 40 and like_C >= 40:
            call glitch_C_angry from _call_glitch_C_angry_7
        $ like_C -= 7.5
        call hide_C_angry from _call_hide_C_angry_10
        if like_J1 - 2.5 < 50 and like_J1 >= 50:
            call glitch_J1_angry from _call_glitch_J1_angry_4
        $ like_J1 -= 2.5
        call hide_J1_angry from _call_hide_J1_angry_4
        if like_J2 - 15 < 40 and like_J2 >= 40:
            call glitch_J2_sad from _call_glitch_J2_sad_4
        $ like_J2 -= 15
        call hide_J2_sad from _call_hide_J2_sad_5
        if like_G - 2.5 < 50 and like_G >= 50:
            call glitch_G_angry from _call_glitch_G_angry_3
        $ like_G -= 2.5
        call hide_G_angry from _call_hide_G_angry_3
        $ like_K += 7.5
        P "(김솔풍 조교님이 신경을 많이 써주셨는데, 이번에 좀 더 가까워지고 싶어.)"
        P "다들 미안, 나 조교님한테 들를 일이 있어서 이만 갈게!"
        jump date_with_K

label date_with_J1:

    scene bg_night with fade
    stop music fadeout 1.0
    play music "audio/bgm_date_night.mp3" fadein 1.0 loop

    "[player_name]와 주하민은 밤에 캠퍼스 근처 공원에서 만나기로 했다."

    "가을 밤, 살짝 쌀쌀한 공원에는 가로등 불빛 아래로 사람들이 산책을 하고 있었다."

    P "호민아, 여기야!"

    call show_J1_happy from _call_show_J1_happy_13
    voice "audio/ch3/J1_018.mp3"
    J1 "(웃으며 손을 흔든다) 오, [player_name]! 생각보다 일찍 왔네. 추울까봐 걱정했는데 다행이다."

    P "그러게, 날씨가 꽤 선선하네. 근데 왜 공원을 고른 거야?"

    voice "audio/ch3/J1_019.mp3"
    J1 "음, 그냥 이런 분위기가 좋아서? 그리고 너랑 좀 진지하게 얘기하고 싶었거든."

    "둘은 가볍게 걷기 시작했다. 가을 바람이 살짝 불어오며 나뭇잎이 흔들렸다."

    P "뭐 진지하게 할 얘기? 무슨 일이야? 네가 이렇게 진지한 얼굴 하는 건 처음 보네."

    call hide_J1_happy from _call_hide_J1_happy_8
    call show_J1_sad from _call_show_J1_sad_3
    voice "audio/ch3/J1_020.mp3"
    J1 "(잠시 망설이며) 사실... 그냥 네가 요즘 힘들어 보여서."

    P "힘들어 보인다고? 내가?"

    voice "audio/ch3/J1_021.mp3"
    J1 "응. 몰캠 기간 동안 다들 널 의지하잖아. 그거 다 받아주느라 네가 얼마나 힘들었을지 알 것 같아서..."

    P "(약간 당황하며) 아... 그런 거 아니야. 난 그냥..."

    voice "audio/ch3/J1_022.mp3"
    J1 "난 네가 너무 잘하고 있는 거 알아. 근데 넌 가끔 네 자신을 돌보는 걸 잊는 것 같아서."

    P "(머리를 긁적이며) 고마워, 호민아. 네가 그렇게 생각해줘서... 근데 진짜 괜찮아."

    "둘은 잠시 말을 멈추고 벤치에 앉았다."

    voice "audio/ch3/J1_023.mp3"
    J1 "그래도 이런 시간은 필요하잖아? 그냥 아무 생각 없이 걷고, 얘기하고..."

    P "그러게. 너랑 이렇게 걷는 것도 오랜만이다."

    call hide_J1_sad from _call_hide_J1_sad_3
    call show_J1_happy from _call_show_J1_happy_14
    voice "audio/ch3/J1_024.mp3"
    J1 "(웃으며) 어릴 땐 맨날 내가 널 끌고 다녔잖아. 너 기억나? 자전거 타다 너 넘어져서 엄청 울었을 때."

    P "(웃으며) 그 얘기 또 꺼내냐? 네가 뒤에서 갑자기 밀어버려서 그런 거잖아!"

    voice "audio/ch3/J1_025.mp3"
    J1 "야, 그건 네가 너무 느리게 타서 그렇지! 그럼 내가 뭐 어쩌라고!"

    "둘은 그 추억을 떠올리며 한참을 웃었다."

menu:

    "호민에게 진지하게 감사한다":
        
        P "(진지한 표정으로) 고마워, 호민아. 네가 이렇게 신경 써주니까 기운이 난다."
        
        call hide_J1_happy from _call_hide_J1_happy_9
        $ like_J1 += 7.5
        call show_J1_surprised from _call_show_J1_surprised_1
        voice "audio/ch3/J1_026.mp3"
        J1 "(약간 당황하며) 아, 뭐야. 갑자기 이렇게 진지하게 말하면 나도 민망하잖아!"

        voice "audio/ch3/J1_027.mp3"
        J1 "그래도... 네가 그렇게 말해주니까 나도 기분 좋다!"
        jump end_date_with_J1

    "장난스럽게 받아친다":
        $ like_J1 += 5
        P "(웃으며) 에이, 네가 그렇게 말하면 내가 마치 어마어마한 히어로라도 된 것 같잖아."

        voice "audio/ch3/J1_028.mp3"
        J1 "(웃으며) 뭐, 히어로는 아니어도 네가 좀 멋지긴 해!"

        P "뭐야, 그렇게 쉽게 넘어오면 안 되지. 내가 더 놀릴 거라고!"
        jump end_date_with_J1

    "무거운 이야기를 피하며 농담으로 넘긴다":
        if like_J1 - 5 < 50 and like_J1 >= 50:
            call glitch_J1_happy from _call_glitch_J1_happy_1
        $ like_J1 -= 5
        P "(농담하듯) 네가 너무 심각하게 말하니까 무섭다. 혹시 네가 몰캠에서 날 감시하고 있는 거야?"
        
        call hide_J1_happy from _call_hide_J1_happy_10
        call show_J1_sad from _call_show_J1_sad_4
        voice "audio/ch3/J1_029.mp3"
        J1 "뭐야, 그런 얘기 하는 거 아니야. 난 진지했는데..."

        voice "audio/ch3/J1_030.mp3"
        J1 "(살짝 실망한 표정) 아무튼 그래. 그냥 네가 너무 무리하지 않았으면 좋겠다는 뜻이야."
        jump end_date_with_J1

label end_date_with_J1:

    scene bg_night_park with dissolve
    "벤치에 앉아 가벼운 얘기와 추억을 나누며 밤이 깊어갔다."

    call show_J1_excited from _call_show_J1_excited_4
    voice "audio/ch3/J1_031.mp3"
    J1 "오늘 정말 좋다. 이런 시간을 자주 가질 수 있었으면 좋겠어."

    P "그러게. 너랑 있으면 편하고 재밌어."

    voice "audio/ch3/J1_032.mp3"
    J1 "[player_name], 다음에도 나랑 이런 시간 보내줄 거지?"

    P "당연하지. 너랑 같이 있는 건 언제나 좋으니까."

    "둘은 웃으며 공원을 천천히 걸어나갔다. 가로등 아래 비친 호민의 미소는 왠지 더 밝게 느껴졌다."

    jump week3_presentation_intro


label date_with_J2:

    scene bg_night with fade
    stop music fadeout 1.0
    play music "audio/bgm_date_night.mp3" fadein 1.0 loop

    "[player_name]와 주유재는 밤에 캠퍼스 내 조용한 정원에서 만나기로 했다."

    "밤하늘에는 별이 반짝이고, 정원에는 은은한 조명과 함께 가을의 정취가 가득했다."

    call show_J2_happy from _call_show_J2_happy_5
    voice "audio/ch3/J2_026.mp3"
    J2 "오빠, 여기요~!"

    "유재는 작은 꽃다발을 들고 웃으며 손을 흔들고 있었다."

    P "(놀라며) 어? 그거 뭐야? 꽃?"

    call hide_J2_happy from _call_hide_J2_happy_4
    call show_J2_excited from _call_show_J2_excited_3
    voice "audio/ch3/J2_027.mp3"
    J2 "(씨익 웃으며) 네, 선물이에요. 오빠 생각나서 준비했어요. 별 거 아니에요~"

    P "(어색하게 웃으며) 아... 고맙다. 내가 이런 걸 받아도 되는지 모르겠네."

    voice "audio/ch3/J2_028.mp3"
    J2 "그럼 제가 가져가도 돼요?"

    P "아니, 아냐! 고맙게 받을게. 진짜 고마워."

    "둘은 정원을 천천히 걸으며 가벼운 대화를 나누기 시작했다."

    call hide_J2_excited from _call_hide_J2_excited_3
    call show_J2_happy from _call_show_J2_happy_6
    voice "audio/ch3/J2_029.mp3"
    J2 "오빠는 이런 데 자주 와요? 아니면 제가 불러서 온 거예요?"

    P "(웃으며) 뭐, 너 아니면 이런 데 잘 안 오지. 여기 되게 조용하고 좋다."

    voice "audio/ch3/J2_030.mp3"
    J2 "맞아요. 저도 사람 많은 데보다는 이런 조용한 곳이 좋아요."

    P "의외네. 넌 주목받는 걸 좋아할 줄 알았는데."

    call hide_J2_happy from _call_hide_J2_happy_5
    call show_J2_excited from _call_show_J2_excited_4
    voice "audio/ch3/J2_031.mp3"
    J2 "(씨익 웃으며) 주목받는 건 일할 때나 좋아요. 그 외엔 그냥 조용히 있는 게 좋아요."

    "둘은 벤치에 앉아 가을 바람을 느끼며 밤하늘을 올려다보았다."

    voice "audio/ch3/J2_032.mp3"
    J2 "오빠, 별 좋아해요?"

    P "별? 음... 좋아하는 편이지. 너도 좋아해?"

    voice "audio/ch3/J2_033.mp3"
    J2 "네. 별을 보면 기분이 편안해져요. 오늘 밤하늘도 참 예쁘죠?"

    "유재는 잠시 말을 멈추고 하늘을 바라보며 생각에 잠겼다."

    voice "audio/ch3/J2_034.mp3"
    J2 "오빠는 요즘 어떤 생각하면서 살아요?"

    P "(놀라며) 뭐? 갑자기 그건 왜?"

    voice "audio/ch3/J2_035.mp3"
    J2 "그냥요. 오빠는 어떤 생각하면서 하루를 보낼까 궁금해서요."

menu:

    "솔직하게 대답한다":
        $ like_J2 += 10
        P "사실... 요즘 좀 복잡해. 몰캠도 그렇고, 나를 의지하는 사람들이 많아서 책임감 느끼는 일이 많아졌어."

        voice "audio/ch3/J2_036.mp3"
        J2 "(웃으며) 오빠가 그렇게 진지하게 생각하는 사람인 줄 몰랐어요."

        P "너야말로... 이런 걸 물어보는 거 보면 생각보다 깊은 사람 같네."

        voice "audio/ch3/J2_037.mp3"
        J2 "원래 깊은 사람이에요. 오빠가 지금 알았을 뿐."
        jump end_date_with_J2

    "농담으로 넘긴다":
        $ like_J2 += 5
        P "(웃으며) 뭐, 오늘은 별 보면서 '난 역시 대단하다' 생각했지."

        voice "audio/ch3/J2_038.mp3"
        J2 "(씨익 웃으며) 그거 진심이에요? 오빠, 자기애 넘치는 거 처음 봐요."

        P "농담이지! 사실 아무 생각 없었어. 그냥 오늘이 좋아."

        voice "audio/ch3/J2_039.mp3"
        J2 "저도 오늘 너무 좋아요."
        jump end_date_with_J2

    "대답을 피하며 화제를 돌린다":
        if like_J2 - 5 < 40 and like_J2 >= 40:
            call glitch_J1_happy from _call_glitch_J1_happy_2
        $ like_J2 -= 5
        hide J2_excited
        P "(머뭇거리며) 음... 별 생각 없었어. 그냥 이렇게 너랑 있으니까 좋다?"

        call show_J2_sad from _call_show_J2_sad_2
        voice "audio/ch3/J2_040.mp3"
        J2 "(약간 실망한 듯) 아, 그렇구나... 저는 뭔가 더 진지한 대답이 나올 줄 알았는데."

        P "(당황하며) 아니야, 그냥... 오늘은 별 생각 없이 쉬고 싶어서."
        jump end_date_with_J2

label end_date_with_J2:

    scene bg_night_park with dissolve
    "유재는 밝게 웃으며 [player_name]를 바라보았다."

    call show_J2_happy from _call_show_J2_happy_7
    voice "audio/ch3/J2_041.mp3"
    J2 "오빠랑 이렇게 얘기하니까 참 편해요. 이상하죠? 사람 많은 데서는 불편한데 오빠랑 있을 땐 괜찮아요."

    P "그래? 나도 너랑 있으니까 꽤 재밌어."

    call hide_J2_happy from _call_hide_J2_happy_6
    call show_J2_excited from _call_show_J2_excited_5
    voice "audio/ch3/J2_042.mp3"
    J2 "(웃으며) 저 재밌는 사람인가요? 다행이네요."

    "둘은 다시 정원을 걸으며 가벼운 얘기와 함께 밤을 보냈다."

    "유재는 헤어지기 전, [player_name]를 향해 작게 속삭였다."

    voice "audio/ch3/J2_043.mp3"
    J2 "오빠, 오늘 정말 고마웠어요. 그리고 다음에도... 또 같이 걸어요."

    P "(미소를 지으며) 응, 꼭 그러자."

    "유재는 환하게 웃으며 돌아섰고, [player_name]는 그런 유재의 뒷모습을 바라보며 마음이 묘하게 편안해졌다."

    jump week3_presentation_intro


label date_with_C:

    scene bg_night with fade
    stop music fadeout 1.0
    play music "audio/bgm_date_night.mp3" fadein 1.0 loop
    "[player_name]와 침채린은 밤에 캠퍼스 근처 호수공원에서 만나기로 했다."

    "밤하늘 아래 호수는 은은한 달빛에 반짝이고, 침채린은 이미 벤치에 앉아 [player_name]를 기다리고 있었다."

    call show_C_angry from _call_show_C_angry_7
    voice "audio/ch3/C_011.mp3"
    C "어이, [player_name]! 늦었잖아. 누나가 이렇게 추운데 기다렸단 말이야."

    P "(헐레벌떡 달려오며) 미안, 미안! 생각보다 멀어서 좀 걸렸어."

    call hide_C_angry from _call_hide_C_angry_11
    call show_C_happy from _call_show_C_happy_16
    voice "audio/ch3/C_012.mp3"
    C "(손으로 가볍게 머리를 쥐어박으며) 참나, 넌 진짜 내가 챙겨주지 않으면 큰일 나겠다."

    P "(머리를 감싸며) 야, 누나. 너무한다~! 나도 열심히 뛰어왔거든?"

    "침채린은 웃으며 자리에서 일어나 호수 쪽으로 손을 뻗었다."

    voice "audio/ch3/C_013.mp3"
    C "자, 얼른 와봐. 여기 앉으면 호수도 잘 보이고, 바람도 딱 좋다니까."

    "[player_name]는 침채린 옆에 앉아 호수를 바라보며 숨을 고른다."

    P "그러게. 분위기 진짜 좋다. 여기 어떻게 알았어?"

    voice "audio/ch3/C_014.mp3"
    C "나? 내가 이런 데는 또 잘 알지. 몰캠 시작하기 전에 혼자 돌아다니면서 찾은 거야."

    P "(웃으며) 역시 침채린. 이런 거엔 진심이네."

    "침채린은 갑자기 가방에서 과자 봉지를 꺼내 [player_name]에게 건넸다."

    voice "audio/ch3/C_015.mp3"
    C "자, 과자라도 먹어. 이런 데 왔으면 또 먹으면서 수다 떨어야지~"

    P "(과자를 받아들며) 너 진짜 준비성 철저하다. 뭐야, 피크닉 나왔어?"

    call hide_C_happy from _call_hide_C_happy_12
    call show_C_excited from _call_show_C_excited_5
    voice "audio/ch3/C_016.mp3"
    C "(우스꽝스러운 포즈를 취하며) 어머! [player_name]님께서는 이런 낭만을 모르는 건가요? 이런 밤엔 과자와 수다가 국룰이지!"

    P "(웃으며) 참나, 그런 국룰이 어딨냐. 그래도 고맙다."

    "둘은 과자를 나눠 먹으며 가볍게 대화를 나누었다."

    call hide_C_excited from _call_hide_C_excited_5
    call show_C_happy from _call_show_C_happy_17
    voice "audio/ch3/C_017.mp3"
    C "[player_name], 너 요즘 잘 지내? 솔직히 내가 봤을 땐, 네가 너무 바쁘게 사는 것 같아서."

    P "어? 뭐... 괜찮아. 나름 즐겁게 지내고 있어."

    voice "audio/ch3/C_018.mp3"
    C "그런 말 하는 애치곤 너 요즘 눈 밑에 다크서클 진짜 심하던데?"

    P "(눈을 비비며) 아, 그건 그냥... 밤샌 거야. 괜찮아."

    call hide_C_happy from _call_hide_C_happy_13
    call show_C_angry from _call_show_C_angry_8
    voice "audio/ch3/C_019.mp3"
    C "(팔짱을 끼며) 참, 너 진짜 이런 데선 거짓말 못한다. 너 혹시 누나가 걱정하는 거 싫어?"

menu:

    "솔직히 말한다":

        P "(웃으며) 사실 네가 이렇게 신경 써주는 게 고맙긴 해. 근데 좀 민망해서 그런 거지."

        call hide_C_angry from _call_hide_C_angry_12
        $ like_C += 2.5
        call show_C_surprised from _call_show_C_surprised_1
        voice "audio/ch3/C_020.mp3"
        C "(살짝 당황하며) 뭐야, [player_name]. 너 나한테 고마운 줄은 알았네?"

        P "당연하지. 그래도 내가 은근히 네 덕 많이 보고 있어."

        voice "audio/ch3/C_021.mp3"
        C "그래~? 그럼 더 신경 써줄게. 앞으로는 두 배로!"
        jump continue_date_with_C

    "농담으로 넘긴다":
        P "(웃으며) 아, 누나. 내가 이런 거까지 다 보고해야 돼?"

        call hide_C_angry from _call_hide_C_angry_13
        call show_C_excited from _call_show_C_excited_6
        voice "audio/ch3/C_022.mp3"
        C "(웃으며) 야! 내가 걱정돼서 물어본 건데, 넌 참~"

        P "그래도 덕분에 위로받는 기분이긴 해. 고맙다!"

        voice "audio/ch3/C_023.mp3"
        C "그런 소리 할 줄은 몰랐네. 칭찬은 받아들이겠음!"
        jump continue_date_with_C

    "대답을 피한다":
        if like_C - 5 < 40 and like_C >= 40:
            call glitch_C_excited from _call_glitch_C_excited
        $ like_C -= 5
        call hide_C_excited from _call_hide_C_excited_6
        P "(어색하게) 아, 뭐... 별 거 아니야. 그냥 좀 피곤했을 뿐이야."

        call show_C_sad from _call_show_C_sad_3
        voice "audio/ch3/C_024.mp3"
        C "(살짝 실망하며) 뭐, 그러든가. 그래도 내가 네 건강은 챙길 거니까 딴소리 말고 잘 먹어."

        P "알았어. 고맙다, 누나."
        jump continue_date_with_C

label continue_date_with_C:

    scene bg_night_park with dissolve

    "둘은 호수를 따라 천천히 걷기 시작했다. 침채린은 여전히 밝은 목소리로 농담을 던지며 분위기를 풀어갔다."

    call show_C_q from _call_show_C_q_2
    voice "audio/ch3/C_025.mp3"
    C "근데 [player_name], 너는 왜 그렇게 혼자 고생하려는 거야? 조금은 다른 사람들한테 기대도 되잖아."

    P "그러게... 가끔은 그래야 할지도 모르겠어."

    call hide_C_q from _call_hide_C_q_2
    call show_C_excited from _call_show_C_excited_7
    voice "audio/ch3/C_026.mp3"
    C "(웃으며) 좋아, 그럼 다음부턴 내가 네가 힘들어 보이면 무조건 끌어낼 거야. 알았지?"

    P "(웃으며) 너가 끌어낼 거라면 별 수 없네. 알았어, 맡길게."

    "침채린은 만족스러운 미소를 지으며 [player_name]를 바라봤다."

    voice "audio/ch3/C_027.mp3"
    C "좋아, 그럼 이걸로 오늘은 내 승리다! [player_name], 다음에도 나랑 꼭 이런 데이트하자~"

    P "데이트? 너 진짜 말은 막 던진다니까."

    voice "audio/ch3/C_028.mp3"
    C "(씨익 웃으며) 어머, 내가 이렇게 매력적인데 그게 말이야? 진짜라니까~"

    "[player_name]는 그런 침채린의 말에 어이없어 하며 웃었지만, 마음 한구석에서는 묘한 기분이 들었다."

    jump week3_presentation_intro


label date_with_G:

    scene bg_cafe with fade
    stop music fadeout 1.0
    play music "audio/bgm_date_night.mp3" fadein 1.0 loop
    "[player_name]는 궤하린 교수님의 초대로 늦은 저녁, 캠퍼스 근처 조용한 카페에서 만났다."

    "조용한 클래식 음악이 흐르는 카페는 손님이 많지 않아 한적한 분위기였다."

    call show_G_happy from _call_show_G_happy_5
    voice "audio/ch3/G_016.mp3"
    G "[player_name], 여기야. 늦지 않아서 다행이네."

    P "교수님, 안녕하세요! 그런데 이런 분위기 좋은 곳에서 보자고 하신 이유가...?"

    voice "audio/ch3/G_017.mp3"
    G "(미소 지으며) 그냥 너랑 이런 데서 이야기하면 좋을 것 같아서. 내가 데리고 다닐 제자가 이런 데에 익숙해져야지."

    P "(당황하며) 제자라니요? 저는 아직 그런 수준이 아니라..."

    voice "audio/ch3/G_018.mp3"
    G "ㅎㅎ 그런 겸손한 태도가 네 장점이긴 한데, 가끔은 자신감도 필요해. 너, 생각보다 괜찮은 사람이니까."

    "궤하린 교수님은 메뉴를 골라 [player_name]에게 권했다."

    voice "audio/ch3/G_019.mp3"
    G "자, 이건 내가 추천하는 디저트야. 맛있을 거야. 그리고 음료는 네가 좋아하는 걸로 골라."

    P "(디저트를 한 입 먹으며) 와... 진짜 맛있어요! 이런 데를 어떻게 아셨어요?"

    voice "audio/ch3/G_020.mp3"
    G "(잔을 들며) 내가 대전에 있는 맛집은 웬만큼 다 알아놨지. 연구와는 별개로 이런 것도 나름 내 취미거든."

    P "교수님 진짜 대단하시네요. 연구도 열심히 하시면서 이런 데까지..."

    voice "audio/ch3/G_021.mp3"
    G "다 잘하는 사람은 없어. 나도 가끔은 부족함을 느껴. 근데 네가 있어서 요즘은 조금 힘이 되는 것 같아."

    P "(놀라며) 제가요? 제가 뭘 했다고요?"

    call hide_G_happy from _call_hide_G_happy_4
    call show_G_excited from _call_show_G_excited
    voice "audio/ch3/G_022.mp3"
    G "(미소를 지으며) 너, 모르는 척 하는 거야? 지난번 학회 때도 그렇고, 네가 옆에 있어서 내가 훨씬 편했어."

    P "(머리를 긁적이며) 아... 그건 그냥 운 좋게 도와드린 거였어요."

    voice "audio/ch3/G_023.mp3"
    G "ㅎㅎ 운이라도 네가 없었으면 어땠을지 몰라. 덕분에 전남친에게 완벽히 승리했잖아?"

    P "그... 그 얘긴 이제 안 꺼내셔도 될 것 같은데요..."

    voice "audio/ch3/G_024.mp3"
    G "(웃으며) 그래, 알겠어. 안 꺼낼게."

    "둘은 잠시 조용히 디저트를 먹으며 시간을 보냈다. [player_name]는 교수님의 세련된 모습과 은은한 미소에 살짝 긴장했다."

    call hide_G_excited from _call_hide_G_excited
    call show_G_happy from _call_show_G_happy_6
    voice "audio/ch3/G_025.mp3"
    G "[player_name], 너는 요즘 어떻게 지내? 몰캠은 잘 하고 있어?"

    P "아, 네. 몰캠도 바쁘지만... 생각보다 재미있어요. 교수님께 배운 것도 많고요."

    voice "audio/ch3/G_026.mp3"
    G "그래? 그럼 됐다. 근데 너무 무리하지는 말고. 네가 너무 열심히 하면 옆 사람들은 다 질릴지도 몰라."

    P "(웃으며) 교수님이 그렇게 말하시니까 진짜 그런 것 같아요."

    voice "audio/ch3/G_027.mp3"
    G "(잔을 내려놓으며) 농담이고, 네 열정은 참 대단하다고 생각해. 그거 계속 유지했으면 좋겠어."

menu:

    "교수님께 감사의 마음을 전한다":
        $ like_G += 2.5
        P "교수님, 진심으로 감사해요. 교수님 덕분에 저도 몰캠에서 더 열심히 하게 된 것 같아요."

        voice "audio/ch3/G_028.mp3"
        G "(살짝 놀라며) 그런 말을 듣다니... 내가 조금 더 잘해줘야겠네."
        jump continue_date_with_G

    "교수님의 칭찬을 농담으로 받아넘긴다":
        P "(웃으며) 아, 교수님. 그런 칭찬은 위험해요. 저 지금부터 더 열심히 해서 교수님을 감동시킬지도 몰라요."

        call hide_G_happy from _call_hide_G_happy_5
        call show_G_excited from _call_show_G_excited_1
        voice "audio/ch3/G_029.mp3"
        G "(웃으며) 그래, 너라면 진짜 그럴 수도 있겠네. 기대할게."
        jump continue_date_with_G

    "대답 대신 화제를 돌린다":
        if like_G - 5 < 50 and like_G >= 50:
            call glitch_G_happy from _call_glitch_G_happy
        $ like_G -= 5
        call hide_G_happy from _call_hide_G_happy_6
        P "(가볍게 웃으며) 네, 교수님. 그런데 교수님은 요즘 어떤 연구에 집중하고 계세요?"

        call show_G_angry from _call_show_G_angry
        voice "audio/ch3/G_030.mp3"
        G "(살짝 당황하며) 음, 요즘은... 여러 가지 일이 겹쳐서 좀 바쁘긴 하지만, 나름대로 재밌게 하고 있어."
        jump continue_date_with_G

label continue_date_with_G:

    scene bg_night_park with dissolve
    "시간이 흘러 카페를 나서는 길, 궤하린 교수는 [player_name]를 조용히 불렀다."

    call show_G_happy from _call_show_G_happy_7
    voice "audio/ch3/G_031.mp3"
    G "[player_name], 오늘 이렇게 시간 내줘서 고마워. 너랑 이야기하면서 나도 많은 생각을 정리할 수 있었어."

    P "교수님, 제가 더 감사하죠. 이런 좋은 시간 만들어주셔서..."

    call hide_G_happy from _call_hide_G_happy_7
    call show_G_excited from _call_show_G_excited_2
    voice "audio/ch3/G_032.mp3"
    G "(미소 지으며) 그래, 그럼 앞으로도 잘 부탁할게. 우리 관계가 더 특별해질 수 있다면 좋겠어."

    "궤하린 교수는 살짝 웃으며 [player_name]에게 손을 흔들고, [player_name]는 두근거리는 마음으로 돌아섰다."

    jump week3_presentation_intro



label date_with_K:

    scene bg_night_park with fade
    stop music fadeout 1.0
    play music "audio/bgm_date_night.mp3" fadein 1.0 loop

    "김솔풍 조교와 저녁이 지난 늦은 밤, 캠퍼스에서 가까운 호숫가에서 만나기로 했다."

    "호숫가는 조명이 은은하게 비춰 분위기를 더했고, 물결은 잔잔하게 흔들렸다."

    P "조교님, 여기요!"

    call show_K_happy from _call_show_K_happy_2
    voice "audio/ch3/K_001.mp3"
    K "(웃으며 손을 흔든다) 어, [player_name]! 생각보다 일찍 왔네? 조교님한테 잘 보이려고 그런 거야?"

    P "(웃으며) 아니에요. 그냥 이런 데서 조교님이 기다리시는 건 좀 이상해서요."

    voice "audio/ch3/K_002.mp3"
    K "ㅎㅎ 너는 말도 잘한다니까. 근데 나도 조교라는 걸 잠깐 잊고 싶어서 너 부른 거야. 오늘은 그냥 풍이라고 불러."

    P "아, 네... 풍 조교님?"

    call hide_K_happy from _call_hide_K_happy_4
    call show_K_excited from _call_show_K_excited_1
    voice "audio/ch3/K_003.mp3"
    K "(웃으며) '조교님' 빼라고 했잖아! 이래서야 내가 너를 어떻게 편하게 대해?"

    "둘은 함께 호숫가를 따라 천천히 걷기 시작했다."

    call hide_K_excited from _call_hide_K_excited_1
    call show_K_happy from _call_show_K_happy_3
    voice "audio/ch3/K_004.mp3"
    K "오늘 하루는 어땠어? 몰캠은 아직 안 질리고 잘 하고 있어?"

    P "네, 뭐 힘들긴 하지만 재미있어요. 조교님 덕분에 많이 배우고 있기도 하고요."

    voice "audio/ch3/K_005.mp3"
    K "오, 이거 의외인데? 너 나한테 칭찬 잘 안 하잖아. 사실 나랑 얘기하고 싶어서 나온 거지?"

    P "(당황하며) 그건 아니고요, 그냥... 조교님이 부르셨으니까요."

    call hide_K_happy from _call_hide_K_happy_5
    call show_K_excited from _call_show_K_excited_2
    voice "audio/ch3/K_006.mp3"
    K "(웃으며) 너 진짜 재밌다. 그래서 내가 너랑 얘기하는 걸 좋아해."

    "김솔풍은 장난스러운 표정을 지으며 [player_name]를 바라봤다."

    voice "audio/ch3/K_007.mp3"
    K "사실 나 너한테 고맙기도 해서 이 자리를 마련한 거야."

    P "고맙다뇨? 제가 한 게 뭐 있다고요?"

    voice "audio/ch3/K_008.mp3"
    K "몰캠 동안 네가 반 분위기를 잘 이끌고 있잖아. 나도 조교지만, 반 애들끼리 잘 지내는 건 네 덕이 크다고 생각해."

    P "(머리를 긁적이며) 에이, 그런 건 아닌데요..."

    voice "audio/ch3/K_009.mp3"
    K "맞다니까! 그래서 내가 너한테 뭐라도 해주고 싶어서 오늘 이렇게 부른 거야."

    "김솔풍은 벤치에 앉으며 가방에서 뭔가를 꺼냈다. 그것은 소형 텀블러 두 개였다."

    call hide_K_excited from _call_hide_K_excited_2
    call show_K_happy from _call_show_K_happy_4
    voice "audio/ch3/K_010.mp3"
    K "짠! 내가 만든 허브차야. 스트레스 많이 받을 때 딱 좋아."

    P "(받으며) 와, 이런 것도 만드시네요. 조교님 진짜 만능이시다..."

    voice "audio/ch3/K_011.mp3"
    K "ㅎㅎ 만능은 아니고, 그냥 좋아하는 걸 너랑 나누고 싶었어."

    "둘은 조용히 허브차를 마시며 잠시 바람 소리와 물결 소리를 들었다."

    voice "audio/ch3/K_012.mp3"
    K "[player_name], 너는 참 묘한 애야. 처음엔 그저 학생 중 하나였는데, 보면 볼수록 사람을 끌어당기는 매력이 있어."

    P "(놀라며) 제가요? 저 같은 사람이 뭐가..."

    voice "audio/ch3/K_013.mp3"
    K "넌 자신을 너무 과소평가해. 내가 너를 이렇게 밤에 불러낸 것만 봐도 알잖아."

    "김솔풍은 진지한 눈빛으로 [player_name]를 바라봤다."

menu:

    "김솔풍 조교님께 솔직히 감사의 마음을 전한다":
        
        P "조교님... 아니, 풍아. 정말 감사합니다. 조교님 덕분에 몰캠이 훨씬 즐겁고, 이렇게 좋은 시간까지 보낼 수 있네요."

        call hide_K_happy from _call_hide_K_happy_6
        $ like_K += 2.5
        call show_K_excited from _call_show_K_excited_3
        voice "audio/ch3/K_014.mp3"
        K "(미소 지으며) 너 진짜 귀엽다. 이런 말은 아무나에게 쉽게 못 하잖아? 나도 고마워."
        jump continue_date_with_K

    "김솔풍 조교님의 말을 장난으로 받아넘긴다":
        P "(웃으며) 조교님, 너무 과대평가하시는 거 아니에요? 제가 사람을 끌어당긴다니, 그건 조교님께서 착각하시는 거죠."

        call hide_K_happy from _call_hide_K_happy_7
        call show_K_excited from _call_show_K_excited_4
        voice "audio/ch3/K_015.mp3"
        K "(웃으며) 그래? 그럼 다음번엔 내가 더 제대로 평가해볼게. 기대해!"
        jump continue_date_with_K

    "김솔풍 조교님의 말을 대수롭지 않게 흘려버린다":
        if like_K - 5 < 45 and like_K >= 45:
            call glitch_K_happy from _call_glitch_K_happy
        $ like_K -= 5
        call hide_K_happy from _call_hide_K_happy_8
        P "(대수롭지 않게) 그런 말도 하시네요. 근데 제가 그럴 정도로 특별한 사람은 아니에요."

        call show_K_nervous from _call_show_K_nervous_2
        voice "audio/ch3/K_016.mp3"
        K "(살짝 실망하며) 그런가... 그래도 나는 너를 그렇게 생각하고 있으니까, 네가 조금 더 자신감 가졌으면 좋겠어."
        jump continue_date_with_K

label continue_date_with_K:

    scene bg_night_park with dissolve
    "데이트가 끝날 무렵, 김솔풍은 살짝 장난스러운 미소를 지으며 말했다."

    call show_K_happy from _call_show_K_happy_5
    voice "audio/ch3/K_017.mp3"
    K "오늘 정말 재밌었어. 다음에 또 이렇게 얘기할 기회가 있으면 좋겠다."

    P "저도요. 풍아, 오늘 덕분에 진짜 좋은 시간 보냈어요."

    voice "audio/ch3/K_018.mp3"
    K "그래? 그럼 앞으로도 잘 부탁할게. 너도 나한테 기대고 싶을 땐 언제든 말해."

    "김솔풍은 손을 흔들며 멀어졌고, [player_name]는 점점 더 따뜻해지는 마음을 느꼈다."

    jump week3_presentation_intro


label week3_presentation_intro:

    scene bg_computer with dissolve
    stop music fadeout 1.0
    play music "audio/bgm_daily_7.mp3" fadein 1.0 loop

    "3주차 마지막 날, 실습실에서는 발표 준비가 한창이었다."

    voice "audio/ch3/C_029.mp3"
    call show_C_q from _call_show_C_q_3
    C "야, [player_name]. 우리 발표 진짜 잘할 수 있을까?"

    
    P "잘 될 거야. 지금까지 준비한 게 있는데 괜찮겠지."

    if like_J2 >= 40:
        show J2_sad at right, fade_in:
            zoom 0.75
    else:
        show JooWoo_sad at right, fade_in:
            zoom 0.75
    voice "audio/ch3/J2_044.mp3"
    J2 "맞아요, 오빠. 발표 순서가 거의 끝이라 더 긴장되는 거 같아요."
    call hide_C_q from _call_hide_C_q_3
    call hide_J2_sad from _call_hide_J2_sad_6
    "김솔풍 조교가 실습실로 들어오며 발표 규칙을 설명하기 시작했다."

    call show_K_happy from _call_show_K_happy_6
    voice "audio/ch3/K_019.mp3"
    K "얘들아~! 발표 준비 잘 하고 있지? 오늘은 궤하린 교수님도 같이 평가하실 거야."

    if like_G >= 50:
        show G_happy at left, fade_in:
            zoom 0.75
    else:
        show Gdo_happy at left, fade_in:
            zoom 0.75
    voice "audio/ch3/G_033.mp3"
    G "발표는 준비된 순서대로 진행하고, 내가 추가로 피드백도 줄 거야. 긴장하지 말고 최선을 다하렴."
    call hide_K_happy from _call_hide_K_happy_9
    call hide_G_happy from _call_hide_G_happy_8

    "팀원들이 조금 긴장한 듯한 표정을 짓는다."

    call show_C_sad from _call_show_C_sad_4
    voice "audio/ch3/C_030.mp3"
    C "아... 이거 발표 전에 마음 좀 풀어야 할 거 같은데..."

    "침채린이 갑자기 자리에서 일어나며 제안했다."
    
    call hide_C_sad from _call_hide_C_sad_3
    call show_C_surprised from _call_show_C_surprised_2
    voice "audio/ch3/C_031.mp3"
    C "야, 다들 너무 긴장하는 거 아니야? 내가 준비한 거 있어!"

    P "뭐 또 이상한 거 준비한 거 아냐?"

    call hide_C_surprised from _call_hide_C_surprised_1
    call show_C_angry from _call_show_C_angry_9
    voice "audio/ch3/C_032.mp3"
    C "이상한 거라니! 너희를 위해 특별히 준비했어. 틀린그림찾기다!"

    call show_J1_q from _call_show_J1_q_4
    voice "audio/ch3/J1_033.mp3"
    J1 "틀린그림찾기? 발표 전에 이게 무슨..."

    call hide_C_angry from _call_hide_C_angry_14
    call show_C_happy from _call_show_C_happy_18
    voice "audio/ch3/C_033.mp3"
    C "그냥 발표 전에 머리 좀 풀자는 거지. 대신, 게임 성공하면 발표 보너스 포인트 준대!"

    P "(고개를 갸우뚱하며) 보너스 포인트...? 진짜 그런 게 있어?"

    call hide_J1_q from _call_hide_J1_q_5
    call show_K_happy from _call_show_K_happy_7
    voice "audio/ch3/K_020.mp3"
    K "(웃으며) 아, 재미로 한 거 같은데? 그래도 한번 해보지 그래?"

    "결국, 모두가 침채린의 제안에 따라 틀린그림찾기 미니게임을 하기로 했다."

    scene black

    "발표 전 뇌를 말~랑하게 만들어볼까요?"

    "미니게임: 틀린그림찾기를 시작합니다. 제한 시간은 90초입니다!!"

    call minigame from _call_minigame

    jump spot_the_difference_game

label spot_the_difference_game:

    # 틀린그림찾기 미니게임 UI 및 진행
    # 미니게임 결과에 따라 성공/실패를 판정.
    scene bg_computer with fade
    stop music fadeout 1.0
    play music "audio/bgm_daily_7.mp3" fadein 1.0 loop

    if success:
        "게임 성공! 팀원들의 사기가 올라갔다."
        $ like_C += 2.5
        $ like_J2 += 5
        jump presentation_success
    else:
        "게임 실패... 팀원들이 살짝 긴장한 모습이다."
        if like_C - 5 < 40 and like_C >= 40:
            call glitch_C_happy from _call_glitch_C_happy_1
        $ like_C -= 5
        call hide_C_happy from _call_hide_C_happy_14

        if like_J2 - 5 < 40 and like_J2 >= 40:
            call glitch_J2_happy from _call_glitch_J2_happy_1  
        $ like_J2 -= 5
        call hide_J2_happy from _call_hide_J2_happy_7

        jump presentation_failure

label presentation_success:

    scene bg_N1_117 with fade
    stop music fadeout 1.0
    play music "audio/bgm_daily_6.mp3" fadein 1.0 loop

    "미니게임에서 성공한 덕분에 팀원들이 사기가 올라 발표 준비에 긍정적인 영향을 미쳤다."

    P "좋아, 다들 힘내서 발표하자!"

    call show_C_happy from _call_show_C_happy_19
    voice "audio/ch3/C_034.mp3"
    C "맞아. 틀린그림찾기 덕분에 머리 좀 풀렸어. 고생했어, [player_name]."

    call show_J1_happy from _call_show_J1_happy_15
    voice "audio/ch3/J1_034.mp3"
    J1 "이제 우리 차례네. 긴장하지 말고 가자."

    "발표는 순조롭게 진행되었고, 궤하린 교수와 김솔풍 조교의 긍정적인 피드백을 받았다."

    call hide_C_happy from _call_hide_C_happy_15
    call hide_J1_happy from _call_hide_J1_happy_11
    call show_G_excited from _call_show_G_excited_3
    voice "audio/ch3/G_034.mp3"
    G "이번 발표는 굉장히 잘 준비된 것 같아. 특히, 구성과 전달력이 좋아."

    if like_K >= 45:
        show K_excited at left, fade_in:
            zoom 0.75
    else:
        show KPoong_excited at left, fade_in:
            zoom 0.75
    voice "audio/ch3/K_021.mp3"
    K "그러니까~! 팀워크도 돋보였고, 다음 주에도 기대할게."

    $ like_G += 5
    $ like_K += 10

    jump week3_end

label presentation_failure:

    scene bg_N1_117 with fade
    stop music fadeout 1.0
    play music "audio/bgm_daily_6.mp3" fadein 1.0 loop

    "미니게임 실패로 팀원들이 조금 긴장한 상태로 발표를 시작했다."

    P "괜찮아, 그래도 우리가 준비한 게 있으니까 잘 될 거야."

    call show_C_sad from _call_show_C_sad_5
    voice "audio/ch3/C_035.mp3"
    C "너무 긴장돼서 실수하면 어쩌지?"

    "발표는 조금 매끄럽지 않았지만, 그래도 최선을 다한 모습을 보였다."

    call hide_C_sad from _call_hide_C_sad_4
    call show_G_happy from _call_show_G_happy_8
    voice "audio/ch3/G_035.mp3"
    G "준비한 건 많은데 조금 더 다듬었으면 좋겠어. 다음 주는 조금 더 신경 써보길 바라."

    if like_K >= 45:
        show K_happy at left, fade_in:
            zoom 0.75
    else:
        show KPoong_happy at left, fade_in:
            zoom 0.75
    voice "audio/ch3/K_022.mp3"
    K "그래도 수고했어. 이번엔 부족한 점을 보완할 수 있는 기회로 삼자!"

    if like_G - 5 < 50 and like_G >= 50:
        call glitch_G_happy from _call_glitch_G_happy_1   
    $ like_G -= 5
    call hide_G_happy from _call_hide_G_happy_9

    if like_K - 5 < 45 and like_G >= 45:
        call glitch_K_happy from _call_glitch_K_happy_1
    $ like_K -= 5
    call hide_K_happy from _call_hide_K_happy_10

    jump week3_end

label week3_end:

    scene bg_N1_outside with dissolve
    stop music fadeout 1.0
    play music "audio/bgm_daily_4.mp3" fadein 1.0 loop

    "발표가 끝나고, 팀원들은 결과에 따라 아쉬움과 만족감을 나눴다."
    
    call show_C_happy from _call_show_C_happy_20
    voice "audio/ch3/C_036.mp3"
    C "다음 주는 더 잘해야겠다. 그래도 수고했어, [player_name]!"

    P "(미소를 지으며) 그래, 다들 잘했어. 다음 주는 우리가 더 잘할 수 있을 거야."

    jump chapter3_end

label chapter3_end:
    scene bg_ch3_end
    show screen display_likes

    "이제 마지막 챕터만을 남겨두고 있네요."

    "침하하~"
    jump chapter4