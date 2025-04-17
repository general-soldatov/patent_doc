from app.config.yaml_config import ProjectReader
from app.templates.word_template import AuthorConsentOne

def project():
    authorConsentOne = AuthorConsentOne()
    project = ProjectReader("examples/project_1.yaml")
    authorConsentOne.data = project.authorConsentOne()
    authorConsentOne.create_document()