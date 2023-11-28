from SimpleCV import Camera

cam = Camera()

img = cam.getImage()
# img.save("captured_frame.jpg")
img.show()
