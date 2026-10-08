def average_intensity(pixels):
    total = sum(pixels)
    average = total / len(pixels)
    return average

pixel = input("Enter pixel values: ")

pixels = list(map(float, pixel.split()))

result = average_intensity(pixels)

print("Average Pixel Intensity =", result)