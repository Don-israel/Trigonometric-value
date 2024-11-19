import math

# Function to calculate trigonometric values
def calculate_trigonometric_values(angle_in_degrees):
    # Convert angle to radians
    angle_in_radians = math.radians(angle_in_degrees)

    # Calculate sine, cosine, and tangent
    sine_value = math.sin(angle_in_radians)
    cosine_value = math.cos(angle_in_radians)
    tangent_value = math.tan(angle_in_radians)

    # Display the results
    print(f"Angle: {angle_in_degrees}°")
    print(f"Sine: {sine_value}")
    print(f"Cosine: {cosine_value}")
    print(f"Tangent: {tangent_value}")

# Input from the user
try:
    angle = float(input("Enter an angle in degrees: "))
    calculate_trigonometric_values(angle)
except ValueError:
    print("Please enter a valid number.")
