import pandas as pd
import streamlit as st
import plotly.express as px

#importing Data
data='https://raw.githubusercontent.com/AbineshArumugam/World_Dashboard/main/World.csv'
df=pd.read_csv(data)

#sidebar

page=st.sidebar.radio('select Page ',['Home','Country Comparison','Population','Life Expectancy','GDP per Capita'])

#Title

st.title('World Dashboard')

#Home page

if page=='Home':

    #Filters

    continent_list=st.selectbox('Select Continent',df['continent'].unique())
    country_list=st.selectbox('Select Country',df[df['continent']==continent_list]['country'].unique())
    year_list=st.select_slider('Select Year',list(df['year'].unique()))

    col1,col2,col3= st.columns(3)
    with col1:
        st.markdown('**Population**')
    with col2:
        st.markdown('**Life Expectancy**')
    with col3:
        st.markdown('**GDP Per Capita**')

    col1,col2,col3= st.columns(3)
    with col1:
        st.write(int(df[(df['continent']==continent_list)&(df['country']==country_list)&(df['year']==year_list)]['pop']))
    with col2:
        st.write(round(float(df[(df['continent']==continent_list)&(df['country']==country_list)&(df['year']==year_list)]['lifeExp']),2))
    with col3:
        st.write(round(float(df[(df['continent']==continent_list)&(df['country']==country_list)&(df['year']==year_list)]['gdpPercap']),2))

#country Comparison page
if page=='Country Comparison':

    st.header('Country Comparison')
    col1,col2=st.columns(2)
    with col1:
        continent1=st.selectbox('Select Continent 1',df['continent'].unique())
    with col2:
        continent2=st.selectbox('Select Continent 2',df['continent'].unique())

    col1,col2=st.columns(2)
    with col1:
            country1=st.selectbox('Select Country 1',df[df['continent']==continent1]['country'].unique())
    with col2:
            country2=st.selectbox('Select Country 2',df[df['continent']==continent2]['country'].unique())

    col1,col2=st.columns(2)
    with col1:
            year1=st.select_slider('Select Year 1',list(df['year'].unique()))
    with col2:
            year2=st.select_slider('Select Year 2',list(df['year'].unique()))
    col1,col2,col3= st.columns(3)
    with col1:
        st.markdown('**Population comparison in %**')
    with col2:
        st.markdown('**Life Expectancy comparison in %**')
    with col3:
        st.markdown('**GDP Per Capita comparison in %**')

    col1,col2,col3=st.columns(3)
    with col1:
        p1=int(df[(df['continent']==continent1)&(df['country']==country1)&(df['year']==year1)]['pop'])
        p2=int(df[(df['continent']==continent2)&(df['country']==country2)&(df['year']==year2)]['pop'])
        p=round((((p2-p1)/p1)*100),2)
        st.write(p)
    with col2:
        l1=float(df[(df['continent']==continent1)&(df['country']==country1)&(df['year']==year1)]['lifeExp'])
        l2=float(df[(df['continent']==continent2)&(df['country']==country2)&(df['year']==year2)]['lifeExp'])
        l=round((((l2-l1)/l1)*100),2)
        st.write(l)
    with col3:
        g1=float(df[(df['continent']==continent1)&(df['country']==country1)&(df['year']==year1)]['gdpPercap'])
        g2=float(df[(df['continent']==continent2)&(df['country']==country2)&(df['year']==year2)]['gdpPercap'])
        g=round((((g2-g1)/g1)*100),2)
        st.write(g)

