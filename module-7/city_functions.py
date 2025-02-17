# Ryan Monnier
# CSD 325
# Module 7 assignmnet
# 16-Feb-2025



# defining the main function for this assignment
def city_country(city, country, population=None, language=None):
    if population and language:
        return f"{city}, {country} - population {population}, {language}"
    elif population:
        return f"{city}, {country} - population {population}"
    else:
        return f"{city}, {country}"

# The instructions dictate that I should call the function 3 times
# This was originally just" Chicago, USA" 3 times... but then I added in the other criteria that was asked for

# City, Country, Pop
print(city_country("Chicago", "USA", population=2000000))

# City, Country (the original)
print(city_country("Chicago", "USA"))

# City, Country, Pop, Lang
print(city_country("Chicago", "USA", population=2000000, language="English"))
