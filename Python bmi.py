# BMI Calculator 

def calculate_bmi():
    """Calculates and displays the Body Mass Index (BMI)."""
    
    # Get user input for weight and height
    print("Welcome to the BMI Calculator!")
    try:
        # Get weight in kilograms (kg)
        weight_kg = float(input("Enter your weight in kilograms (kg): "))
        
        # Get height in meters (m)
        height_m = float(input("Enter your height in meters (m): "))
        
    except ValueError:
        print("\n**Error:** Please enter valid numbers for weight and height.")
        return # Stop execution if input is not a number
    
    # Check for non-positive values
    if weight_kg <= 0 or height_m <= 0:
        print("\n**Error:** Weight and height must be positive values.")
        return

    #  Calculate BMI using the formula: weight / (height ** 2)
    # The ** operator is used for exponentiation (raising to a power)
    bmi = weight_kg / (height_m ** 2)
    
    # Display the result
    print(f"\n--- Result ---")
    # Round the BMI to two decimal places for readability
    print(f"Your calculated BMI is: **{bmi:.2f}**")
    
    # 4. Interpret the BMI result (simple classification)
    if bmi < 18.5:
        print("Classification: **Underweight**")
    elif 18.5 <= bmi < 25:
        print("Classification: **Normal weight**")
    elif 25 <= bmi < 30:
        print("Classification: **Overweight**")
    else:
        print("Classification: **Obesity**")
    print("------------")

# Call the function to run the calculator
calculate_bmi()
