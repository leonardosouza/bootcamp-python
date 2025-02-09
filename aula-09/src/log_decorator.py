from loguru import logger

logger.remove()

logger.add("app.log", format="{time} {level} {message} {file}", level="INFO")


def logger_decorator(func):
    def wrapper(*args, **kwargs):  # Capture all arguments
        print(f"Calling {func.__name__} with args: {args} and kwargs: {kwargs}")
        result = func(*args, **kwargs)  # Call the original function
        print(f"{func.__name__} returned {result}")
        return result

    return wrapper


def double_args_decorator(func):
    def wrapper(*args, **kwargs):
        new_args = tuple(
            arg * 2 if isinstance(arg, (int, float)) else arg for arg in args
        )
        new_kwargs = {
            k: v * 2 if isinstance(v, (int, float)) else v for k, v in kwargs.items()
        }
        print(f"Calling {func.__name__} with args: {args} and kwargs: {new_kwargs}")
        return func(*new_args, **new_kwargs)

    return wrapper
