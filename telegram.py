import telepot

# 깃 pull 이후 이 부분만 바꿔주기(네이버 메모 참조)
token = "1401572057:AAE5fXpieSu2bm9iVFpKx0rrjakmmFtFGu4"

bot = telepot.Bot(token)
me = "1532557286"
mother = "1116127289"

user_list = [me]


# 나에게 텔레그램봇으로 메시지를 보낸다
def sendMessage(msg):
    # 모든 멤버에게 보낸다
    for i in user_list:
        # sendMessage(대상 id, 문자열): 해당 봇이 대상 id 에게 문자열을 보낸다
        bot.sendMessage(i, msg)

# 엄마만
user_list2 = [mother]

def sendFamilyMessage(msg):
    # 모든 멤버에게 보낸다
    for i in user_list2:
        # sendMessage(대상 id, 문자열): 해당 봇이 대상 id 에게 문자열을 보낸다
        bot.sendMessage(i, msg)