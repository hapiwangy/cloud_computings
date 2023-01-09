from flask import Flask, render_template, request, redirect, url_for, send_from_directory
# 功能新增
import funcs
import os 

pic_path = r"static\pictures"
current_pic_path = r""
numbers = 0
app = Flask(__name__)
@app.route("/")
def hello():
    return "Hello, World!"


# 下載圖片

@app.route('/download', methods=['GET'])
def download():
    print(current_pic_path)
    return send_from_directory('upload', current_pic_path, as_attachment=True)

# 換顏色
@app.route("/change_color")
def change_color():
    file_name = current_pic_path.split("\\")[-1]
    title = f"顏色轉換：{file_name}"
    color_pic = funcs.change_color(current_pic_path)
    return render_template("HTMLPage2.html", img_path=color_pic, title = title)
# 換風格(只抓取線條)
@app.route("/change_style")
def change_style():
    file_name = current_pic_path.split("\\")[-1]
    title = f"風格轉換：{file_name}"
    color_pic = funcs.img_sharp(current_pic_path)
    return render_template("HTMLPage2.html", title=title, img_path=color_pic)

@app.route("/change_masioc")
def change_masioc():
    file_names = current_pic_path.split("\\")[-1]
    title = f"馬賽克:{file_names}"
    return render_template("HTMLPage2.html", title = title, img_path=mac_pic)
    
    
@app.route("/home", methods=['GET','POST'])
def home():
    path = r"C:\Users\ASUS\Desktop\cloud_computing\static\pictures\origin"
    files = funcs.get_all_files(path)
    global pic_path
    global current_pic_path
    global numbers
    global mac_pic
    global file_names
    opic_path = pic_path + "\\origin"
    if request.method == 'POST':
        if request.values['send'] == "send_pic_path":
            file_path = request.form.get('file_name')
            if file_path != "":
                opic_path = opic_path+"\\"+file_path
                current_pic_path = opic_path
                return render_template('HTMLPage1.html', files = files, img_path=current_pic_path)
        else:
            print("here")
            mac_pic = funcs.do_masioc(current_pic_path, numbers)
            current_pic_path = mac_pic
            return redirect(url_for('change_masioc'))
    else:
        return render_template('HTMLPage1.html', files = files, img_path="static\\pictures\\default\\bed.jpg")


if __name__ == '__main__':
    app.run(debug=True)