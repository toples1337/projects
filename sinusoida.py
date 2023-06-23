import numpy as np
import matplotlib.pyplot as plt
from math import pi
# функция
y = lambda x: np.sin(x)
# создаём рисунок с координатную плоскость
fig = plt.subplots()
# создаём область, в которой будет
# - отображаться график
x = np.linspace(-2*pi, 2*pi,100)
# 1 - левая граница
# 2 - правая граница
# - качество прорисовки графика
# рисуем график
plt.plot(x, y(x))
# показываем график
plt.show()