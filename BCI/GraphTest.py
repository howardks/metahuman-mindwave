import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

def create_linegraph(dataf):
    plt.plot(dataf['delta'], color='red', label='delta')
    plt.plot(dataf['theta'], color='orange', label='theta')
    plt.plot(dataf['lowAlpha'], color='yellow', label='low alpha')
    plt.plot(dataf['highAlpha'], color='green', label='high alpha')
    plt.plot(dataf['lowBeta'], color='blue', label='low beta')
    plt.plot(dataf['highBeta'], color='indigo', label='high beta')
    plt.plot(dataf['lowGamma'], color='violet', label='low gamma')
    plt.plot(dataf['highGamma'], color='pink', label='high gamma')
    plt.legend()
    plt.title("Mindwave Mobile 2 EEG Wave Quantities")
    plt.xlabel("Time")
    plt.ylabel("Amount")
    plt.show()

def create_plotly(dataf):
    fig = px.line(dataf, title='delta')
    fig.write_html('BCI//Data//wave_data.html', auto_open=True)

if __name__ == '__main__':
    df = pd.read_csv('BCI//Data//test.csv')
    df.drop(['Unnamed: 0', 'attention', 'meditation'], axis=1, inplace=True)
    # create_linegraph(df)
    create_plotly(df)