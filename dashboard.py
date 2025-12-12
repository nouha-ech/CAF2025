import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime


st.set_page_config(
    page_title="🏆 AFCON 2025 Morocco",
    page_icon="⚽",
    layout="wide",
    initial_sidebar_state="collapsed"
)


st.markdown("""
<style>
    :root {
        --primary: #c1272d;
        --dark: #0d0d0d;
        --gray: #1e1e1e;
        --light-gray: #2d2d2d;
        --text: #f0f0f0;
    }
    .stApp {
        background-color: var(--dark);
        color: var(--text);
    }
    h1, h2, h3, h4, h5 {
        color: white !important;
        font-weight: 700;
    }
    .kpi-row .stMetric {
        background: white !important;
        border-radius: 10px !important;
        padding: 16px !important;
        box-shadow: 0 3px 10px rgba(0,0,0,0.08) !important;
        border: 1px solid #eee !important;
    }
    .kpi-row [data-testid="stMetricLabel"] > div {
        color: #333 !important;
        font-weight: 600 !important;
        font-size: 1.1rem !important;
    }
    .kpi-row [data-testid="stMetricValue"] > div {
        color: #c1272d !important;
        font-size: 1.5rem !important;
        font-weight: 800 !important;
    }

    .stMetric {
        background: var(--gray);
        border-radius: 10px;
        padding: 16px;
        box-shadow: 0 4px 8px rgba(0,0,0,0.3);
    }
    .match-card {
        background: var(--light-gray);
        border-radius: 8px;
        padding: 12px;
        margin: 8px 0;
        border-left: 4px solid var(--primary);
    }
    .group-header {
        background: linear-gradient(90deg, var(--primary), #800000);
        color: white;
        padding: 12px;
        border-radius: 8px;
        margin: 16px 0 8px;
        font-weight: bold;
    }
    .flag { font-size: 1.3em; }
    .kpi-row .stMetric {
    background: white !important;
    color: #0d0d0d !important;
    border-radius: 10px !important;
    padding: 16px !important;
    box-shadow: 0 3px 10px rgba(0,0,0,0.08) !important;
    border: 1px solid #eee !important;
}

</style>
""", unsafe_allow_html=True)


@st.cache_data
def load_data():
    try:
        groups = pd.read_csv("groups.csv")
        players = pd.read_csv("players.csv")
        matches = pd.read_csv("matches.csv")
        matches["Date"] = pd.to_datetime(matches["Date"])
        return groups, players, matches
    except:
        
        import io
        groups = pd.read_csv(io.StringIO("""Group,Team,Flag,ISO
A,Morocco,🇲🇦,MA
A,Zambia,🇿🇲,ZM
A,Tunisia,🇹🇳,TN
A,Comoros,🇰🇲,KM"""))
        players = pd.read_csv(io.StringIO("""Rank,Player,Nationality,Club,MarketValue,Flag
1,Bryan Mbeumo,Cameroon,Brentford,75.0,🇨🇲
2,Victor Osimhen,Nigeria,Galatasaray,75.0,🇳🇬"""))
        matches = pd.read_csv(io.StringIO("""Date,Time,Home,Away,Venue,Group,HomeFlag,AwayFlag
2025-12-21,20:00,Morocco,Comoros,Casablanca,A,🇲🇦,🇰🇲"""))
        matches["Date"] = pd.to_datetime(matches["Date"])
        return groups, players, matches

df_groups, df_players, df_matches = load_data()

# ====== HEADER ======
col_logo, col_title = st.columns([1, 5])
with col_logo:
    st.image("https://tmssl.akamaized.net//images/logo/header/afcn.png?lm=1764661339", width=80)
with col_title:
    st.title("🏆 Africa Cup of Nations 2025")
    st.subheader("Morocco • Dec 21, 2025 – Jan 18, 2026")

st.markdown(f"<div style='background:#c1272d;color:white;padding:8px;border-radius:6px;margin:10px 0;'>"
            f"<b>✅ 24 Teams • 6 Groups • 52 Matches • Host: Morocco</b></div>",
            unsafe_allow_html=True)


st.markdown('<div class="kpi-row">', unsafe_allow_html=True)

kpi1, kpi2, kpi3, kpi4 = st.columns(4)
with kpi1:
    st.metric("📱 Teams", "24")
with kpi2:
    st.metric("💰 Avg. Squad Value", "€82.6m")
with kpi3:
    st.metric("⭐ Top MVP", "B. Mbeumo (€75m)")
with kpi4:
    st.metric("🏟️ Venues", "6 Cities")

st.markdown('</div>', unsafe_allow_html=True)
st.markdown("---")


tab_groups, tab_players, tab_matches, tab_analysis = st.tabs([
    "ParallelGroups",
    "⚽ Star Players",
    "📅 Match Schedule",
    "📊 Analytics"
])


with tab_groups:
    st.subheader("ParallelGroups A–F")
    for grp in sorted(df_groups["Group"].unique()):
        teams = df_groups[df_groups["Group"] == grp]
        st.markdown(f'<div class="group-header">Group {grp}</div>', unsafe_allow_html=True)
        cols = st.columns(4)
        for i, (_, row) in enumerate(teams.iterrows()):
            with cols[i % 4]:
                st.markdown(
                    f'<div style="text-align:center;padding:12px;background:#2d2d2d;border-radius:8px;">'
                    f'<div class="flag">{row["Flag"]}</div>'
                    f'<div style="font-weight:bold;margin-top:6px;">{row["Team"]}</div>'
                    f'</div>',
                    unsafe_allow_html=True
                )


