from imageai.Detection import ObjectDetection
import time
import matplotlib.pyplot as pl
import os

execution_path = os.getcwd()
img_to_read = 'laptop.jpeg'
detector = ObjectDetection()
detector.setModelTypeAsRetinaNet()
detector.setModelPath( os.path.join(execution_path , "resnet50_coco_best_v2.0.1.h5"))
detector.loadModel()
custom = detector.CustomObjects(tv=True, laptop=True)
detections = detector.detectObjectsFromImage(input_image=os.path.join(execution_path , img_to_read), output_image_path=os.path.join(execution_path , "imagenew.jpg"))
count=0
for eachObject in detections:
    print(eachObject["name"] , " : " , eachObject["box_points"] )
    coordinate = eachObject["box_points"]
    img = pl.imread(os.path.join(execution_path , img_to_read))
    print(img.shape)
    img_cropped = img[coordinate[1]:coordinate[3],coordinate[0]:coordinate[2],:]
    print(img_cropped.shape)
imgplot = pl.imshow(img_cropped)
pl.show()
time.sleep(3)