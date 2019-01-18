import sys
from p4module import load_p4module


class process_commandline:

    def read_file(self, file):
        f = open(file, 'r')
        g = f.read()

        parser = parser_composition(g)

        #print(parser.scan_apply())

        parser.scan_control_block()

    def parser_command_line(Extension, Host):

        '''
        TODO 
        
        interpret commands

        read P4 files

        push modules and operators into queue

        process the composition

        '''
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
