import numpy as np
import cv2
from PIL import ImageGrab

fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter("out.avi", fourcc, 22.0, (1366,768))

while 1:
    img = ImageGrab.grab()
    img_np = np.array(img)

    frame = cv2.cvtColor(img_np, cv2.COLOR_BGR2RGB)
    out.write(frame)
    if cv2.waitKey(1) == 27:
        break

out.release()
cv2.destroyAllWindows()
