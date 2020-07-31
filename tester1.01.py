#!/usr/bin/env python3

import textfsm
import yaml
import sys
import json
from pathlib import Path

def create_file(text_file):
    Path('./{}'.format(text_file)).touch()

def raw_to_json(raw_text, parsed_text, text_fsm_template):
    input_file = open(raw_text, encoding='utf-8')
    raw_text_data = input_file.read()
    input_file.close()
    template = open(text_fsm_template)
    read_fsm = textfsm.TextFSM(template)
    json_result = read_fsm.ParseText(raw_text_data)
    print('json result from parse:   {}'.format(json_result))
    return json_result

def json_to_yml(json_result, parsed_text):
    yaml_output = yaml.dump(json_result)
    print(yaml_output, file=open(parsed_text, "a"))
    print(yaml_output)
 
def main():
    
    command = 'cisco_ios_show_environment_power_all'

    raw_text = '{}.raw'.format(command)
    parsed_text = '{}.yml'.format(command)
    text_fsm_template = '{}.textfsm'.format(command)

    create_file(raw_text)
    create_file(parsed_text)
    create_file(text_fsm_template)
    
    json_work = raw_to_json(raw_text, parsed_text, text_fsm_template)
    json_to_yml(json_work, parsed_text)    

if __name__== "__main__" :
    main()










