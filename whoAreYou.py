from import_lib import *
from setting import *

def search_food(mode):
    food = {
        'normal': lambda mode: input('What do you want?', type=TEXT, placeholder='百頁豆腐', required=True),
        'child': lambda mode: input('What do you want?', type=TEXT, placeholder='蔬菜沙拉', required=True),
        'dead': lambda mode: input('What do you want?', type=TEXT, placeholder='香雞排', required=True)
    }[mode](mode)
    return food

def choose_eat_type(name):
    with use_scope('eat_type', if_exist='remove'):
        clear_scope('eat_type')
        clear('BMI')
        eat_type = select('Choose your eatago:', ['我X麼是個正常人', '小朋友才吃健康食物', '明天腸胃科見'])
        if (eat_type == '我X麼是個正常人'):
            normal(name)
        elif (eat_type == '小朋友才吃健康食物'):
            child(name)
        else:
            dead(name)


def normal(name):
    with use_scope('normal', if_exist='remove'):
        clear_scope('normal')
        put_text('今天吃了沒～？')
        put_buttons(['重新搜尋'], onclick=[whoAreYou])
        store_page()
        hold()

def child(name):
    with use_scope('child', if_exist='remove'):
        clear_scope('child')
        put_text('一天eatago，醫生遠離我')
        put_buttons(['重新搜尋'], onclick=[whoAreYou])
        store_page()
        hold()

def dead(name):
    with use_scope('dead', if_exist = 'remove'):
        clear_scope('dead')
        put_text('今天吃大餐，明天領藥單')
        put_buttons(['重新搜尋'], onclick=[whoAreYou])
        store_page()
        hold()


def whoAreYou():
    with use_scope('whoAreYou', if_exist='clear'):
        clear_scope('whoAreYou')
        global name
        img = open('eatago_logo.jpg', 'rb').read()
        style(put_image(img, width='300px'), 'display: flex' 'justify-content: center')

        # show time
        time_list = show_time()
        put_text('Current time: ', time_list[0],"/", time_list[1], "/", time_list[2], "  ", time_list[3], " : ", time_list[4])
        # choose time period
        if time_list[3] < 12:
            put_text('It is breakfast time!')
        elif time_list[3] > 12 and time_list[3] < 18:
            put_text('It is lunch time')
        else:
            put_text('It is dinner time')
        # button to BMI
        #put_buttons(['press here to BMI calculation'], onclick=[BMI])

        if name=='':
            #name = input("What is your name?", type=TEXT, placeholder='Annie', required=True)
            name = select('Who are you?', ['Annie', 'Anderson'])
        choose_eat_type(name)
        hold()

if __name__ == '__main__':
    start_server(whoAreYou, auto_open_webbrowser=True)

