import qrcode


def generate_qr_code(url, filename="qrcoode.png"):
    # Create a QR Code instance
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    
    # Add the URL to the QR Code
    qr.add_data(url)
    qr.make(fit=True)

    # Create an image from the QR Code instance
    img = qr.make_image(fill_color="black", back_color="white")

    # Save the image to a file
    img.save(filename)
    print(f"QR Code generated and saved as {filename}")
    
if __name__ == "__main__":
    # Example URL
    url_input = input("Enter the URL to generate QR Code: ")
    generate_qr_code(url_input)
