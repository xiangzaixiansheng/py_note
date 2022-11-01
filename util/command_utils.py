import os

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
