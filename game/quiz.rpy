# quiz.rpy

label programming_quiz:
    # 문제 1: 리스트 컴프리헨션
    scene quiz1
    stop music fadeout 1.0
    play music "audio/bgm_minigame_card.mp3" fadein 2.0 loop
    $ correct_answer = "[4, 16]"
    $ is_answer_correct = False

    while not is_answer_correct:
        $ answer1 = renpy.input("다음 코드의 결과를 입력하세요. \n 공백에 유의하세요!!")
        $ answer1 = answer1.strip()

        if answer1 == correct_answer:
            "정답입니다!"
            $ is_answer_correct = True
            jump programming_quiz2
        else:
            "틀렸습니다. 다시 시도하세요."

    return

label programming_quiz2:
    # 문제 1: 딕셔러니와 키 조회
    scene quiz2

    $ correct_answer = "2 0"
    $ is_answer_correct = False

    while not is_answer_correct:
        $ answer1 = renpy.input("다음 코드의 결과를 입력하세요. \n 공백에 유의하세요!!")
        $ answer1 = answer1.strip()

        if answer1 == correct_answer:
            "정답입니다!"
            $ is_answer_correct = True
            jump programming_quiz3
        else:
            "틀렸습니다. 다시 시도하세요."

    return

label programming_quiz3:
    # 문제 1: 딕셔러니와 키 조회
    scene quiz3

    $ correct_answer = "11"
    $ is_answer_correct = False

    while not is_answer_correct:
        $ answer1 = renpy.input("다음 코드의 결과를 입력하세요. \n 공백에 유의하세요!!")
        $ answer1 = answer1.strip()

        if answer1 == correct_answer:
            "정답입니다!"
            $ is_answer_correct = True
            jump programming_quiz4
        else:
            "틀렸습니다. 다시 시도하세요."

    return

label programming_quiz4:
    # 문제 1: 딕셔러니와 키 조회
    scene quiz4

    $ correct_answer = "Bark"
    $ is_answer_correct = False

    while not is_answer_correct:
        $ answer1 = renpy.input("다음 코드의 결과를 입력하세요. \n 공백에 유의하세요!!")
        $ answer1 = answer1.strip()

        if answer1 == correct_answer:
            "정답입니다!"
            $ is_answer_correct = True
            jump programming_quiz5
        else:
            "틀렸습니다. 다시 시도하세요."

    return

label programming_quiz5:
    # 문제 1: 딕셔러니와 키 조회
    scene quiz5

    $ correct_answer = "120"
    $ is_answer_correct = False

    while not is_answer_correct:
        $ answer1 = renpy.input("다음 코드의 결과를 입력하세요. \n 공백에 유의하세요!!")
        $ answer1 = answer1.strip()

        if answer1 == correct_answer:
            "정답입니다!"
            $ is_answer_correct = True
        else:
            "틀렸습니다. 다시 시도하세요."

    return

return
    # $ answer2 = renpy.input("다음 코드의 결과를 입력하세요.\n\nmy_dict = {'apple': 1, 'banana': 2, 'cherry': 3}\nresult = my_dict.get('banana', 0)\nresult2 = my_dict.get('orange', 0)\n")
    # $ answer2 = answer2.strip()

    # if answer2 == "2 0":
    #     "정답입니다!"
    # else:
    #     "틀렸습니다. 다시 시도하세요."
    #     return