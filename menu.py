from import_lib import *
from tqdm import *

Name = ""
Id = 0
def to_menu(choice,id):
    l = id[0].split("/")
    global flink
    flink = id[1]
    global ulink
    ulink = id[2]
    global  store_name
    store_name = choice
    menu_page(choice,l[5])

def to_store():
    store_page(Id , Name)

def store_page(sheet_id , name):
    global  Name
    global Id
    Id = sheet_id
    Name = name
    with tqdm(total=100) as pbar:
        put_processbar('bar', auto_close=True)
        for i in range(10):
            pbar.update(10)
            time.sleep(0.3)
            with use_scope('bar', if_exist = 'remove'):
                set_processbar('bar', pbar.n/pbar.total)
    with use_scope("store",if_exist = "remove"):
        clear('cart')
        clear('menu')
        sheet_url = 'https://gsx2json.com/api?id=' + sheet_id
        resp = requests.get(sheet_url)
        print(resp)
        lst = [["店名", "照片", "菜單"]]

        for row in json.loads(resp.text)['rows']:
            t = [ row['name'] , put_image(row['picurl'], width="150px") , put_buttons( [dict(label="看菜單",value = row['name'], color = 'info')] , onclick = partial( to_menu, id = (row['menu'],row['flink'],row['ulink'])))]
            #t = [row['name'], "" ,put_buttons([dict(label="看菜單", value=row['name'], color='info')],onclick=partial(to_menu, id=(row['menu'], row['flink'], row['ulink'])))]
            lst.append(t)
        put_table(lst)
        hold()


def delete(choice,id):
    order.pop(id)
    cart()

def record():
    global Name
    now = datetime.now()
    time = str(now.year) + "-" + str(now.month) + "-" + str(now.day) + " " + str(now.hour) + ":" +  str(now.minute)
    print(Name)
    if Name == "Annie":
        data = {"entry.1577758997": time , "entry.2103521038": store_name , "entry.887967252": order,"entry.1033381325" : Id}
        if len(order) != 0:
            requests.get("https://docs.google.com/forms/d/e/1FAIpQLSfEfntFlruSOVX9Z56eJr7jQrWEKISFQVuDAs-OaixxOOyu0Q/formResponse",data)
    else :
        # https://docs.google.com/forms/d/e/1FAIpQLSfwShv8t4PjIcuPJWo5AEDbCCuskVRDYPps4XL_5CzG28dgJg/viewform?usp=pp_url&entry.1040772690=time&entry.1247007904=store&entry.1175688414=menu
        data = {"entry.1040772690": time, "entry.1247007904": store_name, "entry.1175688414": order}
        if len(order) != 0:
            requests.get("https://docs.google.com/forms/d/e/1FAIpQLSfwShv8t4PjIcuPJWo5AEDbCCuskVRDYPps4XL_5CzG28dgJg/formResponse",data)
    popup('', '已記錄', size=PopupSize.SMALL)


