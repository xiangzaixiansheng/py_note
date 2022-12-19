import string
import base64
import uuid
import json
import random
import math


class Mask(object):
    """
        生成设备指纹
    """

    @staticmethod
    def mac():
        """
            MAC 地址随机
        :return:        MAC地址
        """
        mac_list = []
        for num in range(1, 7):
            random_key = "".join(random.sample("0123456789abcdef", 2))
            mac_list.append(random_key)
        random_mac = ":".join(mac_list)
        return random_mac

    @staticmethod
    def get_black():
        session_id = "smyfinancial" + str(uuid.uuid4()).replace("-", "")[:32],
        version = "2.0.2",
        system = "Android",
        device_id = "sNy93rXqiOef" + base64.b64encode(
            str(uuid.uuid4()).replace("-", "")[:32].encode()).decode().replace(
            "", "").replace("", ""),
        device_json = {"os": system, "version": version, "session_id": session_id,
                       "device_id": device_id}
        black_box = base64.b64encode(json.dumps(device_json, separators=(",", ":")).encode()).decode()
        return black_box

    @staticmethod
    def imei(tac=None):
        """
            中国区 imei 随机
        :return:        IMEI值
        """
        if tac is None or len(tac) != 8:
            tac = "86" + "".join(random.choice(string.digits) for i in range(6))
        snr = "".join(random.choice(string.digits) for i in range(6))
        imei = tac + snr

        imei_list = []
        for num in range(len(imei)):
            if num % 2 == 0:
                imei_list.append(int(imei[num]))
            else:
                pass
                imei_list.append((int(imei[num]) * 2 % 10 + int(imei[num]) * 2 // 10))
        imei_sum = sum(imei_list)
        if imei_sum % 10 == 0:
            sp = "0"
        else:
            sp = str(10 - (imei_sum % 10))
        return imei + sp

    def info(self):
        """
            生成 android 设备信息
        """

        smartid = random.choice(["1080x1920", "1776x1080", "720x1280", "640x1136", "1080x2040"])
        mobile = random.choice(
            ["Nexus 5", "Nexus 6", "Nexus 6p", "Nexus 7", "Nexus 10", "Xiaomi", "HUAWEI", "HTC 802t", "HTC M8St",
             "vivo X7", "vivo X9",
             "vivo X9i", "vivo X9L", "OPPO A57", "vivo Y66", "Galaxy A3"])
        version = random.choice(["5.1.1", "5.1", "6.0.1", "6.0", "7.1.2", "8.0", "9.0", "7.0.1", "7.0"])
        unique_d = str(uuid.uuid4()).replace("-", "")[:15]
        return {"smartid": smartid, "version": version, "mobile": mobile, "uniqueId": unique_d, "mac": self.mac(),
                "black_box": self.get_black(), "imei": self.imei()}


# 这里的参数包括一个基准点，和一个距离基准点的距离
def generate_random_gps(base_log=None, base_lat=None, radius=None):
    radius_in_degrees = radius / 111300
    u = float(random.uniform(0.0, 1.0))
    v = float(random.uniform(0.0, 1.0))
    w = radius_in_degrees * math.sqrt(u)
    t = 2 * math.pi * v
    x = w * math.cos(t)
    y = w * math.sin(t)
    longitude = y + base_log
    latitude = x + base_lat
    # 这里是想保留6位小数点
    loga = "%.6f" % longitude
    lata = "%.6f" % latitude
    return loga, lata

#
# log1, lat1 = generate_random_gps(base_log=120.7, base_lat=30, radius=1000000)
# print(log1, lat1)