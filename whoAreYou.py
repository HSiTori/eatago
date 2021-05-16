from import_lib import *
from setting import *

Current_User = ""

Mode = 0
store_id = ["1RKVPuWTM1FPYXU09QZkMfPXQ9PJ6OhOxrNGDX7ISL7U"  #normal breakfast
            ,"1f-WtnvXj4lStS0Fj1LH_oUMjqTewXpKr2Wt-3iknm5k" #health breakfast
            ,"1JjIVrEG8ENISzTb8LsTFH8QfwkYhCOGlIns5umvZm0Q" #dead breakfast

            ,"1YToghu1MrOqdHvUFzD3YRZVLd-oRIXbNGAW_j6nIfwQ" #lunch
            ,"12IqQLDGPIEANvWNaPfkq1TTPBiAenZRty-UG7bULD6s"
            ,"1xk3meEKilDrQT9D6F2b5bLsydIxabwUyTRu8WST6Wvs"

            ,"19EP3_fgRu4tgTHzEbRzb2pRHhSe4Vv09E5_D9J_sDQs" #dinner
            ,"12QmcwqcZWo6wjV8d1K3_NP7WVjaW-ckwkRea9W56I0I"
            ,"1Z9eIh4YEutF6Q_GyZ1RT9YXWMm_zchnK4usFFDfeDTc"]

drink_list = ["三兩茶 (陽光三月店)",
              "青釉茶事 (新竹遠百店)",
              "法豆綠豆沙牛奶",
              "手作功夫茶 (新竹寶山店)",
              "迷客夏milkshop",
              "路易莎咖啡",
              "百鮮專業現打果汁",
              "茶湯會",
              "可不可熟成紅茶",
              "百鮮 ALWAYS FRESH"]

fried_list = ["旺萊鹹酥雞 (新竹林森店)",
              "繼光香香雞",
              "開源社香雞排",
              "艋舺雞排 (新竹武昌店)",
              "胖老爹美式炸雞",
              "自由先生雞排炸物",
              "雞排中隊 (新竹南大店)",
              "魔王狂爆雞排 (新竹西大店)",
              "嵐町雞排 (新竹民族店)",
              "百源雞排"]

def search_food(mode):
    food = {
        'normal': lambda mode: input('What do you want?', type=TEXT, placeholder='百頁豆腐', required=True),
        'child': lambda mode: input('What do you want?', type=TEXT, placeholder='蔬菜沙拉', required=True),
        'dead': lambda mode: input('What do you want?', type=TEXT, placeholder='香雞排', required=True)
    }[mode](mode)
    return food

def choose_eat_type():
    with use_scope('eat_type', if_exist='remove'):
        clear_scope('eat_type')
        sheet_id = User_Dict[Current_User]
        sheet_url = 'https://gsx2json.com/api?id=' + sheet_id
        resp = requests.get(sheet_url)
        print(resp)
        style(put_text(str(Current_User) + " 的近期紀錄"),'font-size:0.5cm; font-weight:500')
        lst = [["時間","店名","餐點"]]
        length = len(json.loads(resp.text)['rows'])

        drink_cnt = 0
        night_cnt = 0
        fried_cnt = 0

        if length>=1  and length <= 10:
            for i in range(length - 1 , -1, -1):
                row = json.loads(resp.text)['rows'][i]
                l = [row['time'], row['store'], row['menu']]

                if row['store'] in drink_list:
                    drink_cnt += 1

                if row['store'] in fried_list:
                    fried_cnt += 1

                time = row['time'].split(" ")
                time = time[1].split(":")
                time = int(time[0])
                if (time >= 23) or (time <= 3):
                    night_cnt += 1

                lst.append(l)
        elif length >= 10:
            for i in range(10):
                row = json.loads(resp.text)['rows'][length - i - 1]
                l = [row['time'], row['store'], row['menu']]

                if row['store'] in drink_list:
                    drink_cnt += 1

                if row['store'] in fried_list:
                    fried_cnt += 1

                #print(row['time'])
                time = row['time'].split(" ")
                #print(time)
                time = time[1].split(":")
                #print(time)
                time = int(time[0])
                if (time >= 23) or (time <= 3):
                    night_cnt += 1

                lst.append(l)
        put_table(lst)

        style(put_text("你最近點了 " + str(drink_cnt) + "次飲料 , " + str(night_cnt) + "次宵夜 , " + str(fried_cnt) +"次炸物"),'font-size:0.5cm; font-weight:400; color:blue;')

        if drink_cnt <= 2 and night_cnt <= 2 and fried_cnt <= 2:
            style(put_text("你很健康"), 'color:green; font-size:0.7cm; font-weight:400;')
        else:
            if drink_cnt > 2:
                style(put_text("喝太多飲料了"), 'color:red; font-size:0.7cm; font-weight:400;')
            if night_cnt > 2:
                style(put_text("別再熬夜了"), 'color:red; font-size:0.7cm; font-weight:400;')
            if fried_cnt > 2:
                style(put_text("好油喔 peko"), 'color:red; font-size:0.7cm; font-weight:400;')

        eat_type = select('Choose Your Eatago , 今天想要怎麼吃?', ['我X麼是個正常人(正常吃飯)', '小朋友才吃健康食物(健康生活)', '明天腸胃科見(暴飲暴食)'])
        if (eat_type == '我X麼是個正常人(正常吃飯)'):
            normal()
        elif (eat_type == '小朋友才吃健康食物(健康生活)'):
            child()
        else:
            dead()


