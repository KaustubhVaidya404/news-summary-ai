import streamlit as st

import plotly.express as px
import plotly.graph_objects as go

from utils import expose

st.title(":blue[Akaike News AI] :newspaper:")
st.text("👉 The news articles belongs to Time of India")
st.text("👉 This project is only for educational purposes")

company_name_input = st.text_input("Company Name", "Tesla")

score, articles = expose(company_name_input)

max_sentiment = max(score, key=score.get)

with st.container():

    if max_sentiment == 'positive':
        st.subheader(f":green[{max_sentiment}] 📈")
    elif max_sentiment == 'negative':
        st.subheader(f":red[{max_sentiment}] 📉")
    else:
        st.subheader(f":grey[{max_sentiment}] 😑")

    score_data = {
        "key": ['positive', 'negative', "neutral"],
        "value": [score['positive'], score['negative'], score['neutral']]
    }

    figure = px.pie(
        names=score_data['key'],
        values=score_data['value'],
        title="Comparative Sentiment Analysis Report"
    )

    st.plotly_chart(figure)

    for article in articles:
        st.subheader(f":blue[{article['title']}]")
        st.caption(article['date'])
        st.subheader(article['summary'])
        with st.container():
            categories = ["Negative", "Neutral", "Positive", "Compound"]
            values = [article['sentiment']['neg'], article['sentiment']['neu'], article['sentiment']['pos'], article['sentiment']['compound']]
            fig = go.Figure(
                data = go.Scatterpolar(
                    r=values,
                    theta=categories,
                    fill='toself'
                )
            )
            fig.update_layout(
                polar=dict(
                    radialaxis=dict(
                        visible=True,
                        range=[-1, 1]
                    )
                ),
                showlegend=False,
                title="Sentiment Redar Chart"
            )
            st.plotly_chart(fig)
        st.divider()
