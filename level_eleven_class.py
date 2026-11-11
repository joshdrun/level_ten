import pandas as pd

national_park_data = pd.read_csv("national_parks_sample.csv")
print(national_park_data)



park_info = pd.read_csv("national_parks_sample.csv")

#you can get rows and columns with loc
print(park_info.loc[park_info["Waterfalls"] == "Yes"]) 

 
#you can get rows and columns with iloc
print(park_info.iloc[1])


#you can get and set a single value with at. Doesn't change the csv, only the panda
park_info.at[1, "Waterfalls"] = "Yes"

print(park_info.at[1, "Waterfalls"])


#you can iterate through rows with iterrows
for row, col in park_info.iterrows():
    print(row, col)
    print()


print(park_info.query("HighestPointFeet >= 10000 and Waterfalls == 'Yes'")[["Park", "HighestPointFeet", "Waterfalls"]])