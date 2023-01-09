# import os
# # 測試抓所有圖片
# place = r"C:\Users\ASUS\Desktop\pictures\origin"
# for _, x, y in os.walk(place):
#     print(y)
# #


# # from flask import Flask
# # from flask import render_template
# # import os
# # import cv2
# # import random
# # import requests
# # from bs4 import BeautifulSoup

# # app = Flask(__name__)
# # img_folder = os.path.join('static', 'pics')

# # app.config['UPLOAD_FOLDER'] = img_folder


# # @app.route('/testpage')
# # def show():
# #     url = r'http://127.0.0.1:8080/chancolor'
# #     response = requests.get(url)
# #     content = BeautifulSoup(response.text,"html.parser")
# #     content = content.find("img")
# #     pics = content['src']
# #     return render_template(r'index.html',
# #                            img_stream=pics)

# # @app.route('/chancolor')
# # def chco():
# #     img = cv2.imread(r"C:\Users\clark\Desktop\happy\test1\static\pics\test.jpg")
# #     r1, r2, r3 = [random.randint(0, 256) for _ in range(3)]
# #     img[1,:,:] = r1
# #     img[:,1,:] = r2
# #     img[:,:,1] = r3
# #     cv2.imwrite(r'C:\Users\clark\Desktop\happy\test1\static\pics\test1.jpg', img)
# #     dog1 = os.path.join(app.config['UPLOAD_FOLDER'], 'test1.jpg')
# #     return render_template(r'index.html',
# #                            img_stream=dog1)
# @app.route('/masico/<int:a>')
# def masico(a):
#     img = cv2.imread(r"C:\Users\clark\Desktop\happy\test1\static\pics\test.jpg")
#     size = img.shape         # 取得原始圖片的資訊
#     level = a          # 縮小比例 ( 可當作馬賽克的等級 )
#     h = int(size[0]/level)   # 按照比例縮小後的高度 ( 使用 int 去除小數點 )
#     w = int(size[1]/level)   # 按照比例縮小後的寬度 ( 使用 int 去除小數點 )
#     mosaic = cv2.resize(img, (w,h), interpolation=cv2.INTER_LINEAR)   # 根據縮小尺寸縮小
#     mosaic = cv2.resize(mosaic, (size[1],size[0]), interpolation=cv2.INTER_NEAREST)
#     cv2.imwrite(r'C:\Users\clark\Desktop\happy\test1\static\pics\test2.jpg', mosaic)
#     # mdog1 = os.path.join(app.config['UPLOAD_FOLDER'], 'test1.jpg')
#     mdog1 = r'../static/pics/test2.jpg'
#     return render_template(r'index.html',
#                            img_stream=mdog1)


# # @app.route('/')
# # def hello_world():
# #     dog = os.path.join(app.config['UPLOAD_FOLDER'], 'test.jpg')
# #     return render_template(r'index.html',
# #                            img_stream=dog)


# # if __name__ == '__main__':
# #     app.run(debug=True, port=8080)\
import cv2
img = cv2.imread(r"C:\Users\ASUS\Desktop\cloud_computing\static\pictures\origin\test.jpg")
size = img.shape         # 取得原始圖片的資訊
level = 15               # 縮小比例 ( 可當作馬賽克的等級 )
h = int(size[0]/level)   # 按照比例縮小後的高度 ( 使用 int 去除小數點 )
w = int(size[1]/level)   # 按照比例縮小後的寬度 ( 使用 int 去除小數點 )
mosaic = cv2.resize(img, (w,h), interpolation=cv2.INTER_LINEAR)   # 根據縮小尺寸縮小
mosaic = cv2.resize(mosaic, (size[1],size[0]), interpolation=cv2.INTER_NEAREST) # 放大到原本的大小
cv2.imshow('oxxostudio', mosaic)
cv2.waitKey(0)           # 按下任意鍵停止
cv2.destroyAllWindows()