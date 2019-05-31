import json
import configparser

# read training dataset contents for manipulation
config = configparser.ConfigParser()
config.read('properties.ini')
training_file = config['FewRel']['Training_Data_JSON_File_Name_and_Path']
test_file = config['FewRel']['Test_Data_JSON_File_Name_and_Path']

with open(training_file) as input_json_file:
    loaded_json_data = json.load(input_json_file)

    print("Number of relations: " + str(len(loaded_json_data)))

    for relation_name, relation_instances in loaded_json_data.items():
        print("\n" + str(relation_name) + " has " + str(len(relation_instances)) + " elements")

        number_of_items_to_delete = int((len(relation_instances)*0.90))
        print("" + str(relation_name) + " will be reduced by " + str(number_of_items_to_delete) + " elements")
        number_of_items_deleted = 0
        while number_of_items_deleted < number_of_items_to_delete:
            relation_instances.pop()
            number_of_items_deleted += 1

        print("" + str(relation_name) + " has " + str(len(relation_instances)) + " elements after selection or deletion")

# save test dataset
with open(test_file, "w") as outfile:
    json.dump(loaded_json_data, outfile)