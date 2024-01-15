import qrcode
from flask import Flask, render_template
from io import BytesIO
import threading
import webbrowser

app = Flask(__name__)

# HTML page data
html_page_content = "https://dhruvkathrotiya.github.io/Personal-Website/"
# Generate QR code for the HTML page
def generate_qr_code(html_content):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(html_content)
    qr.make(fit=True)

    # Create an image from the QR code
    img = qr.make_image(fill_color="black", back_color="white")

    # Save the QR code image
    img.save("generated_qr_code.png")  # Save to the static folder

    print("QR code generated successfully.")

# Open the HTML page in the default web browser
def open_html_page():
    webbrowser.open("http://127.0.0.1:5000/scanned_page")

@app.route('/')
def index():
    # Generate QR code for the HTML page and pass the QR code image path to the template
    generate_qr_code(html_page_content)
    threading.Thread(target=open_html_page).start()
    return render_template('index.html', qr_code_image="generated_qr_code.png")

@app.route('/scanned_page')
def scanned_page():
    return html_page_content

if __name__ == '__main__':
    app.run(debug=True)


