import json

with open('appsettings.json') as f:
    data = json.load(f)
    TIMEOUT = data['setup']['timeout']
    ASSETS_DIR = data['setup']['assets_dir']
    RSA_PIN = data['rsa']['pin']
    RSA_PATH = data['rsa']['path']
    VPN_USERNAME = data['global_protect']['username']
    VPN_PASSWORD = data['global_protect']['password']
    GLOBAL_PROTECT_PATH = data['global_protect']['path']
    f.close()