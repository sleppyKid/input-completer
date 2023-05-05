# input_completer

Simple tool to autocomplete text input from given list

For windows install pyreadline3:
```commandline
pip install pyreadline3
```

```python
from input_completer import ListAutoCompleter

# Options must be Iterable[str]
animals = ['cat', 'dog', 'chicken', 'bird', 'horse', 'monkey', 'rabbit']
default = animals[0]

number = ListAutoCompleter(
    options=animals,
    default=default,
    input_text='Select animal from list\nDefault is ({}):'
).run()
```

```commandline
Select animal from list
Default is (cat): <tab>
bird    cat     chicken dog     horse   monkey  rabbit

Select animal from list
Default is (cat): c<tab>
cat     chicken

Select animal from list
Default is (cat): ch<tab>icken
```


