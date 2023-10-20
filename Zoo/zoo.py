""" Zoo project """

print("""I love animals!
Let's check out the animals...
The deer looks fine.
The lion looks healthy.""")

# Camel
camel = r"""
The camel habitat...
 ___.-''''-.
/___  @    |
',,,,.     |         _.'''''''._
     '     |        /           \
     |     \    _.-'             \
     |      '.-'                  '-.
     |                               ',
     |                                '',
      ',,-,                           ':;
           ',,| ;,,                 ,' ;;
              ! ; !'',,,',',,,,'!  ;   ;:
             : ;  ! !       ! ! ;  ;   :;
             ; ;   ! !      ! !  ; ;   ;,
            ; ;    ! !     ! !   ; ;     
            ; ;    ! !    ! !     ; ;
           ;,,      !,!   !,!     ;,;
           /_I      L_I   L_I     /_I
Look at that!"""

# Lion
lion = r"""
The lion habitat...
                                               ,w. 
                                             ,YWMMw  ,M  , 
                        _.---.._   __..---._.'MMMMMw,wMWmW, 
                   _.-""        '''           YP"WMMMMMMMMMb, 
                .-' __.'                   .'     MMMMW^WMMMM;     
            _, .'.-'"; `,       /`     .--""      :MMM[==MWMW^; 
 ,mM^"     ,-'.'   /   ;      ;      /   ,       MMMMb_wMW"  @\ 
,MM:.    .'.-'   .'     ;     `\    ;     `,     MMMMMMMW `"=./`-, 
WMMm__,-'.'     /      _.\      F'''-+,,   ;_,_.dMMMMMMMM[,_ / `=_} 
"^MP__.-'    ,-' _.--""   `-,   ;       \  ; ;MMMMMMMMMMW^``; __|            
          /   .'            ; ;         )  )`{  \ `"^W^`,   \  :           
          /  .'             /  (       .'  /     Ww._     `.  `" 
         /  Y,              `,  `-,=,_{   ;      MMMP`""-,  `-._.-,         
         (--, )                `,_ / `) \/"")      ^"      `-, -;"\: 

The lion is roaring!"""

# Deer
deer = r"""
The deer habitat...
   /|       |\
`__\\       //__'
   ||      ||
 \__`\     |'__/
   `_\\   //_'
   _.,:---;,._
   \_:     :_/
     |@. .@|
     |     |
     ,\.-./ \
     ;;`-'   `---__________-----.-.
     ;;;                         \_\
     ';;;                         |
      ;    |                      ;
       \   \     \        |      /
        \_, \    /        \     |\
          |';|  |,,,,,,,,/ \    \ \_
          |  |  |           \   /   |
          \  \  |           |  / \  |
           | || |           | |   | |
           | || |           | |   | |
           | || |           | |   | |
           |_||_|           |_|   |_|
          /_//_/           /_/   /_/
Pretty good!"""
# Goose
goose = r"""
The goose habitat...
                                _,-"" "". 
                              ,'  ____   `. 
                            ,'  ,'    `.   `._ 
   (`.         _..--.._   ,'  ,'        \     \ 
  (`-.\    .-""        ""'   /          (  d _ b 
 (`._  `-"" ,._             (            `-(    \  
 <_  `     (  <`<            \              `-._\   
 <`-       (__< <            :    
 (__          (_<_<          ; 
 `------------------------------------------ 
Beautiful!"""

# Bat
bat = r"""
The bat habitat...
_________________               _________________
 ~-.              \  |\___/|  /              .-~
     ~-.           \ / o o \ /           .-~
        >           \\  W  //           <
       /             /~---~\             \
      /_            |       |            _\
         ~-.        |       |        .-~
            ;        \     /        i
           /___      /\   /\      ___\
                ~-. /  \_/  \ .-~
                   V         V
It's doing fine."""

# Rabbit
rabbit = r"""
The rabbit habitat...
                      /|      __
                     / |   ,-~ /             
                    Y :|  //  /       
                    | jj /( .^     
                    >-"~"-v"           
                   /       Y
                  jo  o    |     
                 ( ~T~     j    
                  >._-' _./      
               /| ;-"~ _  l
              / l/ ,-"~    \   
              \//\/      .- \
               Y        /    Y
               l       I     !
               ]\      _\    /"\
              (" ~----( ~   Y.  )
It looks fine!"""

animals = [camel, lion, deer, goose, bat, rabbit]
print("Please enter the number of the habitat you would like to view:")
while True:
    user_input = input()
    if user_input.isdigit():
        user_input = int(user_input)
        if 1 <= user_input <= len(animals):
            print(animals[int(user_input)-1])
            print("Please enter the number of the habitat you would like to view:")
        else:
            print("Please enter a valid number or 'exit' to exit.")
    elif user_input == "exit":
        print("See you later!")
        break
    else:
        print("Please enter a valid number or 'exit' to exit.")
