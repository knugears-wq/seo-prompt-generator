import streamlit as st

# ─────────────────────────────────────────────
# 페이지 설정
# ─────────────────────────────────────────────
st.set_page_config(
    page_title="SEO 프롬프트 생성기",
    page_icon="🔍",
    layout="wide"
)

st.title("🔍 SEO 블로그 프롬프트 생성기")
st.caption("원문 정보를 입력하면 Claude에 바로 붙여넣을 수 있는 완성된 SEO 프롬프트를 생성합니다.")

# ─────────────────────────────────────────────
# 프롬프트 템플릿 생성 함수
# ─────────────────────────────────────────────
def generate_prompt(source_content: str, target_audience: str, target_keyword: str, tone: str) -> str:
    prompt = f"""<role>
당신은 Google SEO 전문가이자 워드프레스 콘텐츠 전략가입니다.
검색엔진 알고리즘(Google E-E-A-T, Core Web Vitals)에 정통하며,
키워드 최적화와 독자 경험을 동시에 고려한 콘텐츠를 설계합니다.
</role>

<task>
내가 제공하는 원문 내용을 바탕으로:
1. SEO 관점에서 글의 구조를 재편성하고
2. 핵심 키워드 및 LSI 키워드를 전략적으로 배치하며
3. 워드프레스에 바로 적용 가능한 형태로 최종 콘텐츠를 작성해줘.
</task>

<input_required>
[원문 내용]
{source_content}

[타겟 독자]
{target_audience}

[목표 키워드]
{target_keyword}

[톤앤매너]
{tone}
</input_required>

<seo_rules>
반드시 아래 SEO 규칙을 적용해줘:

[키워드 전략]
- 메인 키워드: 제목(H1), 첫 단락 100자 이내, 메타 디스크립션에 반드시 포함
- 서브 키워드(LSI): H2, H3 소제목에 자연스럽게 분산 배치
- 키워드 밀도: 전체 글의 1~2% 유지 (과도한 반복 금지)
- 롱테일 키워드: 소제목 또는 FAQ 섹션에 활용

[글 구조]
- 전체 분량: 최소 1,200자 이상 (SEO 권장)
- H1(1개) → H2(3~5개) → H3(필요시) 계층 구조 유지
- 도입부: 독자의 Pain Point를 짚고 글의 가치를 명확히 제시
- 본문: 정보의 논리적 흐름 유지, 핵심 내용은 앞에 배치
- 마무리: 핵심 요약 + CTA(Call to Action) 포함

[워드프레스 최적화]
- 메타 제목(Title Tag): 60자 이내, 메인 키워드 포함
- 메타 디스크립션: 150~160자, 키워드 + 클릭 유도 문구 포함
- URL Slug 추천: 영문 소문자, 하이픈(-) 구분, 키워드 포함
- 이미지 ALT 텍스트: 키워드 포함 문구 추천
- 내부 링크 위치: [내부링크: 관련 글 제목] 형태로 표시
- 추천 태그/카테고리 제안 포함
</seo_rules>

<output_format>
최종 결과물은 아래 순서로 출력해줘:
---
[SEO 분석 요약]
- 메인 키워드:
- 서브 키워드 목록:
- 예상 검색 의도(User Intent):

[워드프레스 설정값]
- 메타 제목:
- 메타 디스크립션:
- URL Slug:
- 추천 카테고리/태그:
- 이미지 ALT 텍스트 예시:

[최종 블로그 본문]
(H1 / H2 / H3 계층 구조로 작성된 완성 본문)

[내부 링크 제안]

[FAQ 섹션]
---
</output_format>

<constraints>
- 키워드를 억지로 끼워 넣지 말고 문맥상 자연스럽게 삽입할 것
- 독자가 끝까지 읽고 싶은 흐름을 유지할 것
- 표절 없이 내가 제공한 원문을 재구성하는 것에 집중할 것
- 불필요한 미사여구, 중복 표현 제거
</constraints>

위 내용을 바탕으로 SEO 최적화 블로그 글을 작성해줘.

---

[썸네일 이미지 프롬프트]
위 블로그 내용의 분위기에 맞는 Flora AI용 썸네일 이미지 프롬프트를 영문으로 작성해줘. (1280x720, 클린/미니멀 + 인포그래픽 스타일)"""

    return prompt


# ─────────────────────────────────────────────
# 메인 UI
# ─────────────────────────────────────────────
col_left, col_right = st.columns([1, 1], gap="large")

with col_left:
    st.subheader("📝 원문 정보 입력")

    source_content = st.text_area(
        "원문 내용 *",
        height=200,
        placeholder="여기에 보유하고 있는 정보나 초안을 입력하세요."
    )

    target_audience = st.text_area(
        "타겟 독자 *",
        height=80,
        placeholder="예: 30대 직장인, 투자 초보자, 창업 준비자 등"
    )

    target_keyword = st.text_area(
        "목표 키워드",
        height=80,
        placeholder='예: "재테크 방법", "ETF 투자 초보" — 없으면 추천해줘 라고 입력'
    )

    tone = st.text_area(
        "톤앤매너 *",
        height=80,
        placeholder="예: 친근하고 쉬운 설명체, 전문적이고 신뢰감 있는 어조 등"
    )

    generate_btn = st.button("🚀 프롬프트 생성", type="primary", use_container_width=True)


# ─────────────────────────────────────────────
# 결과 출력
# ─────────────────────────────────────────────
with col_right:
    st.subheader("📄 생성된 프롬프트")

    if generate_btn:
        if not source_content.strip():
            st.error("❌ 원문 내용을 입력해주세요.")
        elif not target_audience.strip():
            st.error("❌ 타겟 독자를 입력해주세요.")
        elif not tone.strip():
            st.error("❌ 톤앤매너를 입력해주세요.")
        else:
            keyword_value = target_keyword.strip() if target_keyword.strip() else "추천해줘"
            result = generate_prompt(source_content, target_audience, keyword_value, tone)

            st.success("✅ 프롬프트 생성 완료! 아래 내용을 복사해서 Claude에 붙여넣으세요.")

            # 복사용 텍스트 박스
            st.text_area(
                "복사용 프롬프트",
                value=result,
                height=500,
                label_visibility="collapsed"
            )

            st.divider()

            # 다운로드 버튼
            dl_col1, dl_col2 = st.columns(2)
            with dl_col1:
                st.download_button(
                    label="💾 MD 파일 저장",
                    data=result,
                    file_name="seo_prompt.md",
                    mime="text/markdown",
                    use_container_width=True
                )
            with dl_col2:
                st.download_button(
                    label="💾 TXT 파일 저장",
                    data=result,
                    file_name="seo_prompt.txt",
                    mime="text/plain",
                    use_container_width=True
                )
    else:
        st.info("👈 왼쪽에 원문 정보를 입력하고 [프롬프트 생성] 버튼을 눌러주세요.")
