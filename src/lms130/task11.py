from to_do import TODO


def task11_1(guests):

    result = len(guests)

    print(result)
    return result
if __name__ == "__main__":
    task11_1(["Lia-K", "Mar-A", "Luz-K","Ulf-V",])


def task11_2(guests, condition):
    result = []
    for num in range(len(guests)):
        if (condition in guests[num]):
            result.append(guests[num])

    print(result)
    return result



if __name__ == "__main__":
    task11_2( ["Lia-K", "Mar-A", "Luz-K", "Ulf-V"],"-K")

    # Change the situation to either "-V", "-A", or "-K" to test your code under different situation
    situation = "-v"
    guest_list = [
        "Stéphanie-A",
        "Edmée-K",
        "Maëlla-K",
        "Océanne-K",
        "Géraldine-K",
        "Maëline-K",
    ]

    # NOTE: Uncomment the code below when you are ready to test your answers
    print(f"The event has a total of {task11_1(guest_list)} guests.")
    print(
        f"The attendees with condition '{situation}' are {task11_2(guest_list, situation)}"
    )
