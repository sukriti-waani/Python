# Install required libraries before running:
# pip install qrcode
# pip install pillow

import qrcode                              # For generating QR codes
from PIL import Image                      # For image operations (combining, displaying)

# Step 1: Take UPI ID as input from user
upi_id = input("Enter your UPI ID = ")

# Step 2: 
# UPI payment URL format used by most UPI-supported apps:
# upi://pay?pa=UPI_ID&pn=NAME&am=AMOUNT&cu=CURRENCY&tn=MESSAGE
# Here:
#   pa = payee address (UPI ID)
#   pn = payee name
#   mc = merchant code (optional)
#   am = amount (optional)
#   cu = currency (optional, default is INR)
#   tn = transaction note/message (optional)

# Now we create UPI payment URLs for different payment apps
# We use formatted strings (f-strings) to inject the upi_id into the URL

phonepe_url = f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'
paytm_url = f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'
google_pay_url = f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'

# Step 3: Generate QR codes images
# qrcode.make(data) generates a QR code from the provided data string
phonepe_qr = qrcode.make(phonepe_url)
paytm_qr = qrcode.make(paytm_url)
google_pay_qr = qrcode.make(google_pay_url)

# Step 4: Save each generated QR code as a PNG image file
phonepe_qr.save("phonepe_qr.png")
paytm_qr.save("paytm_qr.png")
google_pay_qr.save("google_pay_qr.png")

# Step 5: Combine all QR codes into one image (side-by-side)

# Convert QR codes to RGB format for combining
phonepe_img = phonepe_qr.convert("RGB")
paytm_img = paytm_qr.convert("RGB")
google_pay_img = google_pay_qr.convert("RGB")

# Get width and height of QR images (assume all are same size)
width, height = phonepe_img.size

# Create new blank image with enough width to hold all three side-by-side
combined_img = Image.new("RGB", (width * 3, height), "white")

# Paste individual QR images into the combined image
combined_img.paste(phonepe_img, (0, 0))
combined_img.paste(paytm_img, (width, 0))
combined_img.paste(google_pay_img, (width * 2, 0))

# Step 6: Save and show the combined image
combined_img.save("combined_qr_codes.png")
combined_img.show()
