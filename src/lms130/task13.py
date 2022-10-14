from to_do import TODO


def task13_1(customers):
    result = list(dict.fromkeys(customers))

    print(result)
    return result



if __name__ == "__main__":
    task13_1(["mary@tv.com","john@nas.gov","john@nas.gov","ema@post.com","ema@post.com"])


def task13_2(customers):
    result = []

    x = customers
    y = set(x)

    for number in y:
        occurences = x.count(number)
        if (occurences > 1):
            result.append(number)

    print(result)
    return result



if __name__ == "__main__":
    task13_2(["mary@tv.com","john@nas.gov","john@nas.gov","ema@post.com","ema@post.com"])


def task13_3(customers):
    result = []

    start = "@"
    end = "."

    for email in range(len(customers)):
        text = customers[email]
        result.append(text[text.index(start) + len(start):text.index(end)])

    result = list(dict.fromkeys(result))
    print(result)
    return result


if __name__ == "__main__":
    task13_3(["mary@tv.com","john@nas.gov","john@nas.gov","ema@post.com","ema@post.com"])



if __name__ == "__main__":
    customer_list = [
        "tgundrey1l@prlog.org",
        "bgrix1u@apache.org",
        "mbreakspear1v@wordpress.com",
        "cdalli1w@ft.com",
        "rclayborn1x@mtv.com",
        "rclayborn1x@mtv.com",
        "jchidlow1y@nasa.gov",
        "jchidlow1y@nasa.gov",
        "kovell1z@washingtonpost.com",
        "kovell1z@washingtonpost.com",
        "kovell1z@washingtonpost.com",
    ]

    print(f"The customers who purchased from your product: {task13_1(customer_list)}")
    print(
        f"The customers that purchased multiple times include: {task13_2(customer_list)}"
    )
    print(f"The companies that purchased from you include: {task13_3(customer_list)}")
