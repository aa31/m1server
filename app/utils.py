import os, hashlib, json, math, time, psutil
from flask import jsonify


# 网络信息
def get_net_addrs():
    return psutil.net_if_addrs()


# cpu占用率
def getCpuState():
    return str(psutil.cpu_percent(1))


# 内存占用率
def getMemState():
    return psutil.virtual_memory().percent


# 磁盘占用率
def getDiskState():
    return str(psutil.disk_usage('/').percent)


# 获取系统时间
def get_systimes():
    return time.strftime('%Y/%m/%d %H:%M:%S',time.localtime(time.time()))


# 获取ip和网关
def get_ipnetmask():
    if_addrs = psutil.net_if_addrs()
    # if_list = if_addrs['本地连接']
    if_list = if_addrs['eth0']
    for i in range(len(if_list)):
        if 'AddressFamily.AF_INET: 2' in str(if_list[i]):
            return if_list[i]


# 获取ip
def get_ip():
    return get_ipnetmask().address


# 获取网关
def get_netmask():
    return get_ipnetmask().netmask


# 时间格式化
def changeTime(allTime):
    day = 24*60*60
    hour = 60*60
    min = 60
    if allTime <60:
        return  "%d 秒"%math.ceil(allTime)
    elif  allTime > day:
        days = divmod(allTime,day)
        return "%d 天 %s"%(int(days[0]),changeTime(days[1]))
    elif allTime > hour:
        hours = divmod(allTime,hour)
        return '%d 小时 %s'%(int(hours[0]),changeTime(hours[1]))
    else:
        mins = divmod(allTime,min)
        return "%d 分钟 %d 秒"%(int(mins[0]),math.ceil(mins[1]))


# 获取系统运行时间
def get_stsruntime():
    return time.time()-psutil.boot_time()


# 创建json文件并保存
def createJson(filename,data):
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False)
        f.close()


# 读取数据
def readJson(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        data = json.load(f)
        return data


def jsonInit():
    # config.json
    base = {"port": "9909", "host": "0.0.0.0"}
    video = {"resolution": "2", "coltype": "0", "target":"0,1"}
    swj = {"ip": "", "port": "", "rtsp": ""}
    network = {'ip': get_ip(), 'netmask': get_netmask(),'port':'9909', 'type': '1', 'gw': ''}
    user = {"user": "bezm", "password": "e10adc3949ba59abbe56e057f20f883e"}
    data = {"video": video, "swj": swj, "network":network, "base":base, "user":user}
    createJson('./app/config.json', data)
    # videoParams.json
    resolution = {'0': "800*600", '1': "1024*768", '2': "1920*1080"}
    coltype = {'0': "每帧采样", '1': "隔帧采样"}
    target = {'0': "四旋翼无人机", '1': "固定翼无人机",'2':'气球', '3':"风筝","4":"人","5":"车"}
    data = {'resolution': resolution, 'coltype': coltype, "target":target}
    createJson('./app/static/json/videoParams.json', data)


def getApi(code, content, msg):
    data = {'code':code, "data":content, "msg": msg}
    return jsonify(data)


def md5(str):
    hl = hashlib.md5()
    hl.update(str.encode('utf-8'))
    return hl.hexdigest()


if os.path.isfile("config.json"):
    pass
else:
    jsonInit()



