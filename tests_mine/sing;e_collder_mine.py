"""This is a template script for generation 1 of simulation study, in which ones generates a
particle distribution and a collider from a MAD-X model."""

# ==================================================================================================
# --- Imports
# ==================================================================================================
#%%
# Import standard library modules
import logging
import os
import sys
sys.path.append("../")  # Adjust the path to your study_da module

## Import third-party modules
#sys.path.append("/home/kaltchev/study-DA/study_da")

# Import user-defined modules
from study_da.generate import MadCollider, ParticlesDistribution
from study_da.utils import (
    load_dic_from_path,
    set_item_in_dic,
    write_dic_to_path,
)

# Set up the logger here if needed


# %%

# Set up the logger here if needed

#%%
# ==================================================================================================
# --- Script functions
# ==================================================================================================
def build_distribution(config_particles):
    # Build object for generating particle distribution
    distr = ParticlesDistribution(config_particles)

    # Build particle distribution
    particle_list = distr.return_distribution_as_list()

    # Write particle distribution to file
    distr.write_particle_distribution_to_disk(particle_list)


def build_collider(config_mad):
    # Build object for generating collider from mad
    mc = MadCollider(config_mad)

    # Build mad model
    mad_b1b2, mad_b4 = mc.prepare_mad_collider()

    # Build collider from mad model
    collider = mc.build_collider(mad_b1b2, mad_b4)

    # Twiss to ensure everything is ok
    mc.activate_RF_and_twiss(collider)

    # Clean temporary files
    mc.clean_temporary_files()

    # Save collider to json
    mc.write_collider_to_disk(collider)


# ==================================================================================================
# --- Parameters placeholders definition
# ==================================================================================================
dict_mutated_parameters = {}
path_configuration = "{}"
path_root_study = "/home/kaltchev/study-DA/examples/in_docs_case_studies/simple_collider/single_job_study_hllhc16"

# In case the placeholders have not been replaced, use default path

if path_configuration.startswith("{}"):
    path_configuration = "config.yaml"

if path_configuration.startswith("{}"):    
    path_configuration = "config_J000.yaml"

if path_root_study.startswith("{}"):
    path_root_study = "."

sys.path.append(path_root_study)
# Import modules placed at the root of the study here
# ==================================================================================================
# --- Script for execution
# ==================================================================================================

if __name__ == "__main__":
    logging.info("Starting script to build particle distribution and collider")

    # Load full configuration
    full_configuration, ryaml = load_dic_from_path(path_configuration)

    # Mutate parameters in configuration
    for key, value in dict_mutated_parameters.items():
        set_item_in_dic(full_configuration, key, value)

    # Dump configuration
    name_configuration = os.path.basename(path_configuration)
    write_dic_to_path(full_configuration, name_configuration, ryaml)

    # Build and save particle distribution
    build_distribution(full_configuration["config_particles"])

    # Build and save collider
    build_collider(full_configuration["config_mad"])

    logging.info("Script finished")


# %%
