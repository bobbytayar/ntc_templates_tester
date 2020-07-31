#!/usr/bin/env python3

import textfsm
import yaml
import sys
import json
from pathlib import Path

def create_file(text_file):
    Path('./{}'.format(text_file)).touch()

def raw_to_json(raw_text, yml_text, text_fsm_template):
    input_file = open(raw_text, encoding='utf-8')
    raw_text_data = input_file.read()
    input_file.close()
    template = open(text_fsm_template)
    read_fsm = textfsm.TextFSM(template)
    json_result = read_fsm.ParseText(raw_text_data)
    json_output = [dict(zip(read_fsm.header, row)) for row in json_result]
    print('json result from parse:   {}'.format(json_output))
    return json_output

def json_to_yml(json_result, yml_text):
    yaml_output = yaml.dump(json_result)
    print("---\nparsed_sample:\n{}".format(yaml_output), file=open(yml_text, "a"))
    print(yaml_output)
 
def main():
    
    command = 'cisco_ios_show_environment_power_all'

    raw_text = '{}.raw'.format(command)
    yml_text = '{}.yml'.format(command)
    textfsm = '{}.textfsm'.format(command)
    textjson = '{}.json'.format(command)
    

    create_file(raw_text)
    create_file(yml_text)
    create_file(textfsm)
    create_file(textjson)
    
    json_work = raw_to_json(raw_text, yml_text, textfsm)
    json_to_yml(json_work, yml_text)    

if __name__== "__main__" :
    main()










