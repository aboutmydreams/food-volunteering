import os,time,datetime,xlrd
from xlrd import open_workbook
from xlutils.copy import copy
def get_timemin():
    now_time0 = '[\''+time.ctime().replace(':','\',\'').replace(' ','\',\'')+'\']'
    return eval(now_time0)
def mkdir(path):
    path=path.strip()
    path=path.rstrip("\\")
    if isExists := os.path.exists(path):
        # 如果目录存在则不创建，并提示目录已存在
        print(f'{path} 目录已存在')
        return False
    else:
        os.makedirs(path)
        print(f'{path} 创建成功')
        return True
def getYesterday():
    today=datetime.date.today()
    oneday=datetime.timedelta(days=1)
    return str(today-oneday).replace('-','')
def today():
    return str(datetime.date.today()).replace('-','')
'''
# 定义要创建的目录
#mkpath="data"
#mkdir(mkpath)
'''
def write_actname(time1):
    with open('data/allact.txt','a') as fa:
        fa.write(time1+'\n')

def read_actname():
    fa = open('data/allact.txt','r')
    return eval(str(fa.readlines()).replace('\\n',''))

def write_set(time1,time2,title,num):
    with open('data/time.txt','w') as f:
        f.write(time1+'\n'+time2+'\n'+title+'\n'+num)
    if is_e := os.path.exists(f'data/log/{time1}.txt'):
        print('存在')
    else:
        with open(f'data/log/{time1}.txt', 'w') as f1:
            f1.write('[]')
        write_actname(time1)

def read_set():
    with open('data/time.txt','r') as f:
        sets = eval(str(f.readlines()).replace('\\n',''))
    return sets

def now_num():
    near_time = read_set()[0]
    with open(f'data/log/{near_time}.txt', 'r') as f:
        data = eval(f.read())
        num = len(data)
    return str(num) 

def baoming(name,phone):
    data = []
    hour = get_timemin()[-4]
    near_time = read_set()[0]
    f = open(f'data/log/{near_time}.txt', 'r')
    data0 = eval(f.read())
    name_list = []
    if len(data0)!=0:
        name_list.extend(i[0] for i in data0)
        if name in name_list:
            name_site = name_list.index(name)
            data0[name_site][-1]=phone
            print(name_site)
            f.close()
            f = open(f'data/log/{near_time}.txt', 'w')
            fs = open('data/ban.json','r')
        else:
            f.close()
            f = open(f'data/log/{near_time}.txt', 'w')
            fs = open('data/ban.json','r')
            ban_list_zidian = eval(fs.read())
            this_ban = ban_list_zidian[f'{name}'] if name in ban_list_zidian else ''
            data.extend((name, this_ban, phone))
            data0.append(data)
    else:
        f.close()
        f = open(f'data/log/{near_time}.txt', 'w')
        fs = open('data/ban.json','r')
        ban_list_zidian = eval(fs.read())
        this_ban = ban_list_zidian[f'{name}'] if name in ban_list_zidian else ''
        data.extend((name, this_ban, phone))
        data0.append(data)
    f.write(str(data0))
    f.close()

def get_qinkuang():
    near_time = read_set()[0]
    with open(f'data/log/{near_time}.txt', 'r') as f:
        data = eval(f.read())
    return data

def get_qian1():
    hour = get_timemin()[-4]
    f = open('data/time.txt','r')
    data = eval(str(f.readlines()).replace('\\n',''))
    if len(data)!=4:
        return [0,['1','2','设置错误，联系开发者调试','20']]
    starttime = int(data[0])#开始时间
    deadtime = int(data[1])#结束时间
    today1 = int(today())#今天日期
    setnum = int(data[-1])#设定名额
    now_num1 = now_num()#当前名额
    if (starttime > today1) or ((starttime==today1) and (int(hour)<21)):
    	return [4,data,now_num1]
    if setnum > int(now_num1):
        if (today1 < deadtime):
            return [1,data,now_num1]
        elif (today1 == deadtime) and int(hour) < 21:
            return [1,data,now_num1]
        else:
            return [0,[]]
    else:
        return [3,[]]

def wri_ex():
    data = xlrd.open_workbook('data/2.xls', formatting_info=True)
    table = data.sheets()[0]   #通过索引顺序获取
    w=copy(data)
    mydata = get_qinkuang()
    for n, i in enumerate(mydata, start=3):
        w.get_sheet(0).write(n,2,i[0])
        w.get_sheet(0).write(n,3,i[1])
        w.get_sheet(0).write(n,4,i[2])
    filename = read_actname()[-1]
    w.save('book2.xls')
    w.save(f'data/excels/{filename}.xls')
    data1 = xlrd.open_workbook('book2.xls')
    table1 = data1.sheets()[0]
    for i in range(18):
        a = table1.row_values(i)
        print(a)
# write_set('20181103','20181104','大爱心','20')
# print(read_set()[0])
# wri_ex()
# print(now_num())
# write_set('10181102','20181103','title','num')
# print(get_qian1())
# baoming('dws0h','151ne4')
# print(get_timemin(),today())