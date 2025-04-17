import jinja2
from abc import ABC, abstractmethod
from docxtpl import DocxTemplate

class WordDocument(ABC):
    def __init__(self, path_doc: str = None, path: str = ""):
        self.doc: DocxTemplate = DocxTemplate(path)
        self.data: dict = {'full_name': "NoName"}
        self.type_doc: str = "NoneType"
        self.name_file = ""
        self.path_doc = path_doc
        self.jinja_env = jinja2.Environment()

    def create_name(self):
        path = self.path_doc + "/" if self.path_doc else ""
        self.name_file = f"{path}{self.type_doc}_{self.data['full_name']}.docx"

    @abstractmethod
    def create_document(self) -> str | Exception:
        self.create_name()
        return self.__document_create(self.doc, self.name_file, self.data, self.jinja_env)


    @staticmethod
    def __document_create(docs: DocxTemplate, name_file: str, context: dict, jinja_env: jinja2.Environment) -> str | Exception:
        try:
            docs.render(context, jinja_env)
            docs.save(name_file)
            return name_file
        except Exception as e:
            return e

class AuthorConsentOne(WordDocument):
    def __init__(self, path_doc = None, path = "app/templates/authors_consent_1.docx"):
        super().__init__(path_doc, path)
        self.type_doc = "Согласие_п.3"
        self.data = {}

    def create_document(self):
        return super().create_document()

class AuthorConsentTwo(WordDocument):
    def __init__(self, path_doc = None, path = "app/templates/authors_consent_2.docx"):
        super().__init__(path_doc, path)
        self.type_doc = "Согласие_п.4"
        self.data = {
            "name_of_prog": "ЭВМ контроль семян",
            "copyright_holder": "Федеральное государственное бюджетное образовательное учреждение высшего образования «Воронежский государственный аграрный университет имени императора Петра I»",
            "copyright_adress": "394087, РФ, г. Воронеж, ул. Мичурина, 1",
            "copiright_ogrn": "1033600074090",
            "copyright_inn": "3666031208",
            "full_name": "Солдатов",
            "citizenship": "РФ",
            "day_birth": "1",
            "month_birth": "02",
            "year_birth": "19",
            "full_address": "Ломонова 11",
            "passport_data": "3915 23190",
            "short_description": "Разработка модели, алгоритма, написание и развертывание программы.",
            "copyright_position": "И.о. проректора по научной работе ФГБОУ ВО Воронежский ГАУ",
            "copyright_name": "С.Н. Семенов",
            "today": "«07» октября 2024 г."
        }

    def create_document(self):
        return super().create_document()


class ReportOfPatent(WordDocument):
    def __init__(self, path_doc = None, path = "app/templates/report_template.docx"):
        super().__init__(path_doc, path)
        self.type_doc = "Реферат"
        self.data = {
            "name_of_prog": "ЭВМ контроль семян".upper(),
            "full_name": "Солдатов",
            "authors": "Гиевский Алексей Михайлович, Солдатов Юрий Игоревич",
            "copyright_holder": "Федеральное государственное бюджетное образовательное учреждение высшего образования «Воронежский государственный аграрный университет имени императора Петра I»",
            "abstract": "Программа реализует математическую модель полёта семени при отрыве от отверстия высевающего аппарата, движение по наклонному сборочному лотку до попадания в камеру разделения воздушным потоком. В качестве исходных данных используется начальная скорость и угол отрыва семени от высевающего аппарата, математическая функция, описывающая форму лотка, коэффициент парусности.",
            "type_of_computer": "ПК на базе процессора не ниже Pentium 2,3 ГГц.",
            "operation_system": "Microsoft Windows 7, 8.1, 10, 11.",
            "program_language": "Maple",
            "size_of_program": "744 кб"
        }

    def create_document(self):
        return super().create_document()


class DataOfAutors(WordDocument):
    def __init__(self, path_doc = None, path = "app/templates/data_of_authors.docx"):
        super().__init__(path_doc, path)
        self.type_doc = "Сведения_авторы"
        self.data = {
            "name_of_prog": "ЭВМ контроль семян".upper(),
            "full_name": "Солдатов",
            "authors": [
                {
                    "full_name": "Солдатов",
                    "citizenship": "РФ",
                    "day_birth": "1",
                    "month_birth": "02",
                    "year_birth": "199",
                    "full_address": "Ломова 114"
                },
                {
                    "full_name": "Солдатов",
                    "citizenship": "РФ",
                    "day_birth": "19",
                    "month_birth": "02",
                    "year_birth": "19",
                    "full_address": "Ломонoва 14"
                }
            ]
        }

    def create_document(self):
        return super().create_document()


if __name__ == "__main__":
    output_file = DataOfAutors().create_document()
    print(f"Document create {output_file}")