#Population page
if page=='Population':

    st.header('Population Dashboard')
    
    #Filters

    popyear=st.sidebar.select_slider('Year',list(df['year'].unique()))
    popcontinent=st.sidebar.selectbox('Select Continent',df['continent'].unique())
    popcountry=st.sidebar.selectbox('Select Country',df[df['continent']==popcontinent]['country'].unique())

    #pie chart for world Population over years
    p1=df[df['year']==popyear].groupby('continent').sum().reset_index().drop('year',1)
    figp1=px.pie(p1,values='pop',names='continent',color_discrete_sequence=px.colors.sequential.Aggrnyl,title='World Population continent wise')
    st.plotly_chart(figp1)

    #Population Growth
    p2=df[df['country']==popcountry]
    figp2=px.line(p2,x='year',y='pop',markers=True,color_discrete_sequence=px.colors.sequential.Aggrnyl,title='Population growth')
    figp2.update_layout(xaxis=dict(showgrid=False),yaxis=dict(showgrid=False))
    st.plotly_chart(figp2)
    #Top 5 countries based on Population
    p3=df[(df['continent']==popcontinent)&(df['year']==popyear)].sort_values('pop',0,ascending=False).head(5)
    figp3=px.funnel(p3,'pop','country',color_discrete_sequence=px.colors.sequential.Aggrnyl,title='Top 5 Countries')
    figp3.update_layout(xaxis=dict(showgrid=False),yaxis=dict(showgrid=False))
    st.plotly_chart(figp3)

    p4=df.groupby(['continent','year']).sum('pop').reset_index()
    figp4=px.bar(p4,x='year',y='pop',color='continent',color_discrete_sequence=px.colors.sequential.Aggrnyl,title='Population growth over Years')
    st.plotly_chart(figp4)

 # Life Expectancy Page
 
if page == 'Life Expectancy':
    #Filters
    leyear=st.sidebar.select_slider('Year',list(df['year'].unique()))
    lecontinent=st.sidebar.selectbox('Select Continent',df['continent'].unique())
    lecountry=st.sidebar.selectbox('Select Country',df[df['continent']==lecontinent]['country'].unique())

    l1=df[df['year']==leyear].groupby('continent').mean().reset_index().drop('year',1)
    figl1=px.pie(l1,values='lifeExp',names='continent',color_discrete_sequence=px.colors.sequential.Aggrnyl,title='Average life Expectancy')
    st.plotly_chart(figl1)

    l2=df[df['country']==lecountry]
    figl2=px.line(l2,x='year',y='lifeExp',markers=True,color_discrete_sequence=px.colors.sequential.Aggrnyl,title='Life Expactancy Growth')
    figl2.update_layout(xaxis=dict(showgrid=False),yaxis=dict(showgrid=False))
    st.plotly_chart(figl2)

    l3=df[(df['continent']==lecontinent)&(df['year']==leyear)].sort_values('lifeExp',0,ascending=False).head(5)
    figl3=px.funnel(l3,'lifeExp','country',color_discrete_sequence=px.colors.sequential.Aggrnyl,title='Top 5 Countries')
    st.plotly_chart(figl3)
    
    l4=df[df['country']==lecountry]
    figl4=px.scatter(l4,x='pop',y='lifeExp',color_discrete_sequence=px.colors.sequential.Aggrnyl,title='Population Vs Life Expectancy')
    figl4.update_layout(xaxis=dict(showgrid=False),yaxis=dict(showgrid=False))
    st.plotly_chart(figl4)

#GDP per Capita page

if page=='GDP per Capita':
    #Filters
    gdpyear=st.sidebar.select_slider('Year',list(df['year'].unique()))
    gdpcontinent=st.sidebar.selectbox('Select Continent',df['continent'].unique())
    gdpcountry=st.sidebar.selectbox('Select Country',df[df['continent']==gdpcontinent]['country'].unique())

    g1=df[df['year']==gdpyear].groupby('continent').mean().reset_index().drop('year',1)
    figg1=px.pie(g1,values='gdpPercap',names='continent',color_discrete_sequence=px.colors.sequential.Aggrnyl,title='Average GDP prt capita')
    st.plotly_chart(figg1)

    g2=df[df['country']==gdpcountry]
    figg2=px.line(g2,x='year',y='gdpPercap',markers=True,color_discrete_sequence=px.colors.sequential.Aggrnyl,title='GDP per Capita Growth')
    figg2.update_layout(xaxis=dict(showgrid=False),yaxis=dict(showgrid=False))
    st.plotly_chart(figg2)

    g3=df[(df['continent']==gdpcontinent)&(df['year']==gdpyear)].sort_values('gdpPercap',0,ascending=False).head(5)
    figg3=px.funnel(g3,'gdpPercap','country',color_discrete_sequence=px.colors.sequential.Aggrnyl,title='Top 5 Countries')
    st.plotly_chart(figg3)

    g4=df[df['country']==gdpcountry]
    figg4=px.scatter(g4,x='pop',y='gdpPercap',color_discrete_sequence=px.colors.sequential.Aggrnyl,title='Population Vs GDP per Capita')
    figg4.update_layout(xaxis=dict(showgrid=False),yaxis=dict(showgrid=False))
    st.plotly_chart(figg4)