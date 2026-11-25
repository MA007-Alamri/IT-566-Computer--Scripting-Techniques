"""Entry point for the family expenses application."""

import yaml

def main():
    with open("config/family_expenses_config.yaml", "r") as expense_file:
       expense_config = yaml.safe_load(expense_file)

    print(expense_config["meta"]["app_name"])


if __name__ == "__main__":
    main()



