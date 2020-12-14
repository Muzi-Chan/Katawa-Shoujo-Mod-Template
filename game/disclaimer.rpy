 label en_disclaimer:
     "WARNING:" "This is a fan made mod, not affiliated nor approuved by Four Leaf Studio."
     "WARNING:" "This means you should have played the original game before this mod."
     menu:
         "WARNING:" "Do you certify you have played the original game before ?"
         'Yes':
             return
         'No':
             "WARNING:" "Go play the original game before this mod, NOW."
             $ renpy.quit()
