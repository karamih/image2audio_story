import streamlit as st
from imageCaptioning import imageCaptioning

from sequentialChain import chain


def main():
    st.set_page_config(page_title='Image 2 Audio Story')

    uploader_file = st.file_uploader('select an image ...', type='jpg')

    if uploader_file is not None:
        data = uploader_file.getvalue()
        with open(uploader_file.name, 'wb') as f:
            f.write(data)

        st.image(uploader_file, caption='Uploaded Image')

        text = imageCaptioning(uploader_file.name)
        story = chain.run(text)

        with st.expander('scenario'):
            st.write(text)
        with st.expander('story'):
            st.write(story)


if __name__ == '__main__':
    main()