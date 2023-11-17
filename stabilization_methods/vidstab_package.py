from vidstab import VidStab
import matplotlib.pyplot as plt
import os


def stabilize_with_vidstab(video_path, video_name, video_path_out):
    stabilizer = VidStab()
    stabilizer.stabilize(
        input_path=os.path.join(video_path, video_name), output_path=video_path_out
    )

    stabilizer.plot_trajectory()
    plt.show()

    stabilizer.plot_transforms()
    plt.show()
