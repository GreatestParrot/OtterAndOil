import os
import datetime
import shutil
import json


def create_timestamped_suffix() -> str:
    """
    Creates a filename for an experiment with the current date and time.

    Parameters:
    - Empty

    Returns:
    - str: The generated timestamp in YYYYMMDD_HHMMSS.
    """
    # Get the current date and time
    now = datetime.datetime.now()

    # Format the date and time as 'YYYYMMDD_HHMMSS'
    timestamp = now.strftime("%Y%m%d_%H%M%S")

    return timestamp


def create_timestamped_filename_ext(base_name: str, suffix: str, extension: str) -> str:
    if len(suffix):
        return f"{base_name}_{suffix}.{extension}"
    else:
        return f"{base_name}_{create_timestamped_suffix()}.{extension}"


def create_timestamped_folder(*args, base_path="./data", timestamped_suffix=""):
    """
    Creates a new folder with a name containing the current date and time.

    Parameters:
    - base_path (str): The base directory where the new folder will be created. Defaults to the current directory.

    Returns:
    - str: The path to the created folder.
    """

    # Construct the folder name
    folder_name = "expt_"
    for arg in args:
        folder_name += f"{arg}_"
    if len(timestamped_suffix):
        folder_name += timestamped_suffix
    else:
        folder_name += create_timestamped_suffix()

    # Create the full path
    folder_path = os.path.join(base_path, folder_name)

    # Create the new folder
    os.makedirs(folder_path, exist_ok=True)

    return folder_path


def clean_data():
    """
        Deletes the 'data' folder in the script's directory if it exists.
        """
    # Get the path of the script's directory
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # Path to the 'data' folder
    data_folder_path = os.path.join(script_dir, "..", "data")

    # Check if the 'data' folder exists
    if os.path.exists(data_folder_path) and os.path.isdir(data_folder_path):
        # Delete the 'data' folder and its contents
        shutil.rmtree(data_folder_path)
        print(f"Deleted 'data' folder at: {data_folder_path}")
    else:
        print(f"'data' folder does not exist at: {data_folder_path}")


class Arguments:
    def __init__(self, **arguments):
        #print(arguments)
        self.clean_cache = arguments["clean_cache"]
        self.big_picture = arguments["big_picture"]
        self.not_animated = arguments["not_animated"]
        self.store_raw = arguments["store_raw"]
        self.show_intensity = arguments["show_intensity"]
        self.isometric = arguments["isometric"]
        self.isolines = arguments["isolines"]
        self.peaks_filename = arguments["peaks_filename"]
        self.cache_dir = arguments["cache_dir"]
        self.peak_type = arguments["peak_type"]
        self.shift_vehicle = arguments["shift_vehicle"]
        self.shift_xyz = arguments["shift_xyz"]
        self.N = arguments["N"]
        self.sample_time = arguments["sample_time"]
        self.cycles = arguments["cycles"]
        self.radius = arguments["radius"]
        self.catamarans = arguments["catamarans"]
        self.grid_size = arguments["grid_size"]
        self.FPS = arguments["FPS"]
        self.V_current = arguments["V_current"]
        self.beta_current = arguments["beta_current"]

    def get_json_data(self):
        return {
                    "clean_cache": self.clean_cache,
                    "big_picture": self.big_picture,
                    "not_animated": self.not_animated,
                    "store_raw": self.store_raw,
                    "show_intensity": self.show_intensity,
                    "isometric": self.isometric,
                    "isolines": self.isolines,
                    "peaks_filename": self.peaks_filename,
                    "cache_dir": self.cache_dir,
                    "peak_type": self.peak_type,
                    "shift_vehicle": self.shift_vehicle,
                    "shift_xyz": self.shift_xyz,
                    "N": self.N,
                    "sample_time": self.sample_time,
                    "cycles": self.cycles,
                    "radius": self.radius,
                    "catamarans": self.catamarans,
                    "grid_size": self.grid_size,
                    "FPS": self.FPS,
                    "V_current": self.V_current,
                    "beta_current": self.beta_current
                }

    # Save the variables to a new JSON file
    def store_in_config(self, folder, suffix):
        with open(os.path.join(folder,
                               create_timestamped_filename_ext("config",
                                                               suffix,
                                                               "json")), 'w') as config:
            json.dump(self.get_json_data(), config, indent=4)


def read_and_assign_arguments(input_filename):
    with open(input_filename, 'r') as file:
        data = json.load(file)
    return Arguments(**data)


def overwrite_file(old_name, new_name):
    """
    Overwrite a file with a different name.

    Parameters:
    old_name (str): The name of the file to be overwritten.
    new_name (str): The new name of the file.
    """
    # Check if the old file exists
    if not os.path.exists(old_name):
        raise FileNotFoundError(f"The file '{old_name}' does not exist.")

    # Remove the new file if it already exists
    if os.path.exists(new_name):
        os.remove(new_name)

    # Copy the old file to the new file name (overwriting if exists)
    shutil.copyfile(old_name, new_name)


