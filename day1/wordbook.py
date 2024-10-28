with open("python/day1/volcabulary.txt","w") as file:
    while True:

        eng_word = input("영어 단어를 입력하세요: ")        

        if eng_word == "q":
            break

        kor_word = input("한국어 뜻을 입력하세요: ")
        if kor_word == "q":
            break

        file.write("{}: {}\n".format(eng_word,kor_word))
        
        
