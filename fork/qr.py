import qrcode
import os
import uuid

print("---------------------------------------")
print("                                       ")
print("-- Welcome To QR Code Generator --")
print("                                       ")
print("---------------------------------------")
print("                                       ")

print("1. Store Text or any other data.")
print("2. Store Link.")

choice = input("Enter your choice (1 or 2): ")

if choice == '1':
    data = input("Enter the text or data you want to store in the QR code: ")
elif choice == '2':
    data = input("Enter the link you want to store in the QR code: ")
else:
    print("Invalid choice! Exiting...")
    exit(1)

qr_img = qrcode.make(data)

# Create directory if it does not exist
output_dir = "qr-img"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Generate a random filename
filename = f"{uuid.uuid4()}.jpg"
output_path = os.path.join(output_dir, filename)
qr_img.save(output_path)

print(f"QR code generated and saved to {output_path} as {filename}")
