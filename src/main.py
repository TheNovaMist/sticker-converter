import os
import subprocess
from src.utils import mkdir


# 转换 sticker
def convert(image_path, output_dir):
    subprocess.run(['magick', 'convert', image_path, output_dir])


# 筛选后缀为 png 且不包含 key 关键词的文件名
def check_image(file):
    if file.endswith('.png') and not '_key' in file:
        return True

    return False


if __name__ == '__main__':

    # 输入输出目录
    input = 'image'
    output = 'dist'

    root_path = os.getcwd()

    input_dir = os.path.join(root_path, input)
    output_dir = os.path.join(root_path, output)

    # 创建输出文件夹
    mkdir(output)

    # 读取当前目录全部图片路径
    dirs = os.listdir(input_dir)

    # 过滤路径去除 key 关键字
    img_iterator = filter(check_image, dirs)

    imgList = list(img_iterator)

    print(imgList)

    # imgList = ['435105518@2x.png',
    #            '435105515@2x.png']

    for image_name in imgList:
        # 输入输出文件地址
        input_png_path = os.path.join(input_dir, image_name)

        output_gif_path = os.path.join(
            output_dir, image_name.replace('png', 'gif'))

        # print(output_dir)

        convert(input_png_path, output_gif_path)
