def rating_hesapliyici():
    global rating
    rating = (like_num/ (like_num + dislike_num))*100

def rating_gosterici():
    print("Bu videonun begenilme orani: %",rating)

    if (rating > 50):
        print("Bu video begenildi")
    else:
        print("rezalet")

def user_input():
    global like
    global dislike
    global like_num
    global dislike_num

    print("lütfen video begeni oranini giriniz:")
    try:
        like_num = int(input())

    except ValueError:
        print("kanka sayi gircen 134 gibi")
    user_input()

    print("Lütfen video dislike degerini giriniz:")
    try:
        dislike_num = int(input())

    except ValueError:
        print("kanka sayi girsen sayi 134 gibi")
        user_input()


    print("Selamun Aleykum")
    user_input()


    