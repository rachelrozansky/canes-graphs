# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.14.4
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

import streamlit as st
import pandas as pd
#import matplotlib.pyplot as plt
from statistics import mean
import matplotlib.pyplot as plt
import altair as alt
import plotly.express as px


@st.cache
def load_data():
    df = pd.read_csv('ticket_sales_3.csv')
    return df


df = pd.read_csv('ticket_sales_3.csv')
df['plan_base_price'] = df['plan_base_price'].astype('int')
type(df['plan_base_price'])

options=['Renewed Full Season', 'Renewed PH Full Season','New PH Full Season', 'New Full Season', 'Renewed Half Season',
        'Renewed Partial Season', 'New Partial Season', 'New Half Season', '\xa0','Platinum PH Full Season']
df=df[df['tickettypesid'].isin(options)]
#df2=df

df['9%']=df['plan_base_price']*1.09
df.loc[df['section_listing'] == 'Row 1', '9%'] = df['plan_base_price']*1.3365
df.loc[df['section_listing'] == 'Row 2', '9%'] = df['plan_base_price']*1.16
df.loc[df['section_listing'] == 'Lower Level North', '9%'] = df['plan_base_price']*1.1672
df.loc[df['section_listing'] == 'Lower Level North Preferred', '9%'] = df['plan_base_price']*1.1852



#col1, col2 = st.columns(2)
#with col1:
    #st.image("canes_map.png", width=350)
#with col2:
    #st.image("legend.png", width = 250)
st.image("canes_map.png", width=700)
st.image("legend.png", width = 250)

# +

df_full=df.loc[df['plan'] == 'Full Season'] 
df_half=df.loc[df['plan'] == 'Half Season'] 
df_partial=df.loc[df['plan'] == 'Partial Season'] 
values_tot= []
values_full= []
values_half= []
values_partial= []
sections_list=[]
for i in df['section_listing'].unique():
    temp_tot = df.loc[df['section_listing'] == i] 
    temp_full = df_full.loc[df['section_listing'] == i] 
    temp_half = df_half.loc[df['section_listing'] == i] 
    temp_partial = df_partial.loc[df['section_listing'] == i] 
    seat_tot=sum(temp_tot['num_seats'])
    seat_full=sum(temp_full['num_seats'])
    seat_half=sum(temp_half['num_seats'])
    seat_partial=sum(temp_partial['num_seats'])
    sections_list.append(i)
    values_tot.append(seat_tot)
    values_full.append(seat_full)
    values_half.append(seat_half)
    values_partial.append(seat_partial)
totals = {
    "Sections" : sections_list,
    "Total_seats" : values_tot,
    "Full_Season_seats" : values_full,
    "Half_Season_seats" : values_half,
    "Partial_Season_seats" : values_partial
}
df_total_revenue = pd.DataFrame(totals)

# +

df_full=df.loc[df['plan'] == 'Full Season'] 
df_half=df.loc[df['plan'] == 'Half Season'] 
df_partial=df.loc[df['plan'] == 'Partial Season'] 
values_tot= []
values_full= []
values_half= []
values_partial= []
sections_list=[]
for i in df['section_listing'].unique():
    temp_tot = df.loc[df['section_listing'] == i] 
    temp_full = df_full.loc[df['section_listing'] == i] 
    temp_half = df_half.loc[df['section_listing'] == i] 
    temp_partial = df_partial.loc[df['section_listing'] == i] 
    seat_tot=sum(temp_tot['FSE'])
    seat_full=sum(temp_full['FSE'])
    seat_half=sum(temp_half['FSE'])
    seat_partial=sum(temp_partial['FSE'])
    sections_list.append(i)
    values_tot.append(seat_tot)
    values_full.append(seat_full)
    values_half.append(seat_half)
    values_partial.append(seat_partial)
totals = {
    "Sections" : sections_list,
    "Total_seats" : values_tot,
    "Full_Season_seats" : values_full,
    "Half_Season_seats" : values_half,
    "Partial_Season_seats" : values_partial
}
df_total_revenue['Total_Seats_per_Game']=values_tot
df_total_revenue['Full_Season_Seats_per_Game']=values_full
df_total_revenue['Half_Season_Seats_per_Game']=values_half
df_total_revenue['Partial_Season_Seats_per_Game']=values_partial
# -

