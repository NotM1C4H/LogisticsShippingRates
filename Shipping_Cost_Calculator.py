#Shipping Cost Calculator

## Input package weight and shipping rate
weight = float(input("Enter the package weight (Kg): "))
rate = float(input("Enter the shipping rate per kilogram: "))

## Calculate shipping cost
shipping_cost = weight*rate

## Display the result
print(f"Shipping cost: {shipping_cost} USD")
