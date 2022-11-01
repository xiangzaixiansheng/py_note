
# File 相关练习
import os


def test():
    target_dir = "./pic"
    flag = "png"
    # 创建文件夹
    if not os.path.exists(target_dir):
            print('文件夹不存在 创建文件夹:' + target_dir)
            try:
                os.makedirs(target_dir)
            except Exception as e:
                print(e)
    
    # 遍历文件夹
    flists = os.listdir(target_dir)
    flists = filter(lambda f: f.endswith(flag), flists)
    for file_name in flists:
        print('含有', flag, file_name)

    #读文件 
    with open(target_dir + "/somefile.txt", "r") as tmp_file:    
        for line in tmp_file.readlines():
            print(line)

    print("#####读一行文件")

    #读一行文件
    with open(target_dir + "/somefile.txt", "r") as _f:
        while True:
            line = _f.readline()
            if not line : break
            print(line)
                    

if __name__ == "__main__":
    test()