df_full=df.loc[df['plan'] == 'Full Season'] 
df_half=df.loc[df['plan'] == 'Half Season'] 
df_partial=df.loc[df['plan'] == 'Partial Season'] 
values_tot= []
values_full= []
values_half= []
values_partial= []
sections_list=[]
for i in df['section_listing'].unique():
    temp_tot = df.loc[df['section_listing'] == i] 
    temp_full = df_full.loc[df['section_listing'] == i] 
    temp_half = df_half.loc[df['section_listing'] == i] 
    temp_partial = df_partial.loc[df['section_listing'] == i] 
    seat_tot=sum(temp_tot['plan_base_price'])
    seat_full=sum(temp_full['plan_base_price'])
    seat_half=sum(temp_half['plan_base_price'])
    seat_partial=sum(temp_partial['plan_base_price'])
    sections_list.append(i)
    values_tot.append(seat_tot)
    values_full.append(seat_full)
    values_half.append(seat_half)
    values_partial.append(seat_partial)
totals = {
    "Total_Revenue_py" : values_tot,
    "Full_Season_Revenue_py" : values_full,
    "Half_Season_Revenue_py" : values_half,
    "Partial_Season_Revenue_py" : values_partial
}
df_total_revenue['Total_Revenue_per_Season']=values_tot
df_total_revenue['Full_Season_Revenue_per_Season']=values_full
df_total_revenue['Half_Season_Revenue_per_Season']=values_half
df_total_revenue['Partial_Season_Revenue_per_Season']=values_partial

df_full=df.loc[df['plan'] == 'Full Season'] 
df_half=df.loc[df['plan'] == 'Half Season'] 
df_partial=df.loc[df['plan'] == 'Partial Season'] 
values_tot= []
values_full= []
values_half= []
values_partial= []
sections_list=[]
for i in df['section_listing'].unique():
    temp_tot = df.loc[df['section_listing'] == i] 
    temp_full = df_full.loc[df['section_listing'] == i] 
    temp_half = df_half.loc[df['section_listing'] == i] 
    temp_partial = df_partial.loc[df['section_listing'] == i] 
    seat_full=sum(temp_full['plan_base_price'])/41
    seat_half=sum(temp_half['plan_base_price'])/22
    seat_partial=sum(temp_partial['plan_base_price'])/11
    seat_tot=seat_full+seat_half+seat_partial
    sections_list.append(i)
    values_tot.append(seat_tot)
    values_full.append(seat_full)
    values_half.append(seat_half)
    values_partial.append(seat_partial)
totals = {
    "Total_Revenue_py" : values_tot,
    "Full_Season_Revenue_py" : values_full,
    "Half_Season_Revenue_py" : values_half,
    "Partial_Season_Revenue_py" : values_partial
}
df_total_revenue['Total_Revenue_per_Game']=values_tot
df_total_revenue['Full_Season_Revenue_per_Game']=values_full
df_total_revenue['Half_Season_Revenue_per_Game']=values_half
df_total_revenue['Partial_Season_Revenue_per_Game']=values_partial

df_full=df.loc[df['plan'] == 'Full Season'] 
df_half=df.loc[df['plan'] == 'Half Season'] 
df_partial=df.loc[df['plan'] == 'Partial Season'] 
values_tot= []
values_full= []
values_half= []
values_partial= []
sections_list=[]
for i in df['section_listing'].unique():
    temp_tot = df.loc[df['section_listing'] == i] 
    temp_full = df_full.loc[df['section_listing'] == i] 
    temp_half = df_half.loc[df['section_listing'] == i] 
    temp_partial = df_partial.loc[df['section_listing'] == i] 
    seat_full=sum(temp_full['9%'])/41
    seat_half=sum(temp_half['9%'])/22
    seat_partial=sum(temp_partial['9%'])/11
    seat_tot=seat_full+seat_half+seat_partial
    sections_list.append(i)
    values_tot.append(seat_tot)
    values_full.append(seat_full)
    values_half.append(seat_half)
    values_partial.append(seat_partial)
