class parser_composition:
    table_names = []
    action_names = []

    def __init__(self, src_p4):
        self.it_lines = 0
        self.it_symbols = 0
        self.colchetes = 0
        self.src_code = src_p4
        self.buffer_ = []
        self.apply_block = []

    #just load a block between '{' and '}'
    #all recursive calls inside the block are loaded with it
    def parse_codeBlock(self):
        local_buffer = []
        while True:
            if(self.src_code[self.it_lines] == '{'):
                self.colchetes = self.colchetes + 1
            elif(self.src_code[self.it_lines] == '}'):
               if(self.colchetes == 0):
                   return local_buffer
               else:
                   self.colchetes = self.colchetes - 1
            local_buffer.append(self.src_code[self.it_lines])
            self.it_lines = self.it_lines + 1
        return -1     

    def parse_name(self):
        _name = []
        while true:
            if(src_code[it_lines] != '{'):
                _name.append(src_code[it_lines])
            else:
                break
            it_lines = it_lines + 1
        return trim(_name)


    def scan_table_def(self):
        table_ = ['t', 'a', 'b', 'l', 'e', 'n', '{', '*', '}']
        buffer_ = []

        while True:
            if apply_[self.it_symbols] == '*':
                return self.parse_codeBlock(self)
            else:
                #keep parsing
                if(apply_[self.it_symbols] == self.src_code[it_lines]):
                    if(self.src_code[self.it_symbols] == '{'):
                        self.colchetes = self.colchetes + 1
                    self.it_symbols = self.it_symbols + 1
                else:
                    self.it_symbols = 0;
            it_lines = it_lines + 1


    def scan_apply(self):
        apply_ = ['a', 'p', 'p', 'l', 'y', ' ','{', '*', '}']

        while True: 
            #print self.src_code[self.it_lines]
            #scan main block
            if (apply_[self.it_symbols] == '*'):
                self.apply_block = self.parse_codeBlock()
                return self.apply_block
            else:
                #keep parsing
                if(apply_[self.it_symbols] == self.src_code[self.it_lines]):
                    if(self.src_code[self.it_symbols] == '{'):
                        self.colchetes = self.colchetes + 1
                    self.it_symbols = self.it_symbols + 1
                else:
                    self.it_symbols = 0;

            self.it_lines = self.it_lines + 1


    def scan_control_block(self):
        '''TODO
        > scan command
        
            if is a table definition
                table_names.append(scan_table())
            if is a action
                action_names.append(scan_action())
            if is a apply
                control_block = scan_apply
        '''

        with open('your_file.txt', 'w') as f:
            for item in self.apply_block:
                f.write("%s" % item)