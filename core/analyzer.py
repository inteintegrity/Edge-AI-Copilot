import re

# 可以不断扩充
HARDWARE = [
    "RK3576",
    "RK3588",
    "Jetson",
    "Raspberry Pi",
    "ESP32",
    "XIAO",
]

MODELS = [
    "YOLO",
    "YOLOv5",
    "YOLOv8",
    "YOLO11",
    "Whisper",
    "PaddleOCR",
    "SAM",
]

FRAMEWORKS = [
    "RKNN",
    "TensorRT",
    "ONNX",
    "OpenCV",
    "NCNN",
    "TFLite",
]

DEPLOYMENT = [
    "Docker",
    "docker-compose",
    "Python",
    "C++",
]


def search_keywords(text, keywords):

    found = []

    lower = text.lower()

    for k in keywords:

        if k.lower() in lower:

            found.append(k)

    return sorted(list(set(found)))


def analyze_repository(files):

    text = ""

    for content in files.values():

        text += content + "\n"

    result = {}

    result["Hardware"] = search_keywords(text, HARDWARE)

    result["AI Models"] = search_keywords(text, MODELS)

    result["Inference"] = search_keywords(text, FRAMEWORKS)

    result["Deployment"] = search_keywords(text, DEPLOYMENT)

    return result