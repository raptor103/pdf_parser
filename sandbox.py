data = ["ahoj", "regi-", "strace", "kosek", "kate-", "rina", "koskova"]

def concat_words_with_hyphen(list_of_words):
    for i in range(len(list_of_words)):
        # if we are no in last word
        if len(list_of_words) != (i+1):
            first_word = list_of_words[i]
            second_word = list_of_words[i+1]
            if first_word[-1] == "-":
                new_word = (first_word+second_word).replace("-", "")

concat_words_with_hyphen(data)
