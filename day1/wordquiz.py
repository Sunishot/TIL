with open("python\day1\cabulary.txt","r",encoding="UTF-8") as f:
    for line in f:
        eng_word, kor_word = line.strip().split(": ")
        guess = input("{}: ".format(kor_word))
        if guess == eng_word:
            print("맞았습니다!")
        else:
            print("아쉽습니다. 정답은 {}입니다.".format(eng_word))
            

       
        
        
        