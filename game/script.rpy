# init python:
#     from alan import *
#     from serra import *
#     from klein import *
#     from loc import *

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


label start:
    # Scene 1 - University and the start of the story
    scene uni with fade
    play music mattari loop

    na "Universities and schools have been opened again. Most of the students are happy to be back..."

    show kh with dissolve
    k "ARCADE!"

    show kn with dissolve
    a "Bro, we are going to spend a week at the arcade?"

    show kshock with dissolve
    k "No, just one day, man!"

    show ku with dissolve
    a "Ahaha, one day, then it is okay, Klein!"

    show kh with dissolve
    k "Yeah, let’s plan something big, Lan!"

    # Transition to next scene
    scene rain_uni with fade
    na "The downpour was no joke. Alan had to wait under a flyover with other bikers."

    # play music music_rain loop
    a "Just my lucky day."

    na "While waiting for the rain to cool down, Alan turned on his phone and looked at his social media app."

    a "No way!"

    na "Alan quickly got on his bike. The other bikers were shocked at seeing what he was doing."

    a "I need answers!"

    na "Alan raced off. He wasn’t thinking straight, and tears poured from his eyes. He wasn't focused on the road."

    na "Alan didn’t hear the bikers shouting warnings. There was a car heading toward his lane. Everything turned black."

    # Transition to the arcade
    scene arcade with fade
    stop music
    # play music music_arcade loop

    na "Two guys are in an arcade. The arcade was lively. There were a lot of people, and happy sounds can be heard."

    k "So, this machine is what I like to play. You used to sit around waiting for me to finish..."

    a "Sorry, Klein..."

    k "Chill bro, we are in this together, right?"

    na "The arcade is still buzzing. More people came in. It’s Saturday, and the movement control order restrictions were lifted."

    na "Klein and Alan approached a bench, and Alan sat down."

    k "Alan, you don't mind me going to the washroom real quick?"

    a "Nah, I can wait here, go first."

    # Klein goes to the washroom
    scene arcade with fade
    k "I hope this helps, bro."

    na "Klein walks toward the washroom, reflecting on the past."

    # Flashback - July 4, 2020
    scene uni with fade
    k "Great news from the doc, you are recovering well and can use crutches soon."

    a "I guess so..."

    k "You still haven’t remembered what happened during that incident, right?"

    k "If it weren’t for the bike riders there, you would have been toast, you know?!"

    a "I wish I remember who had helped. Luckily, I didn’t suffer major injuries, except for the amnesia."

    a "Haven’t seen you laugh in some time."

    k "Your amnesia and your limb injuries, bro."

    a "True, maybe you can solve my amnesia by hitting my head."

    k "I did think about it, but not in your current condition."

    # Transition back to arcade scene
    scene arcade with fade

    na "Klein quickly walks to the washroom. He wonders about his friend, Alan."

    k "I just hope Alan is alright. I always make him wait. If he was back to his old self, he'd meme me for being late again."

    # Alan's reaction in the arcade
    scene arcade with fade
    a "Why, why, why, why does she seem to be so important?!"

    na "Alan's head hurts more than his injuries as he rushes to the girl. He falls down, and people rush to help."

    w "Alan?!"

    a "I need answers!"

    # Next phase: Alan confronts Serra
    scene store with fade
    w "You forgot me?! And you disappeared without even telling me anything!"

    a "I lost my memories, and Klein was the one who was with me. You weren’t there."

    w "I’m sorry."

    a "Okay, then, who are you?"

    w "I’m Serra..."

    a "Rings a bell."

    w "We used to hang out together, but Klein stopped showing up."

    a "So, something happened?"

    w "Kind of his own assumptions."

    # Tension builds
    scene arcade_nightmare with fade
    w "You’ll get your answers, but we need to go up to the second floor."

    na "They reach the second floor. Alan is confused."

    w "Let me explain everything, but first, let’s check out this machine."

    # Transition into supernatural scene
    na "The arcade machine lights up suddenly."

    a "What? This thing is working?"

    w "Can you just listen for once?"

    # Light begins to intensify
    scene arcade_nightmare with flash
    na "The light grows brighter, and Alan and Serra are pulled into the machine."

    # Klein arrives back at the arcade, confused
    scene arcade with fade
    k "Where are they? I just hope nothing happened."

    na "Klein is searching the arcade, confused."

    # Klein finds the bags
    scene store with fade
    k "Serra, what have you done?!"

    na "Klein picks up the bags and wonders where Serra and Alan have gone."

    # Supernatural event intensifies
    scene arcade_nightmare with flash
    na "The arcade machine powers up again, and Klein is drawn into the light."

    k "This has gotta be some sort of joke!"

    na "The light envelops Klein as he disappears."

    # Transition to unknown location
    scene arcade_nightmare with fade
    "The scene changes to an unknown location. Time is stagnant."

    s "I think I hit my head or something."

    a "Where’s Serra? Klein?"

    na "Alan looks around, confused by the unfamiliar environment."

    a "Well, guess some supernatural stuff happened... Not sure what to care about."

    return
