define k = Character("Klein", color="#FFA500")  # Orange
define a = Character("Alan", color="#FF0000")  # Red
define p = Character("People", color="#FFFFFF")  # White
define m = Character("Man", color="#008000")  # Green
define w = Character("Woman", color="#800080")  # Purple
define r = Character("Registry", color="#800080")  # Purple
define s = Character("Serra", color="#0000FF")  # Blue
define n = Character("Nolan", color="#8B4513")  # Brown
define na = Character("Narration", color="#808080")  # Grey
define l = Character("Lucia", color="#FFFF00")  # Yellow. Original name Luciana, meaning illuminate in Latin, or light
#but Klein always call her Lucia





transform left_side:
    xalign -0.4
    yalign -0.3

transform center_side:
    xalign 0.5
    yalign 1.0

transform right_side:
    xalign 1.0
    yalign -0.3
init python:
    # Change scene with dissolve
    
    def set_scene(image_name, trans=dissolve, layer="master"):
        # 1) Clear the layer (equivalent to: scene)
        renpy.scene(layer=layer)
        # 2) Show an image by its defined name (equivalent to: show <name>)
        renpy.show(image_name, layer=layer)
        # 3) Apply transition (equivalent to: with dissolve)
        if trans:
            renpy.with_statement(trans)

    # Play background music
    def play_music(music_file, music_vol=0.5):
        if music_file:
            renpy.music.play(music_file, fadein=3.0, loop=True, synchro_start=True, channel="music")
            renpy.music.set_volume(music_vol, delay=0, channel="music")

    # Stop background music
    def stop_music():
        renpy.music.stop(fadeout=3.0, channel="music")

    def _safe_show(image_name, at_transform=None, layer="master"):
        """
        Shows an image only if it's defined; logs a note otherwise.
        """
        try:
            # renpy.has_image works with tag names like "klein neutral"
            if renpy.has_image(image_name):
                if at_transform is not None:
                    renpy.show(image_name, at_list=[at_transform], layer=layer)
                else:
                    renpy.show(image_name, layer=layer)
                return True
            else:
                renpy.log("-- Image not found: {}".format(image_name))
                return False
        except Exception as e:
            renpy.log("-- Error showing '{}': {}".format(image_name, e))
            return False

    def show_left(initial_character, new_character):
        renpy.hide(initial_character)
        _safe_show(new_character, at_transform=left_side)

    def show_center(initial_character, new_character):
        renpy.hide(initial_character)
        _safe_show(new_character, at_transform=center_side)

    def show_right(initial_character, new_character):
        renpy.hide(initial_character)
        _safe_show(new_character, at_transform=right_side)

    # ---- slide-on-entry helpers (transitions are applied with 'with', not in at_list)
    def enter_from_left(image_name, at_transform=center_side):
        if _safe_show(image_name, at_transform=at_transform):
            renpy.with_statement(moveinleft)

    def enter_from_right(image_name, at_transform=center_side):
        if _safe_show(image_name, at_transform=at_transform):
            renpy.with_statement(moveinright)
