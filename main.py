import json
from pathlib import Path
from runzero_port_switch_mapper.utils import parse_inventory_items, write_csv_output


def main():
    input_file = Path("data/assets-20231017075514-Tomra-tag_lier.json")
    output_file = Path("output/output.csv")

    with open(input_file, "r") as f:
        input_inventory = json.loads(f.read())
        inventory = parse_inventory_items(input_inventory)
        write_csv_output(output_file, inventory)


if __name__ == "__main__":
    main()
