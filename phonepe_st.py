import streamlit as st
from streamlit_option_menu import option_menu
from PIL import Image
import plotly.express as px
from st_aggrid import AgGrid
import pandas as pd
import numpy as np
import json
import mysql.connector
conn = mysql.connector.connect(host = 'localhost', password = 'Saravanan123', user = 'root', port = 3307, database = 'phonepe')
cursor = conn.cursor()

img = Image.open('C:\\Users\\WELCOME\\OneDrive\\Desktop\\saravanan\\Visual_Studio_Code\\images\\images.jpeg')
st.set_page_config(page_title = 'Phonepe Project', page_icon = img, layout = 'wide')

selected = option_menu('Phonepe Pulse Data Visualization and Exploration', ["Home", "About", "Analysis", 'Visualization','Conclusion'], 
    icons=['house', 'display', "pie-chart-fill", 'map-fill','aspect-ratio-fill'], 
    menu_icon='bar-chart-line-fill', default_index=0, orientation="horizontal",
    styles={
        "container": {"padding": "0!important", "background-color": "#fafafa"},
        "icon": {"color": "violet", "font-size": "15px"}, 
        "nav-link": {"font-size": "20px", "text-align": "center", "margin":"0px", "--hover-color": "#eee"},
        "nav-link-selected": {"background-color": "#6F36AD"},
    }
)

if selected == 'Home':
    st.markdown("## :black[Project Title:]")
    st.markdown("### :violet[Phonepe Pulse Data Visualization and Exploration]")
    st.markdown("## :black[Technologies:]")
    st.markdown("### :violet[Github Cloning, Python, Pandas, MySQL,mysql-connector-python, Streamlit, and Plotly.]")
    st.markdown("## :black[Domain:]")
    st.markdown("### :violet[Fintech]")
    st.markdown("## :black[DataSet:]")
    url = "https://github.com/PhonePe/pulse#readme"
    st.markdown("### :violet[Dataset Link: [Data Link](%s)]"% url)
    url = "https://www.phonepe.com/pulse/explore/transaction/2022/4/"
    st.markdown("### :violet[Inspired From: [PhonePe Pulse](%s)]"% url)

elif selected == 'About':
    img = Image.open('C:\\Users\\WELCOME\\OneDrive\\Desktop\\saravanan\\Visual_Studio_Code\\images\\download.png')
    st.image(img)
    st.markdown("# :violet[Introduction:]")
    st.markdown("#### :violet[The Indian digital payments story has truly captured the world's imagination. From the largest towns to the remotest villages, there is a payments revolution being driven by the penetration of mobile phones, mobile internet and state-of-the-art payments infrastructure built as Public Goods championed by the central bank and the government. Founded in December 2015, PhonePe has been a strong beneficiary of the API driven digitisation of payments in India. When we started, we were constantly looking for granular and definitive data sources on digital payments in India. PhonePe Pulse is our way of giving back to the digital payments ecosystem.]")
    st.markdown("# :violet[Phonepe Pulse | THE BEAT OF PROGRESS :]")
    column1,column2 = st.columns([2,2], gap = 'large')
    with column1:
        st.video('C:\\Users\\WELCOME\\OneDrive\\Desktop\\saravanan\\Visual_Studio_Code\\images\\Introducing PhonePe Pulse.mp4')
    with column2:
        img = Image.open('C:\\Users\\WELCOME\\OneDrive\\Desktop\\saravanan\\Visual_Studio_Code\\images\\phonepe.webp')
        st.image(img)
    st.markdown("# :violet[Guide:]")
    col1,col2 = st.columns([2,2])  
    with col1:
        img1 = Image.open('C:\\Users\\WELCOME\\OneDrive\\Desktop\\saravanan\\Visual_Studio_Code\\images\\aggregated.webp')
        st.image(img1,width=500)
    with col2:
        st.markdown("# :violet[1. Aggregated]")
        st.markdown("## :violet[Aggregated values of various payment categories as shown under Categories section]")
    col1,col2 = st.columns([2,2])  
    with col1:
        img1 = Image.open('C:\\Users\\WELCOME\\OneDrive\\Desktop\\saravanan\\Visual_Studio_Code\\images\\map.webp')
        st.image(img1,width=500)
    with col2:
        st.markdown("# :violet[2. Map]")
        st.markdown("## :violet[Total values at the State and District levels]")
    col1,col2 = st.columns([2,2])  
    with col1:
        img1 = Image.open('C:\\Users\\WELCOME\\OneDrive\\Desktop\\saravanan\\Visual_Studio_Code\\images\\top.webp')
        st.image(img1,width=500)
    with col2:
        st.markdown("# :violet[3. Top]")
        st.markdown("## :violet[Totals of top States / Districts / Postal Codes]")
    url = "https://github.com/PhonePe/pulse/blob/master/LICENSE"
    st.markdown("### :violet[To unleash the power of information and to give back to the ecosystem and the developer community, we decided to open the anonymised aggregate data sets that demystify the what, why and how of digital payments in India. Licensed under the [CDLA-Permissive-2.0 open data license](%s), the PhonePe Pulse Dataset API is a first-of-its-kind open data initiative in the payments space.]"% url)   
        
