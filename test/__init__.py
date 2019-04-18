import numpy as np
import csv
import math


def read_file_and_tran_to_matrix(file_name):
    file = open(file_name, 'r')
    csv_reader = csv.reader(file)
    list = []
    for line in csv_reader:
        list.append(line)
    array = np.array(list, dtype='float')
    return array


def getDistance(line_point_1, line_point_2, point):
    line_length = np.linalg.norm(line_point_1 - line_point_2)
    return np.linalg.norm(np.cross(line_point_1-point,line_point_1-line_point_2))/line_length


if __name__ == '__main__':
    d1_array = read_file_and_tran_to_matrix("d1.csv")
    d1_corr = d1_array[:, [1, 2, 3]]
    d2_array = read_file_and_tran_to_matrix("d2.csv")
    d2_corr = d2_array[:, [1, 2, 3]]
    center = read_file_and_tran_to_matrix("mass.csv")
    center_corr = center[:, [1, 2, 3]]

    # 处理垂直向下
    center_low = center[:, [1, 2, 3]]
    center_low[:, 2] -= 625.245


    length = []
    # 求直线方程
    for (d1, d2, point,point_low) in zip(d1_corr, d2_corr, center_corr,center_low):
        a = getDistance(d1,d2,point)
        b = getDistance(d1,d2,point_low)
        c = np.linalg.norm(point - point_low)
        length.append([a,b,c])
    result = []
    file = open("result.csv", 'w+')
    csv_writer = csv.writer(file)
    for array,d1 in zip(length,d1_array):
        d=math.acos((array[2]*array[2]+array[0]*array[0]-array[1]*array[1])/(array[2]*array[1]*2))
        csv_writer.writerow([d1[0],math.tan(d)])
        result.append([d1[0],math.tan(d)])







