from random import randint # Do not delete this line

def displayIntro():
    file=open("hangman-ascii.txt", 'r')
    print(''.join(file.readlines()[0:23]))


def displayEnd(result):
    if result==True:
        file=open("hangman-ascii.txt", 'r')
        print(''.join(file.readlines()[190:203]))
    else:
        file=open("hangman-ascii.txt", 'r')
        print(''.join(file.readlines()[99:112]))


    
            
def displayHangman(state):
    if state == 5:
        file=open("hangman-ascii.txt", 'r')
        print(''.join(file.readlines()[23:33]))
    elif state == 4:
        file=open("hangman-ascii.txt", 'r')
        print(''.join(file.readlines()[36:46]))
    elif state == 3:
        file=open("hangman-ascii.txt", 'r')
        print(''.join(file.readlines()[49:59]))  
    elif state == 2:
        file=open("hangman-ascii.txt", 'r')
        print(''.join(file.readlines()[62:72]))
    elif state == 1:
        file=open("hangman-ascii.txt", 'r')
        print(''.join(file.readlines()[75:85]))      
    elif state == 0:
        file=open("hangman-ascii.txt", 'r')
        print(''.join(file.readlines()[88:98]))   
        
def getWord():
    file=open("hangman-words.txt", 'r')
    get_Random = file.readlines()[randint(0,852)].replace('\n','')
    return(get_Random)

def valid(c):
    if c.isalpha() and c.islower():
        if len(c)==1:
            return True
        else:
            return False
    else:
        return False


def play():
    get_Random=getWord()
    numOfUnder=[]
    hearts=5
    replacer = False
    for i in range(len(get_Random)):
        numOfUnder.append('_')

    while 0<hearts<=5:
        replacer = False
        displayHangman(hearts)
        print('Guess the word:  ' + ''.join(numOfUnder))
        print('Enter the letter:')
        c = input()  
        if valid(c) == True:

            for identifier in range(len(get_Random)):
                if get_Random[identifier] == c:
                    numOfUnder[identifier] = c
                    replacer = True
                else:
                  continue  

            

            if replacer == False:
                hearts-=1

        if hearts == 0:
            displayHangman(0)
            print('Hidden word was:  '+ get_Random)        
            return False
        if get_Random==''.join(numOfUnder):
            print('Hidden word was:  '+ get_Random)        
            return True
            

            


def hangman():
    while True:
        displayIntro()
        result = play()
        displayEnd(result)
        print('Do you want to play again? (yes/no)')
        replay = input()
        if replay=='yes':
            continue
        elif replay=='no':
            break
        

if __name__ == "__main__":
    hangman()

