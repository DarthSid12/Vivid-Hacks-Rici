import random
countryMaps = [
   {
       'name':'malaysia',
       'map':'''
    ..................................................
..................................................
..................................................
..................................................
..................................................
..................................................
..................................................
..................................................
..:.......................................:%!.....
.:$&!.:*.................................*SBS*:...
..*BSSSB&*.............................!@BBBBB#&*:
..:#BBBBBB!.........................!.*&BBBBBBS$!.
...%BBBBBB*.......................:$B&SB%!!!**!:..
....*BBBBB*...................::!%SBBBB#:.........
.....*&BBBS*.................%SBBBBBBB#:..........
.......:%&B#!............*%%*SBB#SBBS#:...........
..........:::............:*&@$@*..!!:.............
..................................................
..................................................
..................................................
..................................................
..................................................
..................................................
..................................................
..................................................
..................................................
..................................................
    '''
   },
    {'name':'kuwait',
     'map':'''
    ..................................................
..................................................
..................................................
..................................................
..................................................
..................................................
..................................................
..................................................
..:.......................................:%!.....
.:$&!.:*.................................*SBS*:...
..*BSSSB&*.............................!@BBBBB#&*:
..:#BBBBBB!.........................!.*&BBBBBBS$!.
...%BBBBBB*.......................:$B&SB%!!!**!:..
....*BBBBB*...................::!%SBBBB#:.........
.....*&BBBS*.................%SBBBBBBB#:..........
.......:%&B#!............*%%*SBB#SBBS#:...........
..........:::............:*&@$@*..!!:.............
..................................................
..................................................
..................................................
..................................................
..................................................
..................................................
..................................................
..................................................
..................................................
..................................................
    '''
    }]

countriesNameCapital = [
    'United States',
    'Afghanistan',
    'Albania',
    'Algeria',
    'American Samoa',
    'Andorra',
    'Angola',
    'Anguilla',
    'Antarctica',
    'Antigua And Barbuda',
    'Argentina',
    'Armenia',
    'Aruba',
    'Australia',
    'Austria',
    'Azerbaijan',
    'Bahamas',
    'Bahrain',
    'Bangladesh',
    'Barbados',
    'Belarus',
    'Belgium',
    'Belize',
    'Benin',
    'Bermuda',
    'Bhutan',
    'Bolivia',
    'Bosnia And Herzegowina',
    'Botswana',
    'Bouvet Island',
    'Brazil',
    'Brunei Darussalam',
    'Bulgaria',
    'Burkina Faso',
    'Burundi',
    'Cambodia',
    'Cameroon',
    'Canada',
    'Cape Verde',
    'Cayman Islands',
    'Central African Rep',
    'Chad',
    'Chile',
    'China',
    'Christmas Island',
    'Cocos Islands',
    'Colombia',
    'Comoros',
    'Congo',
    'Cook Islands',
    'Costa Rica',
    'Cote D`ivoire',
    'Croatia',
    'Cuba',
    'Cyprus',
    'Czech Republic',
    'Denmark',
    'Djibouti',
    'Dominica',
    'Dominican Republic',
    'East Timor',
    'Ecuador',
    'Egypt',
    'El Salvador',
    'Equatorial Guinea',
    'Eritrea',
    'Estonia',
    'Ethiopia',
    'Falkland Islands (Malvinas)',
    'Faroe Islands',
    'Fiji',
    'Finland',
    'France',
    'French Guiana',
    'French Polynesia',
    'French S. Territories',
    'Gabon',
    'Gambia',
    'Georgia',
    'Germany',
    'Ghana',
    'Gibraltar',
    'Greece',
    'Greenland',
    'Grenada',
    'Guadeloupe',
    'Guam',
    'Guatemala',
    'Guinea',
    'Guinea-bissau',
    'Guyana',
    'Haiti',
    'Honduras',
    'Hong Kong',
    'Hungary',
    'Iceland',
    'India',
    'Indonesia',
    'Iran',
    'Iraq',
    'Ireland',
    'Israel',
    'Italy',
    'Jamaica',
    'Japan',
    'Jordan',
    'Kazakhstan',
    'Kenya',
    'Kiribati',
    'Korea (North)',
    'Korea (South)',
    'Kuwait',
    'Kyrgyzstan',
    'Laos',
    'Latvia',
    'Lebanon',
    'Lesotho',
    'Liberia',
    'Libya',
    'Liechtenstein',
    'Lithuania',
    'Luxembourg',
    'Macau',
    'Macedonia',
    'Madagascar',
    'Malawi',
    'Malaysia',
    'Maldives',
    'Mali',
    'Malta',
    'Marshall Islands',
    'Martinique',
    'Mauritania',
    'Mauritius',
    'Mayotte',
    'Mexico',
    'Micronesia',
    'Moldova',
    'Monaco',
    'Mongolia',
    'Montserrat',
    'Morocco',
    'Mozambique',
    'Myanmar',
    'Namibia',
    'Nauru',
    'Nepal',
    'Netherlands',
    'Netherlands Antilles',
    'New Caledonia',
    'New Zealand',
    'Nicaragua',
    'Niger',
    'Nigeria',
    'Niue',
    'Norfolk Island',
    'Northern Mariana Islands',
    'Norway',
    'Oman',
    'Pakistan',
    'Palau',
    'Panama',
    'Papua New Guinea',
    'Paraguay',
    'Peru',
    'Philippines',
    'Pitcairn',
    'Poland',
    'Portugal',
    'Puerto Rico',
    'Qatar',
    'Reunion',
    'Romania',
    'Russian Federation',
    'Rwanda',
    'Saint Kitts And Nevis',
    'Saint Lucia',
    'St Vincent/Grenadines',
    'Samoa',
    'San Marino',
    'Sao Tome',
    'Saudi Arabia',
    'Senegal',
    'Seychelles',
    'Sierra Leone',
    'Singapore',
    'Slovakia',
    'Slovenia',
    'Solomon Islands',
    'Somalia',
    'South Africa',
    'Spain',
    'Sri Lanka',
    'St. Helena',
    'St.Pierre',
    'Sudan',
    'Suriname',
    'Swaziland',
    'Sweden',
    'Switzerland',
    'Syrian Arab Republic',
    'Taiwan',
    'Tajikistan',
    'Tanzania',
    'Thailand',
    'Togo',
    'Tokelau',
    'Tonga',
    'Trinidad And Tobago',
    'Tunisia',
    'Turkey',
    'Turkmenistan',
    'Tuvalu',
    'Uganda',
    'Ukraine',
    'United Arab Emirates',
    'United Kingdom',
    'Uruguay',
    'Uzbekistan',
    'Vanuatu',
    'Vatican City State',
    'Venezuela',
    'Viet Nam',
    'Virgin Islands (British)',
    'Virgin Islands (U.S.)',
    'Yemen',
    'Yugoslavia',
    'Zaire',
    'Zambia',
    'Zimbabwe'
]
countriesNameLower = []
for country in countriesNameCapital:
    countriesNameLower.append(country.lower())

print('''
Welcome to WORLDLE
We will display a country to you. You have to guess which country is displayed in 6 tries. We will also give you the distance between the country guessed and the country displayed as well.
Let's get started!
''')
i=0
totalGuesses = 6
correctCountry = random.choice(countryMaps)
print(correctCountry['map'])
guessed = False
while i<totalGuesses:
    guess = input("")
    
    if guess.lower() == correctCountry['name']:
        print("Congratulations, you got it.")
        guessed = True
    elif guess in countriesNameLower:#Check if guess is a country
        print(f"Close, but wrong You have ${totalGuesses - i} guesses left")
    
