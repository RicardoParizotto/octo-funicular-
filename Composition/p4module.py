
from parser import parser_composition

class load_p4module:
    #there is a need to include registers
    #but im too lazy now
    tables_ = []
    actions_ = []
    apply_ = []


    def __init__(self, host):
        self.load = parser_composition(host)
        self.load.scan_control_block()


    #this actually builds the new program    
    def parallel_composition(self):
        #print("ERRO")

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

        print(self.load.tables_)
        #merge tables (this is the naive way)
        tables = self.load.tables_  + extension.tables_
        actions = self.load.actions_ + extension.actions_ 

        '''
        open and write the merged structures to a new file
        it is importante to note that the verification must come earlier
        '''
        with open('composition.txt', 'w') as f:
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
