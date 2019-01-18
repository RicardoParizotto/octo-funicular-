import sys
from p4module import load_p4module


class process_commandline:

    modules_ = []
    operators = []

    def read_file(self, file):
        f = open(file, 'r')
        return f.read()

    def parser_command_line(self, Host):



        l = load_p4module(self.read_file(Host))

        l.parallel_composition()

        '''
        TODO 
        
        interpret commands

        read P4 files

        push modules and operators into queue

        process the composition
        '''

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
    p.parser_command_line(sys.argv[1])
