from import_lib import *
from tqdm import *

def to_menu(choice,id):
    l = id.split("/")
    print(l[5])
    menu_page(choice,l[5])

def to_store():
    store_page()

def store_page():
    with tqdm(total=100) as pbar:
        put_processbar('bar', auto_close=True)
        for i in range(10):
            pbar.update(10)
            time.sleep(0.3)
            with use_scope('bar', if_exist = 'remove'):
                set_processbar('bar', pbar.n/pbar.total)
    with use_scope("store", if_exist="remove"):
        clear_scope('store')
        clear('cart')
        clear('menu')
        sheet_id = "1HVFC318_8JaPQDG6qNIH2gbpd9jyhP6yKwE-oCed53A" ##
        ##
        #sheet_id = "1HVFC318_8JaPQDG6qNIH2gbpd9jyhP6yKwE-oCed53A"
        sheet_url = 'https://gsx2json.com/api?id=' + sheet_id
        resp = requests.get(sheet_url)
        lst = [["店名", "照片", "菜單"]]
        print(resp)
        #print(json.loads(resp.text)['rows'])
        for row in json.loads(resp.text)['rows']:
            #put_image(row['picurl'], width="300px")
            t = [row['name'],put_image(row['picurl'], width="100px"), put_buttons([dict(label="看菜單",value = row['name'], color='info')], onclick=partial(to_menu, id=row['menu']))]
            lst.append(t)
        put_table(lst)
        hold()




def delete(choice,id):
    order.pop(id)
    cart()

def record():
    #https://docs.google.com/forms/d/e/1FAIpQLSfEfntFlruSOVX9Z56eJr7jQrWEKISFQVuDAs-OaixxOOyu0Q/viewform?usp=pp_url&entry.1577758997=time&entry.2103521038=store&entry.887967252=menu
    time = "2021/5/16"
    data = {"entry.1577758997": time , "entry.2103521038": store_name , "entry.887967252": order}
    if len(order)  != 0:
        requests.get(
            "https://docs.google.com/forms/d/e/1FAIpQLSfEfntFlruSOVX9Z56eJr7jQrWEKISFQVuDAs-OaixxOOyu0Q/formResponse",data)

def cart():
    with use_scope("cart", if_exist = "remove"):
        lst = [["","品項","數量","foodpanda","Ubereats"]]
        f_total = 0;
        u_total = 0;
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
            l = [put_buttons([dict(label="刪除",value = 'p', color='danger')], onclick=partial(delete, id=i)),i,order[i],f,u]
            lst.append(l)
        l = ["","總價","",f_total,u_total]
        lst.append(l)
        put_table(lst)
        if f_flag and u_flag:
            if f_total < u_total:
                put_text("Foodpanda 比較便宜")
            elif f_total > u_total:
                put_text("Ubereats 比較讚啦")
            else:
                put_text("兩個一樣 擇其所望")
        elif f_flag:
            put_text("Ubereats 比較讚啦")
        elif u_flag:
            put_text("Foodpanda 比較便宜")
        else:
            if f_total < u_total:
                put_text("Foodpanda 比較便宜")
            elif f_total > u_total:
                put_text("Ubereats 比較讚啦")
            else:
                put_text("兩個一樣 擇其所望")


def pop_up_page(choice, id):
    num = input(rows = 1, label = "數量",type = NUMBER)
    #popup(id, [put_text("數量:"),put_text(num)], size=PopupSize.SMALL)

    if id not in order:
        order[id] = num
    else:
        order[id] += num
    cart()



def menu_page(name , sheet_id):#sheet_id):
    with use_scope('menu',if_exist = "remove"):
        clear('store')
        global order
        global dic
        order = {}
        dic = {}
        put_buttons([dict(label='<',value = 'p', color='info')], onclick = [to_store] )
        put_text(name)
        #sheet_id="19dJIc0j0qfHvdgZEBOZHNe5OPX53nGmVslf1uIP-hfY"
        sheet_url = 'https://gsx2json.com/api?id='+sheet_id
        resp = requests.get(sheet_url)
        print(resp)
        for row in json.loads(resp.text)['rows']:
            name = row['foodpanda']
            price = row['fprice']
            if (str(name) != "0"):
                if name in dic:
                    dic[name][0] = price
                else:
                    dic[name] = [price,0]
            name = row['ubereats']
            price = row['uprice']

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
        put_text("\n購物車")
        cart()
        hold()
