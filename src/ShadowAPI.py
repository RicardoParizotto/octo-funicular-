

import sys
import json

from merge import Merger


if __name__ == "__main__":

    """ss
    TODO
    passe file names as a param for __init__
    """
    #this should open the basis code json
    with open(sys.argv[1]) as f:
        baseCode = json.load(f)

    #this must be the modular one json -- extensionn
    with open(sys.argv[2]) as k:
       extension = json.load(k)
 
    shadowGuard = Merger(baseCode)
    shadowGuard.composition(extension)

    #sw1.addProgram(firewall.p4)