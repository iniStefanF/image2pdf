import streamlit as st
import img2pdf
from PIL import Image
from io import BytesIO

# Streamlit app title
st.title("Image to PDF Converter")

# File uploader for multiple images
uploaded_files = st.file_uploader("Choose images to combine into a PDF", type=['jpg', 'jpeg', 'png'], accept_multiple_files=True)

# Button to generate PDF
if st.button("Generate PDF"):
    if not uploaded_files:
        st.warning("Please upload at least one image.")
    else:
        # List to store image byte data for img2pdf
        image_data = []

        # Process each uploaded image file
        for uploaded_file in uploaded_files:
            # Open the uploaded image file
            image = Image.open(uploaded_file)

            # Convert to RGB mode if not already
            if image.mode in ("RGBA", "P"):
                image = image.convert("RGB")

            # Save the image to a BytesIO object
            img_byte_arr = BytesIO()
            image.save(img_byte_arr, format='JPEG')
            image_data.append(img_byte_arr.getvalue())

        # Convert the images to a single PDF file
        pdf_bytes = img2pdf.convert(image_data)

        # Create a download button for the generated PDF
        st.download_button(
            label="Download PDF",
            data=pdf_bytes,
            file_name="output.pdf",
            mime="application/pdf"
        )

        st.success("PDF file has been successfully generated.")