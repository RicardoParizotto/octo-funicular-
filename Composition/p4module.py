
from parser import parser_control_flow
from packet_parser import packet_parser

class load_p4module:
    #there is a need to include registers
    #but im too lazy now
    tables_ = []
    actions_ = []

    def __init__(self, host):
        self.load = parser_control_flow(host)
        self.load.scan_control()
        self.parser = packet_parser(host)
        self.parser.scan_control()

    #just calculates de union of table definitions
    def table_union(self, extension):
        self.tables_ = self.tables_ + extension.tables_

    def action_union(self, extension):
        self.actions_ = self.actions_ + extension.actions_

    #this actually builds the new program
    def parallel_composition(self):
        return 'TODO'


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



