"""
  Copyright 2015 INFN (Italy)

  Licensed under the Apache License, Version 2.0 (the "License");
  you may not use this file except in compliance with the License.
  You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

  Unless required by applicable law or agreed to in writing, software
  distributed under the License is distributed on an "AS IS" BASIS,
  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
  See the License for the specific language governing permissions and
  limitations under the License.
"""

from rdflib import Graph, OWL, RDF
from rdflib.exceptions import TypeCheckError

__author__ = 'marco'


class OWLontology(object):
    """
    This class should represent the ontology to analyse or the one just built
    """

    def __init__(self, ontology=None, file_path=None):
        """
        Initialise the ontology
        :param ontology:
        :param filepath:
        :return:
        """
        self.graph = Graph()
        if ontology:
            self.graph.parse(ontology)
        elif file_path:
            self.graph.parse(file_path)
        self.graph.bind('owl', 'http://www.w3.org/2002/07/owl#')

    def add_namespace(self, prefix, namespace):
        self.graph.bind(prefix, namespace)

    def get_xml_document(self, format='pretty-xml'):
        """
        Get the xml version of the ontology
        :param format: Formats recognised by rdflib
        :return: String with the xml
        """
        return self.graph.serialize(format=format)

    def add_owl_individual(self, individual):
        """

        :return:
        """
        if not isinstance(individual, NamedIndividual):
            raise TypeCheckError("Type not provided for the search")
        self.graph.add((individual.identifier, RDF.type, OWL.NamedIndividual))
        self.graph.add((individual.identifier, RDF.type, individual.type))

    def get_owl_individual(self, identifier):
        """

        :return:
        """
#        if not isinstance(rdftype, BNode):
#            raise TypeCheckError("Type not provided for the search")

        self.graph.add((identifier, RDF.about, OWL.NamedIndividual))


class NamedIndividual(object):
    """
    Identify an OWL NamedIndividual
    """

    def get_identifier(self):
        return self._identifier

    def set_identifier(self, identifier):
        self._identifier = identifier

    def del_identifier(self):
        pass

    identifier = property(get_identifier,
                          set_identifier,
                          del_identifier,
                          'This is the identifier for the individual')

    def get_type(self):
        return self._type

    def set_type(self, type):
        self._type = type

    def del_type(self):
        pass

    type = property(get_type,
                    set_type,
                    del_type,
                    'This is the type for the individual')
