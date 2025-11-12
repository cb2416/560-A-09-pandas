import pandas as pd

composer_last = ["Beethoven", "Mozart", "Bach", 
                 "Tchaikovsky", "Debussy", "Stravinsky", 
                 "Verdi", "Gershwin", "Glass", "Zimmer"]
composer_first = ["Ludwig", "Wolfgang", "J.S.", 
                  "Pyotr", "Claude", "Igor", 
                  "Giuseppe", "George", "Philip", "Hans"]
country = ["Germany", "Austria", "Germany",
           "Russia", "France", "Russia",
           "Italy", "US", "US", "Germany"]
genre = ["Classical/ Romantic", "Classical", "Baroque",
         "Romantic", "Impressionist", "Modernist",
         "Opera", "Jazz", "Minimalist", "Film Score"]
birth_year = [1770, 1756, 1685, 
              1840, 1862, 1882, 
              1813, 1898, 1937, 1957]

#Philip Glass and Hans Zimmer aren't dead, but I want to calculate their age, hence 2025
death_year = [1827, 1791, 1750,
              1893, 1918, 1971, 
              1901, 1937, 2025, 2025]

composer = {"Last Name": composer_last,
            "First Name": composer_first,
            "Country of Origin": country,
            "Genre": genre,
            "Date of Birth": birth_year,
            "Date of Death": death_year}
data = pd.DataFrame(composer)

data["Age"] = (data["Date of Death"])-(data["Date of Birth"])

print(data)

data.to_csv("age.csv")

