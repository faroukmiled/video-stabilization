import cv2, os
import numpy as np


def translate_vertically(frame, translation_rate):
    frame1 = np.zeros(frame.shape)
    h, w, _ = frame.shape

    if translation_rate > 0:
        frame1[translation_rate:h, :] = frame[: h - translation_rate, :]
    else:
        frame1[: h - translation_rate, :] = frame[translation_rate:h, :]
    return frame1


def translate_horizontally(frame, translation_rate):
    frame1 = np.zeros_like(frame)
    h, w, _ = frame.shape

    if translation_rate > 0:
        frame1[:, translation_rate:w] = frame[:, : w - translation_rate]
    else:
        frame1[:, : w - translation_rate] = frame[:, translation_rate:w]
    return frame1


def translate_video_horizontally(
    video_path_in, video_name, translation_rate, video_path_out
):
    video = os.path.join(video_path_in, video_name)

    video = cv2.VideoCapture(video)
    fourcc = cv2.VideoWriter_fourcc("M", "J", "P", "G")
    width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = video.get(cv2.CAP_PROP_FPS)
    video_writer = cv2.VideoWriter(video_path_out, fourcc, fps, (width, height))
    while True:
        ret, frame = video.read()
        if not ret:
            break
        result = translate_horizontally(frame, translation_rate)
        translation_rate += 5
        video_writer.write(result)
    video_writer.release()
    video.release()


def translate_video_vertically(
    video_path_in, video_name, translation_rate, video_path_out
):
    video = os.path.join(video_path_in, video_name)

    video = cv2.VideoCapture(video)
    fourcc = cv2.VideoWriter_fourcc("M", "J", "P", "G")
    width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = video.get(cv2.CAP_PROP_FPS)
    video_writer = cv2.VideoWriter(video_path_out, fourcc, fps, (width, height))
    while True:
        ret, frame = video.read()
        if not ret:
            break
        result = translate_vertically(frame, translation_rate)
        translation_rate += 5
        video_writer.write(result)
    video_writer.release()
    video.release()
