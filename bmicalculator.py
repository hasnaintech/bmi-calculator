# Program to find out whether a person has a normal BMI or not
def calculateBmi(weight, height):                  # BMI formula: kg/m^2
    height_meters = height / 100
    return weight / height_meters**2

def weight_check(bmi):
    if bmi < 18.5:
        return "You are underweight because the normal BMI range is 18.5 - 24.9"
    elif bmi <= 24.9:
        return "Your weight is normal as the normal BMI range is 18.5 - 24.9"
    elif bmi <= 29.9:
        return "You are overweight because the normal BMI range is 18.5 - 24.9"
    else:
        return "You are obese because the normal BMI range is 18.5 - 24.9"

def main():
    weight = float(input("Enter your weight (kg): "))
    height = float(input("Enter your height (cm): "))

    bmi = calculateBmi(weight, height)
    print(f"Your BMI is: {bmi}")
    print(weight_check(bmi))

    min_bmi = 18.5 * (height / 100)**2
    max_bmi = 24.9 * (height / 100)**2
    print(f"Normal BMI range as per your height is: {min_bmi:.2f} kg - {max_bmi:.2f} kg")

if __name__ == "__main__":
    main()
