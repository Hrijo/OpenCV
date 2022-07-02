import cv2
from cv2 import waitKey
import numpy as np

img = cv2.imread('check_1.jpg')

#threshold on orange
lower = (0,0,0)
upper = (50,165,255)
    
#threshold on Blue
# lower = (112,2,33)
# upper = (255,204,110)

#threshold on Blue test 2
# lower = (66,1,1)
# upper = (255,184,184)


thresh = cv2.inRange(img, lower, upper)

# apply morphology and make 3 channels as mask
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5,5))
mask = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)
mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
mask = cv2.merge([mask,mask,mask])

# create 3-channel grayscale version
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)

# blend img with gray using mask
result = np.where(mask==255, img, gray)

# # save images
cv2.imwrite('orange_cone_thresh.jpg', thresh)
cv2.imwrite('orange_cone_mask.jpg', mask)
cv2.imwrite('orange_cone_result.jpg', result)

# Display images
cv2.imshow("orginal", img)
cv2.imshow("mask", mask)
cv2.imshow("result", result)
cv2.destroyAllWindows()