from src import logger
import yaml, json
import joblib, pickle
from dataclasses import dataclass
from box import ConfigBox
from ensure import ensure_annotations
from pathlib import Path

config_path = "config.yaml"
params_path = "params.yaml"


def read_yaml(path: str):
    """Read yaml file from the given path and return a ConfigBox object"""
    try:
        with open(path, "r") as f:
            data = yaml.safe_load(f)
            logger.info(f"Read yaml file from {path}")
            return ConfigBox(data)
    except Exception as e:
        logger.error(f"Error reading yaml file from {path} {e}")


def read_pickle(path: str):
    """Read pickle file from the given path and return a ConfigBox object"""
    try:
        with open(path, "r") as f:
            data = pickle.load(f)
            logger.info(f"Read pickle file from {path}")
            return data
    except Exception as e:
        logger.error(f"Error reading pickle file from {path} {e}")


@ensure_annotations
def save_json(path: Path, data: dict):
    """save json data"""
    try:
        with open(path, "w") as f:
            json.dump(data, f, indent=4)
            logger.info(f"Saved json file to {path}")
    except Exception as e:
        logger.error(f"Error saving json file to {path} {e}")
        
