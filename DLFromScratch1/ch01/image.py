#%%
import matplotlib.pyplot as plt
from matplotlib.image import imread

img = imread("honeybadger.jpeg") # 이미지 파일이 현재 작업 디렉터리에 있음
plt.imshow(img)
plt.show()
# %%
