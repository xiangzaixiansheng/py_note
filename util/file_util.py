

def get_lines(filepath):
    try:
        with open(filepath, 'r') as f:
            lines = f.read().splitlines()
            return lines
    except Exception as e:
        print(e)
    return None


def get_line(filepath, line_num):
    '''

    :param filepath:
    :param line_num:
    :return:
    '''
    if line_num >= 1:
        lines = get_lines(filepath)
        if lines and line_num <= len(lines):
            try:
                return lines[line_num - 1]
            except Exception as e:
                print(e)
    return ''


def get_line_count(filepath):
    lines = get_lines(filepath)
    return len(lines) if lines else 0
