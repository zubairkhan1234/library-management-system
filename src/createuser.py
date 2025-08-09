def create_user():
    name = input("Enter your Name")
    email = input('Enter your Email')
    address = input('Enter your complete Address')
    country = input("Enter your Country Name")
    city = input('Enter your City Name')
    cnic = input("Enter your cnic Name")

    userData = {"name": name, "email": email, "address": address, "country": country, "city": city, "cnic": cnic}
    return userData