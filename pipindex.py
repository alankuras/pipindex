import pathlib
from argparse import ArgumentParser, RawDescriptionHelpFormatter
from wheel_inspect import inspect_wheel


argparse_help = """
Reorganizes the structure for pip packages (for serving over http)
"""

parser = ArgumentParser(description=argparse_help, formatter_class=RawDescriptionHelpFormatter)
parser.add_argument("--path", "-p", help="Path to directory with packages", required=True, default=".")
args = parser.parse_args()

path = pathlib.Path(args.path)

packages = [x for x in path.iterdir() if not x.is_dir() and x.name.endswith(".whl")]

if not packages:
    print(f"No packages to process in {path.resolve()}")
else:
    for package in packages:
        try:
            expected_dir_name = inspect_wheel(package)["dist_info"]["metadata"]["name"]
            package_dir = pathlib.Path(path/expected_dir_name)
            if not package_dir.exists():
                pathlib.Path.mkdir(package_dir)
            package.rename(package_dir/package.name)
        except Exception as e:
            print(f"Couldn't process package {e}")
    print(f"Processed {len(packages)} packages")



"""
pip download package_name --dest ~/pipfiles
python main.py -p ~/pipfiles
twistd3 -n web --path ~/pipfiles

wheel_inspect is used because packages with "-" or "_" in name can cause issues.
"""
