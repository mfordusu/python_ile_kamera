import cv2

# Kamera aygıtını yakalama (0 birincil kamera, 1 ikincil kamera)
cap = cv2.VideoCapture(0)

# Video kaydetme için codec ve VideoWriter nesnesini oluşturma
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret:
        # Kamera görüntüsünü kaydetme
        out.write(frame)

        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):  # 'q' tuşuna basıldığında çıkış yap
            break
    else:
        break

# Her şey tamamlandığında, kayıt işlemini serbest bırak
cap.release()
out.release()
cv2.destroyAllWindows()