totals = {
    "Total_Revenue_py" : values_tot,
    "Full_Season_Revenue_py" : values_full,
    "Half_Season_Revenue_py" : values_half,
    "Partial_Season_Revenue_py" : values_partial
}
df_total_revenue['New_Total_Revenue_per_Game']=values_tot
df_total_revenue['New_Full_Season_Revenue_per_Game']=values_full
df_total_revenue['New_Half_Season_Revenue_per_Game']=values_half
df_total_revenue['New_Partial_Season_Revenue_per_Game']=values_partial

df_full=df.loc[df['plan'] == 'Full Season'] 
df_half=df.loc[df['plan'] == 'Half Season'] 
df_partial=df.loc[df['plan'] == 'Partial Season'] 
values_tot= []
values_full= []
values_half= []
values_partial= []
sections_list=[]
for i in df['section_listing'].unique():
    temp_tot = df.loc[df['section_listing'] == i] 
    temp_full = df_full.loc[df['section_listing'] == i] 
    temp_half = df_half.loc[df['section_listing'] == i] 
    temp_partial = df_partial.loc[df['section_listing'] == i] 
    seat_full=sum(temp_full['9%'])
    seat_half=sum(temp_half['9%'])
    seat_partial=sum(temp_partial['9%'])
    seat_tot=seat_full+seat_half+seat_partial
    sections_list.append(i)
    values_tot.append(seat_tot)
    values_full.append(seat_full)
    values_half.append(seat_half)
    values_partial.append(seat_partial)
totals = {
    "Total_Revenue_py" : values_tot,
    "Full_Season_Revenue_py" : values_full,
    "Half_Season_Revenue_py" : values_half,
    "Partial_Season_Revenue_py" : values_partial
}
df_total_revenue['New_Total_Revenue_per_Season']=values_tot
df_total_revenue['New_Full_Season_Revenue_per_Season']=values_full
df_total_revenue['New_Half_Season_Revenue_per_Season']=values_half
df_total_revenue['New_Partial_Season_Revenue_per_Season']=values_partial

df_total_revenue = df_total_revenue[:-1]


# +
col1, col2 = st.columns(2)

with col1:
    section = st.multiselect(
        'What Sections would you like to compare?',
        ('Terrace Value', 'Lower Level South', 'Sideline Preferred',
           'Center Ice Top 8', 'Center Ice Terrace', 'Shoot Twice Goal Zone',
           'Center Ice  ', 'Lower Level North Preferred',
           'Center Ice Preferred', 'Mezzanine', 'FanZone', 'Champions Club',
           'Sideline  ', 'Club Ledge', 'Row 1', 'Lower Level South Preferred',
           'Lower Level North', 'Center Ice Club', 'Terrace Preferred',
           'Club Select', 'Row 2', 'Champions Club Preferred'))
with col2:
    attribute = st.selectbox(
        'What attributes would you like to look at?',
        ('Total Revenue per Season','Total Revenue per Game','Total Season Ticket Holders','Number of Season Ticket Holders per Game',)
        )
# -

temp= df_total_revenue.loc[df_total_revenue['Sections'].isin(section)]


if 'Total Season Ticket Holders' in attribute:
    fig = px.bar(temp, x="Sections", y=["Total_seats", "Full_Season_seats", "Half_Season_seats","Partial_Season_seats"], barmode='group', height=400)
    # st.dataframe(df) # if need to display dataframe
    st.plotly_chart(fig)

if 'Total Revenue per Season' in attribute:
    fig = px.bar(temp, x="Sections", y=["Total_Revenue_per_Season", "Full_Season_Revenue_per_Season", 
                                        "Half_Season_Revenue_per_Season","Partial_Season_Revenue_per_Season"], 
                 barmode='group', height=400)
    # st.dataframe(df) # if need to display dataframe
    st.plotly_chart(fig)

