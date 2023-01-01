#!/usr/bin/python
import sys
from colorama import Fore, Back, Style
import art
import time

try :
    name=sys.argv[1]
    cake="""
              *                                             *
    
                                                   *
    
                        *
    
                                      *
    
                                                                *
    
             *
    
                                                      *
    
                 *
    
                               *             *
    
                                                         *
    
          *                                                               *
    
                   *
    
                                   (             )
    
                           )      (*)           (*)      (
    
                  *       (*)      |             |      (*)
    
                           |      |~|           |~|      |          *
    
                          |~|     | |           | |     |~|
    
                          | |     | |           | |     | |
    
                         ,| |a@@@@| |@@@@@@@@@@@| |@@@@a| |.
    
                    .,a@@@| |@@@@@| |@@@@@@@@@@@| |@@@@@| |@@@@a,.
    
                  ,a@@@@@@| |@@@@@@@@@@@@.@@@@@@@@@@@@@@| |@@@@@@@a,
    
                 a@@@@@@@@@@@@@@@@@@@@@' . `@@@@@@@@@@@@@@@@@@@@@@@@a
    
                 ;`@@@@@@@@@@@@@@@@@@'   .   `@@@@@@@@@@@@@@@@@@@@@';
    
                 ;@@@`@@@@@@@@@@@@@'     .     `@@@@@@@@@@@@@@@@'@@@;
    
                 ;@@@;,.aaaaaaaaaa       .       aaaaa,,aaaaaaa,;@@@;
    
                 ;;@;;;;@@@@@@@@;@      @.@      ;@@@;;;@@@@@@;;;;@@;
    
                 ;;;;;;;@@@@;@@;;@    @@ . @@    ;;@;;;;@@;@@@;;;;;;;
    
                 ;;;;;;;;@@;;;;;;;  @@   .   @@  ;;;;;;;;;;;@@;;;;@;;
    
                 ;;;;;;;;;;;;;;;;;@@     .     @@;;;;;;;;;;;;;;;;@@@;
    
             ,%%%;;;;;;;;@;;;;;;;;       .       ;;;;;;;;;;;;;;;;@@;;%%%,
    
          .%%%%%%;;;;;;;@@;;;;;;;;     ,%%%,     ;;;;;;;;;;;;;;;;;;;;%%%%%%,
    
         .%%%%%%%;;;;;;;@@;;;;;;;;   ,%%%%%%%,   ;;;;;;;;;;;;;;;;;;;;%%%%%%%,
    
         %%%%%%%%`;;;;;;;;;;;;;;;;  %%%%%%%%%%%  ;;;;;;;;;;;;;;;;;;;'%%%%%%%%
    
         %%%%%%%%%%%%`;;;;;;;;;;;;,%%%%%%%%%%%%%,;;;;;;;;;;;;;;;'%%%%%%%%%%%%
    
         `%%%%%%%%%%%%%%%%%,,,,,,,%%%%%%%%%%%%%%%,,,,,,,%%%%%%%%%%%%%%%%%%%%'
    
           `%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%'
    
               `%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%'
    
                        ''''''''''''',,,,,,,,,''''''''''''''' 
                                     `%%%%%%%'
    
                                      `%%%%%'
    
                                        %%%                  
    
                                       %%%%%
    
                                    .,%%%%%%%,.
    
                               ,%%%%%%%%%%%%%%%%%%%,
    
    
    """
    
    happybd="""
    
                                                  YYYY            YY
    
    HHHHH         HHHHH                             YYY          YYYY
    
    HHHHH         HHHHH                  PP PPPPPP   YYY         YYY
    
      HHH         HHH                     PPP    PP   YYY       YYY
    
      HHH         HHH    AAAAA  PP PPPPPP  PP    PP    YYY     YYY
    
      HHH         HHH   AAAAAAA  PPP    PP PP    PP     YYY   YYY
    
      HHH         HHH  AA     AA  PP    PP PP    PP      YYY YYY
    
      HHH         HHH  AA     AA  PP    PP PPPPPPP        YYYYY
    
      HHHHHHHHHHHHHHH  AA     AA  PP    PP PP             YYYY
    
      HHHHHHHHHHHHHHH  AA     AA  PPPPPPP  PP            YYYY   -------
    
      HHHHHHHHHHHHHHH  AAAAAAAAA  PP       PP           YYYY    -------
    
      HHH         HHH  AAAAAAAAA  PP       PP          YYYY     -------
    
      HHH         HHH  AA     AA  PP       PP         YYYY
    
      HHH         HHH  AA     AA  PP       PP        YYYY
    
      HHH         HHH  AA     AA  PP       PP      YYYYYY
    
      HHH         HHH  AA     AA  PP       PP     YYYYYYY
    
      HHH         HHH             PP       PP    YYYYYYY
    
    HHHHH         HHHHH           PP       PP   YYYYYYY
    
    HHHHH         HHHHH           PP       PP  YYYYYYY
    
                                                YYYYY
    
    BBBBBBBBBBBBB                                YYY
    
    BBBBBBBBBBBBBB                                Y
    
     BBBB       BBB    II                                   YYY             YYY
    
      BB         BB    II               DDDDDDDDDDDDD       YYYY           YYYY
    
      BB         BB                     DDDDDDDDDDDDDD        YY            YY
    
      BB         BB   III  RRR RRRR        DDD      DDD      A YY          YY
    
      BB         BB    II   RRRR  RR       DDD      DDD     AAA YY        YY
    
      BB        BBB    II    RRR           DDD      DDD    AAAAA YY      YY
    
      BBB     BBBB     II    RR            DDD      DDD   AAAAAAA YY    YY
    
      BBBBBBBBBBB      II    RR            DDD      DDD  AA     AA YY  YY
    
      BBBBBBBBB        II    RR            DDD      DDD  AA     AA  YYYY
    
      BBBBBBBBBBB      II    RR            DDD      DDD  AAAAAAAAA   YYY
    
      BBB     BBBB    IIII  RRRR           DDD      DDD  AAAAAAAAA   YYY
    
      BB        BBB             HHH        DDD      DDD  AA     AA   YYY
    
      BB         BBB    TT     HHHH        DDD      DDD  AA     AA   YYY
    
      BB         BBB    TT     HH          DDD      DDD  AA     AA   YYY
    
      BB          BBB TTTTTT   HH          DDD      DDD  AA     AA   YYY
    
      BB          BBB   TT     HH          DDD      DDD              YYY
    
      BB          BBB   TT     HHHHHHHH  DDDDDDDDDDDDD               YYY
    
      BB         BBB    TT     HH     HH DDDDDDDDDDDD               YYYY
    
     BBBB       BBBB    TT     HH     HH                           YYYY
    
    BBBBBBBBBBBBBBB     TT  TT HH     HH    YYYYYYYYYYYYYYYYYYYYYYYYYY
    
    BBBBBBBBBBBBBB       TTTT  HH     HH    YYYYYYYYYYYYYYYYYYYYYYYY
    
                              HHHH   HHHH   YYYYYYYYYYYYYYYYYYYYYY
    
    
    
    ------------------------------------------------
    """
    
    
    
    
    wish1="""           )

          (.)

          .|.

          l8J

          | |

      _.--| |--._

   .-';  ;`-'& ; `&.

  & &  ;  &   ; ;   \

  \      ;    &   &_/

   F''''---...---''''J

   | | | | | | | | |

   J | | | | | | | F

    `---.|.|.|.---'

                


\nWish you a many many happy returns of the day.\n May God bless you with health, wealth and prosperity in your life.\n HAPPY BIRTHDAY"""
    
    
    wish2="""                 ,

                (_)

                |-|

                | |

                | |

               .| |.

              |'---'|

              |~  ~~|

          .-@'|  ~  |'@-.

         (@    '---'    @)

         |'-@..__@__..@-'|

      () |~  ~ ~ ~     ~ | ()

     .||'| ~() ~   ~ ()~ |'||.

    ( || @'-||.__~__.||-'@ || )

    |'-.._  ||   @   ||  _..-'|

    |~ ~  '''---------'''  ~  |

    |  ~  ~  H A P P Y ~  ~  ~|

    | ~   B I R T H D A Y ~ ~ |

sub  '-.._By LearnEHKing_..-'

          '''---------'''\nMay your sweet smile never fade away.\nI wish you a very happy and sweet birthday.\nGood bless you."""
    
    wish3="""                0   0

                |   |

            ____|___|____

         0  |~ ~ ~ ~ ~ ~|   0

         |  |           |   |

      ___|__|___________|___|__

      |/\/\/\/\/\/\/\/\/\/\/\/|

  0   |       H a p p y       |   0

  |   |/\/\/\/\/\/\/\/\/\/\/\/|   |

 _|___|_______________________|___|__

|/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/|

|                                   |

|         B i r t h d a y! ! !      |

| ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ |

|___________________________________|



\nMay you achieve everything you desire in life.\nI wish you a very sweet and happy birthday.\nMay you have an awesome life ahead.\nEnjoy your day"""
    
    print(Fore.BLUE)
    for a in cake :
        print(a,end='')
        time.sleep(0.003)
    print(Fore.MAGENTA)
    for a in happybd :
        print(a,end='')
        time.sleep(0.003)
    print("\n"*5)
    print(Fore.RED)
    for a in wish1 :
        print(a,end='')
        time.sleep(0.003)
    print("\n"*5)
    print(Fore.YELLOW)
    for a in wish2 :
        print(a,end='')
        time.sleep(0.003)
    print("\n"*5)
    print(Fore.CYAN)
    for a in wish3 :
        print(a,end='')
        time.sleep(0.003)
    
    print("\n"*5)
    
    
    print(Fore.RED+"HAPPY BIRTHDAY ..........")
    time.sleep(1)
    
    print("\n"*5)
    
    
    
    print(Fore.BLUE+Back.RED)
    print("\n"*5)
    art.tprint("Happy \n     Birthday \t\n"+name)
    print(Style.RESET_ALL)
    print("By LearnEHKing")
except Exception as e :
    print(e,"\nUsage : bash birthdaywish/main.sh 'name'")
    print("Example: bash birthdaywish/main.sh 'LearnEHKing'")
    print("For wishing Birthday")
    
    print("\n\nBy LearnEHKing \nYouTube -> LearnEHKing")
    print("\nSubscribe for more tutorials and Tools.")