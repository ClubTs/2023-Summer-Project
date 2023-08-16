import streamlit as st
from api.AI import get_summarization_result
from api.AI import get_text_ocr_result

def main():
    st.markdown("2023 HAI 여름 프로젝트")
    st.title("OCR & GPT를 활용한 이미지 문서 요약")

    query = st.file_uploader("요약하고 싶은 글의 이미지 파일을 업로드하세요.")
    if query is not None:
        st.image(query)
        ocr_data = get_text_ocr_result(query)
        result_string = ""

        for image in ocr_data["images"]:
            for field in image["fields"]:
                if "inferText" in field:
                    result_string += field["inferText"] + " "
        st.markdown(result_string)
        
        placeholder = st.empty()
        if placeholder.button("글 요약하기"):
            st.divider()
            summary = get_summarization_result(result_string)
            summary = summary.split(sep="제목:", maxsplit=1)[1]
            summary_t, summary_r = summary.split(sep="요약 결과:", maxsplit=1)
            st.subheader(summary_t)
            st.markdown(summary_r)
            placeholder.empty()

if __name__ == '__main__':
    main()