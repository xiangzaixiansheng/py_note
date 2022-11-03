import os
import subprocess

def command(cmd_str, need_result=False):
    '''
    执行命令行
    :param cmd_str:
    :param need_result:是否需要读结果
    :return:
    '''
    __result = None
    if cmd_str:
        command_obj = os.popen(cmd_str)
        if command_obj:
            try:
                if need_result:
                    __result = command_obj.read().strip()
            except Exception as e:
                print(str(e))
            finally:
                try:
                    command_obj.close()
                except Exception as e:
                     print(str(e))
    return __result


def get_line_count(filepath):
    '''
    获取一个文件的行数
    :param filepath:
    :return:
    '''
    _file_line_count = command("cat " + filepath + " | wc -l")
    return _file_line_count if _file_line_count else 0


def read_line(filepath, line_num):
    '''
    读取一个文件的某一行
    :param filepath:
    :param line_num:
    :return:
    '''
    if line_num > 0:
        read_line_cmd = "sed -n " + str(line_num) + "p " + filepath
        return command(read_line_cmd, True)
    else:
        return ''

def run_command_by_subprocess(run_cmd):
    # run_cmd = run_cmd.split(" ")
    print(run_cmd)
    popen = subprocess.Popen(run_cmd, stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    run_result = popen.stdout.readlines()
    
    popen.wait()
   
    return run_result

# 实时输出结果
def run_command_by_subprocess_real_time(run_cmd):
    #run_cmd = run_cmd.split(" ")
    p = subprocess.Popen(run_cmd, stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)

    for line in iter(p.stdout.readline, b''):
        print(line.decode('gbk'))
    p.stdout.close()
    return ''

if __name__ == "__main__":
    
    print(run_command_by_subprocess("ls -ll"))
    # 实施输出
    run_command_by_subprocess_real_time("ping www.baidu.com")

    # 输出内容到屏幕
    ret = os.system("ls -ll")
    print(ret)

