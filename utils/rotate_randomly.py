import cv2, os


def rotate(frame, angle):
    cols, rows, _ = frame.shape
    rotate_around = (cols // 2, rows // 2)
    rot_mat = cv2.getRotationMatrix2D(rotate_around, angle, 1.0)
    result = cv2.warpAffine(frame, rot_mat, frame.shape[1::-1], flags=cv2.INTER_LINEAR)
    return result


def rotate_video(video_path_in, video_name, rotation_increment, video_path_out):
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
        direction = np.random.choice([-1, 1])
        result = rotate(frame, rotation_increment * direction)
        rotation_increment = rotation_increment * direction
        video_writer.write(result)
    video_writer.release()
    video.release()
