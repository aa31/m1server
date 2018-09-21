from xml.dom import minidom
import os

def createConfigXml():
    # 1.创建DOM树对象
    dom = minidom.Document()
    # 2.创建根节点。每次都要用DOM对象来创建任何节点。
    root_node = dom.createElement('root')
    # 3.用DOM对象添加根节点
    dom.appendChild(root_node)
    video_node = dom.createElement('video')
    root_node.appendChild(video_node)
    resolution_node = dom.createElement('resolution')
    video_node.appendChild(resolution_node)
    resolution_node.setAttribute('no', '2')
    resolution_text = dom.createTextNode('1920*1080')
    resolution_node.appendChild(resolution_text)
    type_node = dom.createElement('coltype')
    video_node.appendChild(type_node)
    type_node.setAttribute('no', '0')
    type_text = dom.createTextNode('每帧采样')
    type_node.appendChild(type_text)
    try:
        with open('config.xml', 'w', encoding='UTF-8') as fh:
            dom.writexml(fh, indent='', addindent='\t', newl='\n', encoding='UTF-8')
            print('写入xml OK!')
    except Exception as err:
            print('错误信息：{0}'.format(err))


def createVideoDetail():
    dom = minidom.Document()
    root_node = dom.createElement('root')
    dom.appendChild(root_node)

    resolution_node = dom.createElement('resolution')
    root_node.appendChild(resolution_node)
    coltype_node = dom.createElement('coltype')
    root_node.appendChild(coltype_node)

    resolution_text_1 = dom.createTextNode('800*600')
    resolution_text_2 = dom.createTextNode('1024*768')
    resolution_text_3 = dom.createTextNode('1920*1080')

    resolution_child_node_1 = dom.createElement('option')
    resolution_child_node_1.setAttribute('no', '0')
    resolution_child_node_1.appendChild(resolution_text_1)

    resolution_child_node_2 = dom.createElement('option')
    resolution_child_node_2.setAttribute('no', '1')
    resolution_child_node_2.appendChild(resolution_text_2)

    resolution_child_node_3 = dom.createElement('option')
    resolution_child_node_3.setAttribute('no', '2')
    resolution_child_node_3.appendChild(resolution_text_3)

    resolution_node.appendChild(resolution_child_node_1)
    resolution_node.appendChild(resolution_child_node_2)
    resolution_node.appendChild(resolution_child_node_3)

    coltype_text_1 = dom.createTextNode('每帧采样')
    coltype_text_2 = dom.createTextNode('隔帧采样')
    coltype_child_node_1 = dom.createElement('option')
    coltype_child_node_1.setAttribute('no', '0')
    coltype_child_node_2 = dom.createElement('option')
    coltype_child_node_2.setAttribute('no', '1')
    coltype_child_node_1.appendChild(coltype_text_1)
    coltype_child_node_2.appendChild(coltype_text_2)
    coltype_node.appendChild(coltype_child_node_1)
    coltype_node.appendChild(coltype_child_node_2)

    try:
        with open('./static/xml/m1detail.xml', 'w', encoding='UTF-8') as fh:
            dom.writexml(fh, indent='', addindent='\t', newl='\n', encoding='UTF-8')
    except Exception as err:
            print('错误信息：{0}'.format(err))


def getNodeVal(node):
    dom = minidom.parse('./static/xml/m1detail.xml')
    root = dom.documentElement
    resolution = root.getElementsByTagName(node)[0]
    resolution_childs = resolution.childNodes
    dict = {}
    for item in resolution_childs:
        if item.nodeName == '#text':
            pass
        else:
            dict[item.getAttribute('no')] = item.childNodes[0].data
            # print(item.getAttribute('no'))
            # print(item.childNodes[0].data)
    return dict





def reXml(node):
    dom = minidom.parse('config.xml')
    root = dom.documentElement
    video = root.getElementsByTagName(node)[0]
    video_childs = video.childNodes[0]
    video_childs.text= '111'



#     print(video_childs.data)
# print(reXml('resolution'))

def basic():
    if os.path.exists('../static/xml/m1detail.xml'):
        pass
    else:
        createVideoDetail()


    if os.path.exists('config.xml'):
        pass
    else:
        createConfigXml()

