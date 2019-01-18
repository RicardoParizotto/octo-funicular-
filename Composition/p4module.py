
from parser import parser_composition

class load_p4module:
    #there is a need to include registers
    #but im too lazy now
    def __init__(self, host):
        self.parser = parser_composition(host)


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
        
