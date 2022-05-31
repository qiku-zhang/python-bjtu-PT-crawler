import os
from chardet.universaldetector import UniversalDetector

def get_filelist(path):
    """
    获取路径下所有csv文件的路径列表
    """
    Filelist = []
    for home, dirs, files in os.walk(path):
        for filename in files:
            if ".csv" in filename:
                Filelist.append(os.path.join(home, filename))
    return Filelist

def read_file(file):
    """
    逐个读取文件的内容
    """
    with open(file, 'rb') as f:
        return f.read()

def get_encode_info(file):
    """
    逐个读取文件的编码方式
    """
    with open(file, 'rb') as f:
        detector = UniversalDetector()
        for line in f.readlines():
            detector.feed(line)
            if detector.done:
                break
        detector.close()
        return detector.result['encoding']

def convert_encode2ascii(file, original_encode, des_encode):
    """
    将文件的编码方式转换为utf-8，并写入原先的文件中。
    """    
    file_content = read_file(file)
    file_decode = file_content.decode(original_encode, 'ignore')
    file_encode = file_decode.encode(des_encode)
    with open(file, 'wb') as f:
        f.write(file_encode)

def read_and_convert(path):
    """
    读取文件并转换
    """
    Filelist = get_filelist(path=path)
    fileNum= 0
    for filename in Filelist:
        try:
            file_content = read_file(filename)
            encode_info = get_encode_info(filename)
            if encode_info != 'ANSI':
                fileNum +=1
                convert_encode2ascii(filename, encode_info, 'ANSI')
                print('成功转换 %s 个文件 %s '%(fileNum,filename))
        except BaseException:
            print(filename,'存在问题，请检查！')

def recheck_again(path):
    """
    再次判断文件是否为utf-8
    """    
    print('---------------------以下文件仍存在问题---------------------')
    Filelist = get_filelist(path)
    for filename in Filelist:
        encode_info_ch = get_encode_info(filename)
        if encode_info_ch != 'ANSI':
            print(filename,'的编码方式是：',encode_info_ch)

    print('--------------------------检查结束--------------------------')
if __name__ == "__main__":
    """
    输入文件路径
    """    
    path = r'C:\Users\张恒瑜\Desktop\爬虫\study用户下载数据'
    read_and_convert(path)
    recheck_again(path)
    print('转换结束！')


