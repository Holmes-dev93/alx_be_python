# weather_advice.py

# 1. Prompt User for Weather Input:
# We use .lower() to convert the input to lowercase, making it case-insensitive.
weather = input("What's the weather like today? (sunny/rainy/cold): ").lower()

# 2. Provide Clothing Recommendations using if, elif, and else:
if weather == "sunny":
    print("Wear a t-shirt and sunglasses.")
elif weather == "rainy":
    print("Don't forget your umbrella and a raincoat.")
elif weather == "cold":
    print("Make sure to wear a warm coat and a scarf.")
else:
    # 3. Handle unexpected input
    print("Sorry, I don't have recommendations for this weather.")
