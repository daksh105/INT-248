import cv2
import matplotlib.pyplot as plt
import cvlib as cv
from cvlib.object_detection import draw_bbox

def calc_car(a):
    im = cv2.imread(a)
    bbox, label, conf = cv.detect_common_objects(im)
    output_image = draw_bbox(im, bbox, label, conf)
    plt.imshow(output_image)
    plt.show()
    lb = label.count('car')
    print('Number of cars in image- ' + str(lb))
    return lb