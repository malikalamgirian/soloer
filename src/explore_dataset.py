import json
import configparser

# read training dataset contents
config = configparser.ConfigParser()
config.read('properties.ini')
training_file = config['FewRel']['Training_Data_JSON_File_Name_and_Path']

with open(training_file) as input_json_file:
    loaded_json_data = json.load(input_json_file)

    print("Number of relations: " + str(len(loaded_json_data)))

    for relation_name, relation_instances in loaded_json_data.items():
        print("\n" + str(relation_name) + " has " + str(len(relation_instances)) + " elements")

        for relation_instance in range(int((len(relation_instances)*0.01))):
            print(relation_instances[relation_instance])