elif selected == 'Analysis':

    with st.sidebar:
        st.markdown("## :violet[Here is the option to Analyze with specific Year and Quarter 👇🏻 :]")
        year=st.slider(':violet[**Choose a Year**:]',2018,2023)
        qua=st.slider(':violet[**Choose a Quarter**]',1,4)
        qua = f'Q{qua}'
    st.markdown("##### :violet[Select an option 👇🏻 to Analyze the Datas:]")
    choice = st.selectbox('',options = ['Aggregated','Map','Top'])
    st.markdown("")
    st.markdown("")
    st.markdown("")
    
    if choice == 'Aggregated':
        st.markdown("##### :violet[In Aggregated Select an option **(Transaction or User)**:]")
        option = st.radio(label = '', options = ['Transaction','User'])
        st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>',unsafe_allow_html=True)
        if option == 'Transaction':
            st.markdown("")
            st.markdown("")
            st.markdown("") 
            cursor.execute(f"select year,quarter,state,Transaction_Type , sum(Transaction_Count)as total_tran_cnt, sum(transaction_amount)as total_tran_amt from agg_tran where Year = {year} group by state,quarter,Transaction_Type order by state")
            data =[]
            for i in cursor:
                data.append(i)
            df = pd.DataFrame(data=data , columns=['Year','Quarter','State','Transaction_Type','Total_Count','Total_Amount'])
            df['State'] = df['State'].apply(lambda x: x.title().replace('-',' '))
            df['Total_Amount'] = pd.to_numeric(df['Total_Amount'])
            st.markdown("## Total Transaction Amount from all States")
            sunburst = px.sunburst(df,path=['Year','Quarter','State','Total_Amount'],color='Total_Amount',color_continuous_scale='magenta',width = 800,hover_data = 'Transaction_Type')#olor_discrete_sequence=px.colors.qualitative.Plotly_r)
            sunburst.update_layout(margin = dict(t=0,l=0,r=0,b=0))
            # sunburst.update_traces(textinfo='label+percent entry')
            st.plotly_chart(sunburst)

            cursor.execute(f"select year,quarter,state,Transaction_Type, sum(Transaction_Count)as total_tran_cnt, sum(transaction_amount)as total_tran_amt from agg_tran where Year = {year} group by state,quarter,Transaction_Type order by state")
            data =[]
            for i in cursor:
                data.append(i)
            df = pd.DataFrame(data=data , columns=['Year','Quarter','State','Transaction_Type','Total_Count','Total_Amount'])
            df['State'] = df['State'].apply(lambda x: x.title().replace('-',' '))
            df['Total_Count'] = pd.to_numeric(df['Total_Count'])
            st.markdown("## Total Transaction Count from all States")
            st.markdown('')
            st.markdown('')
            sunburst = px.sunburst(df,path=['Year','Quarter','State','Total_Count'],color='Total_Count',color_continuous_scale='magenta',width = 800, hover_data = 'Transaction_Type')
            sunburst.update_layout(margin = dict(t=0,l=0,r=0,b=0))
            # sunburst.update_traces(textinfo='label+percent entry')
            st.plotly_chart(sunburst)
            st.markdown('')
            st.markdown('')

            st.markdown("## Total Transaction Amount with their Transaction Type from all States")
            cursor.execute(f"select year,quarter,Transaction_Type,state, sum(Transaction_Count)as total_tran_cnt, sum(transaction_amount)as total_tran_amt from agg_tran where Year = {year} and Quarter = '{qua}' group by state,quarter,Transaction_Type order by state")
            data =[]
            for i in cursor:
                data.append(i)
            df = pd.DataFrame(data=data , columns=['Year','Quarter','Transaction_Type','State','Total_Count','Total_Amount'])
            df['State'] = df['State'].apply(lambda x: x.title().replace('-',' '))
            df['Total_Amount'] = pd.to_numeric(df['Total_Amount'])
            hist = px.histogram(df, x = 'State',y = 'Total_Amount',color = 'Transaction_Type',width = 1000,height = 600)
            st.plotly_chart(hist)
            st.markdown('')
            st.markdown('')

            st.markdown("## Total Transaction Count with their Transaction Type from all States")
            cursor.execute(f"select year,quarter,Transaction_Type,state, sum(Transaction_Count)as total_tran_cnt, sum(transaction_amount)as total_tran_amt from agg_tran where Year = {year} and Quarter = '{qua}' group by state,quarter,Transaction_Type order by state")
            data =[]
            for i in cursor:
                data.append(i)
            df = pd.DataFrame(data=data , columns=['Year','Quarter','Transaction_Type','State','Total_Count','Total_Amount'])
            df['State'] = df['State'].apply(lambda x: x.title().replace('-',' '))
            df['Total_Count'] = pd.to_numeric(df['Total_Count'])
            hist = px.histogram(df, x = 'State',y = 'Total_Count',color = 'Transaction_Type',width = 1000,height = 600)
            st.plotly_chart(hist)

            st.markdown("## Top Transaction Type with their Transaction Amount")
            cursor.execute("select Transaction_Type, sum(transaction_Amount) as transaction_Amount from phonepe.agg_tran group by Transaction_Type order by transaction_Amount")
            data =[]
            for i in cursor:
                data.append(i)
            df = pd.DataFrame(data=data , columns=['Transaction_Type','Total_Amount'])
            df['Total_Amount'] = pd.to_numeric(df['Total_Amount'])
            pie = px.pie(df,names = 'Transaction_Type', values = 'Total_Amount',width = 900,hole = 0.3)
            st.plotly_chart(pie)
            
            st.markdown("## Top Transaction Type with their Transaction Count")
            cursor.execute("select Transaction_Type, sum(transaction_Count) as transaction_Count from phonepe.agg_tran group by Transaction_Type order by transaction_Count")
            data =[]
            for i in cursor:
                data.append(i)
            df = pd.DataFrame(data=data , columns=['Transaction_Type','Total_Count'])
            df['Total_Count'] = pd.to_numeric(df['Total_Count'])
            pie = px.pie(df,names = 'Transaction_Type', values = 'Total_Count',width = 900,hole = 0.3)
            st.plotly_chart(pie)

        elif option == 'User':
            cursor.execute(f"select year,quarter,state, sum(User_Count)as user_cnt from agg_user where Year = {year} group by state,quarter order by state")
            data =[]
            for i in cursor:
                data.append(i)
            df = pd.DataFrame(data=data , columns=['Year','Quarter','State','User_Count'])
            df['State'] = df['State'].apply(lambda x: x.title().replace('-',' '))
            df['User_Count'] = pd.to_numeric(df['User_Count'])
            st.markdown("# Total User Count from all States")
            st.markdown('')
            st.markdown('')
            sunburst = px.sunburst(df,path=['Year','Quarter','State','User_Count'],color='User_Count',color_continuous_scale='blues',width = 900,height = 500)
            sunburst.update_layout(margin = dict(t=1,l=1,r=1,b=1))
            # sunburst.update_traces(textinfo='label+percent entry')
            st.plotly_chart(sunburst)
            st.markdown('')
            st.markdown('')

            st.markdown("## Total User Count with their Brand from all States")
            cursor.execute(f"SELECT State,year,Quarter,User_Brand,sum(User_Count)as User_Count FROM phonepe.agg_user where Year = {year} and Quarter = '{qua}' group by state,Quarter,User_Brand")
            data = []
            for i in cursor:
                data.append(i)
            df = pd.DataFrame(data=data, columns=['State','year', 'Quarter', 'User_Brand','User_Count'])
            df['State'] = df['State'].apply(lambda x: x.title().replace('-', ' '))
            df['User_Count'] = pd.to_numeric(df['User_Count'])
            hist = px.histogram(df, x='State', y='User_Count', color='User_Brand', width = 950,height = 700)
            # hist = px.histogram(df, x='User_Count', color='User_Brand', width = 950,height = 700)
            st.plotly_chart(hist)
            st.markdown('')
            st.markdown('')

            st.markdown("## Total Number of Users with their Brands")
            cursor.execute(f"SELECT State,year,Quarter,User_Brand,sum(User_Count)as User_Count FROM phonepe.agg_user where Year = {year} and Quarter = '{qua}' group by state,Quarter,User_Brand")
            data = []
            for i in cursor:
                data.append(i)
            df = pd.DataFrame(data=data, columns=['State','year', 'Quarter', 'User_Brand','User_Count'])
            df['State'] = df['State'].apply(lambda x: x.title().replace('-', ' '))
            df['User_Count'] = pd.to_numeric(df['User_Count'])
            hist = px.histogram(df, x='User_Brand', y='User_Count', color='User_Brand', width = 950,height = 600)
            st.plotly_chart(hist)

    elif choice == 'Map':
        st.markdown("##### :violet[In Map Select an option **(Transaction or User)**:]")
        option = st.radio(label = '', options = ['Transaction','User'])
        st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>',unsafe_allow_html=True)
        if option == 'Transaction':
            st.markdown("")
            st.markdown("")
            st.markdown("")
            
            column1,column2 = st.columns([2,2], gap = 'small')
            with column1: 
                cursor.execute(f"select year,quarter,state, sum(Transaction_Count)as total_tran_cnt, sum(transaction_amount)as total_tran_amt from map_tran where Year = {year} group by state,quarter order by state")
                data =[]
                for i in cursor:
                    data.append(i)
                df = pd.DataFrame(data=data , columns=['Year','Quarter','State','Total_Count','Total_Amount'])
                df['State'] = df['State'].apply(lambda x: x.title().replace('-',' '))
                df['Total_Amount'] = pd.to_numeric(df['Total_Amount'])
                st.markdown("### Total Transaction Amount from all States")
                sunburst = px.sunburst(df,path=['Year','Quarter','State','Total_Amount'],color='Total_Amount',color_continuous_scale='speed',width = 500)
                st.plotly_chart(sunburst)
            with column2:
                cursor.execute(f"select year,quarter,state, sum(Transaction_Count)as total_tran_cnt, sum(transaction_amount)as total_tran_amt from agg_tran where Year = {year} group by state,quarter order by state")
                data =[]
                for i in cursor:
                    data.append(i)
                df = pd.DataFrame(data=data , columns=['Year','Quarter','State','Total_Count','Total_Amount'])
                df['State'] = df['State'].apply(lambda x: x.title().replace('-',' '))
                df['Total_Count'] = pd.to_numeric(df['Total_Count'])
                st.markdown("### Total Transaction Count from all States")
                st.markdown('')
                # st.markdown('')
                sunburst = px.sunburst(df,path=['Year','Quarter','State','Total_Count'],color='Total_Count',color_continuous_scale='speed',width = 500)
                # sunburst.update_layout(margin = dict(t=0,l=0,r=0,b=0))
                # sunburst.update_traces(textinfo='label+percent entry')
                st.plotly_chart(sunburst)
            st.markdown('')
            st.markdown('')
            st.markdown('## Total Transaction Amount from all States and their Districts')
            option = st.selectbox('**Select any State to Explore:**',options = ['andaman-&-nicobar-islands','andhra-pradesh','arunachal-pradesh','assam',
                    'bihar','chhattisgarh','chhattisgarh','dadra-&-nagar-haveli-&-daman-&-diu',
                    'delhi','goa','gujarat','haryana','himachal-pradesh','jammu-&-kashmir',
                    'jharkhand','karnataka','kerala','ladakh','lakshadweep','madhya-pradesh',
                    'maharashtra','manipur','meghalaya','mizoram','nagaland','odisha',
                    'puducherry','punjab','rajasthan','sikkim','tamil-nadu','telangana',
                    'tripura','uttar-pradesh','uttarakhand','west-bengal'])

            cursor.execute(f"select year,quarter,state,district, sum(Transaction_Count)as total_tran_cnt, sum(transaction_amount)as total_tran_amt from map_tran where Year = {year} and Quarter = '{qua}' and state = '{option}' group by state,quarter,district order by state")
            data =[]
            for i in cursor:
                data.append(i)
            df = pd.DataFrame(data=data , columns=['Year','Quarter','State','District','Total_Count','Total_Amount'])
            df['State'] = df['State'].apply(lambda x: x.title().replace('-',' '))
            df['Total_Amount'] = pd.to_numeric(df['Total_Amount'])
            hist = px.histogram(df, x = 'District', y = 'Total_Amount', color = 'District',hover_data='State',width = 1000,height = 600,title = f'{option}')
            st.plotly_chart(hist)

            st.markdown("## Total Transaction Count from all States and their Districts")
            cursor.execute(f"select year,quarter,state,district, sum(Transaction_Count)as total_tran_cnt, sum(transaction_amount)as total_tran_amt from map_tran where Year = {year} and Quarter = '{qua}' and state = '{option}' group by state,quarter,district order by state")
            data =[]
            for i in cursor:
                data.append(i)
            df = pd.DataFrame(data=data , columns=['Year','Quarter','State','District','Total_Count','Total_Amount'])
            df['State'] = df['State'].apply(lambda x: x.title().replace('-',' '))
            df['Total_Count'] = pd.to_numeric(df['Total_Count'])
            hist = px.histogram(df, x = 'District', y = 'Total_Count', color = 'District',hover_data='State',width = 1000,height = 600,title = f'{option}')
            st.plotly_chart(hist)
        if option == 'User':
            st.markdown("")
            st.markdown("")

            st.markdown("## Total Registered User from all States")
            cursor.execute(f"select year,quarter,state, sum(Registered_Users)as Registered_Users, sum(App_Opens)as App_Opens from map_user where Year = {year} and Quarter = '{qua}' group by state,quarter order by state")
            data =[]
            for i in cursor:
                data.append(i)
            df = pd.DataFrame(data=data , columns=['Year','Quarter','State','Registered_Users','App_Opens'])
            df['State'] = df['State'].apply(lambda x: x.title().replace('-',' '))
            df['Registered_Users'] = pd.to_numeric(df['Registered_Users'])
            hist = px.histogram(df, x = 'State', y = 'Registered_Users', color = 'State',width = 1000,height = 600)
            st.plotly_chart(hist)

            st.markdown("")
            st.markdown("")
            st.markdown("## Total User App Open frequency from all States")
            cursor.execute(f"select year,quarter,state, sum(Registered_Users)as Registered_Users, sum(App_Opens)as App_Opens from map_user where Year = {year} and Quarter = '{qua}' group by state,quarter order by state")
            data =[]
            for i in cursor:
                data.append(i)
            df = pd.DataFrame(data=data , columns=['Year','Quarter','State','Registered_Users','App_Opens'])
            df['State'] = df['State'].apply(lambda x: x.title().replace('-',' '))
            df['App_Opens'] = pd.to_numeric(df['App_Opens'])
            bar = px.bar(df, x = 'State', y = 'App_Opens', color = 'App_Opens',width = 1000,height = 600,hover_data='App_Opens',color_continuous_scale='dense')
            st.plotly_chart(bar)

            st.markdown("")
            st.markdown("")
            st.markdown("## Total Registered User from all States with their Districts")
            option = st.selectbox('**Select any State to Explore data:**',options = ['andaman-&-nicobar-islands','andhra-pradesh','arunachal-pradesh','assam',
                    'bihar','chhattisgarh','chhattisgarh','dadra-&-nagar-haveli-&-daman-&-diu',
                    'delhi','goa','gujarat','haryana','himachal-pradesh','jammu-&-kashmir',
                    'jharkhand','karnataka','kerala','ladakh','lakshadweep','madhya-pradesh',
                    'maharashtra','manipur','meghalaya','mizoram','nagaland','odisha',
                    'puducherry','punjab','rajasthan','sikkim','tamil-nadu','telangana',
                    'tripura','uttar-pradesh','uttarakhand','west-bengal'])
            cursor.execute(f"select year,quarter,state,district, sum(Registered_Users)as Registered_Users, sum(App_Opens)as App_Opens from map_user where Year = {year} and Quarter = '{qua}' and state = '{option}' group by state,quarter,district order by state")
            data =[]
            for i in cursor:
                data.append(i)
            df = pd.DataFrame(data=data , columns=['Year','Quarter','State','District','Registered_Users','App_Opens'])
            df['State'] = df['State'].apply(lambda x: x.title().replace('-',' '))
            df['Registered_Users'] = pd.to_numeric(df['Registered_Users'])
            hist = px.histogram(df, x = 'District', y = 'Registered_Users', color = 'District',width = 1000,height = 500,title = f'{option}')
            st.plotly_chart(hist)

            st.markdown("")
            st.markdown("")
            st.markdown("## Total User App Open frequency from all States with their Districts")
            cursor.execute(f"select year,quarter,state,district, sum(Registered_Users)as Registered_Users, sum(App_Opens)as App_Opens from map_user where Year = {year} and Quarter = '{qua}' and state = '{option}' group by state,quarter,district order by state")
            data =[]
            for i in cursor:
                data.append(i)
            df = pd.DataFrame(data=data , columns=['Year','Quarter','State','District','Registered_Users','App_Opens'])
            df['State'] = df['State'].apply(lambda x: x.title().replace('-',' '))
            df['App_Opens'] = pd.to_numeric(df['App_Opens'])
            bar = px.bar(df, x = 'District', y = 'App_Opens', color = 'App_Opens',hover_data='App_Opens',width = 1000,height = 500,title = f'{option}',color_continuous_scale='Viridis')
            st.plotly_chart(bar)

    elif choice == 'Top':
        st.markdown("##### :violet[In Top Select an option **(Transaction or User)**:]")
        option = st.radio(label = '', options = ['Transaction','User'])
        st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>',unsafe_allow_html=True)
        if option == 'Transaction':
            st.markdown("")
            st.markdown("")
            st.markdown("")
            column1,column2 = st.columns([2,2], gap = 'large')
            with column1:
                st.markdown("### Top 10 State which contain Total Transaction Amount")
                cursor.execute(f"select year,quarter,state, sum(Transaction_Amount)as Transaction_Amount, sum(Transaction_Count)as Transaction_Count from top_tran_district where Year = {year} and Quarter = '{qua}' group by state,quarter order by Transaction_Amount desc limit 10 ")
                data =[]
                for i in cursor:
                    data.append(i)
                    # print(i)
                df = pd.DataFrame(data=data , columns=['Year','Quarter','State','Transaction_Amount','Transaction_Count'])
                df['State'] = df['State'].apply(lambda x: x.title().replace('-',' '))
                df['Transaction_Amount'] = pd.to_numeric(df['Transaction_Amount'])
                df = df[['State','Transaction_Amount']]
                AgGrid(df,fit_columns_on_grid_load=True)
                pie = px.pie(df, values = 'Transaction_Amount', names = 'State', width = 500,color_discrete_sequence=px.colors.sequential.RdBu)
                st.plotly_chart(pie)
            with column2:
                st.markdown("### Top 10 State which contain Total Transaction Count")
                cursor.execute(f"select year,quarter,state, sum(Transaction_Amount)as Transaction_Amount, sum(Transaction_Count)as Transaction_Count from top_tran_district where Year = {year} and Quarter = '{qua}' group by state,quarter order by Transaction_Count desc limit 10 ")
                data =[]
                for i in cursor:
                    data.append(i)
                df = pd.DataFrame(data=data , columns=['Year','Quarter','State','Transaction_Amount','Transaction_Count'])
                df['State'] = df['State'].apply(lambda x: x.title().replace('-',' '))
                df['Transaction_Count'] = pd.to_numeric(df['Transaction_Count'])
                df = df[['State','Transaction_Count']]
                AgGrid(df,fit_columns_on_grid_load=True)
                pie = px.pie(df, names = 'State', values = 'Transaction_Count',color_discrete_sequence=px.colors.sequential.RdBu,width = 500)
                st.plotly_chart(pie)

            st.markdown("")
            st.markdown("")
            column1,column2 = st.columns([2,2], gap = 'large')
            with column1:
                st.markdown("### Top 10 District which contain Total Transaction Amount")
                cursor.execute(f"select year,quarter,state,district ,sum(Transaction_Amount)as Transaction_Amount, sum(Transaction_Count)as Transaction_Count from top_tran_district where Year = {year} and Quarter = '{qua}' group by state,quarter,district order by Transaction_Amount desc limit 10 ")
                data =[]
                for i in cursor:
                    data.append(i)
                df = pd.DataFrame(data=data , columns=['Year','Quarter','State','District','Transaction_Amount','Transaction_Count'])
                df['State'] = df['State'].apply(lambda x: x.title().replace('-',' '))
                df['Transaction_Amount'] = pd.to_numeric(df['Transaction_Amount'])
                df = df[['State','District','Transaction_Amount']]
                AgGrid(df,fit_columns_on_grid_load=True)
                pie = px.pie(df, names = 'District', values = 'Transaction_Amount', color = 'District',color_discrete_sequence=px.colors.sequential.solar_r,width = 500,hover_name='State')
                st.plotly_chart(pie)
            with column2:
                st.markdown("### Top 10 District which contain Total Transaction Count")
                cursor.execute(f"select year,quarter,state,district ,sum(Transaction_Amount)as Transaction_Amount, sum(Transaction_Count)as Transaction_Count from top_tran_district where Year = {year} and Quarter = '{qua}' group by state,quarter,district order by Transaction_Count desc limit 10 ")
                data =[]
                for i in cursor:
                    data.append(i)
                df = pd.DataFrame(data=data , columns=['Year','Quarter','State','District','Transaction_Amount','Transaction_Count'])
                df['State'] = df['State'].apply(lambda x: x.title().replace('-',' '))
                df['Transaction_Count'] = pd.to_numeric(df['Transaction_Count'])
                df = df[['State','District','Transaction_Count']]
                AgGrid(df,fit_columns_on_grid_load=True)
                pie = px.pie(df, names = 'District', values = 'Transaction_Count', color = 'District',color_discrete_sequence=px.colors.sequential.solar_r,width = 500,hover_name='State')
                st.plotly_chart(pie)
            
            st.markdown("")
            st.markdown("")
            column1,column2 = st.columns([2,2], gap = 'large')
            with column1:
                st.markdown("### Top 10 Pincode which contain Total Transaction Amount")
                cursor.execute(f"select year,quarter,state,Pincode ,sum(Transaction_Amount)as Transaction_Amount, sum(Transaction_Count)as Transaction_Count from top_tran_pincode where Year = {year} and Quarter = '{qua}' group by state,quarter,pincode order by Transaction_Amount desc limit 10 ")
                data =[]
                for i in cursor:
                    data.append(i)
                df = pd.DataFrame(data=data , columns=['Year','Quarter','State','Pincode','Transaction_Amount','Transaction_Count'])
                df['State'] = df['State'].apply(lambda x: x.title().replace('-',' '))
                df['Transaction_Amount'] = pd.to_numeric(df['Transaction_Amount'])
                df = df[['State','Pincode','Transaction_Amount']]
                AgGrid(df,fit_columns_on_grid_load=True)
                pie = px.pie(df, names = 'Pincode', values = 'Transaction_Amount', color = 'Pincode',color_discrete_sequence=px.colors.sequential.Viridis,width = 500,hover_name='State')
                st.plotly_chart(pie)
            with column2:
                st.markdown("### Top 10 Pincode which contain Total Transaction Count")
                cursor.execute(f"select year,quarter,state,Pincode ,sum(Transaction_Amount)as Transaction_Amount, sum(Transaction_Count)as Transaction_Count from top_tran_pincode where Year = {year} and Quarter = '{qua}' group by state,quarter,pincode order by Transaction_Count desc limit 10 ")
                data =[]
                for i in cursor:
                    data.append(i)
                df = pd.DataFrame(data=data , columns=['Year','Quarter','State','Pincode','Transaction_Amount','Transaction_Count'])
                df['State'] = df['State'].apply(lambda x: x.title().replace('-',' '))
                df['Transaction_Count'] = pd.to_numeric(df['Transaction_Count'])
                df = df[['State','Pincode','Transaction_Count']]
                AgGrid(df,fit_columns_on_grid_load=True)
                pie = px.pie(df, names = 'Pincode', values = 'Transaction_Count',color_discrete_sequence=px.colors.sequential.Viridis, color = 'Pincode',width = 500,hover_name='State')
                st.plotly_chart(pie)
            
        if option == 'User':
            st.markdown("")
            st.markdown("")
            st.markdown("")

            st.markdown("## Top 10 State which contain Highest Registered Users")
            col1,col2 = st.columns([2,2], gap = 'large')
            with col1:
                cursor.execute(f"select year,quarter,state, sum(Registered_Users)as Registered_Users from top_user_district where Year = {year} and Quarter = '{qua}' group by state,quarter order by Registered_Users desc limit 10 ")
                data =[]
                for i in cursor:
                    data.append(i)
                df = pd.DataFrame(data=data , columns=['Year','Quarter','State','Registered_Users'])
                df['State'] = df['State'].apply(lambda x: x.title().replace('-',' '))
                df['Registered_Users'] = pd.to_numeric(df['Registered_Users'])
                pie = px.pie(df, names = 'State', values = 'Registered_Users',color_discrete_sequence=px.colors.sequential.matter_r, color = 'State',width = 480)
                st.plotly_chart(pie)
            with col2:
                st.markdown('')
                st.markdown('')
                df = df[['State','Registered_Users']]
                AgGrid(df,fit_columns_on_grid_load=True)
            st.markdown("## Top 10 District which contain Highest Registered Users")
            col1,col2 = st.columns([2,2], gap = 'large')
            with col1:
                cursor.execute(f"select year,quarter,state,district, sum(Registered_Users)as Registered_Users from top_user_district where Year = {year} and Quarter = '{qua}' group by state,quarter,district order by Registered_Users desc limit 10 ")
                data =[]
                for i in cursor:
                    data.append(i)
                df = pd.DataFrame(data=data , columns=['Year','Quarter','State','District','Registered_Users'])
                df['State'] = df['State'].apply(lambda x: x.title().replace('-',' '))
                df['Registered_Users'] = pd.to_numeric(df['Registered_Users'])
                pie = px.pie(df, names = 'District', values = 'Registered_Users',color_discrete_sequence=px.colors.sequential.amp_r, color = 'District',width = 500,hover_name = 'State')
                st.plotly_chart(pie)
            with col2:
                st.markdown('')
                st.markdown('')
                df = df[['State','District','Registered_Users']]
                AgGrid(df,fit_columns_on_grid_load=True)

            st.markdown("## Top 10 Pincode which contain Highest Registered User")
            col1,col2 = st.columns([2,2], gap = 'large')
            with col1:
                cursor.execute(f"select year,quarter,state,Pincode, sum(Registered_Users)as Registered_Users from top_user_pincode where Year = {year} and Quarter = '{qua}' group by state,quarter,pincode order by Registered_Users desc limit 10 ")
                data =[]
                for i in cursor:
                    data.append(i)
                df = pd.DataFrame(data=data , columns=['Year','Quarter','State','Pincode','Registered_Users'])
                df['State'] = df['State'].apply(lambda x: x.title().replace('-',' '))
                df['Registered_Users'] = pd.to_numeric(df['Registered_Users'])
                pie = px.pie(df, names = 'Pincode', values = 'Registered_Users',color_discrete_sequence=px.colors.sequential.Plotly3, color = 'Pincode',width = 450,hover_name = 'State')
                st.plotly_chart(pie)
            with col2:
                st.markdown('')
                st.markdown('')
                df = df[['State','Pincode','Registered_Users']]
                AgGrid(df,fit_columns_on_grid_load=True)
            
