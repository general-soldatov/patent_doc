from app.config.yaml_config import ProjectReader
from app.templates.word_template import AuthorConsentOne, AuthorConsentTwo, ReportOfPatent, DataOfAutors

def project():
    project = ProjectReader("examples/project_1.yaml")
    # authorConsentOne = AuthorConsentOne()
    # authorConsentOne.data = project.authorConsentOne()
    # print(authorConsentOne.create_document())

    # authorConsentTwo = AuthorConsentTwo()
    # authorConsentTwo.data = project.authorConsentTwo()
    # print(authorConsentTwo.create_document())

    # report = ReportOfPatent()
    # report.data = project.reportOfPatent()
    # print(report.create_document())

    authors = DataOfAutors()
    authors.data = project.dataOfAutors()
    print(authors.create_document())