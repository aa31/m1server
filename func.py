import psutil
import socket,time
import subprocess, re

def get_net_addrs():
    return psutil.net_if_addrs()


addrs = get_net_addrs()
# print(addrs)


# cpu占用率
def getCpuState():
    return " CPU: " + str(psutil.cpu_percent(1)) + "%"


# 内存占用率
def getMemState():
    return psutil.virtual_memory().percent


def get_net_address(ifname):
    '''
    获取本机网卡IP地址与子网掩码及MAC地址
    :param ifname: #网卡名称,例: eth0
    :return:  #返回dict数据类型,网卡的IP地址,子网掩码,MAC地址 ,
    例: {'ip': '192.168.0.64', 'mac': '00:0C:29:5F:3F:F1', 'mask': '255.255.255.0'}
    '''

    row = {}
    ipconfig_process = subprocess.Popen(["ifconfig", ifname], stdout=subprocess.PIPE)
    output = ipconfig_process.stdout.read()

    # 获取IP
    ip_str = '([0-9]{1,3}\.){3}[0-9]{1,3}'
    ip_pattern = re.compile('(inet addr:%s)' % ip_str)
    pattern = re.compile(ip_str)
    for ipaddr in re.finditer(ip_pattern, str(output)):
        ip = pattern.search(ipaddr.group())
        row['ip'] = ip.group()

    # 获取子网掩码
    mask_str = '0x([0-9a-f]{8})'
    pattern = re.compile(mask_str)
    mask_pattern = re.compile(r'Mask:%s' % ip_str)
    pattern = re.compile(ip_str)
    for maskaddr in mask_pattern.finditer(str(output)):
        mask = pattern.search(maskaddr.group())
        row['mask'] = mask.group()

    # 获取MAC
    mac_str = '([a-zA-Z0-9]{1,2}\:){5}[a-zA-Z0-9]{1,2}'
    mac_pattern = re.compile('(HWaddr %s)' % mac_str)
    pattern = re.compile(mac_str)
    for mac_addr in re.finditer(mac_pattern, str(output)):
        mac = pattern.search(mac_addr.group())
        row['mac'] = mac.group()
    return row


ifconfig = get_net_address('eth0')


print(ifconfig['ip'])

print(ifconfig['mask'])

print(ifconfig['mac'])


# 获取系统时间
def get_systimes():
    return time.strftime('%Y/%m/%d %H:%M:%S',time.localtime(time.time()))


print('cpu物理个数：%s , 逻辑个数 %s' %(psutil.cpu_count(logical=False),psutil.cpu_count()))
print('cpu占用率%s' % (getCpuState()))
print('总内存： %s' % (psutil.virtual_memory().total))
print('内存占用率： %s' % (getMemState()))
print('硬盘信息 %s' % (str(psutil.disk_usage('/'))))
print('系统时间: %s' % (get_systimes()))