with tab_players:
    st.subheader("🌟 Most Valuable Players")
    fig_mv = px.bar(
        df_players,
        x="MarketValue",
        y="Player",
        color="Nationality",
        orientation="h",
        title="Top 7 Most Valuable Players (€m)",
        color_discrete_sequence=px.colors.qualitative.Bold,
        hover_data=["Club", "Flag"]
    )
    fig_mv.update_layout(
        plot_bgcolor="#0d0d0d",
        paper_bgcolor="#0d0d0d",
        font_color="white",
        xaxis_title="Market Value (€m)",
        yaxis=dict(autorange="reversed")
    )
    st.plotly_chart(fig_mv, use_container_width=True)

   
    st.dataframe(
        df_players[["Rank", "Flag", "Player", "Nationality", "Club", "MarketValue"]]
        .rename(columns={"Flag": " ", "MarketValue": "Value (€m)"}),
        use_container_width=True,
        hide_index=True
    )


with tab_matches:
    st.subheader("🗓️ Group Stage Schedule")
    
   
    selected_group = st.selectbox("Filter by Group", ["All"] + sorted(df_groups["Group"].unique()))
    if selected_group != "All":
        df_filt = df_matches[df_matches["Group"] == selected_group]
    else:
        df_filt = df_matches

    for _, row in df_filt.iterrows():
        st.markdown(
            f'''
            <div class="match-card">
                <div style="display:flex;justify-content:space-between;align-items:center;">
                    <div><b>{row["Date"].strftime("%a, %b %d")}</b> • {row["Time"]}</div>
                    <div>{row["Venue"]}</div>
                </div>
                <div style="display:flex;align-items:center;justify-content:center;margin:12px 0;font-size:1.3em;">
                    <span>{row["HomeFlag"]}</span>
                    <span style="margin:0 12px;font-weight:bold;">{row["Home"]}</span>
                    <span style="color:#c1272d;">vs</span>
                    <span style="margin:0 12px;font-weight:bold;">{row["Away"]}</span>
                    <span>{row["AwayFlag"]}</span>
                </div>
                <div style="text-align:right;color:#f0f0f0;">Group {row["Group"]}</div>
            </div>
            ''',
            unsafe_allow_html=True
        )


with tab_analysis:
    st.subheader("📈 Tournament Insights")
    
    col1, col2 = st.columns(2)
    
    with col1:
       
        mv_by_country = df_players.groupby("Nationality").agg(
            MaxValue=("MarketValue", "max"),
            AvgValue=("MarketValue", "mean"),
            Count=("Player", "count")
        ).reset_index()
        # Add flag
        mv_by_country["Flag"] = mv_by_country["Nationality"].map(
            lambda x: df_players[df_players["Nationality"] == x]["Flag"].iloc[0] if not mv_by_country.empty else ""
        )
        mv_by_country["Label"] = mv_by_country["Flag"] + " " + mv_by_country["Nationality"]
        
        fig_country = px.bar(
            mv_by_country,
            x="MaxValue",
            y="Label",
            title="Highest-Valued Player by Nation (€m)",
            color="MaxValue",
            color_continuous_scale="Reds"
        )
        fig_country.update_layout(
            plot_bgcolor="#1e1e1e", paper_bgcolor="#1e1e1e", font_color="white"
        )
        st.plotly_chart(fig_country, use_container_width=True)
    
    with col2:
     
        group_strength = []
        for grp in df_groups["Group"].unique():
            teams = df_groups[df_groups["Group"] == grp]["Team"].tolist()
            mv_sum = df_players[df_players["Nationality"].isin(teams)]["MarketValue"].nlargest(3).sum()
            group_strength.append({"Group": f"Group {grp}", "Strength (€m)": mv_sum})
        df_strength = pd.DataFrame(group_strength)
        
        fig_strength = px.bar(
            df_strength,
            x="Strength (€m)",
            y="Group",
            title="Group Strength (Top 3 Players MV)",
            color="Strength (€m)",
            color_continuous_scale="RdBu_r",
            orientation="h"
        )
        fig_strength.update_layout(
            plot_bgcolor="#1e1e1e", paper_bgcolor="#1e1e1e", font_color="white"
        )
        st.plotly_chart(fig_strength, use_container_width=True)

   
    st.subheader("📆 Match Timeline (Group Stage)")
    df_matches["Start"] = pd.to_datetime(df_matches["Date"].dt.strftime("%Y-%m-%d") + " " + df_matches["Time"])
    df_matches["End"] = df_matches["Start"] + pd.Timedelta(hours=2)
    
    fig_gantt = px.timeline(
        df_matches,
        x_start="Start",
        x_end="End",
        y="Group",
        color="Group",
        title="Match Density by Group",
        hover_data=["Home", "Away", "Venue"]
    )
    fig_gantt.update_yaxes(autorange="reversed")
    fig_gantt.update_layout(
        plot_bgcolor="#0d0d0d", paper_bgcolor="#0d0d0d", font_color="white"
    )
    st.plotly_chart(fig_gantt, use_container_width=True)


st.markdown("---")
st.caption("💡 Data sourced from Transfermarkt & CAF • Dashboard built with Streamlit & Plotly • Updated: Dec 12, 2025")