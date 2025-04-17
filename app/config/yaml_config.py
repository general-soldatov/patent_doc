import yaml
from typing import Dict
from datetime import date

class YamlReader:
    def __init__(self, path: str, encoding: str = 'utf-8'):
        with open(path, 'r', encoding=encoding) as project:
            self._data = yaml.safe_load(project)

class ProjectReader(YamlReader):
    def __init__(self, path, encoding = "utf-8"):
        super().__init__(path, encoding)

    def copyright_info_add(self, dct_import: Dict[str, str]) -> None:
        dct_import.update(self._data["copyriht_info"])

    def info_program_add(self, dct_import: Dict[str, str]) -> None:
        dct_import.update(self._data["info_program"])

    def authorConsentOne(self, num_author: int = 1) -> Dict[str, str]:
        data_author = dict()
        author: Dict[str, str] = self._data["info_authors"][f"author_{num_author}"]
        data_author["full_name"] = f"{author['first_name']} {author['name']} {author['last_name']}"
        data_author["full_address"] = author["full_address"]
        dates: str = date.fromisoformat(author['pasport_date']).strftime("%d.%m.%Y")
        data_author["passport_data"] = f"{author['passport_series']} {author['passport_number']}, выдан {author['pasport_organisation'].strip()}, {dates}"
        data_author["name_of_prog"] = self._data["info_program"]["name_of_prog"]
        return data_author

if __name__ == "__main__":
    data = ProjectReader("examples/project_1.yaml")
    print(data.authorConsentOne())
