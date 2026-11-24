import numpy as np
import streamlit as st
from PIL import Image


st.set_page_config(page_title="Julia Set Visualizer", layout="wide")

st.title("Julia Set Visualizer")

col1, col2 = st.columns(2)

with col2:
    f = st.slider("Imaginary part of c (0 to 1)", 0.0, 1.0, 0.75, step=0.01)
    width = st.slider("Width", 200, 1000, 500)
    height = st.slider("Height", 200, 1000, 500)

real_max = st.sidebar.slider('Real part', 2, 15, 0, step = 1)
im_max = st.sidebar.slider('Imaginary part', 2, 15, 0, step = 1 )

@st.cache_data

def generate_julia(f, width, height,im_max,real_max, max_iterations = 255, escape_radius = 10):

    c = complex(0.0, f)

    image = np.zeros((height, width), dtype =np.uint8)

    im_range = np.linspace(-im_max, im_max, height)
    re_range = np.linspace(-real_max, real_max, width)

    for y,im in enumerate(im_range):
        for x,re in enumerate(re_range):
            z = complex(re, im)
            n = max_iterations
            while abs(z) < escape_radius and n >= 5:
                z = z * z + c
                n -= 1
                image[y, x] = n

    return image


with col1:
    image = generate_julia(f,width, height, im_max, real_max)
    pil_image = Image.fromarray(image, mode="L")
    st.image(pil_image, caption=f"c = 0 + {f}i", use_container_width=True)
