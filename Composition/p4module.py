
from parser import parser_composition

class load_p4module:
    #there is a need to include registers
    #but im too lazy now
    tables_ = []
    actions_ = []
    apply_ = []


    def __init__(self, host):
        self.load = parser_composition(host)
        self.load.scan_control()

    #just calculates de union of table definitions
    def table_union(self, extension):
        self.tables_ = self.tables_ + extension.tables_

    def action_union(self, extension):
        self.actions_ = self.actions_ + extension.actions_

    def assemble_new_program(self, extension):
        '''
        open and write the merged structures to a new file
        it is importante to note that the verification must come earlier
        '''
        with open('composition.p4', 'w') as f:
            for item in actions:
                for action in item: #action name
                    f.write("%s" % "action " + action)
                    for j in item[action]:
                        f.write("%s" % j)         
            for item in tables:
                for table in item:   #table name
                    f.write("%s" % "table " + table)
                    for j in item[table]:
                        f.write("%s" % j)  


    #this actually builds the new program    
    def parallel_composition(self):
        self.parser.scan_control_block()

        print ("actions" + str(self.parser.actions_))
        print("tables" + str(self.parser.tables_))
        print ("apply content" + str(self.parser.apply_block))

        with open('composition.txt', 'w') as f:
            for item in self.parser.tables_:
                for table in item:
                    f.write("%s" % "table " + table)
                    for j in item[table]:
                        f.write("%s" % j)


    def sequential_composition(self, extension):
        #merge tables (this is the naive way)
        tables = self.load.tables_  + extension.tables_
        actions = self.load.actions_ + extension.actions_ 


        catalogue = """    action set_chaining(egressSpec_t prog){
         meta.context_control = 1;      
         meta.extension_id1 = prog;
        } """


        shadow = """table shadow{
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


        #if sequential composition the extension id is always 1. extension

        applys = """
        apply {
            shadow.apply();

            if(meta.context_control == 1){
        """ + """ if(meta.extension_id1 == 1){ """ + """
        """ + ''.join(map(str, extension.apply_['MyIngress'])) + """
            }
        """

        #here there is a need to concatenate applys from the host and the extension

        print(catalogue)
        print(shadow)
        print(applys)