if 'Total Revenue per Game' in attribute:
    fig = px.bar(temp, x="Sections", y=["Total_Revenue_per_Game", "Full_Season_Revenue_per_Game", 
                                        "Half_Season_Revenue_per_Game","Partial_Season_Revenue_per_Game"], 
                 barmode='group', height=400)
    # st.dataframe(df) # if need to display dataframe
    st.plotly_chart(fig)

if 'Number of Season Ticket Holders per Game' in attribute:
    fig = px.bar(temp, x="Sections", y=["Total_Seats_per_Game", "Full_Season_Seats_per_Game", 
                                        "Half_Season_Seats_per_Game","Partial_Season_Seats_per_Game"], 
                 barmode='group', height=400)
    # st.dataframe(df) # if need to display dataframe
    st.plotly_chart(fig)

temp2=df_total_revenue
temp2=temp2.sort_values(by=['Total_Revenue_per_Season'])
if st.sidebar.checkbox('Sections (Sorted by Total Revenue)'):
    fig = px.bar(temp2, x="Sections", y='Total_Revenue_per_Season', 
                 barmode='group', height=400)
    st.plotly_chart(fig)

temp2=df_total_revenue
temp2=temp2.sort_values(by=['Total_seats'])
if st.sidebar.checkbox('Sections (Sorted by Total Seats)'):
    fig = px.bar(temp2, x="Sections", y='Total_seats', 
                 barmode='group', height=400)
    st.plotly_chart(fig)

temp2=df_total_revenue
temp2=temp2.sort_values(by=['New_Total_Revenue_per_Season'])
if st.sidebar.checkbox('Sections  (Sorted by New Total Revenue)'):
    fig = px.bar(temp2, x="Sections", y=["Total_Revenue_per_Season","New_Total_Revenue_per_Season"], 
                 barmode='group', height=400)
    st.plotly_chart(fig)

if st.sidebar.checkbox('Pie Chart of Revenue'):
    fig = px.pie(temp2, values='Total_Revenue_per_Season', names='Sections',
                     title='Total Revenue per Season per Section',
                     height=300, width=200)
    fig.update_layout(margin=dict(l=20, r=20, t=30, b=0),)
    st.plotly_chart(fig, use_container_width=True)

# +
col1, col2 = st.columns(2)

with col1:
    section2 = st.multiselect(
        'What Sections would you like to compare?',
        ('Terrace Value', 'Lower Level South', 'Sideline Preferred',
           'Center Ice Top 8', 'Center Ice Terrace', 'Shoot Twice Goal Zone',
           'Center Ice  ', 'Lower Level North Preferred',
           'Center Ice Preferred', 'Mezzanine', 'FanZone', 'Champions Club',
           'Sideline  ', 'Club Ledge', 'Row 1', 'Lower Level South Preferred',
           'Lower Level North', 'Center Ice Club', 'Terrace Preferred',
           'Club Select', 'Row 2', 'Champions Club Preferred', 'Sideline'))
with col2:
    attribute2 = st.selectbox(
        'What attributes would you like to look at?',
        ('New Total Revenue per Season','New Total Revenue per Game')
        )
# -

temp2= df_total_revenue.loc[df_total_revenue['Sections'].isin(section2)]

if 'New Total Revenue per Season' in attribute:
    fig = px.bar(temp2, x="Sections", y=["New_Total_Revenue_per_Season", "New_Full_Season_Revenue_per_Season", 
                                        "New_Half_Season_Revenue_per_Season","New_Partial_Season_Revenue_per_Season"], 
                 barmode='group', height=400)
    # st.dataframe(df) # if need to display dataframe
    st.plotly_chart(fig)

if 'New Total Revenue per Season per Game' in attribute:
    fig = px.bar(temp2, x="Sections", y=["New_Total_Revenue_per_Game", "New_Full_Season_Revenue_per_Game", 
                                        "New_Half_Season_Revenue_per_Game","New_Partial_Season_Revenue_per_Game"], 
                 barmode='group', height=400)
    # st.dataframe(df) # if need to display dataframe
    st.plotly_chart(fig)
