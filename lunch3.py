import streamlit as st
import random

# 메뉴 데이터
menu_data = {
    "한식": ["김치찌개", "제육볶음", "순대국", "돼지국밥", "불백", "쌈밥", "김치찜", "간장게장", "생고기비빔밥", "곰탕", "시래기국",
           "선지해장국", "갈비탕", "설렁탕", "닭갈비", "찜닭", "닭볶음탕", "쭈꾸미 볶음", "쭈꾸미덮밥", "낙지볶음", "생선구이", "해장국",
           "추어탕", "냉면", "막국수", "콩물국수", "국수", "부대찌개", "순두부찌개", "짜글이", "콩나물국밥", "뼈해장국", "육개장", "알탕", "생태탕"],
    "중식": ["짜장면", "짬뽕","볶음밥","마라탕", "짜장밥", "마파두부"],
    "일식": ["초밥", "소바", "라멘", "텐동","규동", "규카츠", "물회", "카레", "돈까스", "사케동", "치킨덮밥"],
    "양식": ["파스타", "햄버거", "토스트", "서브웨이", "크림우동"],
    "분식": ["김밥", "떡튀순", "라면"],
    "면류": ["쌀국수", "냉면", "막국수", "칼국수", "콩물국수", "국수", "크림우동", "라면", "소바", "짜장면", "짬뽕", "파스타"],
    "탕류": ["부대찌개", "순두부찌개", "짜글이","마라탕", "콩나물국밥", "뼈해장국", "육개장", "곰탕", "알탕", "생태탕", "시래기국", "선지해장국",
           "갈비탕", "설렁탕", "닭볶음탕", "해장국", "추어탕"]
}

# 앱 UI 구성
st.title("🎲 점심메뉴 고르기 🎲")
st.write("원하는 카테고리를 선택하고, '룰렛 돌리기!' 버튼을 클릭하세요.")

# 카테고리 선택
selected_categories = []
for category in menu_data:
    if st.checkbox(category, value=True):
        selected_categories.append(category)

# 메뉴 선택 버튼
if st.button("🎯 룰렛 돌리기!"):
    if not selected_categories:
        st.warning("⚠ 카테고리를 선택해주세요!")
    else:
        # 후보 메뉴 만들기
        candidates = []
        for category in selected_categories:
            candidates.extend(menu_data[category])

        # 메뉴 선정
        selected_menu = random.choice(candidates)
        st.success(f"🍱 오늘은 '{selected_menu}' 어떠세요?")

# '광주수완병원 전산실'과 '만든이 doeun' 추가
st.markdown("<div style='text-align: center; font-size: 12px; color: gray;'>광주수완병원 전산실</div>", unsafe_allow_html=True)
st.markdown("<div style='text-align: center; font-size: 10px; color: gray;'>만든이 doeun</div>", unsafe_allow_html=True)
