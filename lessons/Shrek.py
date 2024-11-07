import random

def intro_story ():
    print ("\n Welcome to the Kingdom of Far Far Away. You are Shrek, a daring, brave ogre.")
    print ("\n You are on a mission to rescue a beautiful princess from a tower guarded by a fierce dragon.")
    print ("\n Good luck on your journey! You may now select your weapon")
    select_weapon ()


def select_weapon ():
    weapons = ["Sword", "Bow", "Onion Breath"]
    print ("\n Choose your weapon via its associated number:")
    for i in range (len(weapons)):
        print (str(i+1) + ' - ' + weapons [i])
    choice = ''
    while not choice.isnumeric():
        choice = input ("\n > ")[0:1]
    choice = int(choice)
    global weapon
    weapon = weapons [choice-1]
    print ("\n You selected: " + weapon)

    if choice == 1:
        sword ()
    if choice == 2:
        bow()
    if choice == 3:
        onion_breath ()
    
    return choice


def sword ():
    print ("\n You selected the sword, good choice.")
    print ("\n Unfortunately this dragon has fire breath and is not challenged by a sword")
    print ("\n The amount of damage you can deal at one time is 8 (out of 8).")
    global player_damage
    player_damage = 8
    coin_toss ()


def bow ():
    print ("\n You selected the bow, excellent choice for a fire breathing dragon.")
    print ("\n Now you can shoot at him from afar.")
    print ("\n The amount of damage you can deal at one time has increased from 8 to 12!")
    global player_damage
    player_damage = 12
    coin_toss ()


def onion_breath ():
    print ("\n You have chosen to use your stinky onion breath, something you are very good at.")
    print ("\n The amount of damage you can deal at one time has increased from 8 to 10!")
    global player_damage
    player_damage = 10
    coin_toss ()


def coin_toss ():
    global player_health
    print ("\n To determine your health points, you must toss a coin.")
    print ("\n You pick up the coin and toss it in the air.")
    coin = random.randint (1,2)
    if coin == 1:
        coin = "heads"
    else:
        coin = "tails"
    print ("\n Pick heads or tails (H/t)")
    choice = ''
    while choice != 'H' and choice != 'T':
        choice = input ("\n > ")[0:1].upper()
    if choice == 'H':
        choice = "heads"
    else:
        choice = "tails"
    if coin == choice:
        print ("\n It's " + choice + ", nice job!")
        print ("\n Your health is at a full 50 points!")
        player_health = 50
        donkey ()
    else:
        print ("\n Sorry, it's " + coin + ". Your health has been decreased by 10.")
        player_health = 40
        donkey ()


def donkey ():
    global donkey_status
    print ("\n Before you begin on your quest, would you like to take Donkey with you?")
    print ("\n Donkey is your friend, but before you decide, remember that bringing him could be helpful, but he could also just get in your way!")
    print ("\n So, do you want to bring him? (Y/n)")
    choice = ''
    while choice != 'Y' and choice != 'N':
        choice = input ("\n > ")[0:1].upper()
    if choice == 'Y':
        print ("\n Awesome choice! Donkey will be able to help you on your quest.")
        donkey_status = 1
        start_game ()
    if choice == 'N':
        print ("\n It was nice you wanted to keep Donkey safe, but now you'll be alone while fighting on your quest.")
        donkey_status = 2
        start_game ()


def start_game ():
    global dragon_health
    dragon_health = 50
    print ("\n Are you ready to begin your journey? (Y/n) ")
    ready = ''
    while ready != 'Y' and ready != 'N':       
        ready = input ("\n > ")[0:1].upper()
    if ready == 'Y':
        knights()
    else:
        give_up ()


def knights ():
    global donkey_status
    global player_health
    print ("\n After a long trek across the land, you finally reach the castle")
    print ("\n The castle looms into the sky and the ominous sound of thunder echoes around you.")
    print ("\n As you approach the castle, you realize it is heavily guarded by knights!")
    if donkey_status == 1:
        print ("\n Thankfully you brought Donkey along, and he easily scares the knights away.")
        enter_castle ()
    if donkey_status == 2:
        print ("\n Too bad you don't have donkey with you! He could've helped...")
        print ("\n You fight the knights, but grow weary after your battle. Health decreases 5 points")
        player_health -= 5
        print ("\n You health is now " + str(player_health))
        enter_castle ()


def enter_castle ():
    print ("\n You carefully walk across a lava moat on a small bridge, barely escaping death")
    print ("\n When you enter into the castle, you hear a roar that shakes the entire building")
    print ("\n Do you still want to continue on your quest? (Y/n)")
    choice = ''
    while choice != 'Y' and choice != 'N':
        choice = input ("\n > ")[0].upper()
    if choice == 'Y':
        print ("\n Shrek, you have chosen to continue. Hopefully your decision was wise.")
        see_dragon()
    else:
        give_up ()


def see_dragon ():
    print ("\n You stumble into a massive stone room, and in the center of it lies the dragon.")
    print ("\n Smoke curls around its nose, and it lunges at you in an attack.")
    print ("\n Do you want to attack back? (Y/n)")
    choice = ''
    while choice != 'Y' and choice != 'N':
        choice = input ("\n >")[0].upper()
    if choice == 'Y':
        attack_dragon()
    if choice == 'N':
        give_up()


