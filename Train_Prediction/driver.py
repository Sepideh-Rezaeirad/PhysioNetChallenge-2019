import pandas as pd
import torch
from torch.utils.data.dataset import Dataset
from torch.utils.data import DataLoader
import torch.utils.data as data_utils

import numpy as np, os, sys
from get_sepsis_score import load_sepsis_model, get_sepsis_score
# from get_sepsis_score2 import load_sepsis_model, get_sepsis_score2
# from get_sepsis_score3 import load_sepsis_model, get_sepsis_score3
from evaluate_sepsis_score import evaluate_sepsis_score

def load_challenge_data(file):
    with open(file, 'r') as f:
        header = f.readline().strip()
        column_names = header.split('|')
        data = np.loadtxt(f, delimiter='|')

    # Ignore SepsisLabel column if present.
    if column_names[-1] == 'SepsisLabel':
        column_names = column_names[:-1]
        data = data[:, :-1]
    return data

def save_challenge_predictions(file, scores, labels):
    with open(file, 'w') as f:
        f.write('PredictedProbability|PredictedLabel\n')
        for (s, l) in zip(scores, labels):
            f.write('%g|%d\n' % (s, l))

def driver():
    input_directory = "../test"
    output_directory = "prediction"

    # Find files.
    files = []
    for f in os.listdir(input_directory):
        if os.path.isfile(os.path.join(input_directory, f)) and not f.lower().startswith('.') and f.lower().endswith(
                'psv'):
            files.append(f)

    if not os.path.isdir(output_directory):
        os.mkdir(output_directory)

    # Load model.
    model = load_sepsis_model()
    # model.eval()

    # Iterate over files.
    for f in files:
        # Load data.
        input_file = os.path.join(input_directory, f)
        data = load_challenge_data(input_file)

        # Make predictions.
        num_rows = len(data)
        scores = np.zeros(num_rows)
        labels = np.zeros(num_rows)
        # for t in range(num_rows):
        # current_data = data[:t + 1]
        current_data = data
        current_score, current_label = get_sepsis_score(current_data, model)
        # current_score, current_label = get_sepsis_score2(current_data, model)
        # current_score, current_label = get_sepsis_score3(current_data, model)
        scores = current_score
        labels = current_label

        # Save results.
        output_file = os.path.join(output_directory, f)
        save_challenge_predictions(output_file, scores, labels)

    ##### Main Evaluation Utility Score
    label_directory = "../outputtest"
    prediction_directory = "prediction"

    result = evaluate_sepsis_score(label_directory, prediction_directory)

    # auroc, auprc, accuracy, f_measure, normalized_observed_utility
    print ('auroc, auprc, accuracy, f_measure, normalized_observed_utility')
    print(result)

    return result