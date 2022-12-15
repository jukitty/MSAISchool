import cv2

def image_show(image):
    cv2.imshow('Show', image)
    cv2.waitKey(0)

def image_show_compare(image1, image2):
    cv2.imshow('Show1', image1)
    cv2.imshow('Show2', image2)
    cv2.waitKey(0)
