import cv2
import face_recognition


ref_images = ["ref_img.jpg", "ref_img2.jpg","ref_img3.jpg","ref_img4.jpg"]
ref_face_encodings = []

for ref_image_path in ref_images:
    ref_image = face_recognition.load_image_file(ref_image_path)
    ref_face_encoding = face_recognition.face_encodings(ref_image)
    if ref_face_encoding:
        ref_face_encodings.append(ref_face_encoding[0])


video_capture = cv2.VideoCapture(0)

frame_rate = 30
frame_count = 0

while True:
    ret, frame = video_capture.read()

    if frame_count % (int(30 / frame_rate)) == 0:
        face_locations = face_recognition.face_locations(frame)

        if len(face_locations) > 0:
            unknown_face_encodings = face_recognition.face_encodings(frame, face_locations)

            if unknown_face_encodings:
                match = False
                for ref_face_encoding in ref_face_encodings:
                    results = face_recognition.compare_faces([ref_face_encoding], unknown_face_encodings[0])
                    if True in results:
                        match = True
                        break

                if match:
                    text = "Match"
                else:
                    text = "Not Match"
            else:
                text = "No Face"
                
            for (top, right, bottom, left) in face_locations:
                cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
        else:
            text = "No Face"

        cv2.putText(frame, text, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    cv2.imshow('Video', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    frame_count += 1

video_capture.release()
cv2.destroyAllWindows()