elif selected == 'Visualization':
    with st.sidebar:
        st.markdown("## :violet[Here is the option to Analyze with specific Year and Quarter and State 👇🏻 :]")
        year=st.slider(':violet[**Choose a Year**:]',2018,2023)
        qua=st.slider(':violet[**Choose a Quarter**]',1,4)
        qua = f'Q{qua}'
        STATE = st.selectbox(':violet[**Select any State to Explore data:**]',options = ['andaman-&-nicobar-islands','andhra-pradesh','arunachal-pradesh','assam',
                    'bihar','chhattisgarh','chhattisgarh','dadra-&-nagar-haveli-&-daman-&-diu',
                    'delhi','goa','gujarat','haryana','himachal-pradesh','jammu-&-kashmir',
                    'jharkhand','karnataka','kerala','ladakh','lakshadweep','madhya-pradesh',
                    'maharashtra','manipur','meghalaya','mizoram','nagaland','odisha',
                    'puducherry','punjab','rajasthan','sikkim','tamil-nadu','telangana',
                    'tripura','uttar-pradesh','uttarakhand','west-bengal'])
    st.markdown("### :violet[Pick one option 👇🏻 to visualize the data with Geo map of India]")
    option = st.selectbox(label='',options=['1. Total Transaction Amount from all States','2. Total Transaction Count from all States','3. Total Phonepe User Count from all States','4. Total Phonepe User Percentage from all States','5. Total Phonepe Registered User from all States','6. Total Phonepe app open Frequency from all states','7. Total Transaction Amount from all Districts','8. Total Transaction Count from all Districts','9. Total Phonepe Registered User from all Districts','10. Total Phonepe app open Frequency from all Districts'])
    
    if option == '1. Total Transaction Amount from all States':
        st.markdown(f"### :violet[Total Transaction Amount from all States]")
        cursor.execute(f"select state, sum(Transaction_Count)as Transaction_Count, sum(Transaction_Amount)as Transaction_Amount from agg_tran where Year = {year} and Quarter = '{qua}' group by state order by state")
        data = []
        for i in cursor:
            data.append(i)
        df = pd.DataFrame(data=data , columns=['State','Transaction_Count','Transaction_Amount'])
        df['State'] = df['State'].apply(lambda x: x.title().replace('-',' '))
        df['State'] = df['State'].apply(lambda x: x.replace('Andaman & Nicobar Islands','Andaman & Nicobar'))
        df['State'] = df['State'].apply(lambda x: x.replace('Dadra & Nagar Haveli & Daman & Diu','Dadra and Nagar Haveli and Daman and Diu'))
        df['Transaction_Amount'] = pd.to_numeric(df['Transaction_Amount'])
        mini = df['Transaction_Amount'].min()
        maxi = df['Transaction_Amount'].max()
        fig = px.choropleth(
        df,
        geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
        featureidkey='properties.ST_NM',
        locations='State',
        color='Transaction_Amount',
        color_continuous_scale='purd',
        width = 800
        )
        fig.update_geos(fitbounds="locations", visible=False)
        # fig.update_layout(margin={"r":1,"t":1,"l":1,"b":1})
        st.plotly_chart(fig)

        st.markdown(f"### :violet[{'Total Transaction Amount with Specific State'}]")
        cursor.execute(f"select state, sum(Transaction_Count)as Transaction_Count, sum(Transaction_Amount)as Transaction_Amount from agg_tran where Year = {year} and Quarter = '{qua}' and state = '{STATE}' group by state order by state")
        data = []
        for i in cursor:
            data.append(i)
            # print(i)
        df = pd.DataFrame(data=data , columns=['State','Transaction_Count','Transaction_Amount'])
        df['State'] = df['State'].apply(lambda x: x.title().replace('-',' '))
        df['State'] = df['State'].apply(lambda x: x.replace('Andaman & Nicobar Islands','Andaman & Nicobar'))
        df['State'] = df['State'].apply(lambda x: x.replace('Dadra & Nagar Haveli & Daman & Diu','Dadra and Nagar Haveli and Daman and Diu'))
        df['Transaction_Amount'] = pd.to_numeric(df['Transaction_Amount'])
        fig = px.choropleth(
        df,
        geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
        featureidkey='properties.ST_NM',
        locations='State',
        range_color = [mini,maxi],
        color='Transaction_Amount',
        color_continuous_scale='purd',
        width = 800
        )
        fig.update_geos(fitbounds="locations", visible=False)
        # fig.update_layout(margin={"r":1,"t":1,"l":1,"b":1}) 21711613255.0,12532855.0
        st.plotly_chart(fig)

    elif option == '2. Total Transaction Count from all States':
        st.markdown(f"### :violet[Total Transaction Count from all States]")
        cursor.execute(f"select state, sum(Transaction_Count)as Transaction_Count, sum(Transaction_Amount)as Transaction_Amount from agg_tran where Year = {year} and Quarter = '{qua}' group by state order by state")
        data = []
        for i in cursor:
            data.append(i)
        df = pd.DataFrame(data=data , columns=['State','Transaction_Count','Transaction_Amount'])
        df['State'] = df['State'].apply(lambda x: x.title().replace('-',' '))
        df['State'] = df['State'].apply(lambda x: x.replace('Andaman & Nicobar Islands','Andaman & Nicobar'))
        df['State'] = df['State'].apply(lambda x: x.replace('Dadra & Nagar Haveli & Daman & Diu','Dadra and Nagar Haveli and Daman and Diu'))
        df['Transaction_Count'] = pd.to_numeric(df['Transaction_Count'])
        mini = df['Transaction_Count'].min()
        maxi = df['Transaction_Count'].max()
        fig = px.choropleth(
        df,
        geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
        featureidkey='properties.ST_NM',
        locations='State',
        color='Transaction_Count',
        color_continuous_scale='turbid',
        width = 800
        )
        fig.update_geos(fitbounds="locations", visible=False)
        # fig.update_layout(margin={"r":1,"t":1,"l":1,"b":1})
        st.plotly_chart(fig)

        st.markdown(f"### :violet[{'Total Transaction Count with Specific State'}]")
        cursor.execute(f"select state, sum(Transaction_Count)as Transaction_Count, sum(Transaction_Amount)as Transaction_Amount from agg_tran where Year = {year} and Quarter = '{qua}' and state = '{STATE}' group by state order by state")
        data = []
        for i in cursor:
            data.append(i)
        df = pd.DataFrame(data=data , columns=['State','Transaction_Count','Transaction_Amount'])
        df['State'] = df['State'].apply(lambda x: x.title().replace('-',' '))
        df['State'] = df['State'].apply(lambda x: x.replace('Andaman & Nicobar Islands','Andaman & Nicobar'))
        df['State'] = df['State'].apply(lambda x: x.replace('Dadra & Nagar Haveli & Daman & Diu','Dadra and Nagar Haveli and Daman and Diu'))
        df['Transaction_Count'] = pd.to_numeric(df['Transaction_Count'])
        fig = px.choropleth(
        df,
        geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
        featureidkey='properties.ST_NM',
        locations='State',
        range_color = [mini,maxi],
        color='Transaction_Count',
        color_continuous_scale='turbid',
        width = 800
        )
        fig.update_geos(fitbounds="locations", visible=False)
        # fig.update_layout(margin={"r":1,"t":1,"l":1,"b":1}) 21711613255.0,12532855.0
        st.plotly_chart(fig)

    elif option == '3. Total Phonepe User Count from all States':
        st.markdown(f"### :violet[Total Phonepe User Count from all States]")
        cursor.execute(f"select state, sum(User_Count)as User_Count from agg_user where Year = {year} and Quarter = '{qua}' group by state order by state")
        data =[]
        for i in cursor:
            data.append(i)
        df = pd.DataFrame(data=data , columns=['State','User_Count'])
        df['State'] = df['State'].apply(lambda x: x.title().replace('-',' '))
        df['State'] = df['State'].apply(lambda x: x.replace('Andaman & Nicobar Islands','Andaman & Nicobar'))
        df['State'] = df['State'].apply(lambda x: x.replace('Dadra & Nagar Haveli & Daman & Diu','Dadra and Nagar Haveli and Daman and Diu'))
        df['User_Count'] = pd.to_numeric(df['User_Count'])
        mini = df['User_Count'].min()
        maxi = df['User_Count'].max()
        fig = px.choropleth(
        df,
        geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
        featureidkey='properties.ST_NM',
        locations='State',
        color='User_Count',
        color_continuous_scale='dense',
        width = 800
        )
        fig.update_geos(fitbounds="locations", visible=False)
        # fig.update_layout(margin={"r":1,"t":1,"l":1,"b":1})
        st.plotly_chart(fig)

        st.markdown(f"### :violet[{'Total Phonepe User Count from Specific State'}]")
        cursor.execute(f"select state, sum(User_Count)as User_Count from agg_user where Year = {year} and Quarter = '{qua}' and state = '{STATE}' group by state order by state")
        data = []
        for i in cursor:
            data.append(i)
            # print(i)
        df = pd.DataFrame(data=data , columns=['State','User_Count'])
        df['State'] = df['State'].apply(lambda x: x.title().replace('-',' '))
        df['State'] = df['State'].apply(lambda x: x.replace('Andaman & Nicobar Islands','Andaman & Nicobar'))
        df['State'] = df['State'].apply(lambda x: x.replace('Dadra & Nagar Haveli & Daman & Diu','Dadra and Nagar Haveli and Daman and Diu'))
        df['User_Count'] = pd.to_numeric(df['User_Count'])
        fig = px.choropleth(
        df,
        geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
        featureidkey='properties.ST_NM',
        locations='State',
        range_color = [mini,maxi],
        color='User_Count',
        color_continuous_scale='dense',
        width = 800
        )
        fig.update_geos(fitbounds="locations", visible=False)
        # fig.update_layout(margin={"r":1,"t":1,"l":1,"b":1})
        st.plotly_chart(fig)

    elif option == '4. Total Phonepe User Percentage from all States':
        st.markdown(f"### :violet[{'Total Phonepe User Percentage from all States'}]")
        cursor.execute(f"select state, sum(User_Percentage)as User_Percentage from agg_user where Year = {year} and Quarter = '{qua}' group by state order by state")
        data =[]
        for i in cursor:
            data.append(i)
        df = pd.DataFrame(data=data , columns=['State','User_Percentage'])
        df['State'] = df['State'].apply(lambda x: x.title().replace('-',' '))
        df['State'] = df['State'].apply(lambda x: x.replace('Andaman & Nicobar Islands','Andaman & Nicobar'))
        df['State'] = df['State'].apply(lambda x: x.replace('Dadra & Nagar Haveli & Daman & Diu','Dadra and Nagar Haveli and Daman and Diu'))
        df['User_Percentage'] = pd.to_numeric(df['User_Percentage'])
        mini = df['User_Percentage'].min()
        maxi = df['User_Percentage'].max()
        fig = px.choropleth(
        df,
        geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
        featureidkey='properties.ST_NM',
        locations='State',
        color='User_Percentage',
        color_continuous_scale='orrd',
        width = 800
        )
        fig.update_geos(fitbounds="locations", visible=False)
        # fig.update_layout(margin={"r":1,"t":1,"l":1,"b":1})
        st.plotly_chart(fig)

        st.markdown(f"### :violet[{'Total Phonepe User Percentage from Specific State'}]")
        cursor.execute(f"select state, sum(User_Percentage)as User_Percentage from agg_user where Year = {year} and Quarter = '{qua}' and state = '{STATE}' group by state order by state")
        data = []
        for i in cursor:
            data.append(i)
        df = pd.DataFrame(data=data , columns=['State','User_Percentage'])
        df['State'] = df['State'].apply(lambda x: x.title().replace('-',' '))
        df['State'] = df['State'].apply(lambda x: x.replace('Andaman & Nicobar Islands','Andaman & Nicobar'))
        df['State'] = df['State'].apply(lambda x: x.replace('Dadra & Nagar Haveli & Daman & Diu','Dadra and Nagar Haveli and Daman and Diu'))
        df['User_Percentage'] = pd.to_numeric(df['User_Percentage'])
        fig = px.choropleth(
        df,
        geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
        featureidkey='properties.ST_NM',
        locations='State',
        range_color = [mini,maxi],
        color='User_Percentage',
        color_continuous_scale='orrd',
        width = 800
        )
        fig.update_geos(fitbounds="locations", visible=False)
        # fig.update_layout(margin={"r":1,"t":1,"l":1,"b":1}) 21711613255.0,12532855.0
        st.plotly_chart(fig)

    elif option == '5. Total Phonepe Registered User from all States':
        st.markdown(f"### :violet[{'Total Phonepe Registered User from all States'}]")
        cursor.execute(f"SELECT state,sum(Registered_Users)as Registered_Users FROM phonepe.map_user where Year = {year} and Quarter = '{qua}' group by state order by state")
        data =[]
        for i in cursor:
            data.append(i)
        df = pd.DataFrame(data=data , columns=['State','Registered_Users'])
        df['State'] = df['State'].apply(lambda x: x.title().replace('-',' '))
        df['State'] = df['State'].apply(lambda x: x.replace('Andaman & Nicobar Islands','Andaman & Nicobar'))
        df['State'] = df['State'].apply(lambda x: x.replace('Dadra & Nagar Haveli & Daman & Diu','Dadra and Nagar Haveli and Daman and Diu'))
        df['Registered_Users'] = pd.to_numeric(df['Registered_Users'])
        mini = df['Registered_Users'].min()
        maxi = df['Registered_Users'].max()
        fig = px.choropleth(
        df,
        geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
        featureidkey='properties.ST_NM',
        locations='State',
        color='Registered_Users',
        color_continuous_scale='magenta',
        width = 800
        )
        fig.update_geos(fitbounds="locations", visible=False)
        # fig.update_layout(margin={"r":1,"t":1,"l":1,"b":1})
        st.plotly_chart(fig)

        st.markdown(f"### :violet[{'Total Phonepe Registered User from Specific State'}]")
        cursor.execute(f"SELECT state,sum(Registered_Users)as Registered_Users FROM phonepe.map_user where Year = {year} and Quarter = '{qua}' and state = '{STATE}' group by state order by state")
        data =[]
        for i in cursor:
            data.append(i)
        df = pd.DataFrame(data=data , columns=['State','Registered_Users'])
        df['State'] = df['State'].apply(lambda x: x.title().replace('-',' '))
        df['State'] = df['State'].apply(lambda x: x.replace('Andaman & Nicobar Islands','Andaman & Nicobar'))
        df['State'] = df['State'].apply(lambda x: x.replace('Dadra & Nagar Haveli & Daman & Diu','Dadra and Nagar Haveli and Daman and Diu'))
        df['Registered_Users'] = pd.to_numeric(df['Registered_Users'])
        fig = px.choropleth(
        df,
        geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
        featureidkey='properties.ST_NM',
        locations='State',
        color='Registered_Users',
        color_continuous_scale='magenta',
        width = 800,
        range_color = [mini,maxi]
        )
        fig.update_geos(fitbounds="locations", visible=False)
        # fig.update_layout(margin={"r":1,"t":1,"l":1,"b":1})
        st.plotly_chart(fig)

    elif option == '6. Total Phonepe app open Frequency from all states':
        st.markdown(f"### :violet[{'Total Phonepe app open Frequency from all states'}]")
        cursor.execute(f"SELECT state,sum(App_Opens)as App_Opens FROM phonepe.map_user where Year = {year} and Quarter = '{qua}' group by state order by state")
        data =[]
        for i in cursor:
            data.append(i)
        df = pd.DataFrame(data=data , columns=['State','App_Opens'])
        df['State'] = df['State'].apply(lambda x: x.title().replace('-',' '))
        df['State'] = df['State'].apply(lambda x: x.replace('Andaman & Nicobar Islands','Andaman & Nicobar'))
        df['State'] = df['State'].apply(lambda x: x.replace('Dadra & Nagar Haveli & Daman & Diu','Dadra and Nagar Haveli and Daman and Diu'))
        df['App_Opens'] = pd.to_numeric(df['App_Opens'])
        mini = df['App_Opens'].min()
        maxi = df['App_Opens'].max()
        fig = px.choropleth(
        df,
        geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
        featureidkey='properties.ST_NM',
        locations='State',
        color='App_Opens',
        color_continuous_scale='sunset',
        width = 800
        )
        fig.update_geos(fitbounds="locations", visible=False)
        # fig.update_layout(margin={"r":1,"t":1,"l":1,"b":1})
        st.plotly_chart(fig)

        st.markdown(f"### :violet[{'Total Phonepe app open Frequency from Specific states'}]")
        cursor.execute(f"SELECT state,sum(App_Opens)as App_Opens FROM phonepe.map_user where Year = {year} and Quarter = '{qua}' and state = '{STATE}' group by state order by state")
        data =[]
        for i in cursor:
            data.append(i)
        df = pd.DataFrame(data=data , columns=['State','App_Opens'])
        df['State'] = df['State'].apply(lambda x: x.title().replace('-',' '))
        df['State'] = df['State'].apply(lambda x: x.replace('Andaman & Nicobar Islands','Andaman & Nicobar'))
        df['State'] = df['State'].apply(lambda x: x.replace('Dadra & Nagar Haveli & Daman & Diu','Dadra and Nagar Haveli and Daman and Diu'))
        df['App_Opens'] = pd.to_numeric(df['App_Opens'])
        fig = px.choropleth(
        df,
        geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
        featureidkey='properties.ST_NM',
        locations='State',
        color='App_Opens',
        color_continuous_scale='sunset',
        width = 800,
        range_color = [mini,maxi]
        )
        fig.update_geos(fitbounds="locations", visible=False)
        # fig.update_layout(margin={"r":1,"t":1,"l":1,"b":1})
        st.plotly_chart(fig)

    elif option == '7. Total Transaction Amount from all Districts':
        st.markdown(f"### :violet[{'Total Transaction Amount from all Districts in India'}]")
        st.info('Note: In this geo map, It will visualize with total year and quarter not with specifi year and quarter')
        data = pd.read_csv('C:\\Users\\WELCOME\\OneDrive\\Desktop\\lat-&-lon-india-district.csv')
        df = pd.DataFrame(data)
        cursor.execute(f"select State,District, sum(Transaction_Count)as total_tran_cnt, sum(Transaction_Amount)as total_tran_amt from map_tran  group by State,District order by State")
        data1 = []
        for i in cursor:
            data1.append(i)
        df1 = pd.DataFrame(data=data1 , columns=['State','District','Transaction_Count','Transaction_Amount'])
        df1['latitude'] = df['Latitude']
        df1['longitude'] = df['Longitude']
        df1['Transaction_Amount'] = pd.to_numeric(df1['Transaction_Amount'])
        try:
            fig = px.scatter_mapbox(df1,lat='latitude',lon='longitude',zoom=3.3,color='Transaction_Amount',width=900,height=600,hover_name='District',hover_data = 'State',color_continuous_scale='jet',size = 'Transaction_Amount',size_max=40)
            fig.update_layout(mapbox_style='open-street-map')
            fig.update_layout(margin={'r':0,'t':50,'l':0,'b':10})
            fig.update_geos(fitbounds="locations")
            # fig.update_layout(mapbox_bounds={"west": -180, "east": -50, "south": 50, "north": 150})                                                                            
            st.plotly_chart(fig)
        except:
            pass

    elif option == '8. Total Transaction Count from all Districts':
        st.markdown(f"### :violet[{'Total Transaction Count from all Districts in India'}]")
        st.info('Note: In this geo map, It will visualize with total year and quarter not with specifi year and quarter')
        data = pd.read_csv('C:\\Users\\WELCOME\\OneDrive\\Desktop\\lat-&-lon-india-district.csv')
        df = pd.DataFrame(data)
        cursor.execute(f"select State,District, sum(Transaction_Count)as total_tran_cnt, sum(Transaction_Amount)as total_tran_amt from map_tran  group by State,District order by State")
        data1 = []
        for i in cursor:
            data1.append(i)
        df1 = pd.DataFrame(data=data1 , columns=['State','District','Transaction_Count','Transaction_Amount'])
        df1['latitude'] = df['Latitude']
        df1['longitude'] = df['Longitude']
        df1['Transaction_Count'] = pd.to_numeric(df1['Transaction_Count'])
        try:
            fig = px.scatter_mapbox(df1,lat='latitude',lon='longitude',zoom=3.3,color='Transaction_Count',width=900,height=600,hover_name='District',hover_data = 'State',color_continuous_scale='jet',size = 'Transaction_Count',size_max=40)
            fig.update_layout(mapbox_style='open-street-map')
            fig.update_layout(margin={'r':0,'t':50,'l':0,'b':10})
            fig.update_geos(fitbounds="locations")
            # fig.update_layout(mapbox_bounds={"west": -180, "east": -50, "south": 50, "north": 150})                                                                           
            st.plotly_chart(fig)
        except:
            pass
    
    elif option == '9. Total Phonepe Registered User from all Districts':
        st.markdown(f"### :violet[{'Total Phonepe Registered User from all Districts'}]")
        st.info('Note: In this geo map, It will visualize with total year and quarter not with specifi year and quarter')
        data = pd.read_csv('C:\\Users\\WELCOME\\OneDrive\\Desktop\\lat-&-lon-india-district.csv')
        df = pd.DataFrame(data)
        cursor.execute(f"select State,District,sum(Registered_users)as Registered_users,sum(App_Opens)as App_Opens  from map_user group by State,District order by State")
        data1 = []
        for i in cursor:
            data1.append(i)
        df1 = pd.DataFrame(data=data1 , columns=['State','District','Registered_users','App_Opens'])
        df1['latitude'] = df['Latitude']
        df1['longitude'] = df['Longitude']
        df1['Registered_users'] = pd.to_numeric(df1['Registered_users'])
        try:
            fig = px.scatter_mapbox(df1,lat='latitude',lon='longitude',zoom=3.3,color='Registered_users',width=900,height=600,hover_name='District',hover_data = 'State',color_continuous_scale='jet',size = 'Registered_users',size_max=40)
            fig.update_layout(mapbox_style='open-street-map')
            fig.update_layout(margin={'r':0,'t':50,'l':0,'b':10})
            fig.update_geos(fitbounds="locations")
            # fig.update_layout(mapbox_bounds={"west": -180, "east": -50, "south": 50, "north": 150})                                                                            
            st.plotly_chart(fig)
        except:
            pass

    elif option == '10. Total Phonepe app open Frequency from all Districts':
        st.markdown(f"### :violet[{'Total Phonepe app open Frequency from all Districts'}]")
        st.info('Note: In this geo map, It will visualize with total year and quarter not with specifi year and quarter')
        data = pd.read_csv('C:\\Users\\WELCOME\\OneDrive\\Desktop\\lat-&-lon-india-district.csv')
        df = pd.DataFrame(data)
        cursor.execute(f"select State,District,sum(Registered_users)as Registered_users,sum(App_Opens)as App_Opens  from map_user group by State,District order by State")
        data1 = []
        for i in cursor:
            data1.append(i)
        df1 = pd.DataFrame(data=data1 , columns=['State','District','Registered_users','App_Opens'])
        df1['latitude'] = df['Latitude']
        df1['longitude'] = df['Longitude']
        df1['App_Opens'] = pd.to_numeric(df1['App_Opens'])
        try:
            fig = px.scatter_mapbox(df1,lat='latitude',lon='longitude',zoom=3.3,color='App_Opens',width=900,height=600,hover_name='District',hover_data = 'State',color_continuous_scale='jet',size = 'App_Opens',size_max=40)
            fig.update_layout(mapbox_style='open-street-map')
            fig.update_layout(margin={'r':0,'t':50,'l':0,'b':10})
            fig.update_geos(fitbounds="locations")
            # fig.update_layout(mapbox_bounds={"west": -180, "east": -50, "south": 50, "north": 150})                                                                            
            st.plotly_chart(fig)
        except:
            pass

