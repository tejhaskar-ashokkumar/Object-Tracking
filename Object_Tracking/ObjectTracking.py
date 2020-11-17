'''File: Object Tracking
Name: Tejhaskar'''

import cv2
import sys
 

if __name__ == '__main__' :
 
 
    tracker_types = ['BOOSTING', 'MIL','KCF', 'TLD', 'MEDIANFLOW', 'CSRT', 'MOSSE']
    tracker_type = input("Enter a tracker type: ")
    tracker_type = tracker_type.upper()
 
    if tracker_type == 'BOOSTING':
        tracker = cv2.TrackerBoosting_create()
    if tracker_type == 'MIL':
        tracker = cv2.TrackerMIL_create()
    if tracker_type == 'KCF':
        tracker = cv2.TrackerKCF_create()
    if tracker_type == 'TLD':
        tracker = cv2.TrackerTLD_create()
    if tracker_type == 'MEDIANFLOW':
        tracker = cv2.TrackerMedianFlow_create()
    if tracker_type == 'CSRT':
        tracker = cv2.TrackerCSRT_create()
    if tracker_type == 'MOSSE':
        tracker = cv2.TrackerMOSSE_create()
 
    video = cv2.VideoCapture("./videos/hurdles.mp4")
 
    if not video.isOpened():
        print("Error opening the video file")
        sys.exit()
 
    
    success, frame = video.read()
    if not success:
        print('Error reading the video file')
        sys.exit()
     
    
    bounding_box = None

 
    
    bounding_box = cv2.selectROI(frame, fromCenter = False, showCrosshair = True)
 
    # Initialize tracker with first frame and bounding box
    success = tracker.init(frame, bounding_box)
 
    while True:
        
        success, frame = video.read()
        if not success:
            break
         
        # Start timer
        timer = cv2.getTickCount()
 
        # Update tracker
        success, bounding_box = tracker.update(frame)
 
        # Calculate Frames per second (FPS)
        fps = cv2.getTickFrequency() / (cv2.getTickCount() - timer);
 
        # Draw bounding box
        if success:
            # Tracking success
            p1 = (int(bounding_box[0]), int(bounding_box[1]))
            p2 = (int(bounding_box[0] + bounding_box[2]), int(bounding_box[1] + bounding_box[3]))
            cv2.rectangle(frame, p1, p2, (50,170,50), 2, 1)
        else :
            # Tracking failure
            cv2.putText(frame, "Tracking failure detected", (100,80), 
                        cv2.FONT_HERSHEY_SIMPLEX, 0.75,(0,0,255),2)
 
        # Display tracker type on frame
        cv2.putText(frame, tracker_type + " Tracker", (100,20), 
                    cv2.FONT_HERSHEY_SIMPLEX, 0.75, (255,0,0),2);
     
        # Display FPS on frame
        cv2.putText(frame, "FPS : " + str(int(fps)), (100,50), 
                    cv2.FONT_HERSHEY_SIMPLEX, 0.75, (255,0,0), 2);
 
        # Display result
        cv2.imshow("Tracking", frame)
        
        # Exit if ESC pressed
        k = cv2.waitKey(1) & 0xff
        if k == 27 : break
