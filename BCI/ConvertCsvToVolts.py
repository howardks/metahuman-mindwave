import pandas as pd

def convert(df):
    const = 1.8 / 4096 / 2000
    df[['delta','theta','lowAlpha','highAlpha','lowBeta','highBeta','lowGamma','highGamma']] = df[['delta','theta','lowAlpha','highAlpha','lowBeta','highBeta','lowGamma','highGamma']].apply(lambda x: x * const, axis=1)
    return df

if __name__ == '__main__':
    print('Input user number: ')
    userNum = input()

    # Read in and cleanup baseline file
    df = pd.read_csv('BCI//Data//{0}_baseline.csv'.format(userNum))
    df.rename(columns={'Unnamed: 0': 'timeStamp'}, inplace=True)
    df.set_index("timeStamp", inplace=True)
    
    # Convert baseline file
    df = convert(df)
    df.to_csv('BCI//Data//ConvertedToVolts//{0}_baseline.csv'.format(userNum))

    # Loop to convert trial files
    for i in range(1, 13):
        # Read in and cleanup trial file
        df = pd.read_csv('BCI//Data//{0}_trial_{1}.csv'.format(userNum, i))
        df.rename(columns={'Unnamed: 0': 'timeStamp'}, inplace=True)
        df.set_index("timeStamp", inplace=True)

        # Convert trial file
        df = convert(df)
        df.to_csv('BCI//Data//ConvertedToVolts//{0}_trial_{1}.csv'.format(userNum, i))