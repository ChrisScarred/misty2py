from os import path
from typing import Callable, Iterable, List, Tuple, Union
import base64

from misty2py.robot import Misty
from misty2py.utils import *
from utils.env_loader import *
from utils.utils import message_parser

def get_non_system_assets(
        misty: Callable, 
        assets: List = ["audio", "image", "video", "recording"], 
    ) -> Dict:
    list_suffix = "_list"
    non_sys_assets = {}
    for asset in assets:
        non_sys_assets[asset] = []
        data = misty.get_info(asset+list_suffix)
        result = data.get("result")
        if result:
            if isinstance(result, Iterable):
                for hit in result:
                    name = hit.get("name")
                    if not name:
                        continue
                    is_system = hit.get("systemAsset")
                    if not isinstance(is_system, type(None)):
                        if not is_system:
                            non_sys_assets[asset].append(name)
    return non_sys_assets


def get_asset_properties(asset_type: str, file: str) -> Tuple[str, str, str]:
    if asset_type == "recording":
        params = {
            "Name": file,
            "Base64": "true"
        }
    else:
        params = {
            "FileName": file,
            "Base64": "true"
        }
    
    split_file_name = file.split(".")
    name = split_file_name[0]
    if len(split_file_name) > 1:
        ext = split_file_name[1]
    else:
        ext = "unknown"

    return params, name, ext


def save_base64_str(full_path: str, content: str, check: bool = True) -> bool:
    if check and path.exists(full_path):
        return True

    try:
        with open(full_path, "w") as f:
            f.write(content)
        return True

    except:
        return False


def save_assets(misty: Callable, assets: Dict, location: str) -> List[str]:
    failed_list = []
    suffix = "_file"
    for asset_type, files in assets.items():
        for file in files:
            params, name, ext = get_asset_properties(asset_type, file)
            response = misty.get_info(asset_type+suffix, params=params)
            result = response.get("result")

            if not result:
                failed_list.append(file)
            
            else:
                file_name = "%s_%s_%s_in_base64.txt" % (asset_type, name, ext)
                full_path = os.path.join(location, file_name)
                file_content = result.get("base64")
                if not file_content:
                    failed_list.append(file)
                else:
                    success = save_base64_str(full_path, file_content)
                    if not success:
                        failed_list.append(file)
                
    return failed_list


def delete_assets(misty: Callable, assets: Dict, ignore_list: List = []) -> List[str]:
    suffix = "_delete"
    delete_list = []

    for asset_type, files in assets.items():
        for file in files:
            if not file in ignore_list:
                if asset_type == "recording":
                    data = {"Name": file}
                else:
                    data = {"FileName": file}
                response = misty.perform_action(asset_type+suffix, data=data)
                status = response.get("status")
                if status:
                    if status == "Success":
                        delete_list.append(file)
                
    return delete_list


def free_memory(
        misty: Callable, 
        assets: List = ["audio", "image", "video", "recording"], 
        save: bool = True,
        save_dir: str = "data"
    ):
    """TODO: Implement function that deletes all audio, video and image files that are not system assets.

    Args:
        misty (Callable): an instance of Misty class.
    """
    assets_to_delete = get_non_system_assets(misty, assets=assets)
    
    failed_list = []

    if save:
        failed_list = save_assets(misty, assets_to_delete, save_dir)

    deleted = delete_assets(misty, assets_to_delete, failed_list)

    if len(deleted) > 0:
        print("Successfully deleted following assets: %s" % str(deleted))
    else:
        print("Failed to delete any assets.")


def main():
    """Creates an instance of Misty class and calls the delete function."""
    m = Misty(MISTY_IP)
    current_dir = path.abspath(path.dirname(__file__))
    #free_memory(m, save_dir=path.join(current_dir,"data"))
    print(m.get_info("audio_file", {"FileName": "deleteThis.wav"}))

if __name__ == "__main__":
    main()
