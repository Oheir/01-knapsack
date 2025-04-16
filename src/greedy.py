class Knapsack:
    def __init__(self, weights, values, capacity):
        self.weights = weights  # List of item weights
        self.values = values    # List of item values
        self.capacity = capacity  # Maximum capacity of the knapsack
    
    def greedy_knapsack(self):
        # Calculate value-to-weight ratio for each item
        rapport = [0] * len(self.weights)
        liste = [0] * len(self.weights)
        tot_w = 0
        
        # Calculate the value-to-weight ratios
        for i in range(len(self.weights)):
            if self.weights[i] > 0:
                rapport[i] = self.values[i] / self.weights[i]
        
        while tot_w < self.capacity:
            # Get the index of the item with the maximum value-to-weight ratio
            x = max(range(len(rapport)), key=lambda i: rapport[i])
            
            # Check if adding this item doesn't exceed the capacity
            if tot_w + self.weights[x] <= self.capacity:
                liste[x] = 1  # Mark this item as selected
                tot_w += self.weights[x]  # Add its weight to the total weight
            
            # After selecting an item, set its ratio to 0 to avoid selecting it again
            rapport[x] = 0
            
            # If no more items can be selected (either all items are selected or the remaining items exceed capacity)
            if all(r == 0 for r in rapport):
                break
        
        return liste