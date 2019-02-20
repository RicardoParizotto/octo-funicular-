import sys
from p4module import load_p4module
from assemble import assemble_P4

class process_commandline:
    modules_ = []
    operators = []

    #im not sure if these instances are here
    tables_ = []
    actions_ = []
    parser_ = ''

    def __init__(self):
        self.comp = program_catalogue()
        
        catalogue = """{
         meta.context_control = 1;
         meta.extension_id1 = prog;
        } """

        shadow = """{
           key = {
              hdr.ethernet.dstAddr: lpm;
           }
           actions = {
               set_chaining;
               NoAction;
           }
           size = 1024;
           default_action = NoAction();
        }"""

        #more param to the set_chatining
        self.actions_.append({'set_chaining': ['(egressSpec_t prog)', catalogue]})
        self.tables_.append({'shadow':shadow})

    def read_file(self, file):
        f = open(file, 'r')
        return f.read()

    def carry_composition(self, Host, Extension):
        if not isinstance(Host, load_p4module):
            Host = load_p4module(self.read_file(Host))
            print('li o host')


        print(Host.load.apply_['MyIngress'])
    
        
        if not isinstance(Extension, load_p4module):                    
            Extension = load_p4module(self.read_file(Extension))
            print('li a extensao')



        print(Host.load.apply_['MyIngress'])
        print(Extension.load.apply_['MyIngress'])


        self.build_composition(Host, Extension)

        return 'file_name'

    #just calculates de union of table definitions
    def table_union(self, extension):
        self.tables_ = self.tables_ + extension.tables_

    def action_union(self, extension):
        self.actions_ = self.actions_ + extension.actions_

    #this builds the new program
    def build_composition(self, host, extension):
        #merge tables (this is the naive way)
        #the paralle composition also utilize the shadow, the catalogue and the apply. 
        #this need to be moved from here
        self.table_union(host.load)
        self.table_union(extension.load)
        self.action_union(host.load)
        self.action_union(extension.load)

        self.parser_ = self.build_parser_extension(extension)
        #This need to be connected to the composition calc

        self.comp.write_composition_gambia(self.comp.calc_sequential_apply(host.load, extension.load))


        #TODO packet parser union
        #concatenate applys from the host and the extension
        assembler = assemble_P4()
        assembler.assemble_new_program(self.parser_, self.actions_, self.tables_, self.comp.applys)

    def build_parser_extension(self, module):
        #remember that packet extracts are optinal
        #remember also that selects may follow from transitions

        parser_def = """
            parser """ + module.parser.parser_name + module.parser.parser_param +""" {\n\n"""

        for item in module.parser.parser_:
            parser_def = parser_def + """ state """ + item + """ { \n"""

            if(item in module.parser.extract_):
                parser_def = parser_def + 'packet.extract' + str(module.parser.extract_[item] + ';\n')

            if(item in module.parser.selects_):
                parser_def = parser_def + 'transition select' + str(module.parser.selects_[item] + '{\n')

            for transition in module.parser.parser_[item]:
                if(transition == '*'):
                    parser_def = parser_def + 'transition ' + str(module.parser.parser_[item]['*']) + """; \n"""
                else:
                    #packet_extract(attr);
                    parser_def = parser_def + str(transition) + ':' + str(module.parser.parser_[item][transition]) + """; \n"""
            if(item in module.parser.selects_):
                parser_def = parser_def + """}\n"""  #close the state brackets    
            parser_def = parser_def + """}\n"""  #close the state brackets
        parser_def = parser_def + "}\n"  #close the parser brackets

        return parser_def

class program_catalogue:
    programs = []

    def __init__(self):
        self.applys = """
        apply {
            shadow.apply();

            if(meta.context_control == 1){ \n"""

    def write_composition_gambia(self, skeleton):
        #if sequential composition the extension id is always 1. Different ids can be used to
        #point to more modules
        self.applys = self.applys + skeleton +"""
            }
        }
        """

    def calc_sequential_apply(self, host, extension):

        return  """if(meta.extension_""" + "host_id" + """==1) { \n
                    """ + ''.join(map(str, host.apply_['MyIngress'])) + """
                }if(meta.extension_""" + "host_id" + """==666){
                    """ + ''.join(map(str, extension.apply_['MyIngress'])) + """
                }
            """
 
    def calc_parallel_apply(self, extension):
        return """if(meta.extension_""" + programs.index(p4module) + """==1) {
                    """ + ''.join(map(str, extension.apply_['MyIngress'])) + """
                } else
            """


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
    p.carry_composition(sys.argv[1], sys.argv[2])
