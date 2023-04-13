Upper = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
Lower = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
Number= ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

def Counter(phrase):
    LetterCharacters=0 
    NumberCharacters=0 
    SpecialCharacters = 0
    for i in range(len(str)):
        if str[i] in Upper:
            LetterCharacters += 1
        
        elif str[i] in Lower:
            LetterCharacters += 1
        
        elif str[i] in Number:
            NumberCharacters += 1
            
        else: 
            SpecialCharacters += 1
    print('Letters:', LetterCharacters)
    print('Digits:', NumberCharacters)
    print('Special characters:', SpecialCharacters)
 

phrase = "3 beautiful days."
Counter(phrase)
