import json

# read training dataset contents
with open(r"c:\Users\malik\Documents\GitHub\FewRel\data\train.json") as input_json_file:
    loaded_json_data = json.load(input_json_file)

    print("Number of relations: " + str(len(loaded_json_data)))

    for relation_name, relation_instances in loaded_json_data.items():
        print("\n" + str(relation_name) + " has " + str(len(relation_instances)) + " elements")

        for relation_instance in range(int((len(relation_instances)*0.01))):
            print(relation_instances[relation_instance])