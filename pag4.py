import streamlit as st
import pandas as pd
import plotly.graph_objects as go

def plot_plotly(df,x, y,title):
    n = df[x].values.tolist()
    fig = go.Figure()
    for name in y:
        m = df[name]
        fig.add_trace(go.Scatter(x=n, y=m,
                      mode='lines',#mode='lines+markers',
                      name=name,hoverlabel=dict(namelength=-1)))
    fig.update_layout(
        showlegend=False,
        hovermode = "x",
        #paper_bgcolor = "rgb(0,0,0)" ,
        #plot_bgcolor = "rgb(10,10,10)" , 
        dragmode="pan",
        paper_bgcolor = "rgb(20,20,20)" ,
        plot_bgcolor = "rgb(50,50,50)" ,
        title=dict(
            x = 0.5,
            text = title,
            font=dict(
                size = 20,
                color = "rgb(255,255,255)"
            )
        )
    )
    return fig

def get_increment(df,select):
    incremento = ( df.iloc[-1,:][select] - df.iloc[-2,:][select] ).values # .to_dict()
    dfn = dict()
    for i in range(0,len(incremento)):
        dfn[select[i]] = incremento[i]
    outdf = pd.DataFrame(dfn, index=["Incremento : " + df["data"].values[-1]])
    return outdf

def get_status(df,select):
    data = ( df.iloc[-1,:][select]) # .to_dict()

    dfn = dict()
    for it,its in zip(data.values,select):
        dfn[its] = it 
    outdf = pd.DataFrame(dfn, index=["Situazione : " + df["data"].values[-1]])
    return outdf


def main():
    # st.button("Re-run")
    st.title("Analisi Covid")
    
    st.markdown(
        f"""
        <style>
            .reportview-container .main .block-container{{
                max-width: 65%;
                padding-top: 5px;
                padding-left: 5px;
                padding-right: 5px;
                padding-bottom: 5px;                
            }}
        </style>
        """,
            unsafe_allow_html=True,
        )

    df = pd.read_csv("https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-andamento-nazionale/dpc-covid19-ita-andamento-nazionale.csv")
    df["data"] = [el[0:10] for el in df["data"].values.tolist()]


    select = ["deceduti","totale_casi","dimessi_guariti","variazione_totale_positivi"]
    incremento = get_increment(df,select)
    data = get_status(df,select)
    st.dataframe(data) #, height=366, width=900)
    st.dataframe(incremento) #, height=366, width=900)


    #st.dataframe(df) #, height=366, width=900)
    select = ["deceduti","totale_casi","dimessi_guariti"]
    select_options = st.multiselect('', list(df.keys()), default=select)
    fig = plot_plotly(df,x ="data", y=select_options,title="Andamento Nazionale")    
    st.plotly_chart(fig, use_container_width=True)


    fig = plot_plotly(df,x ="data", y=["deceduti","ricoverati_con_sintomi","variazione_totale_positivi"],title="Deceduti -Ricoverati Con Sintomi  - Variazione Totale Positivi")    
    st.plotly_chart(fig, use_container_width=True)

    fig = plot_plotly(df,x ="data", y=["terapia_intensiva"],title="Terapia Intensiva")    
    st.plotly_chart(fig, use_container_width=True)
    
if __name__ == "__main__":
    main()

