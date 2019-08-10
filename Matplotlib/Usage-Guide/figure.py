import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()  #an empty figure with no axes(ko co truc)
fig.suptitle('No axes on this figure')  #add title

fig, ax_lst = plt.subplots(2, 2)  #a figure whit 2x2 gird of Axes (figure voi luoi 2x2 cua cac truc)
fig.show()

'''
Axes: Truc
    Gioi han khong gian cua do thi.
    la khung bao quanh do thi

Axis: Truc (truc tung va truc hoanh)
    Co cac moc chia khoang tren cac truc

Artist: Khung ve
    Khung chua tat ca cac hinh trong do
'''
