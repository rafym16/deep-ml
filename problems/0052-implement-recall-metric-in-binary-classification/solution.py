import numpy as np

def recall(y_true, y_pred):
    """
    Calculate the recall metric for binary classification.
    
    Args:
        y_true: Array of true binary labels (0 or 1)
        y_pred: Array of predicted binary labels (0 or 1)
    
    Returns:
        Recall value as a float
    """

    # Your code here
    true_pos_value = 0
    true_neg_value = 0
    false_pos_value = 0
    false_neg_value = 0

    for i in range(len(y_true)):
        if y_pred[i] == 1 and y_true[i] == 1:
            true_pos_value += 1
        elif y_pred[i] == 1 and y_true[i] == 0:
            false_pos_value += 1
        elif y_pred[i] == 0 and y_true[i] == 1:
            false_neg_value += 1
        else:
            true_neg_value += 1

    recall = true_pos_value / (true_pos_value + false_neg_value)
    return recall