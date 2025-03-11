def calculate_variance(data):
    mean = sum(data) / len(data) if data else 0
    return sum((x - mean) ** 2 for x in data) / len(data) if data else 0

# Example usage
if __name__ == "__main__":
    sample_data = [10, 12, 23, 23, 16, 23, 21, 16]
    print("Variance of sample data:", calculate_variance(sample_data))