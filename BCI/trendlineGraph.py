import plotly.express as px
import pandas as pd

print('Input user number: ')
userNum = input()

df = pd.read_csv('BCI//Data//ConvertedToVolts//{0}_baseline.csv'.format(userNum))
deltaDf = pd.DataFrame()
thetaDf = pd.DataFrame()
lowAlphaDf = pd.DataFrame()
highAlphaDf = pd.DataFrame()
lowBetaDf = pd.DataFrame()
highBetaDf = pd.DataFrame()
lowGammaDf = pd.DataFrame()
highGammaDf = pd.DataFrame()

deltaDf = pd.concat([df['delta']], axis=1)
deltaDf.rename(columns = {'delta':'Baseline'},  inplace = True)
thetaDf = pd.concat([df['theta']], axis=1)
thetaDf.rename(columns = {'theta':'Baseline'},  inplace = True)
lowAlphaDf = pd.concat([df['lowAlpha']], axis=1)
lowAlphaDf.rename(columns = {'lowAlpha':'Baseline'},  inplace = True)
highAlphaDf = pd.concat([df['highAlpha']], axis=1)
highAlphaDf.rename(columns = {'highAlpha':'Baseline'},  inplace = True)
lowBetaDf = pd.concat([df['lowBeta']], axis=1)
lowBetaDf.rename(columns = {'lowBeta':'Baseline'},  inplace = True)
highBetaDf = pd.concat([df['highBeta']], axis=1)
highBetaDf.rename(columns = {'highBeta':'Baseline'},  inplace = True)
lowGammaDf = pd.concat([df['lowGamma']], axis=1)
lowGammaDf.rename(columns = {'lowGamma':'Baseline'},  inplace = True)
highGammaDf = pd.concat([df['highGamma']], axis=1)
highGammaDf.rename(columns = {'highGamma':'Baseline'},  inplace = True)

for i in range(1, 13):
    df = pd.read_csv('BCI//Data//ConvertedToVolts//{0}_trial_{1}.csv'.format(userNum, i))

    deltaDf = pd.concat([deltaDf, df['delta']], axis=1)
    deltaDf.rename(columns = {'delta':'Trial {0}'.format(i)},  inplace = True)
    thetaDf = pd.concat([thetaDf, df['theta']], axis=1)
    thetaDf.rename(columns = {'theta':'Trial {0}'.format(i)},  inplace = True)
    lowAlphaDf = pd.concat([lowAlphaDf, df['lowAlpha']], axis=1)
    lowAlphaDf.rename(columns = {'lowAlpha':'Trial {0}'.format(i)},  inplace = True)
    highAlphaDf = pd.concat([highAlphaDf, df['highAlpha']], axis=1)
    highAlphaDf.rename(columns = {'highAlpha':'Trial {0}'.format(i)},  inplace = True)
    lowBetaDf = pd.concat([lowBetaDf, df['lowBeta']], axis=1)
    lowBetaDf.rename(columns = {'lowBeta':'Trial {0}'.format(i)},  inplace = True)
    highBetaDf = pd.concat([highBetaDf, df['highBeta']], axis=1)
    highBetaDf.rename(columns = {'highBeta':'Trial {0}'.format(i)},  inplace = True)
    lowGammaDf = pd.concat([lowGammaDf, df['lowGamma']], axis=1)
    lowGammaDf.rename(columns = {'lowGamma':'Trial {0}'.format(i)},  inplace = True)
    highGammaDf = pd.concat([highGammaDf, df['highGamma']], axis=1)
    highGammaDf.rename(columns = {'highGamma':'Trial {0}'.format(i)},  inplace = True)

deltaFig = px.scatter(deltaDf, trendline='ols')
deltaFig.update_layout(title='Delta Waves')
deltaFig.write_html('BCI//Data//ConvertedToVolts//TrendlineGraphs//{0}_trendlines_delta.html'.format(userNum))

thetaFig = px.scatter(thetaDf, trendline='ols')
thetaFig.update_layout(title='Theta Waves')
thetaFig.write_html('BCI//Data//ConvertedToVolts//TrendlineGraphs//{0}_trendlines_theta.html'.format(userNum))

lowAlphaFig = px.scatter(lowAlphaDf, trendline='ols')
lowAlphaFig.update_layout(title='Low Alpha Waves')
lowAlphaFig.write_html('BCI//Data//ConvertedToVolts//TrendlineGraphs//{0}_trendlines_lowalpha.html'.format(userNum))

highAlphaFig = px.scatter(highAlphaDf, trendline='ols')
highAlphaFig.update_layout(title='High Alpha Waves')
highAlphaFig.write_html('BCI//Data//ConvertedToVolts//TrendlineGraphs//{0}_trendlines_highalpha.html'.format(userNum))

lowBetaFig = px.scatter(lowBetaDf, trendline='ols')
lowBetaFig.update_layout(title='Low Beta Waves')
lowBetaFig.write_html('BCI//Data//ConvertedToVolts//TrendlineGraphs//{0}_trendlines_lowbeta.html'.format(userNum))

highBetaFig = px.scatter(highBetaDf, trendline='ols')
highBetaFig.update_layout(title='High Beta Waves')
highBetaFig.write_html('BCI//Data//ConvertedToVolts//TrendlineGraphs//{0}_trendlines_highbeta.html'.format(userNum))

lowGammaFig = px.scatter(lowGammaDf, trendline='ols')
lowGammaFig.update_layout(title='Low Gamma Waves')
lowGammaFig.write_html('BCI//Data//ConvertedToVolts//TrendlineGraphs//{0}_trendlines_lowgamma.html'.format(userNum))

highGammaFig = px.scatter(highGammaDf, trendline='ols')
highGammaFig.update_layout(title='High Gamma Waves')
highGammaFig.write_html('BCI//Data//ConvertedToVolts//TrendlineGraphs//{0}_trendlines_highgamma.html'.format(userNum))