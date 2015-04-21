from smartowl.__main__ import main
import smartowl
from rdflib import Namespace

def test_main():
    assert main([]) == 0

class Test_smartowl:
    def test_xml_document(self):
        o = smartowl.OWLontology(file_path='./tests/ontologies/ontologia.owl')
        print(o.get_xml_document('xml'))

    def test_xml_document_pretty(self):
        o = smartowl.OWLontology(file_path='./tests/ontologies/ontologia.owl')
        print(o.get_xml_document('pretty-xml'))

    def test_add_owl_individuals(self):
        basic_ontology = smartowl.OWLontology()
        basic_ontology.add_namespace("fede","http://www.ct.infn.it/ontology/federation#")

        basic_ontology.add_owl_individual(
            Namespace("http://www.ct.infn.it/ontology/federation#").paperino
        )
        print(basic_ontology.get_xml_document('pretty-xml'))