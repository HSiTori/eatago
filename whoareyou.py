import pywebio
from pywebio.input import *
from pywebio.output import *
from pywebio import start_server
from pywebio.session import hold
import asyncio

scope_list = ['whoAreYou', 'normal', 'child', 'dead']

def clear_scope(current):
    for scope in scope_list:
        if current not in scope_list:
            clear(scope)

def search_food(mode):
    food = {
        'normal': lambda mode: input('What do you want?', type=TEXT, placeholder='百頁豆腐', required=True),
        'child': lambda mode: input('What do you want?', type=TEXT, placeholder='蔬菜沙拉', required=True),
        'dead': lambda mode: input('What do you want?', type=TEXT, placeholder='香雞排', required=True)
    }[mode](mode)
    return food


def normal(name):
    with use_scope('normal', if_exist='remove'):
        clear_scope('normal')
        put_text('HELLO %s, WELCOME TO NORMAL MODE' % name)
        put_text('今天吃了沒～？')
        put_buttons(['重新搜尋'], onclick=[whoAreYou])
        food = search_food('normal')
        #


        hold()

def child(name):
    with use_scope('child', if_exist='remove'):
        clear_scope('child')
        put_text('HELLO %s, WELCOME TO CHILD MODE' % name)
        put_text('一天eatago，醫生遠離我')
        put_buttons(['重新搜尋'], onclick=[whoAreYou])
        food = search_food('child')
        hold()

def dead(name):
    with use_scope('dead', if_exist = 'remove'):
        clear_scope('dead')
        put_text('HELLO %s, WELCOME TO CHILD MODE' % name)
        put_text('今天吃大餐，明天領藥單')
        put_buttons(['重新搜尋'], onclick=[whoAreYou])
        food = search_food('dead')
        hold()

def whoAreYou():
    with use_scope('whoAreYou', if_exist='remove'):
        img = open('eatago_logo.jpg', 'rb').read()
        style(put_image(img, width='150px'), 'display: flex' 'justify-content: center')
        name = input("What is your name?", type=TEXT, placeholder='Annie', required=True)
        eat_type = select('Choose your eatago:', ['我X麼是個正常人', '小朋友才吃健康食物', '明天腸胃科見'])

        if(eat_type == '我X麼是個正常人'):
            normal(name)
        elif(eat_type == '小朋友才吃健康食物'):
            child(name)
        else:
            dead(name)

        put_text('Hello %s' % name)
        hold()
        # put_image()


start_server(whoAreYou, auto_open_webbrowser=True)

