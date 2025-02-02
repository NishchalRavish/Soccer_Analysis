import cv2

def read_video(video_path):
    cap = cv2.VideoCapture(video_path)
    frames = []
    while True:
        ret, frame = cap.read() #ret returns a flag if there is a frame or not #frame captures the frame
        if not ret: #If video is ended ret flag is 0 and we break out of the loop
            break 
        frames.append(frame)
    return frames

def save_video(output_video_frames,output_video_path): #Takes in a list of frames and video_path
    fourcc = cv2.VideoWriter_fourcc(*'XVID') #output format is xvid
    out = cv2.VideoWriter(output_video_path, fourcc, 24, (output_video_frames[0].shape[1],output_video_frames[0].shape[0])) #Takes in video_path, format, 24 is the number of frames and frame(width,height)
    for frame in output_video_frames: # Loop over each frame and write the frame
        out.write(frame)
    out.release()
    