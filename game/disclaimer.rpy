 label en_disclaimer:
     "WARNING:\n This is a fan made mod, not affiliated nor approuved by Four Leaf Studio."
     "{cps=100}WARNING:{/cps}\n This means you should have played the original game before this mod."
     menu:
         "Do you certify you have played the original game before ?"
         'Yes':
             return
         'No':
             "Go play the original game before this mod, NOW."
             $ renpy.quit()
