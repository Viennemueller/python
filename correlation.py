import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
import statsmodels.api as sm

# Your pitch speed data
pitch_speed = np.array([95.3, 93.9, 95.1, 94.6, 94.2, 95.4, 96.1, 93.8, 95.8, 93.6, 94.8, 95.1, 95.5, 94.7, 94.7])

# Sort the data
pitch_speed_sorted = np.sort(pitch_speed)

# Calculate z-scores
z_scores = (pitch_speed_sorted - np.mean(pitch_speed_sorted)) / np.std(pitch_speed_sorted)

# Generate a standard normal distribution
expected = norm.ppf(np.arange(0.5, len(pitch_speed_sorted) + 0.5) / len(pitch_speed_sorted))

# Create the normal probability plot
plt.scatter(expected, z_scores)
plt.title("Normal Probability Plot")
plt.xlabel("Expected Z-Scores")
plt.ylabel("Observed Z-Scores")
plt.show()

# Calculate the correlation coefficient
corr_coefficient = np.corrcoef(expected, z_scores)[0, 1]

print("Correlation Coefficient:", corr_coefficient)