def cart():
    with use_scope("cart", if_exist = "remove"):
        global flink
        global ulink
        lst = [["","品項","數量","foodpanda","Ubereats"]]
        f_total = 0
        u_total = 0
        f_flag = False
        u_flag = False
        for i in order:
            if dic[i][0] == 0:
                f = "無此品項"
                f_flag = True
            else:
                f = dic[i][0] * int(order[i])
                f_total = f_total + f

            if dic[i][1] == 0:
                u = "無此品項"
                u_flag = True
            else:
                u = dic[i][1] * int(order[i])
                u_total = u_total + u
            l = [put_buttons([dict(label="刪除", value='p', color='danger')], onclick=partial(delete, id = i)),i,order[i],f,u]
            lst.append(l)

        l = [put_buttons([dict(label="紀錄", value='p', color='success')], onclick=[record]), "總價", "", f_total, u_total]
        lst.append(l)
        put_table(lst)
        if f_flag and u_flag:
            if f_total < u_total:
                put_link("Eatago 推薦你使用 Foodpanda (點我前往)", url=flink, new_window=True)
                put_text("")
                put_link("或是你堅持 Ubereats (點我前往)", url=ulink, new_window=True)
            elif f_total > u_total:
                put_link("Eatago 推薦你使用 Ubereats (點我前往)", url=ulink, new_window=True)
                put_text("")
                put_link("或是你堅持 Foodpanda (點我前往)", url=flink, new_window=True)
            else:
                put_text("兩個一樣 擇其所望")
                put_link("前往 Foodpanda ", url=flink, new_window=True)
                put_text("")
                put_link("前往 Ubereats ", url=ulink, new_window=True)
        elif f_flag:
            put_link("Eatago 推薦你使用 Ubereats (點我前往)", url=ulink, new_window=True)
            put_text("")
            put_link("或是你堅持 Foodpanda (點我前往)", url=flink, new_window=True)
        elif u_flag:
            put_link("Eatago 推薦你使用 Foodpanda (點我前往)", url=flink, new_window=True)
            put_text("")
            put_link("或是你堅持 Ubereats (點我前往)", url=flink, new_window=True)
        else:
            if f_total < u_total:
                put_link("Foodpanda 比較便宜 (點我前往) ", url=flink, new_window=True)
                put_text('')
                style(put_text("Eatago 幫你省了", inline=True),
                      'font-size:0.5cm; font-weight:500; color:MidnightBlue')
                style(put_text(str(u_total - f_total) + "元", inline=True),
                      'font-size:0.6cm; font-weight:500; color:red')
                put_text('')
                put_link("或是當個盤子?  ", url=ulink, new_window=True)
            elif f_total > u_total:
                put_link("Ubereats 比較讚啦 (點我前往)", url=ulink, new_window=True)
                put_text('')
                style(put_text("Eatago 幫你省了", inline=True),
                      'font-size:0.5cm; font-weight:500; color:MidnightBlue')
                style(put_text(str(f_total - u_total) + "元", inline=True),
                      'font-size:0.6cm; font-weight:500; color:red')
                put_text('')
                put_link("或是當個盤子?  ", url=flink, new_window=True)
            else:
                style(put_text("兩個一樣 擇其所望"), 'font-size:0.5cm; font-weight:500; color:MidnightBlue')
                put_link("前往 Foodpanda ", url=flink, new_window=True)
                put_text("")
                put_link("前往 Ubereats ", url=ulink, new_window=True)



def pop_up_page(choice, id):
    num = input(rows = 1, label = "數量",type = NUMBER)
    if id not in order:
        order[id] = num
    else:
        order[id] += num
    cart()

def menu_page( name , sheet_id ): #sheet_id
    with use_scope('menu',if_exist = "remove"):
        clear('store')
        global order
        global dic
        order = {}
        dic = {}
        put_buttons([dict(label='<', value='p', color='info')], onclick=[to_store])
        style(put_text(name), 'font-size:0.5cm; font-weight:500; text-indent:170px')
        sheet_url = 'https://gsx2json.com/api?id='+sheet_id
        resp = requests.get(sheet_url)
        print(resp)
        for row in json.loads(resp.text)['rows']:
            name = row['foodpanda']
            price = int(row['fprice'])
            if (str(name) != "0"):
                if name in dic:
                    dic[name][0] = price
                else:
                    dic[name] = [price,0]
            name = row['ubereats']
            price = int(row['uprice'])

            if (str(name) != "0"):
                if name in dic:
                    dic[name][1] = price
                else:
                    dic[name] = [0,price]
        lst = [["","品項","Foodapnda","Ubereats"]]
        for i in dic:
            if (dic[i][0] == 0):
                f = "無此品項"
            else:
                f = dic[i][0]

            if (dic[i][1] == 0):
                u = "無此品項"
            else:
                u = dic[i][1]
            t = [put_buttons([dict(label='點餐',value = 'p', color='info')], onclick=partial(pop_up_page, id=i)),i,f,u]
            lst.append(t)
        put_table(lst)
        style(put_text("購物車"),'font-size:0.5cm; font-weight:500; text-indent:170px')
        cart()
        hold()
