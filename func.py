import psutil
import time
import math
import os


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


# 本地连接
# 获取网关
def get_netmask():
    return get_ipnetmask().netmask


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


# 系统运行时间  时间戳
def get_stsruntime():
    return time.time()-psutil.boot_time()



