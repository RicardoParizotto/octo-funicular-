class parser_composition:

    tables_= []
    actions_ = []
    apply_ = []

    #init structures to help the scanning process
    def __init__(self, src_p4):
        self.it_lines = 0
        self.it_symbols = 0
        self.colchetes = 0
        self.src_code = src_p4
        self.code_len = len(self.src_code)
        self.buffer_ = []
        self.apply_block = []
        self.tables = []

    #just load a block between '{' and '}'
    #all recursive calls inside the block are loaded with it
    def parse_codeBlock(self):
        colchetes = 0
        local_buffer = []

        while self.it_lines < self.code_len:
            if(self.src_code[self.it_lines] == '{'):
                colchetes = colchetes + 1
            elif(self.src_code[self.it_lines] == '}'):
               if(colchetes == 1):
                   return local_buffer
               else:
                   colchetes = colchetes - 1

            local_buffer.append(self.src_code[self.it_lines])
            self.it_lines = self.it_lines + 1
        return -1     

    #just scan the name (id) of a control flow construct
    #its a naive implementation, since 
    def parse_name(self):
        _name = ""
        while self.it_lines < self.code_len:
            if(self.src_code[self.it_lines] != '{'):
                _name = _name + self.src_code[self.it_lines]
            else:
                break
            self.it_lines = self.it_lines + 1

        return _name.strip()

    #scan constructs that have identificator such as 
    #controls, actions and tables definitions
    def scan_named_def(self, dic_):
        it_symbols = 0

        while self.it_lines < self.code_len:
            if dic_[it_symbols] == '*':
                name = self.parse_name()
                block = self.parse_codeBlock()
                return { name : block }
            else:
                if(dic_[it_symbols] == self.src_code[self.it_lines]):
                    it_symbols = it_symbols + 1
                else:
                    return -1
            self.it_lines = self.it_lines + 1


    def scan_apply(self):
        apply_ = ['a', 'p', 'p', 'l', 'y', "*"]

        while self.it_lines < self.code_len: 
            #scan main block
            if (apply_[self.it_symbols] == '*'):
                self.apply_block = self.parse_codeBlock()
                return self.apply_block
            else:
                #keep parsing
                if(apply_[self.it_symbols] == self.src_code[self.it_lines]):
                    self.it_symbols = self.it_symbols + 1
                else:
                    self.it_symbols = 0;
            self.it_lines = self.it_lines + 1

    def scan_control_block(self):
        while self.it_lines < self.code_len:
            if(self.src_code[self.it_lines] == 't'):
                #try to read table
                x = self.scan_named_def("table*")
                self.tables_.append(x)
            elif(self.src_code[self.it_lines] == 'a'):
                if(self.src_code[self.it_lines+1] == 'c'):
                    y = self.scan_named_def("action*")
                    self.actions_.append(y)
                else:
                    self.scan_apply()
            self.it_lines = self.it_lines + 1

