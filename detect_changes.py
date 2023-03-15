import sys
import yaml
from deepdiff import DeepDiff


def yaml_as_dict(my_file):
    my_dict = {}
    with open(my_file, 'r') as fp:
        docs = yaml.safe_load_all(fp)
        for doc in docs:
            for key, value in doc.items():
                my_dict[key] = value
    return my_dict


def validate_input_arguments():
    print('Number of input arguments:', len(sys.argv) - 1)
    if (len(sys.argv)) == 1:
        print('No file passed for comparison. Script stopped.')
        exit()
    elif (len(sys.argv)) == 2:
        print('One file passed for comparison. Two expected script stopped.')
        exit()
    elif (len(sys.argv)) == 3:
        print('First file:', sys.argv[1], '\nSecond file:', sys.argv[2])


def validate_input_extensions():
    if not sys.argv[1].endswith('yaml') or not sys.argv[2].endswith('yaml'):
        print('Incorrect input file format. Yaml expected.')
        exit()


if __name__ == '__main__':
    validate_input_arguments()
    validate_input_extensions()
    yaml_file1 = sys.argv[1]
    yaml_file2 = sys.argv[2]
    yaml_file1_as_dict = yaml_as_dict(yaml_file1)
    yaml_file2_as_dict = yaml_as_dict(yaml_file2)
    ddiff = DeepDiff(yaml_file1_as_dict, yaml_file2_as_dict, ignore_order=True)
    print(ddiff)
