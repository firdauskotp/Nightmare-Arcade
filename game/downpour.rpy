label downpour:
    $ set_scene("flyover")

    na "The downpour was no joke. Alan waits under a flyover with other bikers."
    $ show_center("ashock", "ah")
    a "Just my lucky day… Let's just scroll through Insta while waiting"

    $ set_scene("viewinginsta")

    a "No way…"

    na "Alan's eyes widen as he saw the image"

    na "He rushes to his bike; the other riders stare."
    a "I need answers!"
    b "What are you doing?! You can get hurt!"
    $ set_scene("alanonbike")

    na "A few bikers try to calm him."
    a "I don’t care!"

    na "He speeds off, mind reeling. He isn’t thinking nor riding straight."
    a "No, no, no, no, no!"
    na " He shouted as tears began pouring out of his eyes. The downpour did well to cover up his tears. As he was riding"
    $ set_scene("alanaccident")
    b "Wrong lane! There is a car there!!!"
    na "He did not manage to hear their warning."

    # One-liner that does: stop BGM → fade to black → play accident → wait until done
    $ fade_to_black_and_play_sfx(accident)

    # (Continue the scene after the sound finishes…)
    na "Everything turns black."

    $ set_scene("black")

    jump arcade_beginning