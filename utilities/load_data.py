import pandas as pd
import numpy as np
import os

def load_data():

    data_path = '/Users/jstremme/Documents/git/classifier-recall-over-time/data/test_data.csv'

    return pd.read_csv(data_path)

def perf_measure(y_true, y_hat):

    TP = 0
    FP = 0
    TN = 0
    FN = 0

    for i in range(len(y_hat)): 
        if y_true[i]==y_hat[i]==1:
           TP += 1
        if y_hat[i]==1 and y_true[i]!=y_hat[i]:
           FP += 1
        if y_true[i]==y_hat[i]==0:
           TN += 1
        if y_hat[i]==0 and y_true[i]!=y_hat[i]:
           FN += 1

    return(TP, FP, TN, FN)

def mark_tp(prediction, diagnosed):

    return [int(x==y) for x, y in zip(prediction, diagnosed)]

def get_performance_values(threshold):

    df = load_data()
    df['prediction'] = df['risk_score'].apply(lambda x: 1 if x > threshold else 0)

    y_true = df['diagnosed'].tolist()
    y_hat = df['prediction'].tolist()
    TP, FP, TN, FN = perf_measure(y_true, y_hat)
    recall = round(TP / (TP + FN), 3)
    precision = round(TP / (TP + FP), 3)
    
    df['true_positive'] =  mark_tp(df['prediction'].tolist(), df['diagnosed'].tolist())
    predicted_per_month = df.groupby('idx_date_month')['true_positive'].sum().reset_index()
    total_per_month = df.groupby('idx_date_month')['diagnosed'].sum().reset_index()

    months = predicted_per_month['idx_date_month'].tolist()
    num_recalled = predicted_per_month['true_positive'].values.astype(np.float)
    num_diagnosed = total_per_month['diagnosed'].values.astype(np.float)

    return months, num_recalled, num_diagnosed, recall, precision



