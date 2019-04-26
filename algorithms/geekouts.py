# Reference: https://subscription.packtpub.com/book/application_development/9781785283932/2/ch02lvl1sec25/creating-a-vignette-filter
import cv2
import numpy as np

def foo():
    print('hello this is from geekouts central')


def vignette():
    img = cv2.imread('input.jpg')
    rows, cols = img.shape[:2]

    # generating vignette mask using Gaussian kernels
    kernel_x = cv2.getGaussianKernel(cols, 200)
    kernel_y = cv2.getGaussianKernel(rows, 200)
    kernel = kernel_y * kernel_x.T
    mask = 255 * kernel / np.linalg.norm(kernel)
    output = np.copy(img)

    # applying the mask to each channel in the input image
    for i in range(3):
        output[:,:,i] = output[:,:,i] * mask

        cv2.imshow('Original', img)
        cv2.imshow('Vignette', output)
        cv2.waitKey(0)
