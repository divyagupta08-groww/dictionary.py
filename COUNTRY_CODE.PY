country_code = {'UAE':'00971',
                'India':'0091',
                'greece':'0030'}
print("the country code for greece is")
print(country_code.get('greece','not_found'))
print("the country code for brazil is")
print(country_code.get('brazil','not_found'))
