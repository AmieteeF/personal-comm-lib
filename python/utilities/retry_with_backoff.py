import time
from typing import Callable, Type, Any

MAX_ATTEMPTS = 5
BASE_DELAY = 1
MAX_DELAY = 32

def retry_with_backoff(
        func: Callable[..., Any], 
        max_attempts: int = MAX_ATTEMPTS, 
        base_delay: int = BASE_DELAY, 
        max_delay: int = MAX_DELAY,
        exception_type: Type[BaseException] = Exception,
        **kwargs,
    ):
    """
    Retries `func()` with exponential backoff if `exception_type` is raised.

    :param func: a callable with no arguments (or use lambda for args)
    :param max_attempts (int): total attempts before giving up
    :param base_delay (int): initial delay in seconds
    :param exception_type (Type[BaseException]): exception class to trigger retry. The default is the Exception superclass.
    :param **kwargs: key-word arguments passed to func.
    """
    next_delay = base_delay
    for attempt in range(max_attempts):
        try:
            return func(**kwargs)  # Call the passed-in function with key-word arguments
        except exception_type as e:
            if attempt == max_attempts - 1:
                raise  # Re-raise after last attempt
            next_delay = min(next_delay, max_delay)
            print(f"Attempt {attempt + 1} failed: {e}. Retrying in {next_delay}s...")
            time.sleep(next_delay)
            
            next_delay *= 2  # Exponential increase
