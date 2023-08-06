import streamlit as st
from imageCaptioning import imageCaptioning
from text2story import story_chain
from story2audio import text2speech


def main():
    st.set_page_config(page_title='Image 2 Audio Story')

    uploader_file = st.file_uploader('select an image ...', type='jpg')

    if uploader_file is not None:
        data = uploader_file.getvalue()
        with open(uploader_file.name, 'wb') as f:
            f.write(data)

        st.image(uploader_file, caption='Uploaded Image')

        text = imageCaptioning(uploader_file.name)
        story = story_chain.run(text)
        text2speech(story)

        with st.expander('scenario'):
            st.write(text)
        with st.expander('story'):
            st.write(story)

        st.audio('output.flac',format='flac')


if __name__ == '__main__':
    main()