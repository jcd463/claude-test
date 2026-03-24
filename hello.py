import datetime


def greet(name: str) -> str:
    hour = datetime.datetime.now().hour
    if hour < 12:
        period = "morning"
    elif hour < 18:
        period = "afternoon"
    else:
        period = "evening"
    return f"Good {period}, {name}!"


if __name__ == "__main__":
    print(greet("world"))
    print(greet("Delta"))
