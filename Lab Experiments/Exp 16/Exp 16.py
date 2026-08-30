import math

def sigmoid(x):
    return 1 / (1 + math.exp(-x))

def feed_forward(inputs, weights, bias):
    total = sum(i * w for i, w in zip(inputs, weights)) + bias
    return sigmoid(total)

inputs = [0.5, 0.3]
weights = [0.4, 0.7]
bias = 0.1
output = feed_forward(inputs, weights, bias)
print("Feed Forward Neural Network Output:", output)
