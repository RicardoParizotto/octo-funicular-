
#!/usr/bin/python

import sys

import json
from pprint import pprint

#JSON files produced by p4c are a dic of following lists: 
#(1) header type
#(2) headers
#(3) parsers
#(4) (deparsers)

'''
 Merger must be capable of produce a new JSON file to the composition
'''

class Merger:

    def __init__(self):
        parsers = []
        self.newP4Program = {}    #this is the new created program

    def add_newState(self, newState):
        print ('adds the new state to the newP4Program specification')
    #adds the new state to the newP4Program specification

    def merge_States(self): 
        print ('just merge if headers definition are equivalent')
    #just merge if headers definition are equivalent
    #ifnot, notify the operator to help on this

    def add_newTransition(self, state_ID, newTransition):
        self.newP4Program['parsers'][0]['parse_states'][state_ID]['transitions'].append(stateTransition)
        print(batata2)
        #add a new transition to the sourceState of the newP4Program
        #this probably don't work

    def verify_Loops(self):
        print('verify if the composition have loops')
    #verify if the composition have loops

    def add_headerInstance(self, headerInstance):
        print ('add new header instance to the newP4Program')
    #add new header instance to the newP4Program

    def modularity_Analysis():
    #do nothing
        print ('do nothing')


    def parser_Composition(self, mainP4Program, modularP4Program):

        visitedStates = []      #thats for the search algorithm

        for mainParserState in mainP4Program['parsers'][0]['parse_states']:
            for modularParserState in modularP4Program['parsers'][0]['parse_states']:
                if(mainParserState['name'] == modularParserState['name']):  
                    print("batata")         
                #if (mainParserState == modularParserState):
                    #mark modularParserState as visited
                    visitedStates.append(modularParserState)
                    for stateTransition in modularParserState['transitions']:
                        if stateTransition not in mainParserState['transitions']:
                            #add transitions to the state mainParserState
                            add_transition(mainParserState, stateTransition)

        for modularParserState in modularP4Program['parsers'][0]['parse_states']: 
            if(modularParserState not in visitedStates):
                self.add_newState(modularParserState)


        ##need disambiguation here :(            
        for headerInstances in modularP4Program['headers']:
            if(headerInstances not in mainP4Program['headers']):
                add_headerInstance(headerInstance)       

        print('passa aqui')           

        #add states that were not visited (that are new states)
        #adding new states may need to add new header instances also.
        #add header instance

    #just save the merged code to the main diretory     
    def save_newP4Program(self):
        file = open('newP4Program.json', 'w')
        print('teste')
        file.write(json.dumps(self.newP4Program)) 


if __name__ == "__main__":

    """ss
    TODO
    passe file names as a param for __init__
    """

    print('teste')
    #this should open the basis code json
    with open(sys.argv[1]) as f:
        baseCode = json.load(f)

    #this must be the modular one json -- extensionn
    with open(sys.argv[2]) as k:
       extension = json.load(k)

    print('teste')
 
    shadowGuard = Merger()

    shadowGuard.parser_Composition(baseCode, extension)

    shadowGuard.save_newP4Program()