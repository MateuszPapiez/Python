from distutils.command.upload import upload
from fastapi import FastAPI, Response, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware 
from PIL import Image



App=FastAPI()
origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://127.0.0.1:5500",
]
App.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@App.post("/image-red")
def color_red(file:UploadFile):
    print(file.filename,file.file)
    #print(file.file.read())
    img=Image.open(file.file)
    show_blur(img)
    img.save("mod.png")
    with open ("mod.png","rb") as f:
        return Response(content=f.read())

def pixel_blur (a,b,c,d):
    r=(a[0]+b[0]+c[0]+d[0])//4
    b_=(a[1]+b[1]+c[1]+d[1])//4
    g=(a[2]+b[2]+c[2]+d[2])//4

    return (r,b_,g)


def show_blur (img):
    img_pixels=img.load()
    for i in range (img.size[0]-1):
        for j in range (img.size[1]-1):
            mean2=255-(img_pixels[i,j][0]+img_pixels[i,j][1]+img_pixels[i,j][2])//3
            
            img_pixels[i,j]= mean2

    #img.show()
@App.post("/image-crop")
def image_crop(file:UploadFile):
    img=Image.open(file.file)
    width, height = img.size
    
    left = width /4
    top = height / 4
    right = 3* width /4 
    bottom = 3 * height / 4
    
    img_crop=img.crop((left,top,right,bottom))
    img_crop.save("mod.png")
    with open ("mod.png","rb") as f:
        return Response(content=f.read())