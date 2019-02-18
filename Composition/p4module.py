
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

    '''
    open and write the merged structures to a new file
    it is importante to note that the verification must come earlier
    '''
    def assemble_new_program(self, parser, actions, tables):
        with open('composition.p4', 'w') as f:

            f.write("%s" % parser)

            control = """\n\n\ncontrol MyIngress(inout headers hdr,
                  inout metadata meta,
                  inout standard_metadata_t standard_metadata) {
            """

            f.write("%s" % control)    

            for item in actions:
                for action in item: #action name
                    f.write("%s" % "action " + action)
                    for j in item[action]:
                        if isinstance(j, list):
                            f.write("%s\n\n" % ''.join(map(str, j)))
                        else:
                            f.write("%s" % j)

            for item in tables:
                for table in item:   #table name
                    f.write("%s" % "table " + table)
                    for j in item[table]:
                        f.write("%s" % j)
                    f.write("\n\n")
            f.write("%s" % "}")

    #this actually builds the new program
    def parallel_composition(self):
        self.parser.scan_control_block()

        print ("actions" + str(self.parser.actions_))
        print("tables" + str(self.parser.tables_))
        print ("apply content" + str(self.parser.apply_block))


    def sequential_composition(self, extension):
        #merge tables (this is the naive way)
        tables = self.load.tables_  + extension.tables_
        actions = self.load.actions_ + extension.actions_

        catalogue = """{
         meta.context_control = 1;
         meta.extension_id1 = prog;
        } """

        actions.append({'set_chaining': ['(egressSpec_t prog)', catalogue]})

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

        tables.append({'shadow':shadow})

        #if sequential composition the extension id is always 1. Different ids can be used to

        applys = """
        apply {
            shadow.apply();

            if(meta.context_control == 1){
        """ + """ if(meta.extension_id1 == 1){ """ + """
        """ + ''.join(map(str, extension.load.apply_['MyIngress'])) + """
            }
        """

        parser = self.write_parser_extension(extension)

        self.assemble_new_program(parser, actions, tables)

        #here there is a need to concatenate applys from the host and the extension

    def write_parser_extension(self, extension):
        #remember that packet extracts are optinal
        #remember also that selects may follow from transitions

        parser_def = """
            parser """ + self.parser.parser_name + self.parser.parser_param +""" {\n\n"""

        for item in self.parser.parser_:
            parser_def = parser_def + """ state """ + item + """ { \n"""
            for transition in self.parser.parser_[item]:
                if(transition == '*'):
                    print('transition ' + str(self.parser.parser_[item]['*']) )
                else:
                    print(str(transition) + ' ' + str(self.parser.parser_[item][transition]))
                    #packet_extract(attr);
                    parser_def = parser_def + """
                    """ + str(self.parser.parser_[item]) + """;"""
            parser_def = parser_def + """}"""
        parser_def = parser_def + "}"

        return parser_def



class program_catalogue:
    programs = []

    def write_composition_gambia(self):
        programs = []

        #if sequential composition the extension id is always 1. Different ids can be used to
        #point to more modules

        applys = """
        apply {
            shadow.apply();

            if(meta.context_control == 1){"""

        for p4module in programs:
            applys = applys + calc_sequential_apply(p4module)

        applys = applys + """
            }
        }

        """


    def calc_sequential_apply(self, extension):
        return  """if(meta.extension_""" + programs.index(p4module) + """==1) {
                    """ + ''.join(map(str, extension.apply_['MyIngress'])) + """
                }
            """



    def calc_parallel_apply(self, extension):
        return """if(meta.extension_""" + programs.index(p4module) + """==1) {
                    """ + ''.join(map(str, extension.apply_['MyIngress'])) + """
                } else
            """


