# ex4.py

import matplotlib.pyplot as plt

# print(plt._get_version())

x = [2016, 2017, 2018, 2019, 2020]
y = [350, 410, 520, 695, 543]

plt.plot(x, y)
plt.title('Annual Sales')

plt.xlabel('year')
plt.ylabel('sales')

plt.show()