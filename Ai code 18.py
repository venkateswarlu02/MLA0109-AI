import numpy as np

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def sigmoid_derivative(x):
    return x * (1 - x)

class NeuralNetwork:
    def __init__(self, input_size, hidden_size, output_size):
        self.input_size = input_size
        self.hidden_size = hidden_size
        self.output_size = output_size
        
        self.weights_input_hidden = np.random.randn(self.input_size, self.hidden_size)
        self.bias_input_hidden = np.zeros((1, self.hidden_size))
        
        self.weights_hidden_output = np.random.randn(self.hidden_size, self.output_size)
        self.bias_hidden_output = np.zeros((1, self.output_size))
        
    def forward(self, inputs):
        self.hidden_activation = sigmoid(np.dot(inputs, self.weights_input_hidden) + self.bias_input_hidden)
        self.output = np.dot(self.hidden_activation, self.weights_hidden_output) + self.bias_hidden_output
        return self.output
    
    def train(self, inputs, targets, learning_rate):
        # Forward pass
        self.output = self.forward(inputs)
        
        # Backpropagation
        error = targets - self.output
        output_delta = error
        hidden_error = np.dot(output_delta, self.weights_hidden_output.T)
        hidden_delta = hidden_error * sigmoid_derivative(self.hidden_activation)
        
        # Update weights and biases
        self.weights_hidden_output += np.dot(self.hidden_activation.T, output_delta) * learning_rate
        self.bias_hidden_output += np.sum(output_delta, axis=0, keepdims=True) * learning_rate
        self.weights_input_hidden += np.dot(inputs.T, hidden_delta) * learning_rate
        self.bias_input_hidden += np.sum(hidden_delta, axis=0, keepdims=True) * learning_rate

# Define dataset (XOR problem)
X_train = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
y_train = np.array([[0], [1], [1], [0]])

# Initialize neural network
input_size = 2
hidden_size = 2
output_size = 1
learning_rate = 0.1
epochs = 10000

model = NeuralNetwork(input_size, hidden_size, output_size)

# Training loop
for epoch in range(epochs):
    model.train(X_train, y_train, learning_rate)
    if epoch % 1000 == 0:
        loss = np.mean(np.square(y_train - model.forward(X_train)))
        print(f"Epoch {epoch}, Loss: {loss}")

# Test the trained model
predictions = model.forward(X_train)
print("Predictions:\n", predictions)
