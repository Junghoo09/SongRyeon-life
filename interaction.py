import importlib.util
import os

from informations import first_information, interaction_list


operator_path = os.path.join(os.path.dirname(__file__), "operator.py")
spec = importlib.util.spec_from_file_location("project_operators", operator_path)
operator_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(operator_module)


if __name__ == "__main__":
    print("교류 전:", first_information)
    operator_module.interaction_operators[0](first_information, interaction_list)
    print("교류 후:", first_information)
