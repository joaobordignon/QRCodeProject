import os
import qrcode
import logging
from flask import Flask, render_template, request, send_from_directory, send_file, url_for
from PIL import Image

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ICON_DIR = os.path.join(BASE_DIR, "static", "icons")

def generate_qr_code(url, logo_path=None):
    qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
    qr.add_data(url)
    qr.make(fit=True)
    qr_img = qr.make_image(fill_color="black", back_color="white").convert("RGBA")

    if logo_path:
        logo = Image.open(logo_path).convert("RGBA")
        
        qr_box = qr_img.getbbox()
        logo_size = min(qr_box[2], qr_box[3]) // 4
        logo = logo.resize((logo_size, logo_size))
        logo_pos = ((qr_box[2] - logo_size) // 2, (qr_box[3] - logo_size) // 2)
        
        white_bg = Image.new("RGBA", (logo_size, logo_size), "white")
        white_bg.paste(logo, (0, 0), logo)
        qr_img.paste(white_bg, logo_pos, white_bg)

    return qr_img


@app.route('/', methods=['GET', 'POST'])
def index():
    icons = os.listdir(ICON_DIR)
    selected_icon = None
    qr_img_path = None

    if request.method == 'POST':
        url = request.form.get('url')
        selected_icon = request.form.get('icon')
        
        logging.info(f"Generating QR code for URL: {url} with icon: {selected_icon}")

        logo_path = os.path.join(ICON_DIR, selected_icon) if selected_icon else None
        qr_img = generate_qr_code(url, logo_path)

        qr_img_path = "static/generated_qr.png"
        qr_img.save(os.path.join(BASE_DIR, qr_img_path))
        
        logging.info(f"QR code saved to {qr_img_path}")

    return render_template('index.html', icons=icons, qr_img_path=qr_img_path)

@app.route('/download', methods=['GET'])
def download_qr():
    return send_file(os.path.join(BASE_DIR, "static", "generated_qr.png"), as_attachment=True, download_name="qr_with_logo.png")

if __name__ == '__main__':
    app.run(debug=True)