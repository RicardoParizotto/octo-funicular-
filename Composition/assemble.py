import sys  


class assemble_P4:
    '''
    open and write the merged structures to a new file
    it is importante to note that the verification must come earlier
    '''
    def assemble_new_program(self, parser, actions, tables, apply_):
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

            f.write("%s" % apply_)
