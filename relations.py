from rdflib import Graph
from argparse import ArgumentParser

argparser = ArgumentParser()
argparser.add_argument('--brick',
                       nargs=1,
                       metavar='PATH',
                       help='The path to the Brick ttl file. The path can be either a URL or filesystem path.',
                       default='https://raw.githubusercontent.com/BrickSchema/Brick/master/Brick.ttl',
                       )
argparser.add_argument('--nodes',
                       nargs=2,
                       metavar='nodes',
                       help='The two nodes or instances',
                       required=True
                       )
argparser.add_argument('--model',
                       metavar='model',
                       help='Brick model'
                       )
args = argparser.parse_args()

g = Graph()
g.parse(args.brick, format='turtle')
if args.model:
    g.parse(args.model, format='turtle')
source, target = args.nodes

res = g.query("""
SELECT ?rel WHERE {
    ?rel rdfs:domain ?domain .
    ?rel rdfs:range ?range .
    %s (rdf:type|rdfs:subClassOf|^owl:equivalentClass|owl:equivalentClass)* ?domain .
    %s (rdf:type|rdfs:subClassOf|^owl:equivalentClass|owl:equivalentClass)* ?range .
}
""" % (source, target))

for row in res:
    for rel in row:
        print(source, rel, target)

res = g.query("""
SELECT ?rel WHERE {
?rel rdfs:domain ?domain .
?rel rdfs:range ?range .
%s (rdf:type|rdfs:subClassOf|^owl:equivalentClass|owl:equivalentClass)* ?range .
%s (rdf:type|rdfs:subClassOf|^owl:equivalentClass|owl:equivalentClass)* ?domain .
}
""" % (source, target))

for row in res:
    for rel in row:
        print(target, rel, source)
