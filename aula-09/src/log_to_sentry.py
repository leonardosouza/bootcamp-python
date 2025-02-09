import sentry_sdk
from loguru import logger

logger.add("app.log", format="{time} {level} {message} {file}", level="INFO")

sentry_sdk.init(
    dsn="https://b70aea89a83750fecbc71afb93fa527a@o4508764293103616.ingest.us.sentry.io/4508764295921664",
    # Add data like request headers and IP for users,
    # see https://docs.sentry.io/platforms/python/data-management/data-collected/ for more info
    send_default_pii=True,
    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for tracing.
    traces_sample_rate=1.0,
)


def slow_function():
    import time

    time.sleep(0.1)
    return "done"


def fast_function():
    import time

    time.sleep(0.05)
    return "done"


# Manually call start_profiler and stop_profiler
# to profile the code in between
sentry_sdk.profiler.start_profiler()
for i in range(0, 10):
    slow_function()
    fast_function()
#
# Calls to stop_profiler are optional - if you don't stop the profiler, it will keep profiling
# your application until the process exits or stop_profiler is called.
sentry_sdk.profiler.stop_profiler()

# division_by_zero = 1 / 0


def soma(x, y):
    try:
        return x + y
    except Exception:
        logger.error("falha no calculo", x, y)


soma(4, 5)
soma("5", 5)
