# Example class to start a Waitress server as a windows service
# the specific use case is running Waitress as a windows server using pywin32
# The Waitress docs only show how to use waitress-serve, but since waitress-serve is blocking
# you don't get a return value, which makes it impossible to gracefully stop the Waitress server
# from a windows service
# However, looking at the waitress-serve code, it's easy to write a custom class

# example pywin32 windows service: https://gist.github.com/drmalex07/10554232
from waitress import serve
import main

serve(main.app, host='0.0.0.0', port=5000)
