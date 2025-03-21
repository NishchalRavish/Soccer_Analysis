from utils import read_video, save_video
from trackers import Tracker
import cv2

def main():
    # Read Video
    video_frames = read_video('input_videos/test.mp4')
    
    tracker = Tracker('models/best.pt')
    
    tracks = tracker.get_object_tracks(video_frames,
                                       read_from_stub=True,
                                       stub_path='stubs/track_stubs.pkl')
    
    # Save cropped image of a player
    for track_id, player in tracks['players'][0].items():
        bbox = player['bbox']
        frame = video_frames[0]
        
        # Crop bbox from frame
        cropped_image = frame[int(bbox[1]):int(bbox[3]), int(bbox[0]):int(bbox[2])]

        # Save the cropped image
        cv2.imwrite(f'output_videos/cropped.jpg', cropped_image)
        break
        
    # Draw Output
    ## Draw object Tracks
    
    output_video_frames = tracker.draw_annotations(video_frames, tracks)
    
    # Save video
    save_video(output_video_frames,'output_videos/output_video.avi')
    
if __name__ == "__main__":
    main()