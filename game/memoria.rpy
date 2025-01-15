init python:

    # DEFAULT GAME SETTINGS:
    # default card type set
    all_cards = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
    # width and height of the field
    ww = 4
    hh = 4
    # how many cards can be opened for 1 turn
    max_c = 2
    # text size in the card for text mode
    card_size = 48
    # time allocated for the passage
    max_time = 30
    # pause before the cards disappear
    wait = 0.5
    # mode of cards with images, not with the text
    img_mode = True

    values_list = []
    temp = []

    # Initialize picture cards
    # Must be in the format "images/card_*.png"
    # Required: "card_back.png" and "card_empty.png"
    for fn in renpy.list_files():
        if fn.startswith("images/card_") and fn.endswith(".png"):
            name = fn[12:-4]
            renpy.image("card_" + name, fn)
            if name != "empty" and name != "back":
                temp.append(str(name))

    # Switch to image mode if valid images are found
    if len(temp) > 1:
        all_cards = temp
    else:
        img_mode = False  # Fallback to text mode

    # Initialize the playing field
    def cards_init():
        global values_list
        values_list = []
        while len(values_list) + max_c <= ww * hh:
            current_card = renpy.random.choice(all_cards)
            for i in range(max_c):
                values_list.append(current_card)
        renpy.random.shuffle(values_list)
        while len(values_list) < ww * hh:
            values_list.append('empty')

# Screen for the game
screen memo_scr:
    add "bg_cardgame.png"
    # Timer
    timer 1.0 action If(memo_timer > 1, SetVariable("memo_timer", memo_timer - 1), Jump("memo_game_lose")) repeat True
    # Playing field
    grid ww hh:
        align (0.5, 0.5)  # Center alignment
        for card in cards_list:
            button:
                left_padding 0
                right_padding 0
                top_padding 0
                bottom_padding 0
                background None
                if card["c_value"] == 'empty':
                    if img_mode:
                        add "card_empty"
                    else:
                        text "" size card_size
                else:
                    if card["c_chosen"]:
                        if img_mode:
                            add "card_" + card["c_value"]
                        else:
                            text card["c_value"] size card_size
                    else:
                        if img_mode:
                            add "card_back"
                        else:
                            text "#" size card_size
                # Button action
                action If(
                    (card["c_chosen"] or not can_click),
                    None,
                    [SetDict(cards_list[card["c_number"]], "c_chosen", True), Return(card["c_number"])]
                ) 

    # Timer display
    text str(memo_timer) xalign 0.5 yalign 0.0 size card_size

# Main game logic
label memoria_game:
    $ cards_init()
    $ cards_list = []

    python:
        for i in range(len(values_list)):
            if values_list[i] == 'empty':
                cards_list.append({"c_number": i, "c_value": values_list[i], "c_chosen": True})
            else:
                cards_list.append({"c_number": i, "c_value": values_list[i], "c_chosen": False})

    $ memo_timer = max_time

    # Show game screen
    show screen memo_scr

    # Main game loop
    label memo_game_loop:
        $ can_click = True
        $ turned_cards_numbers = []
        $ turned_cards_values = []
        $ turns_left = max_c

        # Loop for player turns
        label turns_loop:
            if turns_left > 0:
                $ result = ui.interact()
                $ turned_cards_numbers.append(cards_list[result]["c_number"])
                $ turned_cards_values.append(cards_list[result]["c_value"])
                $ turns_left -= 1
                jump turns_loop

        # Prevent opening extra cards
        $ can_click = False

        # Check if cards match
        if turned_cards_values.count(turned_cards_values[0]) != len(turned_cards_values):
            $ renpy.pause(wait, hard=True)
            python:
                for i in turned_cards_numbers:
                    cards_list[i]["c_chosen"] = False
        else:
            $ renpy.pause(wait, hard=True)
            python:
                for i in turned_cards_numbers:
                    cards_list[i]["c_value"] = 'empty'
                if all(card["c_chosen"] or card["c_value"] == 'empty' for card in cards_list):
                    renpy.jump("memo_game_win")

        jump memo_game_loop

# Loss screen
label memo_game_lose:
    hide screen memo_scr
    hide textbutton
    $ renpy.pause(0.1, hard=True)
    #centered "{size=36} ㅋㅋ 이걸 못하네 {/size}"
    "ㅋㅋ 이걸 못하네"
    $ minigame_success = False  # 실패
    return

# Win screen
label memo_game_win:
    hide screen memo_scr
    hide textbutton
    $ renpy.pause(0.1, hard=True)
    #centered "{size=36}{b} 축하합니다. {/b}{/size}"
    "축하합니다. 당신은 이겼습니다!"
    $ minigame_success = True  # 성공
    return
