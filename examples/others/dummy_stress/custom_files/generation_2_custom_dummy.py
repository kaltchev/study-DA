"""This is a template script for generation 1 of simulation study, in which ones generates a
particle distribution and a collider from a MAD-X model."""

# ==================================================================================================
# --- Imports
# ==================================================================================================

# Import standard library modules
import logging
import os
import time

# Import third-party modules
import numpy as np

# Import user-defined modules
from study_da.utils import (
    load_dic_from_path,
    set_item_in_dic,
    write_dic_to_path,
)

# Set up the logger here if needed


# ==================================================================================================
# --- Script functions
# ==================================================================================================
def multiply_and_dump(configuration):
    y = float(configuration["y"])
    x_plus_z = float(configuration["result"]["x_plus_z"])

    # Dump result to txt file
    with open("result.txt", "w") as f:
        f.write(str(x_plus_z * y))


# ==================================================================================================
# --- Parameters placeholders definition
# ==================================================================================================
dict_mutated_parameters = {}  ###---parameters---###
path_configuration = "{}  ###---main_configuration---###"
# In case the placeholders have not been replaced, use default path
if path_configuration.startswith("{}"):
    path_configuration = "config.yaml"

# ==================================================================================================
# --- Script for execution
# ==================================================================================================

if __name__ == "__main__":
    logging.info("Starting custom script")

    # Load full configuration
    full_configuration, ryaml = load_dic_from_path(path_configuration)

    # Mutate parameters in configuration
    for key, value in dict_mutated_parameters.items():
        set_item_in_dic(full_configuration, key, value)

    # Add x and z and write to configuration
    multiply_and_dump(full_configuration)

    # Dump configuration
    name_configuration = os.path.basename(path_configuration)
    write_dic_to_path(full_configuration, name_configuration, ryaml)

    # Wait random time
    time.sleep(np.random.randint(1, 30))

    logging.info("Script finished")
