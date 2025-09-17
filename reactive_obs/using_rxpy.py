# see https://rxpy.readthedocs.io/en/latest/get_started.html

# we may need to pip install reactivex
from reactivex import create
from reactivex import of, operators as op

# def push_five_strings(observer, scheduler):
#     observer.on_next("Alpha")
#     observer.on_next("Beta")
#     observer.on_next("Gamma")
#     observer.on_next("Delta")
#     observer.on_next("Epsilon")
#     observer.on_completed()

# # here we create an observable (in this case, from a function)
# source = create(push_five_strings)

# source.subscribe(
#     on_next = lambda i: print("Received {0}".format(i)),
#     on_error = lambda e: print("Error Occurred: {0}".format(e)),
#     on_completed = lambda: print("Done!"),
# )

# or...
source = of("Alpha", "Beta", "Gamma", "Delta", "Epsilon") # this would be an async stream or streams of data

source.subscribe(lambda value: print("Received {0}".format(value)))

# furthermore...

source = of("Alpha", "Beta", "Gamma", "Delta", "Epsilon")

composed = source.pipe(
    op.map(lambda s: len(s)),
    op.filter(lambda i: i >= 5)
)
composed.subscribe(lambda value: print("Received {0}".format(value)))