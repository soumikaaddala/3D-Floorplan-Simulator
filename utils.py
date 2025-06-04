%%writefile utils.py
import cv2
import numpy as np
import os

def apply_perspective_transform(image):
    h, w = image.shape[:2]
    src = np.float32([[0, 0], [w, 0], [0, h], [w, h]])
    dst = np.float32([[w*0.1, h*0.1], [w*0.9, h*0.05], [w*0.15, h*0.95], [w*0.85, h*0.9]])
    M = cv2.getPerspectiveTransform(src, dst)
    warped = cv2.warpPerspective(image, M, (w, h), borderValue=(0, 0, 0))
    return warped

def enhance_with_shadow(image, shadow_offset=10):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray, 240, 255, cv2.THRESH_BINARY_INV)
    kernel = np.ones((5, 5), np.uint8)
    dilated = cv2.dilate(thresh, kernel, iterations=3)
    shadow = np.zeros_like(image)
    shadow[:, :, 0] = dilated
    shadow[:, :, 1] = dilated
    shadow[:, :, 2] = dilated
    M = np.float32([[1, 0, shadow_offset], [0, 1, shadow_offset]])
    shifted_shadow = cv2.warpAffine(shadow, M, (shadow.shape[1], shadow.shape[0]))
    shadow_layer = cv2.addWeighted(shifted_shadow, 0.3, image, 1, 0)
    return shadow_layer

def process_floorplan(image_path, output_path):
    image = cv2.imread(image_path)
    if image is None:
        raise FileNotFoundError(f"Image not found at path: {image_path}")
    warped = apply_perspective_transform(image)
    enhanced = enhance_with_shadow(warped)
    if not os.path.exists(output_path):
        os.makedirs(output_path)
    output_file = os.path.join(output_path, "FloorPlann_3D.png")
    cv2.imwrite(output_file, enhanced)
    return output_file
