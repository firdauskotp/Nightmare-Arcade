screen rolling_credits:
    tag menu  # So it replaces the current screen

    frame:
        background None
        align (0.5, 1.0)
        xysize (800, 600)

        viewport:
            draggable False
            mousewheel False
            scrollbars "none"

            has vbox:
                spacing 30
                at scroll_up 

                # 🎵 Music Credits
                text "Music Credits" size 20
                text "Aaron Krogh for most of the sound effects"
                text "Sora the Troll"
                text "Soundtracks from pixabay"

                # 🎨 Art & Images
                text "Art & Images" size 20
                text "Characters created using charat"
                text "Background images using ChatGPT"

                # 🙏 Special Thanks
                text "Special Thanks" size 20
                text "To those playing this game!"

                text "THE END" size 30

    # Automatically return after scroll duration
    timer 30 action Return()


# 📜 Auto-scroll transform
transform scroll_up:
    linear 30 yoffset -2000  # Adjust -2000 if you add more text


# 🎬 Label to show the credits
label rolling_credits_label:
    scene black
    $ play_music(ending)

    show text "Credits" at truecenter with dissolve
    pause 2
    $ set_scene("black")  # Optional if you want to clear previous visuals

    call screen rolling_credits

    stop music fadeout 2.0
    return
