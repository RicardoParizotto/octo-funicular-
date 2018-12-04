
#!/usr/bin/python


import json
from pprint import pprint

#JSON files produced by p4c are a dic of following lists: 
#(1) header type
#(2) headers
#(3) parsers
#(4) (deparsers)
#(5) entire control flow
'''
 Merger must be capable of produce a new JSON file to the composition
'''

class Modularity_Analysis:
    def __init__(self):
        print('do the fucking analysis bro')

    #verify if the parser composition have loops or nom-determinism
    def verify_Loops(self):
        print('verify if the composition have loops')
  
    def modularity_Analysis():
        #verify_Loops()
        print ('do nothing')




class Merger:
    def __init__(self, baseProgram):
        parsers = []
        self.newP4Program = baseProgram    #this is the new created program

    #adds the new state to the newP4Program specification
    def add_newState(self, newState):
        self.newP4Program['parsers'][0]['parse_states'].append(newState)

    #add a new transition to the sourceState of the newP4Program
    def add_newTransition(self, parser_state, newTransition):
        parser_state['transitions'].append(newTransition)
        #this probably don't work
        #actually it works pretty fine if transitions are made using the same attribute
    
    #composition of header definitions
    def header_types_composition(self, modularP4Program):
        header_names = []

        for header in self.newP4Program['header_types']:
            header_names.append(header['name'])

        for header_instance in modularP4Program['header_types']:
            if(header_instance['name'] not in header_names):
                self.newP4Program['header_types'].append(header_instance)
   
    #add new header instance to the newP4Program
    def header_instances_composition(self, modularP4Program):
        header_names = []

        for header in self.newP4Program['headers']:
            header_names.append(header['name'])

        for header_instance in modularP4Program['headers']:
            if(header_instance['name'] not in header_names):
                print('adding header instance:' + header_instance['name'])
                self.newP4Program['headers'].append(header_instance)
    

    def parser_composition(self, modularP4Program):
        visitedStates = []      #thats for the search algorithm

        for mainParserState in self.newP4Program['parsers'][0]['parse_states']:
            for modularParserState in modularP4Program['parsers'][0]['parse_states']:
                #for now we just compare names of the parser state
                if(mainParserState['name'] == modularParserState['name']):  
                    #mark modularParserState as visited
                    visitedStates.append(modularParserState['name'])

                    transition_name = []
                    for main_transitions in mainParserState['transitions']:                       
                        transition_name.append(main_transitions['next_state'])        

                    for stateTransition in modularParserState['transitions']:
                        if stateTransition['next_state'] not in transition_name:
                            #add transitions to the state mainParserState
                            print('adding transition:' + stateTransition['next_state'])

                            #this is the case where the host state has no transitions
                            if not mainParserState['transition_key']:
                                mainParserState['transition_key'] = modularParserState['transition_key']

                            self.add_newTransition(mainParserState, stateTransition)

        #this adds states that were not visited by our search algorithm                    
        for modularParserState in modularP4Program['parsers'][0]['parse_states']: 
            if(modularParserState['name'] not in visitedStates):
                self.add_newState(modularParserState)    
        #add states that were not visited (that are new states)
        #adding new states may need to add new header instances also.
        #add header instance

    def pipeline(self, extension):


        #new tables must be inserted here
        self.newP4Program['pipelines'][0]['tables'][0]['id']

        #TODO change this.
        #the shadow table must be the first to process packets
        self.newP4Program['pipelines'][0]['init_table']




    def composition(self, extension):
        #TODO  
        ##need disambiguation here :(   
        ##we may insert constructs with repeated id's. This lead to deployment errors. 
        self.parser_composition(extension)
        self.header_types_composition(extension)
        self.header_instances_composition(extension)

        self.save_newP4Program()

    #just save the merged code to the main diretory     
    def save_newP4Program(self):
        file = open('newP4Program.json', 'w')
        print('Saving the new file')
        file.write(json.dumps(self.newP4Program,  indent=4)) 



