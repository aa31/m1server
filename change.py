import configparser

cf = configparser.ConfigParser()

cf.read('config.py')
print(cf.get('debug'))