label en_exemple:           #THIS IS A PROOF OF CONCEPT I WROTE FOR MY BEST FRIEND
    play music music_lilly fadein 3.0       #Play Lilly's theme
    scene ev lilly_tearoom                  #Lilly Tea room CG
    with Dissolve(3.0)
    #show lilly basic_smile at center       It's a fail, i didn't know it was a CG
    li "Hello, Lumi, I hope you're doing great today."      
    menu:
        "Am I doing great ?"
        "Yes Lilly, I'm fine.":
            return 1                    #It goes to en_ex1
        "No Lilly, I'm not doing well...":
            return 2                    #It goes to en_ex2    
label en_ex1:
    li "That's great!"
    li "I'm happy to hear that you are doing fine."
    
label en_ex2:
    li "Oh no !"
    li "Why aren't you doing well, if you don't mind telling me ?"
    $ reason = renpy.input("Why aren't I'm okay ?")
    li "So you're not doing well because [reason]"

