import random
import string


def get_category():
    categories = ["Animal", "Car", "Country", "Medicine", "Music", "Profession", "Sport", "Vegetable", "Fruit"]
    return categories[random.randint(0, len(categories) - 1)].upper()


def get_secret_word(unique_category):
    words = []

    if unique_category == "ANIMAL":
        words = ["Antelope", "Arctic wolf", "Badger", "Bald eagle", "Porcupine", "Bat", "Bear", "Camel", "Chimpanzee",
                 "Coyote", "Deer", "Elephant", "Elk", "Giraffe", "Gorilla", "Hare", "Hedgehog", "Hippopotamus", "Koala",
                 "Leopard", "Lion", "Lizard", "Mole", "Monkey", "Owl", "Panda", "Rabbit", "Raccoon", "Rat", "Bison",
                 "Reindeer", "Squirrel", "Walrus", "Wolf", "Woodpecker", "Wombat", "Possum", "Chipmunk", "Porcupine",
                 "Hedgehog", "Mongoose", "Meerkat", "Otter", "Raccoon", "Hyena", "Jackal", "Fox", "Monkey", "Red panda",
                 "Deer", "Scimitar Oryx", "Kangaroo", "Tiger", "Cheetah", "Bear", "Lion", "Zebra", "Possum", "Giraffe",
                 "Wombat", "Elephant", "Chimpanzee", "Gorilla", "Bison", "Hippopotamus", "Rhinoceros", "Black Leopard",
                 "Jaguar", "Puma", "Toucan", "King Fisher", "Swift", "Parrot", "HummingBird", "Dove", "Pigeon",
                 "Hornbill", "Spoonbill", "Bee-Eater", "Grebe", "Guinea Fowl", "Goose Bird", "Woodpecker", "Penguin",
                 "Swallow", "Passerine", "Heron", "Gull", "Albatross", "Cuckoo", "Peafowl", "Eagle", "Moa",
                 "Elephant bird", "Vulture", "Raven", "Seahorse", "Sea lion", "Seal", "Shark", "Whale", "Turtle",
                 "Octopus", "Starfish", "Crab", "Squid", "Oyster", "Tuna"]

    elif unique_category == "CAR":
        words = ["Acura", "Alfa Romeo", "Aston Martin", "Audi", "Bentley", "BMW", "Bugatti", "Buick", "Cadillac",
                 "Chevrolet", "Chrysler", "Citroen", "Dodge", "Ferrari", "Fiat", "Ford", "Geely", "General Motors",
                 "GMC", "Honda", "Infiniti", "Jaguar", "Jeep", "Kia", "Koenigsegg", "Lamborghini", "Land Rover",
                 "Lexus", "Maserati", "Mazda", "McLaren", "Mercedes-Benz", "Mini", "Mitsubishi", "Nissan", "Pagani",
                 "Peugeot", "Porsche", "Ram", "Renault", "Rolls Royce", "Saab", "Subaru", "Suzuki", "Tata Motors",
                 "Tesla", "Toyota", "Volkswagen", "Volvo"]

    elif unique_category == "COUNTRY":
        words = ["Afghanistan", "Albania", "Algeria", "Andorra", "Angola", "Antigua and Barbuda", "Argentina",
                 "Armenia", "Australia", "Austria", "Azerbaijan", "The Bahamas", "Bahrain", "Bangladesh", "Barbados",
                 "Belarus", "Belgium", "Belize", "Benin", "Bhutan", "Bolivia", "Bosnia and Herzegovina", "Botswana",
                 "Brazil", "Brunei", "Bulgaria", "Burkina Faso", "Burundi", "Cape Verde", "Cambodia", "Cameroon",
                 "Canada", "Central African Republic", "Chad", "Chile", "China", "Colombia", "Comoros",
                 "Democratic Republic of the Congo", "Republic of the Congo", "Costa Rica", "Cote d’Ivoire", "Croatia",
                 "Cuba", "Cyprus", "Czech Republic", "Denmark", "Djibouti", "Dominica", "Dominican Republic",
                 "East Timor", "Ecuador", "Egypt", "El Salvador", "Equatorial Guinea", "Eritrea", "Estonia",
                 "Swaziland", "Ethiopia", "Fiji", "Finland", "France", "Gabon", "The Gambia", "Georgia", "Germany",
                 "Ghana", "Greece", "Grenada", "Guatemala", "Guinea", "Guinea-Bissau", "Guyana", "Haiti", "Honduras",
                 "Hungary", "Iceland", "India", "Indonesia", "Iran", "Iraq", "Ireland", "Israel", "Italy", "Jamaica",
                 "Japan", "Jordan", "Kazakhstan", "Kenya", "Kiribati", "North Korea", "South Korea", "Kosovo", "Kuwait",
                 "Kyrgyzstan", "Laos", "Lebanon", "Lesotho", "Liberia", "Libya", "Liechtenstein", "Lithuania",
                 "Luxembourg", "Madagascar", "Malawi", "Malaysia", "Maldives", "Mali", "Malta", "Marshall Islands",
                 "Mauritania", "Mauritius", "Mexico", "Federated States of Micronesia", "Moldova", "Mongolia",
                 "Montenegro", "Morocco", "Mozambique", "Myanmar", "Namibia", "Nauru", "Nepal", "Netherlands",
                 "New Zealand", "Nicaragua", "Niger", "Nigeria", "North Macedonia", "Norway", "Oman", "Pakistan",
                 "Palau", "Panama", "Papua New Guinea", "Paraguay", "Peru", "Philippines", "Poland", "Portugal",
                 "Qatar", "Romania", "Russia", "Rwanda", "Saint Kitts and Nevis", "Saint Lucia",
                 "Saint Vincent and the Grenadines", "Samoa", "San Marino", "Sao Tome and Principe", "Saudi Arabia",
                 "Senegal", "Serbia", "Seychelles", "Sierra Leone", "Singapore", "Slovakia", "Slovenia",
                 "Solomon Islands", "Somalia", "South Africa", "Spain", "Sri Lanka", "Sudan", "South Sudan", "Suriname",
                 "Sweden", "Switzerland", "Syria", "Taiwan", "Tajikistan", "Tanzania", "Thailand", "Togo", "Tonga",
                 "Trinidad and Tobago", "Tunisia", "Turkey", "Turkmenistan", "Tuvalu", "Uganda", "Ukraine",
                 "United Arab Emirates", "United Kingdom", "United States", "Uruguay", "Uzbekistan", "Vanuatu",
                 "Vatican City", "Venezuela", "Vietnam", "Yemen", "Zambia", "Zimbabwe"]

    elif unique_category == "MEDICINE":
        words = ["aetiologist", "anaesthetist", "anatomist", "andrologist", "audiologist", "bacteriologist",
                 "balneologist", "cardiologist", "chiropodist", "consultant", "dental hygienist", "dentist",
                 "dermatologist", "diagnostician", "dietitian", "district nurse", "doctor", "electrophysiologist",
                 "embryologist", "endocrinologist", "endodontist", "epidemiologist", "exodontist", "forensic scientist",
                 "gastroenterologist", "geriatrician", "gerontologist", "gynaecologist", "haematologist",
                 "hydrotherapist", "immunologist", "intern", "laboratory technician", "laryngologist", "matron",
                 "midwife", "myologist", "neonatologist", "nephrologist", "neuroanatomist", "neurologist",
                 "neuropathologist", "neurophysiologist", "neuropsychiatrist", "neurosurgeon", "nosologist", "nurse",
                 "nursing officer", "nutritionist", "obstetrician", "odontologist", "oncologist", "ophthalmologist",
                 "optician", "optometrist", "orthodontist", "orthopaedist", "osteologist", "otolaryngologist",
                 "otologist", "paediatrician", "paediatrics", "paramedic", "pathologist", "pharyngologist",
                 "physiotherapist", "plastic surgeon", "proctologist", "psychiatrist", "psychoanalyst", "psychologist",
                 "radiographer", "radiologist", "resident", "rheumatologist", "rhinologist", "serologist",
                 "speech therapist", "surgeon", "syphilologist", "therapist", "toxicologist", "trichologist",
                 "urologist", "venereologist", "veterinary surgeon", "virologist"]

    elif unique_category == "MUSIC":
        words = ["Rock", "Rhythm and blues", "Classical", "Opera", "Country", "Jingles", "Lullaby", "Rap", "Dance",
                 "Electronic", "Pop", "Hip pop", "Instrumental", "Gospel", "Jazz", "Karaoke", "Soul", "Disco", "Reggae",
                 "Songwriter", "Soundtrack", "Acappella", "Vocal", "Juju", "Afro", "Fuji", "Calypso"]

    elif unique_category == "PROFESSION":
        words = ["accountant", "actor", "actress", "air traffic controller", "architect", "artist", "attorney",
                 "banker", "bartender", "barber", "bookkeeper", "builder", "butcher", "carpenter", "cashier", "chef",
                 "coach", "designer", "developer", "economist", "editor", "electrician", "engineer", "farmer",
                 "filmmaker", "fisherman", "flight attendant", "jeweler", "judge", "lawyer", "mechanic", "musician",
                 "painter", "pharmacist", "photographer", "physician", "physician's assistant", "pilot", "plumber",
                 "police officer", "politician", "professor", "programmer", "psychologist", "receptionist",
                 "salesperson", "secretary", "singer", "surgeon", "teacher", "translator", "undertaker", "veterinarian",
                 "videographer", "waiter", "waitress", "writer"]

    elif unique_category == "SPORT":
        words = ["kayaking", "bobsleigh", "canoeing", "cross-country skiing", "rafting", "skibobbing", "surfing",
                 "snorkeling", "swimming", "bodyboarding", "diving", "freediving", "paddleboarding", "rowing",
                 "scuba diving", "synchronized swimming", "aerobics", "aikido", "archery", "artistic gymnastics",
                 "baton twirling", "bodybuilding", "boxing", "cross-country equestrianism", "cross-country running",
                 "cycling", "discus throw", "equestrianism", "fencing", "figure skating", "horse racing", "judo",
                 "karate", "kendo", "kickboxing", "kung fu", "long jump", "marathon", "mixed martial arts",
                 "pole vault", "powerlifting", "racewalking", "rhythmic gymnastics", "sprint", "sumo", "sword-fighting",
                 "trail running", "trampolining", "tumbling", "walking", "weightlifting", "wrestling", "baseball",
                 "basketball", "tennis", "badminton", "bowling", "cricket", "curling", "dodgeball", "football", "golf",
                 "handball", "hockey", "horseball", "hurling", "ice hockey", "kickball", "lacrosse", "paddle", "polo",
                 "racquetball", "rinkball", "rounders", "rugby", "soccer", "softball", "squash", "table tennis",
                 "volleyball", "water polo", "abseiling", "bouldering", "gliding", "kiteboarding", "kitesurfing",
                 "parachuting", "paragliding", "parasailing", "skateboarding", "skydiving", "skysurfing",
                 "snowboarding", "wakeboarding", "windsurfing", "climbing", "cross-country cycling", "hiking",
                 "mountaineering", "drifting", "formula racing", "kart racing", "rallycross", "checkers", "chess",
                 "mahjong"]

    elif unique_category == "VEGETABLE":
        words = ["eggplant", "asparagus", "lentils", "bean sprouts", "black-eyed peas", "green beans", "kidney beans",
                 "butter bean", "mung beans", "navy beans", "peanuts", "pinto beans", "runner beans", "split peas",
                 "soy beans", "peas", "cabbage", "cauliflower", "celery", "endive", "basil", "caraway", "coriander",
                 "fennel", "lavender", "lemongrass", "oregano", "parsley", "rosemary", "sage", "thyme", "lettuce",
                 "arugula", "mushrooms", "nettles", "okra", "onions", "chives", "garlic", "leek", "onion", "pepper",
                 "rhubarb", "beetroot", "carrot", "water chestnut", "ginger", "parsnip", "radish", "potato",
                 "sweet potato", "yam", "turnip", "broccoli", "spinach", "Brussels sprouts", "Oyster Plant",
                 "sweetcorn", "squashes", "courgette", "Zucchini", "cucumber", "tomato", "watercress"]

    elif unique_category == "FRUIT":
        words = ["Apple", "Apricot", "Avocado", "Banana", "Bilberry", "Blackberry", "Blackcurrant", "Black sapote",
                 "Blueberry", "Boysenberry", "Breadfruit", "Cactus pear", "Crab apple", "Currant", "Cherry",
                 "Custard Apple", "Chico fruit", "Cloudberry", "Coconut", "Cranberry", "Date", "Dragonfruit",
                 "Elderberry", "Fig", "Goji berry", "Gooseberry", "Grape", "Raisin", "Grapefruit", "Guava",
                 "Hala Fruit", "Honeyberry", "Huckleberry", "Jackfruit", "Japanese plum", "Jostaberry", "Juniper berry",
                 "Kiwifruit", "Kumquat", "Lemon", "Lime", "Loganberry", "Loquat", "Longan", "Lychee", "Mango",
                 "Mangosteen", "Marionberry", "Melon", "Cantaloupe", "Galia melon", "Honeydew", "Watermelon",
                 "Miracle fruit", "Monstera Delisiousa", "Mulberry", "Nance", "Nectarine", "Orange", "Tangerine",
                 "Papaya", "Passionfruit", "Peach", "Pear", "Persimmon", "Plantain", "Plum", "Pineapple", "Pineberry",
                 "Plumcot", "Pomegranate", "Pomelo", "Purple mangosteen", "Quince", "Raspberry", "Salmonberry",
                 "Rambutan", "Redcurrant", "Salal berry", "Salak", "Satsuma", "Soursop", "Star apple", "Star fruit",
                 "Strawberry", "Surinam cherry", "Tamarillo", "Tamarind", "Tangelo", "Tayberry", "Ugli fruit",
                 "White currant"]

    return words[random.randint(0, len(words) - 1)].upper()


def get_display_string(unique_list):
    new_list = []

    for character in unique_list:
        if character in string.ascii_letters:
            new_list.append("_")
        else:
            new_list.append(character)

    return new_list


def get_correct_options(options_set):
    options = []

    for character in options_set:
        if character in string.ascii_letters:
            options.append(character)

    return options


def get_wrong_options(option_list):
    options = []
    number_of_wrong_options = 5

    while number_of_wrong_options > 0:
        character = random.choice(string.ascii_uppercase)
        if character not in option_list and character not in options:
            options.append(character)
            number_of_wrong_options -= 1

    return options


def get_shuffled_options_list(correct_option_list, wrong_option_list):
    shuffled_list = []
    all_options = list(correct_option_list + wrong_option_list)
    for loop in range(len(all_options)):
        character = random.choice(all_options)
        shuffled_list.append(character)
        all_options.remove(character)

    return shuffled_list
