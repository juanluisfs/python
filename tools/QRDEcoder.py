import cv2

# Load the QR code image
img = cv2.imread('/Users/juanluis/Downloads/IMG_1332.jpg')

# Initialize QR code detector
detector = cv2.QRCodeDetector()

# Detect and decode the QR code
data, bbox, _ = detector.detectAndDecode(img)

# Print the decoded data
if data:
    print(f"Decoded QR code data: {data}")
else:
    print("QR code could not be decoded")