if selected == 'Conclusion':       
    st.markdown("# :violet[Here we Analyzing with overall datas and know explicit details about Phonepe in India]")

    st.markdown('')
    cursor.execute("select sum(Transaction_Amount)as Transaction_Amount,sum(Transaction_Count)as Transaction_Count  from agg_tran where year = 2018")
    year_2018 = cursor.fetchone()
    cursor.execute("select sum(Transaction_Amount)as Transaction_Amount,sum(Transaction_Count)as Transaction_Count  from agg_tran where year = 2019")
    year_2019 = cursor.fetchone()
    cursor.execute("select sum(Transaction_Amount)as Transaction_Amount,sum(Transaction_Count)as Transaction_Count  from agg_tran where year = 2020")
    year_2020 = cursor.fetchone()
    cursor.execute("select sum(Transaction_Amount)as Transaction_Amount,sum(Transaction_Count)as Transaction_Count  from agg_tran where year = 2021")
    year_2021 = cursor.fetchone()
    cursor.execute("select sum(Transaction_Amount)as Transaction_Amount,sum(Transaction_Count)as Transaction_Count  from agg_tran where year = 2022")
    year_2022 = cursor.fetchone()
    cursor.execute("select sum(Transaction_Amount)as Transaction_Amount,sum(Transaction_Count)as Transaction_Count  from agg_tran where year = 2023")
    year_2023 = cursor.fetchone()
    Year = ['2018','2019','2020','2021','2022','2023']
    Total_Amount = [year_2018[0],year_2019[0],year_2020[0],year_2021[0],year_2022[0],year_2023[0]]
    Total_Count = [year_2018[1],year_2019[1],year_2020[1],year_2021[1],year_2022[1],year_2023[1]]

    col1,col2 = st.columns([2,2], gap = 'large')
    with col1:
        hist = px.histogram(x=Year,y=Total_Amount,width = 600,title = 'Comparison of Year vs Overall Transaction Amount in Phonepe')
        st.plotly_chart(hist)
    with col2:
        hist = px.histogram(x=Year,y=Total_Count,width = 600, title = 'Comparison of Year vs Overall Transaction Count in Phonepe')
        st.plotly_chart(hist)


    cursor.execute("select sum(Transaction_Amount)as Transaction_Amount,sum(Transaction_Count)as Transaction_Count  from agg_tran where Quarter = 'Q1'")
    qua_1 = cursor.fetchone()
    cursor.execute("select sum(Transaction_Amount)as Transaction_Amount,sum(Transaction_Count)as Transaction_Count  from agg_tran where Quarter = 'Q2'")
    qua_2 = cursor.fetchone()
    cursor.execute("select sum(Transaction_Amount)as Transaction_Amount,sum(Transaction_Count)as Transaction_Count  from agg_tran where Quarter = 'Q3'")
    qua_3 = cursor.fetchone()
    cursor.execute("select sum(Transaction_Amount)as Transaction_Amount,sum(Transaction_Count)as Transaction_Count  from agg_tran where Quarter = 'Q4'")
    qua_4 = cursor.fetchone()
    Quarter = ['Q1','Q2','Q3','Q4']
    Total_Amount = [qua_1[0],qua_2[0],qua_3[0],qua_4[0]]
    Total_Count = [qua_1[1],qua_2[1],qua_3[1],qua_4[1]]

    col1,col2 = st.columns([2,2], gap = 'large')
    with col1:
        hist = px.histogram(x=Quarter,y=Total_Amount,width = 600, title = 'Comparison of Quarter vs Overall Transaction Amount in Phonepe')
        st.plotly_chart(hist)
    with col2:
        hist = px.histogram(x=Quarter,y=Total_Count,width = 600, title = 'Comparison of Quarter vs Overall Count Amount in Phonepe')
        st.plotly_chart(hist)


    cursor.execute("select sum(User_Count)as User_Count from agg_user where year = 2018")
    year_2018 = cursor.fetchone()
    cursor.execute("select sum(User_Count)as User_Count  from agg_user where year = 2019")
    year_2019 = cursor.fetchone()
    cursor.execute("select sum(User_Count)as User_Count  from agg_user where year = 2020")
    year_2020 = cursor.fetchone()
    cursor.execute("select sum(User_Count)as User_Count  from agg_user where year = 2021")
    year_2021 = cursor.fetchone()
    cursor.execute("select sum(User_Count)as User_Count from agg_user where year = 2022")
    year_2022 = cursor.fetchone()
    cursor.execute("select sum(User_Count)as User_Count from agg_user where year = 2023")
    year_2023 = cursor.fetchone()
    User_Count = [year_2018[0],year_2019[0],year_2020[0],year_2021[0],year_2022[0],year_2023[0]]

    cursor.execute("select sum(Registered_Users)as Registered_User from map_user where year = 2018")
    year_2018 = cursor.fetchone()
    cursor.execute("select sum(Registered_Users)as Registered_User  from map_user where year = 2019")
    year_2019 = cursor.fetchone()
    cursor.execute("select sum(Registered_Users)as Registered_User  from map_user where year = 2020")
    year_2020 = cursor.fetchone()
    cursor.execute("select sum(Registered_Users)as Registered_User  from map_user where year = 2021")
    year_2021 = cursor.fetchone()
    cursor.execute("select sum(Registered_Users)as Registered_User from map_user where year = 2022")
    year_2022 = cursor.fetchone()
    cursor.execute("select sum(Registered_Users)as Registered_User from map_user where year = 2023")
    year_2023 = cursor.fetchone()
    Registered_User = [year_2018[0],year_2019[0],year_2020[0],year_2021[0],year_2022[0],year_2023[0]]

    col1,col2 = st.columns([2,2], gap = 'large')
    with col1:
        hist = px.histogram(x=Year,y=User_Count,width = 600, title = 'Comparison of Year vs Overall User Count of Phonepe App')
        st.plotly_chart(hist)
    with col2:
        hist = px.histogram(x=Year,y=Registered_User,width = 600, title = 'Comparison of Year vs Overall Registered User of Phonepe App')
        st.plotly_chart(hist)


    col1,col2 = st.columns([2,2], gap = 'large')
    with col1:
        cursor.execute("select state, sum(Transaction_Amount)as Transaction_Amount from agg_tran group by state order by Transaction_Amount desc limit 10")
        data = []
        for i in cursor:
            data.append(i)
        df = pd.DataFrame(data,columns = ['state','Transaction_Amount'])
        bar = px.bar(df,x='state',y='Transaction_Amount',width = 600,color = 'state',title = 'Comparison of top State vs Overall Transaction Amount in Phonepe')
        st.plotly_chart(bar)
    with col2:
        cursor.execute("select state, sum(Transaction_Count)as Transaction_Count from agg_tran group by state order by Transaction_Count desc limit 10")
        data = []
        for i in cursor:
            data.append(i)
        df = pd.DataFrame(data,columns = ['state','Transaction_Count'])
        bar = px.bar(df,x='state',y='Transaction_Count',width = 600,color = 'state',title = 'Comparison of top State vs Overall Transaction Count in Phonepe')
        st.plotly_chart(bar)


    col1,col2 = st.columns([2,2], gap = 'large')
    with col1:
        cursor.execute("select district, sum(Transaction_Amount)as Transaction_Amount from map_tran group by district order by Transaction_Amount desc limit 10")
        data = []
        for i in cursor:
            data.append(i)
        df = pd.DataFrame(data,columns = ['district','Transaction_Amount'])
        bar = px.bar(df,x='district',y='Transaction_Amount',width = 600,color = 'district',title = 'Comparison of top District vs Overall Transaction Amount in Phonepe')
        st.plotly_chart(bar)
    with col2:
        cursor.execute("select district, sum(Transaction_Count)as Transaction_Count from map_tran group by district order by Transaction_Count desc limit 10")
        data = []
        for i in cursor:
            data.append(i)
        df = pd.DataFrame(data,columns = ['district','Transaction_Count'])
        bar = px.bar(df,x='district',y='Transaction_Count',width = 600,color = 'district',title = 'Comparison of top District vs Overall Transaction Amount in Phonepe')
        st.plotly_chart(bar)


    col1,col2,col3 = st.columns([2,2,2], gap = 'large')
    with col1:
        cursor.execute("select state, sum(Transaction_Amount)as Transaction_Amount,Transaction_Type from agg_tran where Transaction_Type = 'Merchant payments' group by state order by Transaction_Amount desc limit 5")
        data = []
        for i in cursor:
            data.append(i)
        df = pd.DataFrame(data,columns = ['state','Transaction_Amount','Transaction_Type'])
        pie = px.pie(df,names='state',values='Transaction_Amount',color = 'state',hover_name = 'Transaction_Type',width = 400,title = 'Top State vs Overall Merchant payments')
        st.plotly_chart(pie)
    with col2:
        cursor.execute("select state, sum(Transaction_Amount)as Transaction_Amount,Transaction_Type from agg_tran where Transaction_Type = 'Financial Services' group by state order by Transaction_Amount desc limit 5")
        data = []
        for i in cursor:
            data.append(i)
        df = pd.DataFrame(data,columns = ['state','Transaction_Amount','Transaction_Type'])
        pie = px.pie(df,names='state',values='Transaction_Amount',color = 'state',hover_name = 'Transaction_Type',width = 400,title = 'Top State vs Overall Financial Services')
        st.plotly_chart(pie)
    with col3:
        cursor.execute("select state, sum(Transaction_Amount)as Transaction_Amount,Transaction_Type from agg_tran where Transaction_Type = 'Peer-to-peer payments' group by state order by Transaction_Amount desc limit 5")
        data = []
        for i in cursor:
            data.append(i)
        df = pd.DataFrame(data,columns = ['state','Transaction_Amount','Transaction_Type'])
        pie = px.pie(df,names='state',values='Transaction_Amount',color = 'state',hover_name = 'Transaction_Type',width = 400,title = 'Top State vs Overall Peer-to-peer payments')
        st.plotly_chart(pie)
    col1,col2,col3 = st.columns([2,2,2], gap = 'large')
    with col1:
        cursor.execute("select state, sum(Transaction_Amount)as Transaction_Amount,Transaction_Type from agg_tran where Transaction_Type = 'Recharge & bill payments' group by state order by Transaction_Amount desc limit 5")
        data = []
        for i in cursor:
            data.append(i)
        df = pd.DataFrame(data,columns = ['state','Transaction_Amount','Transaction_Type'])
        pie = px.pie(df,names='state',values='Transaction_Amount',color = 'state',hover_name = 'Transaction_Type',width = 400,title = 'Top State vs Overall Recharge & bill payments')
        st.plotly_chart(pie)
    with col2:
        cursor.execute("select state, sum(Transaction_Amount)as Transaction_Amount,Transaction_Type from agg_tran where Transaction_Type = 'Others' group by state order by Transaction_Amount desc limit 5")
        data = []
        for i in cursor:
            data.append(i)
        df = pd.DataFrame(data,columns = ['state','Transaction_Amount','Transaction_Type'])
        pie = px.pie(df,names='state',values='Transaction_Amount',color = 'state',hover_name = 'Transaction_Type',width = 400,title = 'Top State vs Overall Other payments')
        st.plotly_chart(pie)
    with col3:
        cursor.execute("select sum(Transaction_Amount)as Transaction_Amount,Transaction_Type from agg_tran group by Transaction_Type order by Transaction_Amount desc")
        data = []
        for i in cursor:
            data.append(i)
        df = pd.DataFrame(data,columns = ['Transaction_Amount','Transaction_Type'])
        bar = px.bar(df,x = 'Transaction_Type',y = 'Transaction_Amount',width = 400,title = 'Top Payment Type vs Total Transaction Amount')
        st.plotly_chart(bar)
        conn.close()

    st.markdown("# :violet[ Summarisation of the key find in this project:]")
    st.info("""
    * As we seen in Analysis part, The **Transaction Amount**, **Transaction Count**, and Phonepe App **Registered User** will be increasing year by year.
    * but the Phonepe **User Count** is decreasing, It happen because of unavailability of data in 2022 and 2023.
    * When we analyze in Quarter-wise, The **Transaction Amount** and **Transaction Count** is decreasing, because of **Quarter 4** data were not available in 2023.
    * In **India** country this are the **States** contain huge market in phonepe app they are:                      
    
        **1. Telangana**

        **2. Maharashtra**

        **3. Karnataka**

        **4. Andhra Pradesh**

        **5. Rajasthan**

        **6. Uttar Pradesh**

        **7. Madhya Pradesh**

        **8. Bihar**

        **9. Delhi**
    * In **India** country this are the **Districts** contain huge market in phonepe app they are:

        1. **Bengaluru Urban** from **Karnataka** State.

        2. **Hyderabad** from **Telangana** State.

        3. **Pune** from **Maharashtra** State.

        4. **Jaipur** from **Rajasthan** State.

        5. **RangaReddy** from **Telangana** State.

        6. **Medchal Malkajgiri** from **Telangana** State.

        7. **Central Delhi** from **Delhi** State.
    * In Phone App the top Payment Type is **1. Peer to Peer payments** and **Merchant Payments**. With all this Payment Type there is a three states play major role they are

        **1. Maharashtra** 

        **2. Karnataka**

        **3. Telangana**

    """)
    st.info("* **Suggestion:**  In Phonepe App they make a mistake with giving rewards and offers. They need to analyze with user Transaction Type, Why because Phonepe giving unwanted and unrelated offers,rewards to the users. this may also cause to decrease a user frequency. If they give a useful rewards and offers in festival time or also normal time there will be a chance to growth in Phonepe market")

hide = """
    <style>
    footer {visibility: hidden;}
    #header {visibility: hidden;}
    </style>
    """
st.markdown(hide,unsafe_allow_html = True)       