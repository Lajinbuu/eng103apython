age = 0
film_showing = False
if age >= 18 and film_showing:
    print("You are allowed to buy a ticket for this film")
    print("Enjoy the film")

    print("still is in the if-block")
elif age == 17:
    print("Come back next year")
else:
    print("No dice")
## string is always true unless emppty
print("This will always print")
certificate = "U" # u, PG, 12, 12A, 15 18
# Print corresponding info about the film

if certificate == "U":
    print("suitable for all ages")
elif certificate.upper() in ("pg"):
    print("Parental guidance recommended")
else:
    certificate.upper()
    print("you are not alive")

