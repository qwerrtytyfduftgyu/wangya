from win10toast import ToastNotifier
import time
import random
def notify(random_quote):
    toaster = ToastNotifier()
    toaster.show_toast("眨眨眼睛吧，好好休息一下吧",
                       '请保护好自己的眼睛',
                       icon_path=None,duration=5)
    toaster.show_toast("人生格言",random_quote,
                       icon_path=None,duration=6,threaded=True)
    while toaster.notification_active():
        time.sleep(0.1)

if __name__ == "__main__":
    quotes_list=[]
    with open("quotes.txt",encoding="utf_8") as f:
        for line in f:
            if line != '\n':
                quotes_list.append(line)
    while True:
        rand_item = random.choice(quotes_list)
        notify(rand_item)
        time.sleep(5)