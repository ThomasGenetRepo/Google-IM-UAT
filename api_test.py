# type: ignore
from api import SharePoint

sp = SharePoint()
files = sp._get_files_list("Google Field App Data")
for f in files:
    print(f.name)