def normal():
    with use_scope('normal', if_exist='remove'):
        clear_scope('normal')
        put_row([style(put_text('今天吃了沒～？'),'border-top-style:solid; font-size:0.5cm; font-weight:400; padding-top:15px; padding-right: 30px'),
                 style(put_buttons(['重新搜尋'], onclick=[whoAreYou]),'border-top-style:solid; position:relative; right:0px; padding-top:15px; padding-right:0px; padding-left:17px;')
                 ])
        global Mode
        Mode = Mode*3 + 0
        Id = store_id [Mode]
        #print(Mode)
        store_page(Id, Current_User)
        hold()

def child():
    with use_scope('child', if_exist='remove'):
        clear_scope('child')
        put_row([style(put_text('一天Eatago，醫生遠離我'),
                       'border-top-style:solid; font-size:0.5cm; font-weight:400; padding-top:15px; padding-right: 30px'),
                 style(put_buttons(['重新搜尋'], onclick=[whoAreYou]),
                       'border-top-style:solid; position:relative; right:0px; padding-top:15px; padding-right:0px; padding-left:17px;')
                 ])
        global Mode
        Mode = Mode * 3 + 1
        Id = store_id[Mode]
        #print(Mode)
        store_page(Id, Current_User)
        hold()

def dead():
    with use_scope('dead', if_exist = 'remove'):
        clear_scope('dead')
        put_row([style(put_text('今天吃大餐，明天領藥單'),
                       'border-top-style:solid; font-size:0.5cm; font-weight:400; padding-top:15px; padding-right: 30px'),
                 style(put_buttons(['重新搜尋'], onclick=[whoAreYou]),
                       'border-top-style:solid; position:relative; right:0px; padding-top:15px; padding-right:0px; padding-left:17px;')
                 ])
        global Mode
        Mode = Mode * 3 + 2
        Id = store_id[Mode]
        #print(Mode)
        store_page(Id,Current_User)
        hold()


def whoAreYou():
    with use_scope('whoAreYou', if_exist='clear'):
        clear_scope('whoAreYou')
        clear("menu")
        clear("store")
        clear("cart")
        global name
        img = open('eatago_logo.jpg', 'rb').read()
        img_b = open('food_botton.jpg', 'rb').read()
        img_h = open('hungry_me.jpg', 'rb').read()
        time_list = show_time()
        # choose time period
        global Mode
        if time_list[3] < 11:
            a = put_text('Breakfast time!')
            Mode = 0
        elif time_list[3] > 10 and time_list[3] < 17:
            a = put_text('Lunch time!')
            Mode = 1
        else:
            a = put_text('Dinner time!')
            Mode = 2

        put_row([
            style(put_image(img, width='2000px'), 'display: flex' 'justify-content: center;'), put_column([
            style(put_text(time_list[0], "/", time_list[1], "/", time_list[2], " ", time_list[3], " : ",
                     time_list[4]),'font-size:0.6cm; position:relative; left:60px; top: 90px; text-indent: 150px; font-weight:500;'),
            style(a,'font-size:1.25cm; position:relative; position:relative; left:10px;  text-indent:150px; font-weight:700; color:MidnightBlue')])
        ])

        with use_scope('pic', clear=True):
            put_row([style(put_image(img_h, width='2000px'), 'display: flex' 'justify-content: center;'),
                    style(put_image(img_b, width='2000px'), 'display: flex' 'justify-content: center;')])

        if name == '':
                    name = select('Who are you?', ['Annie', 'Anderson'])

        global Current_User
        Current_User = name
        #print(Current_User)
        clear('pic')
        choose_eat_type()
        hold()

if __name__ == '__main__':
    start_server(whoAreYou, auto_open_webbrowser=True)

