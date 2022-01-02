from pathlib import Path
def get_path(*other):
    """获取数据文件绝对路径"""
    dir_path = Path.cwd().joinpath('data')
    return str(dir_path.joinpath(*other))