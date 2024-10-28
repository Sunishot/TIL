with open("python/day1/cabulary.txt","r",encoding = "UTF-8") as f:
    vocab = {}
    import random
    for line in f:
        data = line.strip().split(": ")
        eng_word, kor_word = data[0], data[1]
        vocab[eng_word] = kor_word

    keys = list(vocab.keys())

    while True:
        index = random.randint(0, len(keys)-1)
        eng_word = keys[index]
        kor_word = vocab[eng_word]
        guess = input("{}: ".format(kor_word))
        
        if guess == "q":
            break

        if guess == eng_word:
            print("맞았습니다!")
        else:
            print("틀렸습니다. 정답은 {}입니다.".format(eng_word))

        



