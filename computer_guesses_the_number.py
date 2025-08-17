import time

def noc1():
    print('''
    1    17   33   49   65   81   97
    3    19   35   51   67   83   99
    5    21   37   53   69   85
    7    23   39   55   71   87
    9    25   41   57   73   89
    11   27   43   59   75   91
    13   29   45   61   77   93
    15   31   47   63   79   95
    ''')
def noc2():
    print('''
    2    18   34   50   66   82   98
    3    19   35   51   67   83   99
    6    22   38   54   70   86
    7    23   39   55   71   87
    10   26   42   58   74   90
    11   27   43   59   75   91
    14   30   46   62   78   94
    15   31   47   63   79   95
    ''')
def noc3():
    print('''
    4    20   36   52   68   84   100
    5    21   37   53   69   85
    6    22   38   54   70   86
    7    23   39   55   71   87
    12   28   44   60   76   92
    13   29   45   61   77   93
    14   30   46   62   78   94
    15   31   47   63   79   95
    ''')
def noc4():
    print('''
    8    15   30   45   60   75   90
    9    24   31   46   61   76   91
    10   25   40   47   62   77   92
    11   26   41   56   63   78   93
    12   27   42   57   72   79   94
    13   28   43   58   73   88   95
    14   29   44   59   74   89
    ''')
def noc5():
    print('''
    16   23   30   53   60   83   90
    17   24   31   54   61   84   91
    18   25   48   55   62   85   92
    19   26   49   56   63   86   93
    20   27   50   57   80   87   94
    21   28   51   58   81   88   95
    22   29   52   59   82   89
    ''')
def noc6():
    print('''
    32   39   46   53   60   99
    33   40   47   54   61   100
    34   41   48   55   62
    35   42   49   56   63
    36   43   50   57   96
    37   44   51   58   97
    38   45   52   59   98
    ''')
def noc7():
    print('''
    64   71   78   85   92   99
    65   72   79   86   93   100
    66   73   80   87   94
    67   74   81   88   95
    68   75   82   89   96
    69   76   83   90   97
    70   77   84   91   98
    ''')


def intro():
    msg=('''
    Welcome to the Number Guess application! 
    Get ready to be amazed as the computer takes on 
    the challenge of guessing your number. 
    Prepare to witness its computational prowess 
    as it cleverly narrows down the possibilities,
    honing in on the mystery number hidden in your mind.
    With each guess, the computer will employ its algorithmic intelligence
    to inch closer to the target, leaving you in awe 
    of its deduction skills. 
    
    Are you ready to put the computer to the test? 
    Let the exciting game of number guessing begin!
    ''')
    for x in msg:
            print(x, end='')
            time.sleep(0.03)
    

def clear():
    for x in range(65):
               print()
    


def main():
           no = 0
           clear()
           intro()
           wait = time.sleep(3) 
           while True:
                 clear()
                 wait=time.sleep(0.5)
                 noc1()
                 a = input('Is the number you are thinking in this list of number? Enter "y" or "yes": ')
                 a.lower()

                 if a == 'y' or a == 'yes':
                    no = no + 1

                 noc2()
                 b = input('Is the number you are thinking in this list of number? Enter "y" or "yes": ')
                 b.lower()

                 if b == 'y' or b == 'yes':
                    no = no + 2

                 noc3()
                 c = input('Is the number you are thinking in this list of number? Enter "y" or "yes": ')
                 c.lower()

                 if c == 'y' or c == 'yes':
                    no = no + 4

                 noc4()
                 d = input('Is the number you are thinking in this list of number? Enter "y" or "yes": ')
                 d.lower()

                 if d == 'y' or d == 'yes':
                    no = no + 8

                 noc5()
                 e = input('Is the number you are thinking in this list of number? Enter "y" or "yes": ')
                 e.lower()

                 if e == 'y' or e == 'yes':
                    no = no + 16

                 noc6()
                 f = input('Is the number you are thinking in this list of number? Enter "y" or "yes": ')
                 f.lower()

                 if f == 'y' or f == 'yes':
                    no = no + 32

                 noc7()
                 g = input('Is the number you are thinking in this list of number? Enter "y" or "yes": ')
                 g.lower()

                 if g == 'y' or g == 'yes':
                    no = no + 64
                 break
           print('Your number is : ', no)


main()