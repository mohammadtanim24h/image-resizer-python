import cv2

# Configurable Params
image_source = "elden_ring.jpg"
destination = "new_image.jpg"

# Percent by which the image is resized
scale_percent = int(input("Enter a number which will be the percentage to scale up/down the image: "))

image = cv2.imread(image_source, cv2.IMREAD_UNCHANGED)

# Calculate the new dimensions from the original dimensions using the entered scale percentage
new_width = int(image.shape[1] * scale_percent / 100)
new_height = int(image.shape[0] * scale_percent / 100)

# Desired new image size
dsize = (new_width, new_height)

# Resize image
output = cv2.resize(image, dsize)

cv2.imwrite(destination, output)