label start:



    $ set_scene("university")
    $ play_music(mattari)
    # play music mattari loop

    na "17th June 2020"

    na "Universities and schools have been opened again. Most of the students are happy to be back as online learning had been difficult."
    na "They missed hanging out with their friends and that 'education' vibe."
    na "At a university in town connected to a mall, two students head out. Semester break is near, and they’re planning what to do."

    # Klein pops in from the left, slightly raised (use your tuned left_side transform)
    $ enter_from_left("kh", at_transform=left_side)
    k "ARCADE!"

    $ enter_from_right("ah", at_transform=right_side)
    a "Bro, we are going to spend a week at the arcade?"

    # Swap Klein to neutral without slide (optional)
    $ _safe_show("kn", at_transform=left_side)
    k "No, just one of the days, man!"
    a "Ahaha, one day—then it’s okay, Klein!"

    k "Hahaha… yeah, let’s plan something big, Lan!"
    a "Of course!"
    na "They chat while walking towards their motorcycles."

    scene rain_uni with fade
    na "Thunder roared as drizzle turned to steady rain."

    k "I think I’ll just park at the nearest station and take the train home."
    a "Eh? Since when are you scared of rain?"
    na "Alan sits on his bike and turns the key. The engine grumbles—then another thunderclap booms."

    k "That doesn’t scare you?"
    na "Klein removes his red cap and starts his scooter."
    na "Alan laughs, pulls on a snow cap, then his helmet. Klein fits a full-face helmet."

    a "Yeah… this is pretty scary."
    a "But there isn’t a train station near my place, remember?"
    k "Alan, your house is further than mine. Ride safely, alright?"
    na "They say their goodbyes and ride off."

    # ===========================
    # Alan’s downpour scene
    # ===========================
    na "The downpour was no joke. Alan waits under a flyover with other bikers."
    a "Just my lucky day… Let's just scroll through Insta while waiting"
    na "He unlocks his phone and scrolls through social media. His eyes widen."
    a "No way…"

    na "He rushes to his bike; the other riders stare."
    a "I need answers!"
    p "What are you doing?! You can get hurt!"
    na "A few bikers try to calm him."
    a "I don’t care!"

    na "He speeds off, mind reeling. He isn’t riding straight."
    a "No, no, no, no, no!"
    na "Tears mix with rain. Shouts from the flyover fade behind him—warnings about a car in his lane."
    na "Everything turns black."

    # ===========================
    # 11th July 2020 — Lively arcade
    # ===========================
    $ set_scene("arcade", trans=fade)
    na "11th July 2020"
    na "The arcade is lively—crowds, lights, and the clatter of buttons and tickets."
    na "But for two men inside, the mood is subdued."

    # Klein present (left), talking; Alan sits/stands nearby (no sprite needed)
    $ _safe_show("kn", at_transform=left_side)
    k "So, this machine’s what I like to play. You used to wait and complain I was wasting money."
    na "Klein points to a rhythm game, forcing a small laugh."

    a "Sorry, Klein…"
    k "Chill, bro. We’re in this together, right?"
    na "Alan gives a brief but sincere smile."

    na "It’s a Saturday; movement restrictions were lifted not long ago. More people drift in."
    na "Alan sits on a bench."
    k "Mind if I run to the washroom?"
    a "Nah, I’ll wait here."

    # ===========================
    # One week earlier — flashback
    # ===========================
    na "A week earlier… 4th July 2020."
    na "Evening birdsong; nearly night. Alan, in a football jacket, pushes Klein’s wheelchair home."

    a "Great news from the doc—you’re recovering well. Crutches soon."
    k "I’m trying to be positive."
    a "I guess so…"
    k "You still haven’t remembered what happened, have you?"
    a "That—and a lot of other things."
    k "Took you a while just to remember my name."
    na "Alan looks guilty; Klein waves it off."
    k "If it weren’t for those riders, you’d have been toast!"
    a "I wish I remembered who helped. Thankfully, no major injuries—just… this amnesia."
    k "Haven’t seen you laugh in a while."
    a "True. Maybe you could fix my amnesia by bonking me."
    k "…I did think of something. Not that."
    a "What?"
    k "Let’s go to the arcade next Saturday. We used to hang out there. Maybe it will jog your memory."
    k "My treat—as your wonderful friend, haha. And to repay you for everything."
    a "Okay… I guess?"
    k "Then it’s settled!"

    # ===========================
    # Back to 11th July — bench
    # ===========================
    na "Back to 11th July."
    k "I hope this helps, bro…"
    na "Klein heads to the washroom."

    na "Alan sits, scanning the crowd."
    a "I do remember fun here… or Klein raging at that rhythm game."
    na "He chuckles—then freezes."
    na "A girl in a snow cap, blue hair, baggy jacket and long trousers passes by."
    a "Why does she feel so important…?"

    na "Alan grabs his crutches and rushes, stumbling. He falls; people hurry over."
    w "Are you okay?"
    na "It’s the girl. She helps him up. Her eyes widen."
    s "Al… Alan?!"

    a "Everyone, I’m alright—thank you. I just need to speak with her."
    a (serious) "Tell me—who are you?"
    s "You’ve got to be joking. You forgot me—and disappeared without a word—now you’re like this?!"
    a "Who are you? I was in an accident and—"
    s "An accident? Sounds like something Klein would tell you to say."
    a "Keep his name out of this. I’ve lost my memories. He was with me—you weren’t."
    a "You seem familiar. You clearly know me."

    s "…I’m sorry."
    a "Thank you. My question still stands."
    s "Serra."
    a "Rings a bell."
    s "Of course it does. We—"
    a "We…?"
    s "Let’s walk the arcade. I’ll explain."
    a "You know Klein too?"
    s "We kind of hate each other."
    a "Why?"
    s "I’ll get to that."

    na "They walk; people ask if Alan’s okay. He nods."
    s "Brings back memories, doesn’t it? Klein introduced us here."
    a "And we came here often?"
    s "A lot. Shooters, a horror cabinet… we used to be a trio. Then Klein stopped coming. It was either you two, or you and me."
    a "Something happened?"
    s "His assumptions."
    a "That doesn’t help."

    # Stairs to 2F (restricted)
    na "They reach a staircase to the second floor, roped off for maintenance."
    s "Let’s go."
    a "Are you daft? We’ll get sued!"
    s "Shh. We need privacy."
    a "I’m not sure I want to hear this now."
    s "Just follow me!"

    # Old machine upstairs
    na "Upstairs stands a huge, worn cabinet. The title is barely legible."
    a "\"Arcade Nightmare\", huh? Cliché."
    a "Go on, Serra. Make it quick—Klein will be back soon."
    s "Fine. From the start…"

    na "A dead screen flickers. A bright light spills from the broken marquee."
    a "Huh? It works?"
    s "Can you listen for once?"
    a "For once? I’ve been listening."
    s "Do you want to fight about this now?"
    na "The light grows—brighter, brighter—"

    # ===========================
    # Klein returns to the bench
    # ===========================
    $ set_scene("arcade")
    k "Who knew the loo was that far… I hope Alan’s alright. If he were himself, he’d meme me for being late."
    na "Klein finds the bench empty. He hurries to the front counter."

    r "Welcome. Can I help?"
    k "Have you seen my friend? Bandages and crutches."
    r "Yes, he fell earlier—caused a bit of a scene."
    k "He WHAT?!"
    r "Relax. A girl helped him. They walked into the arcade together."
    k "A girl, eh? How’d she look?"
    r "About your height. Snow cap. Baggy jacket, long trousers. A bit goth."
    k "…That was his taste… that was his—wait."
    k "Is her hair coloured?"
    r "Blue."
    k "…Thanks. I need to sort this out."

    na "Klein dashes off."
    k "Serra, what are you planning this time…?"
    na "He finds a quiet staircase. No one around."
    k "She wouldn’t… he’s on crutches. Then again, not the first selfish stunt."
    na "Upstairs: the massive cabinet. Dead. No one there."
    k "Two backpacks… Alan’s—and that thorny black satchel. Serra."
    k "Where did you two go? Damn it, Serra—what have you done?!"

    na "The machine hums alive. Light blooms."
    k "It works? Looked rusty enough to be scrap—"
    na "The light surges and engulfs him."
    k "This has got to be a joke—!"

    # ===========================
    # Unknown place
    # ===========================
    $ set_scene("arcade_nightmare", trans=fade)
    na "Location: Unknown. Time: Stagnant. People: Serra, Alan."
    a "Feels like I hit my head."
    na "Alan steadies himself on crutches."
    a "Where’s Serra? Klein?"
    na "Silence answers. Neon shadows curve like a maze."
    a "Well… guess some supernatural nonsense happened."
    na "He scans the room—Pac-Man-esque corridors formed by dead machines and flickering signs…"

    return
