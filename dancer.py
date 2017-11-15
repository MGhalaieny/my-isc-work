#script to interact with the dancing library

import sys
from dancing.dance import boogie
moves = sys.argv[1:]

boogie(moves)
