import psutil
import socket,time


def get_net_addrs():
    return psutil.net_if_addrs()


addrs = get_net_addrs()
print(addrs)


# cpu占用率
def getCpuState():
    return " CPU: " + str(psutil.cpu_percent(1)) + "%"


# 内存占用率
def getMemState():
    return psutil.virtual_memory().percent


# 返回ip
def get_host_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
    finally:
        s.close()
    return ip


# 获取系统时间
def get_systimes():
    return time.strftime('%Y/%m/%d %H:%M:%S',time.localtime(time.time()))



# print('cpu物理个数：%s , 逻辑个数 %s' %(psutil.cpu_count(logical=False),psutil.cpu_count()))
# print('cpu占用率%s' % (getCpuState()))
# print('总内存： %s' % (psutil.virtual_memory().total))
# print('内存占用率： %s' % (getMemState()))
# print('硬盘信息 %s' % (str(psutil.disk_usage('/'))))
# print(get_host_ip())
# print('系统时间: %s' % (get_systimes()))



