import random

def get_words(file_name):
    with open(file_name, "r", encoding="utf-8") as open_file:
        words = [i.strip() for i in open_file]
    return words

def random_word(file_name, last_word=None):
    words = get_words(file_name)
    if last_word in words:
        words.remove(last_word)
    if not words:
        words = get_words(file_name)
    return random.choice(words)

def game_board(word, guesses):
    display_word = ""
    for letter in word:
        if letter.lower() in guesses or letter.upper() in guesses:
            display_word += letter
        else:
            display_word += "_"
    return display_word

def play_again():
    user_ask = input("Tekrar Oynamak İstermisiniz? (E/H): ").lower()
    return user_ask == "e"

def game(file_name):
    last_word = None
    while True:
        print("Adam Asmacaya Hoşgeldiniz!")

        word = random_word(file_name, last_word)
        last_word = word

        hangman = ["_" if letter.isalpha() else letter for letter in word]

        life = 6
        print(" ".join(hangman))
        print("Seçilen Kelime:", word)

        guesses = set()

        while life > 0 and "_" in hangman:
            guess = input("Harf Tahmininizi Girin: ").lower()

            valid = "qwertyuıopğüasdfghjklşizxcvbnmöçQWERTYUIOPĞÜASDFGHJKLŞİZXCVBNMÖÇ "
            if len(guess) != 1 or guess not in valid:
                print("Geçersiz Giriş. Tekrar Deneyin.")
                continue

            guesses.add(guess)
            if guess not in word.lower():
                print("Yanlış Harf!")
                life -= 1
                print("Kalan Canınız: " + str(life))
            else:
                hangman = list(game_board(word, guesses))
                print(" ".join(hangman))

        if life <= 0:
            print("Kaybettiniz! Doğru kelime: {}".format(word))
        else:
            print("Tebrikler Kelimeyi Doğru Bildiniz!")

        if not play_again():
            break

if __name__ == "__main__":
    file = "words.txt"
    game(file)