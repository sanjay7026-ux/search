import streamlit as st
import fitz
from PIL import Image

st.title(" ❤️ File Reader ❤️")

file=st.file_uploader("Upload your file",type=["jpg","jpeg","png","gif","txt","pdf"])

sub=st.button("Submit")

if sub:
    if file is not None:
        filename=file.name.lower()

        if filename.endswith((".jpg",".jpeg",".png",".gif")):
            img=Image.open(file)
            st.image(img,caption="Your image",use_container_width=True)
        elif filename.endswith(".txt"):
            text=file.read().decode("utf-8")
            st.text_area("Content is:",text,height=300)    
        elif filename.endswith(".pdf"):
            d=fitz.open(stream=file.read(),filetype="pdf")
            op=""
            for page in d:
                op+=page.get_text()
            st.text_area("Content is:",op,height=300)  
        else:
            st.error("unsupported file type")
    else:
        st.warning("please upload a file")          
