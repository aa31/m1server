import psutil
import time


def get_net_addrs():
    return psutil.net_if_addrs()


addrs = get_net_addrs()
# print(addrs)


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


# print('cpu物理个数：%s , 逻辑个数 %s' %(psutil.cpu_count(logical=False),psutil.cpu_count()))
# print('cpu占用率%s' % (getCpuState()))
# # print('总内存： %s' % (psutil.virtual_memory().total))
# print('内存占用率： %s' % (getMemState()))
# print('硬盘占用率 %s' % (str(psutil.disk_usage('/').percent)))
# print('系统时间: %s' % (get_systimes()))

# print('网络信息：%s' % (if_addrs))
# print('网络信息：%s' % (ps
# util.net_if_stats()))


if_addrs = psutil.net_if_addrs()


# 获取ip
def get_ip():
    return if_addrs['eth0'][1][1]

# 本地连接
# 获取网关
def get_netmask():
    return if_addrs['eth0'][1][2]


# 开机时间
print(psutil.boot_time())

