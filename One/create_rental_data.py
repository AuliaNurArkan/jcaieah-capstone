# membuat file csv sederhana

import pandas as pd

data = {
    "rental_id": range(1, 11),
    "car_type": ["SUV", "Sedan", "SUV", "Hatchback", "Sedan", "SUV", "Sedan", "Hatchback", "SUV", "Sedan"],
    "rental_duration": [3, 2, 5, 1, 4, 7, 3, 2, 6, 5],
    "rental_cost": [300, 200, 450, 100, 350, 600, 280, 150, 500, 400],
    "customer_gender": ["Male", "Female", "Female", "Male", "Female", "Male", "Female", "Male", "Female", "Male"],

    # 🔹 Kolom tambahan untuk pemula
    "rental_date": [
        "2024-01-01","2024-01-02","2024-01-03","2024-01-04",
        "2024-01-05","2024-01-06","2024-01-07","2024-01-08",
        "2024-01-09","2024-01-10"
    ],
    "branch_city": [
        "Jakarta","Jakarta","Bandung","Bandung","Surabaya",
        "Surabaya","Medan","Medan","Jakarta","Bandung"
    ]
}

df = pd.DataFrame(data)
csv_path = "/Users/aulianurarkan/Documents/Purwadhika/Capstone/One/car_rental.csv"
df.to_csv(csv_path, index=False)

print(df)
