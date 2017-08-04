import numpy as np
import matplotlib.pyplot as plt

#データ作成
x = np.arange(0, 6, 0.1) #0から6までを0.1刻みで作成
y = np.sin(x)

#グラフを描画
plt.plot(x, y)
plt.show()