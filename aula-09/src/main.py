from log_decorator import double_args_decorator


@double_args_decorator
def soma(x, y):
    return x + y


print(soma(2, 4))

print(soma(x=5, y=3))
