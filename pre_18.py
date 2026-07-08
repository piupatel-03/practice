

def mean(numbers):
    return sum(numbers) / len(numbers)

def median(numbers):
    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_numbers[mid - 1] + sorted_numbers[mid]) / 2
    else:
        return sorted_numbers[mid]
    
def mode(numbers):
    from collections import Counter
    count = Counter(numbers)
    mode_data = count.most_common()
    mode_value = mode_data[0][0]
    return mode_value

def standard_deviation(numbers):
    mean_value = mean(numbers)
    variance = sum((x - mean_value) ** 2 for x in numbers) / len(numbers)
    return variance ** 0.5

#  usage:
if __name__ == "__main__":
    data = [1, 2, 2, 3, 4]
    print("Mean:", mean(data))
    print("Median:", median(data))
    print("Mode:", mode(data))
    print("Standard Deviation:", standard_deviation(data))

