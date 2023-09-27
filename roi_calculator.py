### Return on Investment Calculator

principal = float(input("Principal Amount :"))
per_annum = float(input("Annual Interest Rate :"))
type_of_return = input("Type of Return (Daily, Monthly, Yearly) :").strip().title()
roi = float()

if type_of_return == "Daily":
    roi = principal * (per_annum / 100 / 12 / 31)
    print(roi)

elif type_of_return == "Monthly":
    roi = principal * (per_annum / 100 / 12)
    print(roi)

elif type_of_return == "Yearly":
    roi = principal * (per_annum / 100)
    print(roi)