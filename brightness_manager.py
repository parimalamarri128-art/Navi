import screen_brightness_control as sbc


def brightness_up():
    try:
        current = sbc.get_brightness()[0]
        new = min(current + 10, 100)
        sbc.set_brightness(new)
        return f"Brightness increased to {new}%."
    except Exception as e:
        return f"Error: {e}"


def brightness_down():
    try:
        current = sbc.get_brightness()[0]
        new = max(current - 10, 0)
        sbc.set_brightness(new)
        return f"Brightness decreased to {new}%."
    except Exception as e:
        return f"Error: {e}"


def set_brightness(level):
    try:
        sbc.set_brightness(level)
        return f"Brightness set to {level}%."
    except Exception as e:
        return f"Error: {e}"


def get_brightness():
    try:
        current = sbc.get_brightness()[0]
        return f"Current brightness is {current}%."
    except Exception as e:
        return f"Error: {e}"