"""페이지별 로직 — 라우팅 모듈"""
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots


def route(page, marts, st, kpi_card, section_title, insight_box, quote_box, style_fig,
          PRIMARY, ACCENT, DANGER, SUCCESS, WARNING, BG):
    
    # =========================================================================
    # EXECUTIVE SUMMARY
    # =========================================================================
    if page.startswith("🏠"):
        section_title("핵심 요약", "양적 정점, 질적 후퇴, 사회적 인정")
        
        # KPI 5개 상단
        c1, c2, c3, c4, c5 = st.columns(5)
        with c1:
            st.markdown(kpi_card("2025 총 방문자", "567,010", "+127.9%", "up"), unsafe_allow_html=True)
        with c2:
            st.markdown(kpi_card("일평균 방문자", "70,876", "-14.5%", "down"), unsafe_allow_html=True)
        with c3:
            st.markdown(kpi_card("FPI 점수", "64.3", "-12.0%", "down"), unsafe_allow_html=True)
        with c4:
            st.markdown(kpi_card("FLI 효과", "21.1%", "-33.6%", "down"), unsafe_allow_html=True)
        with c5:
            st.markdown(kpi_card("FSI 등급", "77.6 (A)", "+3.6", "up"), unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)
        
        # 신규 KPI 3개 (인스타·뉴스)
        section_title("신규 SNS·뉴스 KPI")
        c1, c2, c3 = st.columns(3)
        with c1:
            st.markdown(kpi_card("SNS 인게이지먼트", "176.3", "+207%", "up"), unsafe_allow_html=True)
        with c2:
            st.markdown(kpi_card("외국어 댓글 비율", "23.9%", "+22.0%p", "up"), unsafe_allow_html=True)
        with c3:
            st.markdown(kpi_card("뉴스 긍정 문장", "270건", "+286%", "up"), unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)
        
        # 핵심 메시지
        col1, col2 = st.columns([1, 1])
        with col1:
            insight_box(
                "★ 양적 정점, 질적 후퇴",
                "2025년은 8일 확대 개최로 총 방문자 56.7만명 (역대 최다) 기록. 하지만 일평균은 -14.5%, FPI -12%, FLI -33.6%로 질적 지표 일제히 후퇴.",
                "warning"
            )
            insight_box(
                "✓ 외국인 블루오션 3중 입증",
                "외국인 방문자 +1,258% (3년) | 외국어 댓글 +1,158% | 뉴스 외국인 영역 강점 28건 — 세 데이터가 모두 같은 방향.",
                "success"
            )
        with col2:
            insight_box(
                "★ 사회적 인정도는 정점",
                "SNS 인게이지먼트 +207%, 뉴스 긍정 평가 +286%, CCI +6.75 (사상최고). 양적 지표는 후퇴했지만 무형 자산은 모두 정점.",
                "success"
            )
            insight_box(
                "⚠ 새로 발견된 약점 3가지",
                "1) 행사후 SNS 인게이지먼트 -50% 급락 (여운 마케팅 부재) 2) 지역연계·편의안내 영역 강점 0건 3) 화성행궁 집중 심화",
                "danger"
            )

        # 종합 시계열
        st.markdown("<br>", unsafe_allow_html=True)
        section_title("8년 종합 추이", "방문자 · FPI · FSI 동시 비교")
        
        df = marts['mart_1-1_종합지표'].sort_values('개최년도')
        
        fig = make_subplots(specs=[[{"secondary_y": True}]])
        fig.add_trace(go.Bar(
            x=df['개최년도'], y=df['(전체)방문자수'], name='방문자수',
            marker_color=PRIMARY, opacity=0.7,
        ), secondary_y=False)
        fig.add_trace(go.Scatter(
            x=df['개최년도'], y=df['FPI'], name='FPI', mode='lines+markers+text',
            line=dict(color=ACCENT, width=3), marker=dict(size=10),
            text=df['FPI'].round(1), textposition='top center',
        ), secondary_y=True)
        fig.add_trace(go.Scatter(
            x=df['개최년도'], y=df['FSI'], name='FSI', mode='lines+markers',
            line=dict(color=SUCCESS, width=3, dash='dot'), marker=dict(size=10),
        ), secondary_y=True)
        fig.update_yaxes(title_text="방문자수", secondary_y=False)
        fig.update_yaxes(title_text="FPI / FSI 점수", secondary_y=True, range=[0, 100])
        st.plotly_chart(style_fig(fig, height=420), use_container_width=True)

    # =========================================================================
    # PART 1 — 방문자 성과
    # =========================================================================
    elif page.startswith("1️⃣"):
        section_title("PART 1. 방문자 성과 분석", "CAGR 18.5% (양적) vs 3.0% (실질)")
        
        df = marts['mart_1-1_종합지표'].sort_values('개최년도')
        
        # KPI 카드
        c1, c2, c3, c4 = st.columns(4)
        with c1:
            st.markdown(kpi_card("CAGR 총방문자", "18.5%", "양적 성장", "up"), unsafe_allow_html=True)
        with c2:
            st.markdown(kpi_card("CAGR 일평균", "3.0%", "실질 성장", "neutral"), unsafe_allow_html=True)
        with c3:
            st.markdown(kpi_card("외국인 +1,258%", "6,289명", "2022→2025", "up"), unsafe_allow_html=True)
        with c4:
            st.markdown(kpi_card("EPI 외부유입력", "72.0%", "2025년", "neutral"), unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)
        col1, col2 = st.columns(2)
        
        # 1-A. 방문자 vs FPI/FLI
        with col1:
            section_title("방문자 vs FPI/FLI")
            fig = make_subplots(specs=[[{"secondary_y": True}]])
            fig.add_trace(go.Bar(x=df['개최년도'], y=df['(전체)방문자수'], name='방문자',
                marker_color=PRIMARY, opacity=0.7), secondary_y=False)
            fig.add_trace(go.Scatter(x=df['개최년도'], y=df['FPI'], name='FPI',
                mode='lines+markers', line=dict(color=ACCENT, width=3),
                marker=dict(size=10)), secondary_y=True)
            fig.add_trace(go.Scatter(x=df['개최년도'], y=df['FLI'], name='FLI',
                mode='lines+markers', line=dict(color=SUCCESS, width=3),
                marker=dict(size=10)), secondary_y=True)
            fig.update_yaxes(title_text="방문자", secondary_y=False)
            fig.update_yaxes(title_text="FPI / FLI", secondary_y=True)
            st.plotly_chart(style_fig(fig, height=380), use_container_width=True)

        # 1-B. CAGR (신규!)
        with col2:
            section_title("★ CAGR — 양적 vs 실질")
            fig = go.Figure()
            fig.add_trace(go.Scatter(x=df['개최년도'], y=df['CAGR_방문자'], name='CAGR 총방문자',
                mode='lines+markers+text', line=dict(color=PRIMARY, width=4),
                marker=dict(size=12), text=df['CAGR_방문자'].round(1).astype(str)+'%',
                textposition='top center'))
            fig.add_trace(go.Scatter(x=df['개최년도'], y=df['CAGR_일평균'], name='CAGR 일평균',
                mode='lines+markers+text', line=dict(color=DANGER, width=4),
                marker=dict(size=12), text=df['CAGR_일평균'].round(1).astype(str)+'%',
                textposition='bottom center'))
            fig.add_hline(y=18.46, line_dash="dot", line_color="rgba(31,56,100,0.4)", 
                         annotation_text="양적 평균 18.5%", annotation_position="right")
            fig.add_hline(y=2.97, line_dash="dot", line_color="rgba(197,48,48,0.4)",
                         annotation_text="실질 평균 3.0%", annotation_position="right")
            fig.update_yaxes(title_text="CAGR (%)", ticksuffix="%")
            st.plotly_chart(style_fig(fig, height=380), use_container_width=True)

        # 1-C. 8일 착시
        col1, col2 = st.columns(2)
        with col1:
            section_title("8일 착시 분해")
            df8 = marts['mart_1-3_8일착시정량화'].sort_values('개최년도')
            fig = go.Figure()
            fig.add_trace(go.Bar(y=df8['개최년도'].astype(str), x=df8['핵심3일환산_방문자'],
                name='핵심3일환산', orientation='h', marker_color=PRIMARY))
            fig.add_trace(go.Bar(y=df8['개최년도'].astype(str), x=df8['기간확대효과'],
                name='기간확대효과', orientation='h', marker_color=ACCENT))
            fig.update_layout(barmode='stack')
            st.plotly_chart(style_fig(fig, height=380), use_container_width=True)
        
        with col2:
            section_title("종합 지표 표")
            cols = ['개최년도', '축제기간_일', '(전체)방문자수', '일평균 방문자수', 'FPI', 'FLI', 'FSI', 'FSI_등급']
            display = df[cols].copy()
            display.columns = ['연도', '기간(일)', '전체방문자', '일평균', 'FPI', 'FLI', 'FSI', '등급']
            for c in ['전체방문자', '일평균']:
                display[c] = display[c].apply(lambda x: f"{int(x):,}")
            st.dataframe(display, hide_index=True, use_container_width=True)

        insight_box(
            "💡 핵심 인사이트",
            "총방문자 CAGR 18.5%는 8일 확대로 인한 양적 폭증을 반영. 일평균 CAGR 3.0%가 진짜 실질 성장률. 두 값의 6배 격차가 \"양적 착시\"의 정확한 크기.",
            "warning"
        )

    # =========================================================================
    # PART 2 — KPI 분석
    # =========================================================================
    elif page.startswith("2️⃣"):
        section_title("PART 2. KPI 분석", "5대 KPI × 6개 연도 매트릭스")
        
        # 2-1. KPI 히트맵
        kpi_df = marts['mart_2-1_KPI히트맵']
        kpi_on = kpi_df[kpi_df['그룹'] == '축제기간'].pivot_table(
            index='지표명', columns='개최년도', values='지표값').round(2)
        
        col1, col2 = st.columns([1.3, 1])
        with col1:
            section_title("축제기간 KPI 히트맵")
            fig = go.Figure(data=go.Heatmap(
                z=kpi_on.values, x=kpi_on.columns, y=kpi_on.index,
                colorscale=[[0, DANGER], [0.5, WARNING], [1, SUCCESS]],
                text=kpi_on.values, texttemplate="%{text:.2f}",
                textfont={"size": 13, "color": "#2D3748"}, showscale=True,
            ))
            st.plotly_chart(style_fig(fig, height=400), use_container_width=True)
        
        with col2:
            section_title("FPI / FLI 추이")
            df = marts['mart_1-1_종합지표'].sort_values('개최년도')
            fig = go.Figure()
            fig.add_trace(go.Scatter(x=df['개최년도'], y=df['FPI'], name='FPI',
                mode='lines+markers+text', line=dict(color=PRIMARY, width=3),
                marker=dict(size=10), text=df['FPI'].round(1), textposition='top center'))
            fig.add_trace(go.Scatter(x=df['개최년도'], y=df['FLI'], name='FLI',
                mode='lines+markers+text', line=dict(color=ACCENT, width=3),
                marker=dict(size=10), text=df['FLI'].round(1), textposition='bottom center'))
            st.plotly_chart(style_fig(fig, height=400), use_container_width=True)

        # 2-3. 축제 vs 비축제
        section_title("축제 vs 비축제 비교", "리프트 효과 시각화")
        years = sorted(kpi_df['개최년도'].unique())
        sel_year = st.selectbox("연도 선택", years, index=len(years)-1)
        
        on_y = kpi_df[(kpi_df['그룹']=='축제기간') & (kpi_df['개최년도']==sel_year)].set_index('지표명')['지표값']
        off_y = kpi_df[(kpi_df['그룹']=='비축제기간') & (kpi_df['개최년도']==sel_year)].set_index('지표명')['지표값']
        
        col1, col2 = st.columns(2)
        with col1:
            fig = go.Figure()
            fig.add_trace(go.Bar(y=on_y.index, x=on_y.values, name='축제기간',
                orientation='h', marker_color=PRIMARY, text=on_y.values.round(2),
                textposition='outside'))
            fig.add_trace(go.Bar(y=off_y.index, x=off_y.values, name='비축제기간',
                orientation='h', marker_color="#A6A6A6", text=off_y.values.round(2),
                textposition='outside'))
            fig.update_layout(barmode='group')
            st.plotly_chart(style_fig(fig, height=380), use_container_width=True)
        
        # 2-4. 변동계수
        with col2:
            section_title("지표 안정성 (CV)")
            cv = marts['mart_2-4_지표안정성CV'].sort_values('CV_퍼센트')
            colors = [SUCCESS if v < 15 else (WARNING if v < 25 else DANGER) for v in cv['CV_퍼센트']]
            fig = go.Figure(go.Bar(y=cv['지표명'], x=cv['CV_퍼센트'], orientation='h',
                marker_color=colors, text=cv['CV_퍼센트'].astype(str)+'%', textposition='outside'))
            fig.add_vline(x=10, line_dash="dot", line_color=SUCCESS, annotation_text="안정")
            fig.add_vline(x=25, line_dash="dot", line_color=DANGER, annotation_text="불안정")
            st.plotly_chart(style_fig(fig, height=380), use_container_width=True)

    # =========================================================================
    # PART 3 — 관광 소비
    # =========================================================================
    elif page.startswith("3️⃣"):
        section_title("PART 3. 팔달구 관광 소비 트렌드", "1인당 4~5만원 정체")
        
        df = marts['mart_3-1_1인당소비']
        
        c1, c2, c3, c4 = st.columns(4)
        with c1:
            st.markdown(kpi_card("2022 소비", "13,075억", "기준점", "neutral"), unsafe_allow_html=True)
        with c2:
            st.markdown(kpi_card("2024 소비 (정점)", "13,331억", "+2.0%", "up"), unsafe_allow_html=True)
        with c3:
            st.markdown(kpi_card("2025 소비", "12,824억", "-3.8%", "down"), unsafe_allow_html=True)
        with c4:
            st.markdown(kpi_card("1인당 (2025)", "5.0만원", "방문 +185% 대비 -7%", "down"), unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)
        col1, col2 = st.columns(2)
        
        with col1:
            section_title("방문자 vs 1인당 소비")
            fig = make_subplots(specs=[[{"secondary_y": True}]])
            fig.add_trace(go.Bar(x=df['개최년도'], y=df['방문자'], name='방문자',
                marker_color=PRIMARY, opacity=0.7,
                text=[f"{int(x/10000)}만" for x in df['방문자']], textposition='outside'),
                secondary_y=False)
            fig.add_trace(go.Scatter(x=df['개최년도'], y=df['1인당_추정소비_만원'],
                name='1인당 소비', mode='lines+markers+text',
                line=dict(color=DANGER, width=4), marker=dict(size=12),
                text=df['1인당_추정소비_만원'].astype(str)+'만원', textposition='top center'),
                secondary_y=True)
            fig.update_yaxes(title_text="방문자수", secondary_y=False)
            fig.update_yaxes(title_text="1인당 소비 (만원)", secondary_y=True, range=[0, 8])
            st.plotly_chart(style_fig(fig, height=400), use_container_width=True)
        
        with col2:
            section_title("업종별 지출 비율 변화")
            biz = marts['mart_2-3a_대분류별비율'].copy()
            if '연도' in biz.columns and '대분류' in biz.columns:
                biz['연도'] = biz['연도'].astype(str)
                biz_pivot = biz.pivot_table(index='연도', columns='대분류',
                    values='대분류_지출비율', aggfunc='sum').fillna(0)
                fig = go.Figure()
                colors = [PRIMARY, ACCENT, SUCCESS, WARNING, DANGER, "#9F7AEA", "#38B2AC"]
                for i, col in enumerate(biz_pivot.columns):
                    fig.add_trace(go.Scatter(x=biz_pivot.index, y=biz_pivot[col], name=col,
                        mode='lines', line=dict(color=colors[i % len(colors)], width=2),
                        stackgroup='one'))
                st.plotly_chart(style_fig(fig, height=400), use_container_width=True)
        
        # 진단지표
        section_title("진단 지표 증감률 5종", "2024년 변곡점 발견")
        diag = marts['mart_2-3b_진단지표증감률']
        if len(diag) > 0 and '연도' in diag.columns:
            fig = go.Figure()
            colors_map = {0: PRIMARY, 1: ACCENT, 2: SUCCESS, 3: WARNING, 4: DANGER}
            indicators = diag['지표명'].unique() if '지표명' in diag.columns else []
            for i, ind in enumerate(indicators):
                sub = diag[diag['지표명'] == ind].sort_values('연도')
                val_col = [c for c in sub.columns if c not in ['연도', '지표명']][0]
                fig.add_trace(go.Scatter(x=sub['연도'], y=sub[val_col], name=ind,
                    mode='lines+markers', line=dict(color=colors_map.get(i, PRIMARY), width=2),
                    marker=dict(size=8)))
            fig.add_hline(y=0, line_dash="dot", line_color="rgba(0,0,0,0.3)")
            st.plotly_chart(style_fig(fig, height=380), use_container_width=True)

    # =========================================================================
    # PART 4 — 검색 트렌드
    # =========================================================================
    elif page.startswith("4️⃣"):
        section_title("PART 4. 관광 검색 트렌드", "10월 코호트 분석")
        
        df = marts['mart_1-2_10월코호트'].sort_values('연도')
        
        c1, c2, c3 = st.columns(3)
        with c1:
            st.markdown(kpi_card("2025 검색", "423,800", "+12.9% vs 2022", "up"), unsafe_allow_html=True)
        with c2:
            st.markdown(kpi_card("2024 전환율", "33.9%", "최고", "up"), unsafe_allow_html=True)
        with c3:
            st.markdown(kpi_card("1인당 소비 (2025)", "10,615원", "-24% vs 2022", "down"), unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)
        col1, col2 = st.columns(2)
        
        with col1:
            section_title("연도별 검색 vs 방문")
            fig = make_subplots(specs=[[{"secondary_y": True}]])
            if '검색건수' in df.columns:
                fig.add_trace(go.Bar(x=df['연도'], y=df['검색건수'], name='검색건수',
                    marker_color=ACCENT, opacity=0.7), secondary_y=False)
            if '전체방문자' in df.columns:
                fig.add_trace(go.Scatter(x=df['연도'], y=df['전체방문자'], name='방문자',
                    mode='lines+markers', line=dict(color=PRIMARY, width=3),
                    marker=dict(size=10)), secondary_y=True)
            st.plotly_chart(style_fig(fig, height=400), use_container_width=True)
        
        with col2:
            section_title("1인당 소비 추이")
            if '1인당평균소비_원' in df.columns:
                fig = go.Figure(go.Bar(x=df['연도'].astype(str), y=df['1인당평균소비_원'],
                    marker_color=PRIMARY, text=df['1인당평균소비_원'].astype(int).astype(str)+'원',
                    textposition='outside'))
                st.plotly_chart(style_fig(fig, height=400), use_container_width=True)
        
        # 검색 Top 10
        section_title("검색 Top 10")
        srch = marts['mart_3-1c_목적지검색순위']
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("**현지인 기준**")
            local = srch[srch['구분'] == '현지인'].head(10) if '구분' in srch.columns else srch.head(10)
            if len(local) > 0:
                cols = [c for c in ['순위', '목적지명', '카테고리'] if c in local.columns]
                st.dataframe(local[cols], hide_index=True, use_container_width=True)
        with col2:
            st.markdown("**외지인 기준**")
            visitor = srch[srch['구분'] == '외지인'].head(10) if '구분' in srch.columns else srch.head(10)
            if len(visitor) > 0:
                cols = [c for c in ['순위', '목적지명', '카테고리'] if c in visitor.columns]
                st.dataframe(visitor[cols], hide_index=True, use_container_width=True)

    # =========================================================================
    # PART 5 — CCI 경쟁력
    # =========================================================================
    elif page.startswith("5️⃣"):
        section_title("PART 5. 관광 수요 경쟁력 (CCI)", "팔달구 vs 전국평균")
        
        df = marts['mart_5_CCI종합'].sort_values('개최년도')
        
        c1, c2, c3 = st.columns(3)
        with c1:
            st.markdown(kpi_card("CCI 2025", "+6.75", "사상 최고", "up"), unsafe_allow_html=True)
        with c2:
            st.markdown(kpi_card("CCI 2021 (저점)", "+3.66", "코로나 영향", "down"), unsafe_allow_html=True)
        with c3:
            st.markdown(kpi_card("팔달구 (2025)", "81.73", "vs 전국 75.0", "up"), unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)
        section_title("CCI 시계열")
        
        fig = make_subplots(specs=[[{"secondary_y": True}]])
        fig.add_trace(go.Scatter(x=df['개최년도'], y=df['전국평균'], name='전국평균',
            mode='lines+markers', line=dict(color="#A6A6A6", width=3),
            marker=dict(size=10)), secondary_y=False)
        fig.add_trace(go.Scatter(x=df['개최년도'], y=df['팔달구'], name='팔달구',
            mode='lines+markers+text', line=dict(color=PRIMARY, width=3),
            marker=dict(size=10), text=df['팔달구'].round(1), textposition='top center'),
            secondary_y=False)
        fig.add_trace(go.Bar(x=df['개최년도'], y=df['CCI'], name='CCI Gap',
            marker_color=SUCCESS, opacity=0.5), secondary_y=True)
        fig.update_yaxes(title_text="점수 (전국/팔달구)", secondary_y=False)
        fig.update_yaxes(title_text="CCI Gap", secondary_y=True, range=[0, 10])
        st.plotly_chart(style_fig(fig, height=420), use_container_width=True)

        # CCI Gap 4지표
        section_title("CCI 4개 지표 분해")
        gap = marts['mart_3-2_CCI_Gap분석']
        if '지표명' in gap.columns and '연도' in gap.columns:
            fig = go.Figure()
            indicators = gap['지표명'].unique()
            colors_map = {0: PRIMARY, 1: ACCENT, 2: SUCCESS, 3: DANGER}
            for i, ind in enumerate(indicators):
                sub = gap[gap['지표명'] == ind].sort_values('연도')
                val_col = [c for c in sub.columns if 'gap' in c.lower() or 'CCI' in c.lower()]
                if val_col:
                    fig.add_trace(go.Scatter(x=sub['연도'], y=sub[val_col[0]], name=ind,
                        mode='lines+markers', line=dict(color=colors_map.get(i, PRIMARY), width=2),
                        marker=dict(size=8)))
            fig.add_hline(y=0, line_dash="dot", line_color="rgba(0,0,0,0.3)",
                annotation_text="전국평균")
            st.plotly_chart(style_fig(fig, height=380), use_container_width=True)
        
        insight_box(
            "✓ 인사이트 4: 관광 경쟁력 상승세 지속",
            "CCI가 2020년 +3.93에서 2025년 +6.75로 꾸준히 상승. 팔달구가 전국평균보다 더 빠른 속도로 성장.",
            "success"
        )

    # =========================================================================
    # PART 6 — 페르소나
    # =========================================================================
    elif page.startswith("6️⃣"):
        section_title("PART 6. 성/연령별 페르소나 분석")
        
        df = marts['mart_3-1e_축제_성연령분포']
        
        c1, c2, c3 = st.columns(3)
        with c1:
            st.markdown(kpi_card("20대 여성", "11.2%", "단일 최대", "up"), unsafe_allow_html=True)
        with c2:
            st.markdown(kpi_card("MZ세대 (20-30대)", "36.8%", "핵심 타겟", "up"), unsafe_allow_html=True)
        with c3:
            st.markdown(kpi_card("시니어 (60+)", "23.8%", "편의 배려", "neutral"), unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)
        col1, col2 = st.columns(2)
        
        with col1:
            section_title("연령대 × 성별")
            if '연령대' in df.columns and '성별' in df.columns:
                pivot = df.pivot_table(index='연령대', columns='성별', values='비율', aggfunc='sum')
                fig = go.Figure()
                if '여성' in pivot.columns:
                    fig.add_trace(go.Bar(y=pivot.index, x=pivot['여성'], name='여성',
                        orientation='h', marker_color=ACCENT))
                if '남성' in pivot.columns:
                    fig.add_trace(go.Bar(y=pivot.index, x=pivot['남성'], name='남성',
                        orientation='h', marker_color=PRIMARY))
                fig.update_layout(barmode='group')
                st.plotly_chart(style_fig(fig, height=400), use_container_width=True)
        
        with col2:
            section_title("외국인 국가별 비중 (2025)")
            ext = marts['mart_3-1b_외국인Top6']
            if '연도' in ext.columns:
                latest = ext[ext['연도'] == ext['연도'].max()]
                fig = go.Figure(go.Pie(labels=latest['국가'], values=latest['방문자_비율_퍼센트'],
                    hole=0.4, marker=dict(colors=[PRIMARY, ACCENT, SUCCESS, WARNING, DANGER, "#9F7AEA"])))
                st.plotly_chart(style_fig(fig, height=400), use_container_width=True)
        
        # 페르소나별 추천
        section_title("페르소나별 추천 관광지")
        per = marts['mart_3-1_페르소나별추천관광지']
        if '페르소나' in per.columns:
            persona_list = per['페르소나'].unique()
            sel_p = st.selectbox("페르소나 선택", persona_list)
            sub = per[per['페르소나'] == sel_p].nlargest(10, '페르소나_적합도점수' if '페르소나_적합도점수' in per.columns else per.columns[-1])
            score_col = '페르소나_적합도점수' if '페르소나_적합도점수' in sub.columns else sub.columns[-1]
            fig = go.Figure(go.Bar(y=sub['관광지명'][::-1], x=sub[score_col][::-1],
                orientation='h', marker_color=PRIMARY,
                text=sub[score_col][::-1].round(1), textposition='outside'))
            st.plotly_chart(style_fig(fig, height=400), use_container_width=True)

    # =========================================================================
    # PART 7 — FSI
    # =========================================================================
    elif page.startswith("7️⃣"):
        section_title("PART 7. FSI 축제성공도 종합 스코어카드")
        
        df = marts['mart_7_FSI스코어카드'].sort_values('개최년도')
        
        c1, c2, c3, c4, c5, c6 = st.columns(6)
        for i, (_, r) in enumerate(df.iterrows()):
            grade = r['FSI_등급']
            color = "up" if grade == 'A' else ("down" if grade == 'C' else "neutral")
            with [c1, c2, c3, c4, c5, c6][i]:
                st.markdown(kpi_card(f"{int(r['개최년도'])}", f"{r['FSI']}", grade, color),
                    unsafe_allow_html=True)
        
        st.markdown("<br>", unsafe_allow_html=True)
        col1, col2 = st.columns([1.3, 1])
        
        with col1:
            section_title("FSI 등급 시계열")
            fig = go.Figure()
            colors_g = [DANGER if g=='C' else (WARNING if g=='B' else SUCCESS) for g in df['FSI_등급']]
            fig.add_trace(go.Bar(x=df['개최년도'], y=df['FSI'], marker_color=colors_g,
                text=df['FSI'].astype(str) + '<br>(' + df['FSI_등급'] + ')',
                textposition='outside', name='FSI'))
            fig.add_hline(y=85, line_dash="dot", line_color=SUCCESS, annotation_text="S등급")
            fig.add_hline(y=75, line_dash="dot", line_color=PRIMARY, annotation_text="A등급")
            fig.add_hline(y=60, line_dash="dot", line_color=WARNING, annotation_text="B등급")
            fig.add_hline(y=50, line_dash="dot", line_color=DANGER, annotation_text="C등급")
            fig.update_yaxes(range=[0, 100])
            st.plotly_chart(style_fig(fig, height=420), use_container_width=True)
        
        with col2:
            section_title("FSI 5차원 분해")
            fig = go.Figure()
            dims = ['방문자_점수', 'FPI_점수', 'FLI_점수', '유입력_점수', '소비_점수']
            colors_d = [PRIMARY, ACCENT, "#9F7AEA", SUCCESS, "#38B2AC"]
            for i, d in enumerate(dims):
                fig.add_trace(go.Bar(x=df['개최년도'], y=df[d], name=d.replace('_점수',''),
                    marker_color=colors_d[i]))
            fig.update_layout(barmode='stack')
            st.plotly_chart(style_fig(fig, height=420), use_container_width=True)
        
        # 등급 표
        section_title("FSI 점수표")
        display = df.copy()
        display.columns = [c.replace('_', ' ') for c in display.columns]
        st.dataframe(display.drop(columns=['연도 날짜'] if '연도 날짜' in display.columns else []),
            hide_index=True, use_container_width=True)

    # =========================================================================
    # PART 8 — 인스타그램 SNS (신규)
    # =========================================================================
    elif page.startswith("8️⃣"):
        section_title("★ PART 8. 인스타그램 SNS 반응 분석", "게시물 293건 + 댓글 분석")
        
        ig = marts['mart_8a_인스타_연도별성과'].sort_values('연도')
        ig = ig[ig['연도'] <= 2025]
        
        c1, c2, c3, c4 = st.columns(4)
        with c1:
            st.markdown(kpi_card("2025 인게이지먼트", "176.3", "사상 최고 +207%", "up"), unsafe_allow_html=True)
        with c2:
            st.markdown(kpi_card("외국어 댓글 (2025)", "23.9%", "vs 1.9% (2024)", "up"), unsafe_allow_html=True)
        with c3:
            st.markdown(kpi_card("총 게시물", "293건", "2022-2026", "neutral"), unsafe_allow_html=True)
        with c4:
            st.markdown(kpi_card("행사후 인게이지먼트", "58.6", "-50% vs 평상시", "down"), unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)
        col1, col2 = st.columns(2)
        with col1:
            section_title("8-A. 인게이지먼트 vs 방문자")
            df_main = marts['mart_1-1_종합지표'].sort_values('개최년도')
            df_main = df_main[df_main['개최년도'].isin(ig['연도'])]
            fig = make_subplots(specs=[[{"secondary_y": True}]])
            fig.add_trace(go.Bar(x=df_main['개최년도'], y=df_main['(전체)방문자수'],
                name='방문자', marker_color=PRIMARY, opacity=0.7), secondary_y=False)
            fig.add_trace(go.Scatter(x=ig['연도'], y=ig['인게이지먼트_평균'],
                name='인게이지먼트', mode='lines+markers+text',
                line=dict(color=ACCENT, width=4), marker=dict(size=12),
                text=ig['인게이지먼트_평균'].round(0), textposition='top center'),
                secondary_y=True)
            fig.update_yaxes(title_text="방문자수", secondary_y=False)
            fig.update_yaxes(title_text="인게이지먼트", secondary_y=True)
            st.plotly_chart(style_fig(fig, height=400), use_container_width=True)

        with col2:
            section_title("8-B. 행사기간별 인게이지먼트 ★")
            ig_b = marts['mart_8b_인스타_행사기간별']
            order = ['평상시', '행사전', '행사중', '행사후']
            agg = ig_b.groupby('행사기간구분')['평균인게이지먼트'].mean().reindex(order)
            colors_b = [PRIMARY, "#4472C4", WARNING, DANGER]
            fig = go.Figure(go.Bar(y=agg.index[::-1], x=agg.values[::-1], orientation='h',
                marker_color=colors_b[::-1], text=agg.values[::-1].round(1),
                textposition='outside'))
            st.plotly_chart(style_fig(fig, height=400), use_container_width=True)

        col1, col2 = st.columns(2)
        with col1:
            section_title("8-C. 외국어 댓글 vs 외국인 방문 ★★")
            df_main2 = marts['mart_1-1_종합지표'].sort_values('개최년도')
            df_main2 = df_main2[df_main2['개최년도'].isin(ig['연도'])]
            fig = make_subplots(specs=[[{"secondary_y": True}]])
            fig.add_trace(go.Bar(x=df_main2['개최년도'], y=df_main2['외국인_비율'],
                name='외국인 비율 (%)', marker_color=PRIMARY, opacity=0.7,
                text=df_main2['외국인_비율'].round(2), textposition='outside'),
                secondary_y=False)
            fig.add_trace(go.Scatter(x=ig['연도'], y=ig['외국어댓글비율_평균'],
                name='외국어 댓글 (%)', mode='lines+markers+text',
                line=dict(color=ACCENT, width=4), marker=dict(size=12),
                text=ig['외국어댓글비율_평균'].round(1).astype(str)+'%',
                textposition='top center'), secondary_y=True)
            fig.update_yaxes(title_text="외국인 비율 (%)", secondary_y=False)
            fig.update_yaxes(title_text="외국어 댓글 (%)", secondary_y=True)
            st.plotly_chart(style_fig(fig, height=400), use_container_width=True)

        with col2:
            section_title("8-D. 해시태그 Top 15")
            tag = marts['mart_8d_인스타_해시태그Top30'].head(15)
            colors_t = [PRIMARY if l == '한글' else ACCENT for l in tag['언어']]
            fig = go.Figure(go.Bar(y=tag['해시태그'][::-1], x=tag['빈도'][::-1],
                orientation='h', marker_color=colors_t[::-1],
                text=tag['빈도'][::-1], textposition='outside'))
            st.plotly_chart(style_fig(fig, height=400), use_container_width=True)

        insight_box("⚠ 인사이트 8 (신규): 행사후 인게이지먼트 -50% 절벽",
            "행사 종료 후 평균 인게이지먼트가 평상시(118.5) 대비 -50%인 58.6으로 급락. 여운 마케팅 부재가 핵심 약점.",
            "danger")
        insight_box("✓ 외국어 댓글 = 외국인 인바운드 선행지표",
            "외국어 댓글 비율(주황선)이 외국인 방문자(파란 막대)보다 시간적으로 선행하는 패턴. 임계점(20%) 도달 시 다음 분기 인프라 확충 필요.",
            "success")

    # =========================================================================
    # PART 9 — 뉴스 담론 (신규)
    # =========================================================================
    elif page.startswith("9️⃣"):
        section_title("★ PART 9. 뉴스 담론 분석", "6,251 문장 → Y활용 322건")
        
        nv = marts['mart_8e_뉴스_영역별평가']
        ng = marts['mart_8g_뉴스_연도별종합']
        
        c1, c2, c3, c4 = st.columns(4)
        with c1:
            st.markdown(kpi_card("2025 긍정 문장", "270건", "+286% vs 2024", "up"), unsafe_allow_html=True)
        with c2:
            st.markdown(kpi_card("외국인 영역 강점", "28건", "전 영역 1위", "up"), unsafe_allow_html=True)
        with c3:
            st.markdown(kpi_card("부정 문장 (총)", "18건", "약점 직접 인용", "down"), unsafe_allow_html=True)
        with c4:
            st.markdown(kpi_card("BI Risk 비율", "33.9%", "↓ vs 35.7%", "up"), unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)
        col1, col2 = st.columns(2)
        with col1:
            section_title("9-A. 영역별 긍정도 매트릭스")
            nv_f = nv[nv['area'] != '기타']
            fig = go.Figure(go.Scatter(x=nv_f['총합'], y=nv_f['긍정도'], mode='markers+text',
                marker=dict(size=nv_f['강점']*2+15, color=nv_f['긍정도'],
                    colorscale=[[0, DANGER], [0.5, WARNING], [1, SUCCESS]], 
                    showscale=False, line=dict(width=2, color='white')),
                text=nv_f['area'], textposition='top center',
                textfont=dict(size=12, color=PRIMARY)))
            fig.add_hline(y=0, line_dash="dot", line_color="rgba(0,0,0,0.3)",
                annotation_text="중립선")
            fig.update_xaxes(title_text="총 언급 수")
            fig.update_yaxes(title_text="긍정도 (강점-문제)")
            st.plotly_chart(style_fig(fig, height=400), use_container_width=True)

        with col2:
            section_title("9-B. 연도별 긍정·부정 vs FSI")
            df_main = marts['mart_1-1_종합지표']
            ng_m = ng.merge(df_main[['개최년도', 'FSI']], left_on='연도', right_on='개최년도', how='left')
            fig = make_subplots(specs=[[{"secondary_y": True}]])
            fig.add_trace(go.Bar(x=ng_m['연도'], y=ng_m['positive_문장수'],
                name='긍정', marker_color=SUCCESS,
                text=ng_m['positive_문장수'], textposition='outside'),
                secondary_y=False)
            fig.add_trace(go.Bar(x=ng_m['연도'], y=ng_m['negative_문장수'],
                name='부정', marker_color=DANGER,
                text=ng_m['negative_문장수'], textposition='outside'),
                secondary_y=False)
            fig.add_trace(go.Scatter(x=ng_m['연도'], y=ng_m['FSI'],
                name='FSI', mode='lines+markers+text', line=dict(color=PRIMARY, width=3),
                marker=dict(size=12), text=ng_m['FSI'].round(1),
                textposition='top center'), secondary_y=True)
            fig.update_yaxes(title_text="문장 수", secondary_y=False)
            fig.update_yaxes(title_text="FSI", secondary_y=True, range=[0, 100])
            fig.update_layout(barmode='group')
            st.plotly_chart(style_fig(fig, height=400), use_container_width=True)

        col1, col2 = st.columns(2)
        with col1:
            section_title("9-C. 부정 문장 직접 인용", "약점 지점 명시")
            neg = marts['mart_8h_뉴스_부정문장']
            for _, r in neg[neg['영역'] != '기타'].head(5).iterrows():
                quote_box(str(r['문장'])[:200], f"[{r['영역']}] {r['언론사']}", negative=True)

        with col2:
            section_title("9-D. 강점 문장 직접 인용", "사회적 인정")
            strong = marts['mart_8i_뉴스_강점문장']
            areas = ['전체'] + list(strong['영역'].unique())
            sel_area = st.selectbox("영역 필터", areas, index=0)
            if sel_area != '전체':
                strong = strong[strong['영역'] == sel_area]
            for _, r in strong.head(5).iterrows():
                quote_box(str(r['문장'])[:200], f"[{r['영역']}] {r['언론사']}")

    # =========================================================================
    # PART 10 — 3중 정합성 (신규)
    # =========================================================================
    elif page.startswith("🔺"):
        section_title("★ PART 10. 3중 데이터 트라이앵글 정합성 검증")
        
        st.markdown("""
        <div class="insight-box">
            <h4>분석 프레임</h4>
            <p>
                <strong>공공데이터</strong> (정량/행동) + <strong>인스타그램</strong> (감성/반응) + <strong>뉴스</strong> (담론/평가)<br>
                동일 가설을 세 데이터로 동시 검증하여 신뢰도 극대화
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        section_title("인사이트별 3중 검증 매트릭스")
        verify_data = pd.DataFrame({
            '인사이트': ['1. 양·질 괴리', '2. FLI 감소', '★ 3. 외국인 블루오션', '4. CCI 상승', '5. 소비 개선', '6. MZ 핵심'],
            '공공': ['✓ 강함', '✓', '✓✓', '✓', '✓', '✓'],
            'SNS': ['✗ 반대', '✓', '✓✓', '△ 간접', '(N/A)', '✓✓'],
            '뉴스': ['△ 중립', '✓ 부정 2건', '✓✓', '✓', '✓ 604억원', '△'],
            '종합': ['△ 재해석 필요', '✓ 입증', '✓✓ 강력 입증', '✓ 입증', '✓ 입증', '✓ 입증']
        })
        st.dataframe(verify_data, hide_index=True, use_container_width=True)
        
        st.markdown("<br>", unsafe_allow_html=True)
        section_title("외국인 블루오션 — 3중 입증 ★★", "공공 + SNS + 뉴스 한 화면")
        
        ig = marts['mart_8a_인스타_연도별성과']
        ig = ig[ig['연도'] <= 2025]
        df_main = marts['mart_1-1_종합지표'].sort_values('개최년도')
        df_main = df_main[df_main['개최년도'].isin(ig['연도'])]
        
        nf = marts['mart_8f_뉴스_연도감성영역']
        if '영역' in nf.columns:
            ext_news = nf[nf['영역'] == '외국인'].groupby('연도')['건수'].sum().reset_index()
        else:
            ext_news = pd.DataFrame({'연도': [2024, 2025], '건수': [4, 31]})
        
        fig = make_subplots(specs=[[{"secondary_y": True}]])
        fig.add_trace(go.Bar(x=df_main['개최년도'], y=df_main['외국인_비율'],
            name='[공공] 외국인 비율 (%)', marker_color=PRIMARY, opacity=0.7,
            text=df_main['외국인_비율'].round(2).astype(str)+'%',
            textposition='outside'), secondary_y=False)
        fig.add_trace(go.Scatter(x=ig['연도'], y=ig['외국어댓글비율_평균'],
            name='[SNS] 외국어 댓글 (%)', mode='lines+markers',
            line=dict(color=ACCENT, width=4), marker=dict(size=14)), secondary_y=True)
        fig.add_trace(go.Scatter(x=ext_news['연도'], y=ext_news['건수'],
            name='[뉴스] 외국인 영역 건수', mode='lines+markers',
            line=dict(color=SUCCESS, width=4, dash='dot'), marker=dict(size=14)), secondary_y=True)
        fig.update_yaxes(title_text="외국인 방문 비율 (%)", secondary_y=False)
        fig.update_yaxes(title_text="외국어 댓글 % / 뉴스 건수", secondary_y=True)
        st.plotly_chart(style_fig(fig, height=450), use_container_width=True)
        
        col1, col2, col3 = st.columns(3)
        with col1:
            insight_box("[공공] 외국인 +1,258%", "2022년 463명 → 2025년 6,289명. 절대 규모는 미미하나 폭발적 성장.", "success")
        with col2:
            insight_box("[SNS] 외국어 댓글 +1,158%", "2024년 1.9% → 2025년 23.9% 폭등. 외국인 인바운드 선행지표.", "success")
        with col3:
            insight_box("[뉴스] 외국인 강점 28건", "전 영역 1위. 부정 0건. 글로벌 축제로 자리매김 인정.", "success")
        
        st.markdown("<br>", unsafe_allow_html=True)
        section_title("새로 발견된 약점 3가지", "보고서 본문 미언급")
        
        col1, col2, col3 = st.columns(3)
        with col1:
            insight_box("1. 행사후 SNS -50% 급락",
                "평상시 118.5 → 행사후 58.6. 여운 마케팅 부재. 행사 후 1개월간 애프터 콘텐츠 필요.",
                "danger")
        with col2:
            insight_box("2. 지역연계·편의안내 강점 0건",
                "뉴스 7개 영역 중 두 영역만 강점 0건. 화성행궁 집중 + 안내 시스템 약화.",
                "danger")
        with col3:
            insight_box("3. 외국어 댓글 선행지표",
                "외국어 댓글이 외국인 방문보다 시간적으로 선행. 임계점 20% 시 인프라 확충.",
                "warning")

    # =========================================================================
    # PART 11 — 인사이트 & 전략
    # =========================================================================
    elif page.startswith("💡"):
        section_title("PART 11. 핵심 인사이트 & 전략 제언")
        
        tab1, tab2 = st.tabs(["💡 인사이트 8개", "🎯 전략 8개"])
        
        with tab1:
            insights = [
                ("1. 양적 성장 vs 질적 성장의 괴리", 
                 "2025년 총 방문자 56.7만명으로 역대 최다이나, 일평균은 2023년(86,351명) 대비 -17.9%. 일평균 KPI 관리가 필수.",
                 "warning"),
                ("2. 축제 리프트 효과 감소 추세",
                 "FLI 2023년 +42.4% → 2025년 +21.1%로 하락. 뉴스의 '콘텐츠 다양성 부족' 등 외부 증언과 일치.",
                 "warning"),
                ("★ 3. 외국인 관광 블루오션 (3중 입증)",
                 "외국인 +1,258%, 외국어 댓글 +1,158%, 뉴스 강점 28건. 가장 강력한 신호.",
                 "success"),
                ("4. 관광 경쟁력 상승세 지속",
                 "CCI 2020년 +3.93 → 2025년 +6.75 사상 최고. 팔달구 구조적 강화.",
                 "success"),
                ("5. 관광소비 지표의 대폭 개선",
                 "축제기간 관광소비 0.366(2024) → 0.659(2025). 뉴스 '604억원' 인용 뒷받침.",
                 "success"),
                ("6. MZ세대 핵심 타겟 확인",
                 "20~30대 36.8%, 인스타 한글 해시태그 Top 10 모두 차지.",
                 "info"),
                ("7. (신규) SNS 화제성과 방문 성과의 비대칭",
                 "2023년 방문 정점이지만 SNS 저점, 2025년 SNS 정점이지만 일평균 하락. 비대칭 구조.",
                 "danger"),
                ("8. (신규) 행사후 인게이지먼트 -50% 절벽",
                 "여운 마케팅 부재로 다음 해 모멘텀 연결 실패.",
                 "danger"),
            ]
            for title, content, type_ in insights:
                insight_box(title, content, type_)
        
        with tab2:
            strategies = [
                ("1. 일평균 방문자 밀도 극대화",
                 "축제 기간 확대보다 핵심 프로그램 집중 편성. 3~4일 핵심 + 전후 연계 → 일평균 90,000명 목표.",
                 "info"),
                ("2. 인바운드 관광 5% 돌파",
                 "외국인 비율 1.11% → 5% 목표. K-컬처 연계, 다국어 안내, 외국인 특화 콘텐츠.",
                 "info"),
                ("3. 체류시간-소비 연계 강화",
                 "야간 프로그램 확대, 맛집 코스 개발, 문화재 야간 개장 → 1인당 7만원+ 목표.",
                 "info"),
                ("4. MZ세대 집중 공략",
                 "SNS 포토스팟, 인플루언서 협업, 20대 여성 타겟 마케팅.",
                 "info"),
                ("5. 데이터 기반 운영 체계 구축",
                 "실시간 모니터링, 히트맵 동선 최적화, AI 수요예측 모델.",
                 "info"),
                ("★ 6. (신규) 행사후 여운 마케팅",
                 "행사 후 1개월 애프터무비, Best Moments 영상, 인플루언서 후기 캠페인.",
                 "success"),
                ("★ 7. (신규) 지역연계·편의안내 정책 신설",
                 "행궁동·팔달문 시장 연계, 스탬프 투어, AI 챗봇·다국어 안내 시스템.",
                 "success"),
                ("★ 8. (신규) 외국어 댓글 모니터링 시스템",
                 "월별 외국어 댓글 비율 추적. 임계점 20% 도달 시 다음 분기 인프라 사전 확충.",
                 "success"),
            ]
            for title, content, type_ in strategies:
                insight_box(title, content, type_)
