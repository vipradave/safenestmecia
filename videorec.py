import cv2

# Open the default camera (index 0)
cap = cv2.VideoCapture(0)
    
# Define the codec and create a VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))

while True:
    # Read a frame from the camera
    ret, frame = cap.read()
    
    # If the frame is read correctly, write it to the output file
    if ret:
        out.write(frame)
        
        # Display the frame (optional)
        cv2.imshow('frame', frame)
        
        # Exit on key press
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

# Release the camera and close the window
cap.release()
out.release()
cv2.destroyAllWindows()