import streamlit as st


import streamlit as st

# 1. 페이지 기본 설정
st.set_page_config(
    page_title="홍길동의 프로필",
    page_icon="👋",
    layout="centered"
)

# 2. 헤더 영역 (이름 및 핵심 요약)
st.title("안녕하세요, ㅄ입니다! 👋")
st.subheader("💡 문제를 만드는 신입 파이썬 개발자")
st.write("새로운 기술을 배우고 적용하는 것을 좋아합니다. 효율적인 코드와 깔끔한 문서화를 지향합니다.")

st.markdown("---")

# 3. 본문 영역 (사이드바 또는 컬럼 활용)
col1, col2 = st.columns([1, 2])

with col1:
    # 프로필 이미지 (이미지 URL이나 로컬 파일 경로를 넣으세요)
    # 이미지 파일이 없다면 이 부분은 주석 처리하거나 기본 이미지를 쓰면 됩니다.
    st.image("https://via.placeholder.com/150", caption="홍길동", use_container_width=True)

with col2:
    st.markdown("### 📝 인적 사항")
    st.write("• **이메일:** gildong@example.com")
    st.write("• **깃허브:** [github.com/gildong](https://github.com)")
    st.write("• **블로그:** [gildong-log.tistory.com](https://tistory.com)")

st.markdown("---")

# 4. 보유 기술 (Tech Stacks)
st.markdown("### 🛠️ 보유 기술 (Tech Stacks)")

# 탭 기능으로 깔끔하게 분류
tab1, tab2 = st.tabs(["Languages", "Frameworks & Tools"])

with tab1:
    st.write("**Python** - 데이터 분석 및 자동화 스크립트 작성 가능")
    st.write("**JavaScript** - 기본적인 DOM 조작 및 웹 프론트엔드 이해")

with tab2:
    st.write("**Streamlit** - 프로토타입 웹 애플리케이션 신속하게 개발 가능")
    st.write("**Git & GitHub** - 형상 관리 및 팀 협업 경험")

st.markdown("---")

# 5. 간단한 방명록 / 연락 남기기 인터랙션
st.markdown("### ✉️ 메시지 남기기")
st.write("저에게 궁금한 점이 있다면 아래에 메시지를 남겨주세요!")

with st.form(key="contact_form"):
    name = st.text_input("이름")
    message = st.text_area("내용")
    submit_button = st.form_submit_button(label="보내기")
    
    if submit_button:
        if name and message:
            st.success(f"🎉 감사합니다, {name}님! 메시지가 성공적으로 전송되었습니다.")
            # 실제 데이터베이스나 이메일로 보내는 로직을 추가할 수 있습니다.
        else:
            st.warning("이름과 내용을 모두 입력해주세요.")