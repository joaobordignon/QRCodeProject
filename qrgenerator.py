import qrcode

def generate_qr_code(link, filename="qr_code.png"):
    """
    Generate a QR code from the provided link and save it as a PNG file.
    
    Args:
    - link (str): The link you want the QR code to direct to.
    - filename (str, optional): The name of the PNG file to save the QR code to. Default is "qr_code.png".
    """
    
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    
    qr.add_data(link)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(filename)

# Example usage
url = input("Enter the URL you want the QR code to link to: ")

filename_input = input("Enter a filename (leave blank for default 'qr_code.png'): ")
if filename_input:
    if not filename_input.endswith('.png'):
        filename_input += '.png'
else:
    filename_input = "qr_code.png"

generate_qr_code(url, filename_input)






