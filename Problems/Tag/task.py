def tagged(func):
    def wrapper(inp):
        return f"<title>{func(inp)}</title>"
    return wrapper
