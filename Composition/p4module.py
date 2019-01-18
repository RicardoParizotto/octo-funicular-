
from parser import parser_composition

class load_p4module:
    #there is a need to include registers
    #but im too lazy now
    def __init__(self, host):
        self.parser = parser_composition(host)


    def parallel_composition(self):
        #print("ERRO")

        self.parser.scan_control_block()

        print ("actions" + str(self.parser.actions_))
        print(self.parser.tables_)
        print (self.parser.apply_block)


        '''
        with open('your_file.txt', 'w') as f:
            for item in self.apply_block:
                f.write("%s" % item)
        '''
