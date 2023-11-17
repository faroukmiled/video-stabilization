# video-stabilization
The main objective of this project is to develop digital methods for stabilizing shaky videos which is crucial for reliable sport video analysis.

## Code and details

* The notebook [1_Introduction_to_Digital_video_stabilization.ipynb](https://github.com/centralelyon/video-stabilization/blob/main/1_Introduction_to_Digital_video_stabilization.ipynb) : 

	- justifies the need for video stabilization.
	- presents examples related to sport that need a pre-processing with this technique before analysis.
	- explains the steps of the stabilization process.
	- presents state of the art methods that implement this process.
	- defines a performance measure to assess the stabilization method.

* The notebook [2_implementation_of_video_stabilization.ipynb](https://github.com/centralelyon/video-stabilization/blob/main/2_implementation_of_video_stabilization.ipynb)  :
	-  generates artificially destabilized videos (zooming, translation, rotation, random_tranlsation/rotation).

   - lists state of the art methods.
    	
* The notebook [3_Performance_measure.ipynb](https://github.com/centralelyon/video-stabilization/blob/main/2_implementation_of_video_stabilization.ipynb)  makes a comparaison between ffmpeg based method which uses gaussian low pass filter algorithm and opencv_feature_matching_based method which trackes interest keypoints and tries to smooth their trajectory.

## Results

Metric used for video stabilization : pixel shift of interest keypoints
<img src="https://github.com/centralelyon/video-stabilization/blob/main/results.png" alt="Results" width="700"/>
