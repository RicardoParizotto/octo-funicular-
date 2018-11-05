

#!/usr/bin/python

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
        #add a new transition to the sourceState of the newP4Program
        #this probably don't work

    def verify_Loops(self):
        print('verify if the composition have loops')
    #verify if the composition have loops

    def add_headerInstance(self, headerInstance):
        print ('add new header instance to the newP4Program')
    #add new header instance to the newP4Program


    def parser_Composition(self, mainP4Program, modularp4Program):

        visitedStates = {}

        for mainParserState in mainP4Program['parsers'][0]['parse_states']:
            for modularParserState in modularP4Program['parsers'][0]['parser_states']:
                if (mainParserState == modularParserState):
                    #mark modularParserState as visited
                    visitedStates.add(modularParserState)
                    for stateTransition in modularParserState['transitions']:
                        if stateTransition not in mainParserState['transitions']:
                            #add transitions to the state mainParserState
                            add_transition(mainParserState, stateTransition)

        for modularParserState in modularP4Program['parsers'][0]['parser_states']: 
            if(modularParserState not in visitedStates):
                add_newState(modularParserStates)


        ##need disambiguation here :(            
        for headerInstances in modularP4Program['headers']:
            if(headerInstances not in mainP4Program['headers']):
                add_headerInstance(headerInstance)       


        #add states that were not visited (that are new states)
        #adding new states may need to add new header instances also.
        #add header instance



    #just save the merged code to the main diretory     
    def save_newP4Program(self):
        file = open('newP4Program.json', 'w')
        file.write(json.dumps(newP4Program)) 


def __init__(self):


    """
    TODO
    passe file names as a param for __init__
    """

    #this should open the basis code
    with open('advanced_tunnel.json') as f:
        baseCode = json.load(f)

    #this must be the modular one
    with open('modularp4.json') as k:
       smallModule = json.load(k)
 