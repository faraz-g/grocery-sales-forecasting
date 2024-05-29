import kaggle
import shutil
import py7zr
from pathlib import Path
from grocery_sales_forecasting.utils import get_dataset_folder_path


def download_data_from_kaggle(skip_if_exists: bool = False) -> None:
    """Downloads the data from the favorita-grocery-sales-forecasting kaggle competition
    to the path returned by: grocery_sales_forecasting.utils.get_dataset_folder_path()"""

    competition_name = "favorita-grocery-sales-forecasting"

    dataset_dir = Path(get_dataset_folder_path())
    if skip_if_exists and dataset_dir.exists:
        return

    try:
        shutil.rmtree(dataset_dir)
    except FileNotFoundError:
        pass

    dataset_dir.mkdir(parents=True)

    kaggle.api.competition_download_files(competition=competition_name, path=dataset_dir, force=True, quiet=False)

    out_file = dataset_dir.joinpath(competition_name).with_suffix(".zip")

    shutil.unpack_archive(
        out_file,
        extract_dir=dataset_dir,
    )

    for file in dataset_dir.glob("*.7z"):
        with py7zr.SevenZipFile(file=file, mode="r") as z:
            z.extractall(dataset_dir)

    # Delete all compressed files in directory
    for file in dataset_dir.glob("*"):
        if file.suffix == ".csv":
            continue

        file.unlink()


if __name__ == "__main__":
    download_data_from_kaggle()
