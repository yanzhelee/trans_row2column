# -*- coding: utf-8 -*-
import sys
import csv

'''
使用方法
----------------
运行命令：
python trans_row2col.py xxx.txt

程序运行成功后，会生成名称类似 xxx.export.txt 的文件
'''
if __name__ == '__main__':

    argv_len = len(sys.argv)
    print('The number of parameters is %d'%(argv_len-1))
    print('Parameter list: %s'%str(sys.argv[1:]))

    if argv_len == 0:
        print('Error:Parameter length does not match')
        sys.exit(1)

    file_path = sys.argv[1]

    raw_data = {}

    columns = []

    # 从CSV文件获取数据
    with open(file_path, newline='', encoding='utf-8') as f:
        reader = csv.reader(f, delimiter='\t')
        head = next(reader)

        for row in reader:

            if row[1] not in columns:
                columns.append(row[1])
            else:
                pass

            key = row[0]
            if key not in raw_data:
                raw_data[key] = {row[1] : row[2]}
            else:
                raw_data[key][row[1]] = row[2]

    # 填充空白数据
    for key in raw_data:
        for item in columns:
            if item not in raw_data[key]:
                raw_data[key][item] = ''

    return_data = ([key]+[raw_data[key][item] for item in columns] for key in raw_data)

    with open(file_path.replace('.', '_export.'), "w",newline="", encoding='utf-8') as f:

        writer = csv.writer(f, delimiter='\t')

        # 写入头信息
        writer.writerow([head[0]] + columns)

        for row in return_data:
            writer.writerow(row)

    print('success')
