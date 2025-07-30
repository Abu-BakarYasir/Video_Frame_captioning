# 📁 frame_extractor.py
import cv2
import os
from PIL import Image

def extract_frames(video_path, interval_sec=2):
    vidcap = cv2.VideoCapture(video_path)
    fps = vidcap.get(cv2.CAP_PROP_FPS)
    total_frames = int(vidcap.get(cv2.CAP_PROP_FRAME_COUNT))
    duration = total_frames / fps

    frames = []
    count = 0
    while True:
        timestamp = count * interval_sec * 1000  # in milliseconds
        vidcap.set(cv2.CAP_PROP_POS_MSEC, timestamp)
        success, image = vidcap.read()
        if not success or (count * interval_sec > duration):
            break

        image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        pil_img = Image.fromarray(image_rgb)
        frames.append((count * interval_sec, pil_img))
        count += 1

    vidcap.release()
    return frames