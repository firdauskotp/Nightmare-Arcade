label meetingserra:
    $ set_scene("arcade", trans=fade)
    $ play_music(bittersweet)
    "15 minutes later"

    $ show_center("ai", "ah")
    a "Hmmm... Klein is taking a long time"
    a "I guess I do remember having fun here or Klein playing and raging at that rhythm game. Not much, but enough to make me laugh." 
    a "Heh"
    $ enter_from_left("sn", at_transform=left_side)
    $ exit_to_right("sn")

    stop music fadeout 1.0

    a "Wait... that girl!"
    n "Alan rushed to the girl"

    $ fade_to_black_and_play_sfx(thud)

    $ fade_to_black_and_play_sfx(alanfall)



    $ enter_from_right("ai", at_transform=right_side)

    a "Sorry, Klein…"
    k "Chill, bro. We’re in this together, right?"
    $ show_left("ksmile", "kn")

    na "It’s a Saturday; movement restrictions were lifted not long ago. More people drift in."
    na "Alan sits on a bench."
    $ set_scene("arcadebench", trans=fade)

    k "Mind if I run to the washroom?"
    a "Nah, I’ll wait here. Take your time"
    k "Haha, sure sure. Be safe alright, call me if you need anything"
    a "Sure!"

    $ set_scene("arcadehallway", trans=fade)
    stop music fadeout 3.0
    $ show_center("kn", "ah")

    k "Alan..."

    $ play_music(memories)
    $ set_scene("flashback1", trans=fade)

    "4th July 2020, Alan's house"

    k "Great news from the doc, you are recovering well and can walk without crutches much...soon."
    a "I guess so..."
    k "You still haven't remembered what happened during that incident, don't you?"
    a "That and even a lot more things"
    k "Yeah, took you a long time to even just remember my name, let alone who I was..."
    a "Klein I..."
    k "Alan, it isn't your fault, it never was."
    k "If it weren't for the bike riders there, you would have been toast, you know."
    a "I wish I remembered who had even helped me. Luckily I idn' suffer major injuries, except this amnesia"
    k "And those bruises you chose to cover up like that"
    a "Ahaha, I guess so"
    a "Hmm, what's that smile?"
    k "Haven't seen you laughed in some time"
    k "Your amnesia and those limb injuries bro"
    a "Maybe you can sovle my amnesia by hitting my head!"
    k "Ehehe"
    a "??? You are not actually"
    k "Not in your current condition. I just thought of a good idea though. Let's plan, next Saturday, arcade!"
    a "Bro what?"
    k "We used to hang out there all the time. Maybe that will jog your memory a bit. I wil bring you, and I will treat you. My offer as being your wonderful friend hahahha"
    k "It is also something small to repay all that you have done for me over the past 5 years."
    a "Okay I guess?"
    k "Then it is settled!"

    $ set_scene("arcadehallway", trans=fade)

    $ show_center("kn", "ah")

    k "I really hope, this helps..."



    
    



