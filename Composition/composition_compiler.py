import sys
from parser import parser_composition


class process_commandline:

    def read_file(self, file):
        f = open(file, 'r')
        g = f.read()

        parser = parser_composition(g)

        print(parser.scan_apply())

        parser.scan_control_block()

    def composition(Extension, Host):
        '''
        TODO 


        '''
        return 'error'

    def parallel_operator(Extension, Host)
        return 'error'


if __name__ == "__main__":

    """ss
    TODO
    passe file names as a param for __init__
    """
    #this should open the basis code json

    #scan the command line (sw, command)

    #parse commandline

    #open files

    #compose
    p = process_commandline()
    p.read_file(sys.argv[1])
