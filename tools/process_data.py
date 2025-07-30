import os
import pandas as pd
import shutil


def organize_images_from_csv(csv_file_path, source_folder, output_folder):
    # 读取CSV文件
    df = pd.read_csv(csv_file_path)

    # 确保输出文件夹存在
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for index, row in df.iterrows():
        # 获取image_filename和classification
        image_filename = row['image_filename']
        classification = row['classification']

        # 构造真实文件名
        parts = image_filename.split('\\')
        real_filename = f"{parts[0]}_{parts[1]}_{parts[2].replace('.tif', '.png')}"

        # 构造源文件路径
        source_file_path = os.path.join(source_folder, real_filename)

        # 根据分类创建输出文件夹
        class_folder = os.path.join(output_folder, classification)
        if not os.path.exists(class_folder):
            os.makedirs(class_folder)

        # 移动文件
        if os.path.exists(source_file_path):
            shutil.move(source_file_path, os.path.join(class_folder, real_filename))
            print(f'Moved: {real_filename} to {class_folder}')
        else:
            print(f'File not found: {source_file_path}')


# 调用方法，传入文件路径
csv_file_path = 'For DL model/f01_outlines.csv'  # CSV文件路径
source_folder = 'For DL model/F01_349'  # 源文件夹路径
output_folder = 'For DL model/organized_images'  # 输出文件夹路径
organize_images_from_csv(csv_file_path, source_folder, output_folder)
