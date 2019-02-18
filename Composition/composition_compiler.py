import sys
from p4module import load_p4module

class process_commandline:

    modules_ = []
    operators = []

    def read_file(self, file):
        f = open(file, 'r')
        return f.read()

    def parallel_composition(self, Host, Extension):
        '''
        TODO
        interpret commands
        read P4 files
        push modules and operators into queue
        process the composition
        '''
        l = load_p4module(self.read_file(Host))
        x = load_p4module(self.read_file(Extension))
        print(x.parser.parser_)

        x.write_parser_extension(x)


        #l.sequential_composition(x.load)

        return 'file_name'

    def sequential_composition(self, Host, Extension):
        l = load_p4module(self.read_file(Host))
        x = load_p4module(self.read_file(Extension))

        l.sequential_composition(x)


        return 'file_name'

if __name__ == "__main__":
    """
    TODO
    #this should open the basis code json
    #scan the command line (sw, command)
    #parse commandline
    #open files
    #compose
    """

    p = process_commandline()
    p.sequential_composition(sys.argv[1], sys.argv[2])
