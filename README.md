# brick-relations
This is a tool to find appropriate brick relationships between two nodes.

## Installing dependencies

```bash
pip3 install -r requirements.txt
```

## Help
```bash
python3 relations.py --help     
```

## Usage

### Relationships between brick classes
```bash
python3 relations.py --nodes brick:FCU brick:Air
```
Output:
```bash
brick:FCU https://brickschema.org/schema/1.1.0/Brick#regulates brick:Air
brick:Air https://brickschema.org/schema/1.1.0/Brick#isRegulatedBy brick:FCU
```
### Specifying brick model
This can be a url or a file path.
```bash
python3 relations.py --brick Brick.ttl --nodes brick:FCU brick:Air
```

### Relationships between instances
```bash
python3 relations.py --model sample.ttl --nodes wean:fcu1 wean:air1
```
Output:
```bash
wean:fcu1 https://brickschema.org/schema/1.1.0/Brick#regulates wean:air1
wean:air1 https://brickschema.org/schema/1.1.0/Brick#isRegulatedBy wean:fcu1
```
