import os
from box.exceptions import BoxValueError
import yaml
from textSummarizer.logging import logger
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any

@ensure_annotations # 
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """
    Args: 
        path_to_yaml (str): path to yaml file (path like input)
    Raises:
        ValueError: if the yaml file is not valid (if yaml file is empty)
        e: Empty yaml file
    Returns:
        ConfigBox: ConfigBox type
    """
    
    try:
        with open(path_to_yaml, 'r') as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file : {path_to_yaml} Loaded Successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError(f"yaml file is empty!!")
    except Exception as e:
        raise e
    

@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """
    Creates a list of directories.
    Args: 
        path_to_directories (list): list of directories (path like input)
        verbose (bool, optional): print info. Defaults to True
        ignore_log(bool, optional): ignore if multiple directories is to be created. Defaults to False
    Raises:
        ValueError: if the directories are not valid (if directories are empty)
        e: Empty directories
    Returns:
        None
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"directory : {path} Created Successfully")
        
@ensure_annotations
def get_size(path: Path) -> str:
    """
    Args: 
        path (Path): path to file (path like input)
    Returns:
        str: size of file
    """
    size_in_kb = round(os.path.getsize(path)/1024, 2)
    return f"{size_in_kb} KB"
    

        