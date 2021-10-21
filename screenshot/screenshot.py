import pyautogui

#
# cap = cv2.VideoCapture(0)
# cap.set(3,720)
# cap.set(4,720)
#
#
#
#
# while True:
#     success,img = cap.read()
#     cv2.imshow('img',img)
#     if cv2.waitKey(1) & 0xFF ==ord('q'):
#         break
# cap.release()
# cv2.destroyAllWindows()
#
#
#
ss = pyautogui.screenshot()
ss.save('Do.png')
