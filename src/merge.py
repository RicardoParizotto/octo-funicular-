

#!/usr/bin/python

import json
from pprint import pprint

#JSON files produced by p4c are a dic of following lists: 
#(1) header type
#(2) headers
#(3) parsers

parsers = []

#first file 
#this should be the basis fale for the merge
with open('advanced_tunnel.json') as f:
    basis_code = json.load(f)

#second file
#this must be the modular one

with open('modularp4.json') as k:
    modular_code = json.load(k)

#new JSON receives this
header_types = basis_code['header_types']
#+header_types of the modularp4


newProgram = {}

#for all transition keys of program 1
#search for 

for k in basis_code['parsers'][0]['parse_states']:
	#newProgram.add(k)

	transition = []
	parser_states = []

	parser_states.append(modular_code['parsers'][0]['parse_states'][0]['parser_ops'])

	for j in modular_code['parsers'][0]['parse_states']:
		if (k['transition_key'] == j['transition_key']) and j['transition_key']:
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