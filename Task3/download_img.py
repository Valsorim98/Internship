import requests

# That's for downloading an image from xkcd.com
receive = requests.get("https://imgs.xkcd.com/comics/history_department.png")
with open(r"C:\Users\PC\Desktop\downloaded_img.png","wb") as f:
    f.write(receive.content)


# That's for downloading an image from httbin.org
receive = requests.get("https://httpbin.org/image/png")
with open (r"C:\Users\PC\Desktop\image1.png", "wb") as f:
    f.write(receive.content)
