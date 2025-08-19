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
    label set_scene(scene_img):
    
        scene expression scene_img with dissolve  # scene image

    label play_music(music_file, music_vol=0.5):
    
    if music_file:
        play music music_file fadein 3.0 volume music_vol

    label stop_music():
        stop music fadeout 3.0

    label show_right(initial_character, new_character):
        hide initial_character
        show new_character:
            right

    label show_left(initial_character, new_character):
        hide initial_character
        show new_character:
            left

    label show_center(initial_character, new_character):
        hide initial_character
        show new_character:
            center

    label move_right(character, position):
        show character with moveinright:
            position

    label move_left(character, position):
        show character with moveinleft:
            position


    scene uni with fade
    play music mattari loop

    na "Universities and schools have been opened again. Most of the students are happy to be back..."

    # Klein appears from left
    show kh at left_half
    k "ARCADE!"

    # Alan appears from right
    show kn at right_half
    a "Bro, we are going to spend a week at the arcade?"

    # Klein responds
    k "No, just one day, man!"

    # Alan laughs
    a "Ahaha, one day, then it is okay, Klein!"

    # Klein plans
    k "Yeah, let’s plan something big, Lan!"

    # Transition to next scene
    scene rain_uni with fade
    na "The downpour was no joke. Alan had to wait under a flyover with other bikers."

    a "Just my lucky day."

    na "While waiting for the rain to cool down, Alan turned on his phone and looked at his social media app."

    a "No way!"

    na "Alan quickly got on his bike. The other bikers were shocked at seeing what he was doing."

    a "I need answers!"

    na "Alan raced off. He wasn’t thinking straight, and tears poured from his eyes. He wasn't focused on the road."

    na "Alan didn’t hear the bikers shouting warnings. There was a car heading toward his lane. Everything turned black."
