'''
This is a more generic class
that includes parsers of names
reads definitions
and parameters

'''


class lib_parser:
    #init structures to help the scanning process
    def __init__(self, src_p4):
        self.it_lines = 0
        self.it_symbols = 0
        self.src_code = src_p4
        self.code_len = len(self.src_code)

    #just scan the name (id) of a control flow construct
    #its a naive implementation, since
    def parse_name(self):
        _name = ""
        while self.it_lines < self.code_len:
            it = self.src_code[self.it_lines]
            if(it != '{' and it != '(' and it != ';'):
                _name = _name + it
            else:
                break
            self.it_lines = self.it_lines + 1
        return _name.strip()


    #scan constructs that have identificator such as
    #controls, actions and tables definitions
    def scan_def(self, dic_):
        it_symbols = 0

        while self.it_lines < self.code_len:
            if dic_[it_symbols] == '*':
                return True
            else:
                if(dic_[it_symbols] == self.src_code[self.it_lines]):
                    it_symbols = it_symbols + 1
                else:
                    return False
            self.it_lines = self.it_lines + 1

    #load param definitions to a different structure
    #this is necessary just for parsing and rewriting
    def parse_params(self):
        params_ = ""

        while self.src_code[self.it_lines] != ')':
            self.it_lines = self.it_lines + 1
            params_ = params_ + self.src_code[self.it_lines]
        self.it_lines = self.it_lines + 1

        return params_