def attack_dragon ():
    global player_damage
    print ("\n You attack the monster for " + str(player_damage) + " damage with your " + weapon.lower())
    global dragon_health
    dragon_health -= player_damage
    if dragon_health <= 0: 
        print ("\n Incredible job Shrek, you defeated the dragon!")
        enter_tower()
    else:
        print ("\n Dragon's health: " + str(dragon_health) + "hp")
        dragon_attack ()


def dragon_attack ():
    damage = random.randint (0,5) * 2
    print ("\n The dragon attacks you for " + str(damage) + " damage")
    global player_health
    player_health -= damage
    if player_health <= 0:
        death ()
    else:
        print ("\n Your health: " + str(player_health) + " hp")
        print ("\n Continue attacking? (Y/n) ")
        choice = ''
        while choice != 'Y' and choice != 'N':
            choice = input ("\n > ")[0:1].upper()
        if choice == 'Y':
            attack_dragon()
        else:
            death()


def enter_tower ():
    print ("\n You enter the tower, climbing up the spiraling staircase")
    print ("\n There could be other traps along the way, do you still want to keep going? (Y/n)")
    choice = ''
    while choice != 'Y' and choice != 'N':
        choice = input ("\n > ")[0:1].upper()
    if choice == 'Y':
        print ("\n Good decision, there weren't any traps!")
        princess ()
    else:
        print ("\n You've come this far Shrek, you can take any other traps thrown in your way! Do you want to keep going? (Y/n) ")
        choice = ''
        while choice != 'Y' and choice != 'N':
            choice = input ("\n > ")[0:1].upper()
        if choice == 'Y':
            print ("\n Good decision, there weren't any traps!")
            princess ()
        else:
            give_up ()


def princess ():
    print ("\n You enter into a room at the top of the tower, and your gaze meets the sleeping princess.")
    print ("\n To wake the princess, will you kiss her or gently shake her awake? (Kiss/shake)")
    choice = ''
    while choice != 'kiss' and choice != 'shake':
        choice = input ("\n > ")
    if choice == 'kiss':
        kiss ()
    else:
        print ("\n Excellent decision! The princess awakens and tells you her name is Fiona.")
        print ("\n You voyage back to your swamp and live happily ever after.")
        print ("""
        
                                                .-.
                    ,                     .-' ,c'.
                __rK                    _)a  7  ;
                /  ~,)                  (_,      (
            _;   /a(                   |_.    :'|
            L/\.'__/                   \       ' )nnnK-.
            S  / (_                  .- L,-'   .dHHHb   |
            S( '\_\\                / dHb'----'dHHHHb    |
            S \  ,  )      _,-._   / dHHHb"x.dHHHHHHb     |
            S |'. '.______/_U/_ '.-z/dHHHp   'dHHHHHb\     |
            [H |  '..___.--'._C__  ) |         dHHHHHHb\ _   |
            /| |_  | \     L/'--._/_ ;                  k '  /
            |//- '-. ---.__         '|                 /     |
            (       '-.   '.        |               _'-.  _/
        .."' `.,  _ ,  :  | \      _\             ,/ ,  '/
        ."       ':   .     : |   .-' '',          : |/(/\]/
                \  /:  '  | :  /_      '...... .'/      |
                |     |  : / .' '--.__,     __.'\      /
                |   : ;  |/ |         '----'L,  |     /
                    \  : .   \  '-.________ /   ]  |____/
                    L_____'..'           _.7' _/  <,    >
                                        <___.'     /    |
                                                \____/
                                                            ____     _____


            """)
        play_again ()


def kiss ():
    print ("\n Not the best choice Shrek! The princess was only sleeping, and now she thinks you're a creep.")
    print ("\n You return to your swamp, but without Fiona. She decided to stay with Lord Farquad instead.")
    play_again ()


def death ():
    print ("\n You fought your hardest, but you have still died a valiant death")
    print ("""
            
        (  )   /\   _                 (     
            \ |  (  \ ( \.(               )                      _____
        \  \ \  `  `   ) \             (  ___                 / _   |
        (_`    \+   . x  ( .\            \/   \____-----------/ (o)   \_
        - .-               \+  ;          (  O                           \____
                                )        \_____________  `              \  /
        (__                +- .( -'.- <. - _  VVVVVVV VV V\                 \/
        (_____            ._._: <_ - <- _  (--  _AAAAAAA__A_/                  |
        .    /./.+-  . .- /  +--  - .     \______________//_              \_______
        (__ ' /x  / x _/ (                                  \___'          \     /
        , x / ( '  . / .  /                                      |           \   /
            /  /  _/ /    +                                      /              \/
        '  (__/                                             /                 |

        """)
    play_again()


def give_up ():
    print ("\n You have let fear get in the way of your success.")
    print ("\n You return to your swamp empty-handed and defeated- a very sad ogre indeed")
    play_again ()


def play_again ():
    print ("\n Would you like to play again? (Y/n)")
    choice = ''
    while choice != 'Y' and choice != 'N':
        choice = input ("\n > ")[0:1].upper()
    if choice == 'Y':
        intro_story ()


intro_story ()