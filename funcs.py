import os
# 取得所有圖片的位址
def get_all_files(url):
    for _, _, y in os.walk(url):
        files = y
    return files
#
import cv2
import random
import numpy as np
# 進行圖片顏色的改變
def change_color(pic_path):
    img = cv2.imread(pic_path)
    r1, r2, r3 = [random.randint(0, 256) for _ in range(3)]
    img[1,:,:] = r1
    img[:,1,:] = r2
    img[:,:,1] = r3
    paths = pic_path.split("\\")    
    basis = paths[:3]
    basis.append("chcol"+paths[-1].split(".")[0])
    new_name = "\\".join(basis)
    cv2.imwrite(f"{new_name}.jpeg" ,img)
    return f"{new_name}.jpeg"

# 進行圖片馬賽克的更改
def do_masioc(pic_path, a):
    img = cv2.imread(pic_path)
    size = img.shape         # 取得原始圖片的資訊
    level = a          # 縮小比例 ( 可當作馬賽克的等級 )
    h = int(size[0]/level)   # 按照比例縮小後的高度 ( 使用 int 去除小數點 )
    w = int(size[1]/level)   # 按照比例縮小後的寬度 ( 使用 int 去除小數點 )
    mosaic = cv2.resize(img, (w,h), interpolation=cv2.INTER_LINEAR)   # 根據縮小尺寸縮小
    mosaic = cv2.resize(mosaic, (size[1],size[0]), interpolation=cv2.INTER_NEAREST)
    paths = pic_path.split("\\")    
    basis = paths[:3]
    basis.append("masi"+paths[-1].split(".")[0])
    new_name = "\\".join(basis)
    cv2.imwrite(f"{new_name}.jpeg" ,mosaic)
    # # cv2.imwrite(f"new_name.jpeg" ,img)
    return f"{new_name}.jpeg"
# 照片銳化
def img_sharp(pic_path):
    img = cv2.imread(pic_path, cv2.IMREAD_GRAYSCALE)
    median_intensity = np.median(img)
    lower_treshold = int(max(0, (1.0 - 0.33) * median_intensity))
    upper_treshold = int(min(255, (1.0 + 0.33) * median_intensity))
    img_canney = cv2.Canny(img, lower_treshold, upper_treshold)
    paths = pic_path.split("\\")    
    basis = paths[:3]
    basis.append("stych"+paths[-1].split(".")[0])
    new_name = "\\".join(basis)
    # print(basis)
    cv2.imwrite(f"{new_name}.jpeg" ,img_canney)
    return f"{new_name}.jpeg"

# if __name__ == '__main__':
#     img_sharp(r"C:\Users\ASUS\Desktop\cloud_computing\static\pictures\origin\test.jpg")