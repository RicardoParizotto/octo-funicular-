

#!/usr/bin/python

import json
from pprint import pprint

#JSON files produced by p4c are a dic of following lists: 
#(1) header type
#(2) headers
#(3) parsers


'''
 Merger must be capable of produce a new JSON file to the composition
'''

class Merger:

    def __init__(self):
        parsers = []
        newP4Program = {}


    def add_newState():
    #adds the new state to the newP4Program specification

    def merge_States(): 
    #just merge if headers definition are equivalent
    #ifnot, notify the operator to help on this

    def add_newTransition(sourceState, newTransition):
    #add a new transition to the sourceState of the newP4Program

    def verify_Loops():
    #verify if the composition have loops



    def parser_Composition(mainP4Program, modularp4Program):

        for mainParserState in mainP4Program['parsers'][0]['parse_states']:
            for modularParserState in modularP4Program['parsers'][0]['parser_states']:
                if (mainParserState == modularParserState):



    def parser_Composition(mainP4Program, modularP4Program):

        #new JSON receives this
        header_types = mainP4Program['header_types']
        #+header_types of the modularp4

        newProgram = {}

        #for all transition keys of program 1
        #search for 

        for mainParserStates in mainP4Program['parsers'][0]['parse_states']:
            #newProgram.add(k)

            transition = []
            parser_states = []

            parser_states.append(modularP4Program['parsers'][0]['parse_states'][0]['parser_ops'])

            for modularParserStates in modularP4Program['parsers'][0]['parse_states']:

                #
                if (mainParserStates['transition_key'] == modularParserStates['transition_key']) and modularParserStates['transition_key']:
                    transition.append(k['transitions'])
                    newProgram['transition_key'] = k['transition_key']
                    for m in j['transitions']:
                        if m not in k['transitions']:
                            print('add_transition')




        newProgram['transition'] = transition
        newProgram['parser_states'] = parser_states
                        
        file = open('newProgram.json', 'w')
        file.write(json.dumps(newProgram)) 
        #parser = basis_code['parsers'][0]['parse_states'][0]['transition_key']


        #to all transition keys:

        #print (basis_code['parsers'][0]['parse_states'][0]['transition_key'])
        #
        #add (modular_code['parsers'][0]['parse_states'][0]['transitions']) that are on the modular_code and not on the basis code


        #parser_states_must have the same name. Similiarlly to what happens on ltsa tools.

        #pprint(data)


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
 