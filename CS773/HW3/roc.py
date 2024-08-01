import matplotlib.pyplot as plt

# Given data
tpr = [0.2, 0.4, 0.4, 0.6, 0.8, 0.8, 0.8, 0.8, 0.8, 1]
fpr = [0, 0, 0.2, 0.2, 0.2, 0.4, 0.6, 0.8, 1, 1]

# Plotting the ROC curve
plt.figure()
plt.plot(fpr, tpr, marker='o', linestyle='-', color='b', label='ROC curve')
plt.plot([0, 1], [0, 1], linestyle='--', color='r', label='Random guess')

# Adding labels and title
plt.xlabel('False Positive Rate (FPR)')
plt.ylabel('True Positive Rate (TPR)')
plt.title('Receiver Operating Characteristic (ROC) Curve')
plt.legend(loc='lower right')

# Show plot
plt.show()
