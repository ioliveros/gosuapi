# gosuapi

### a gosugamers api client

```sh
pip insall -r requirements.txt
```

```sh
~$:cd gosuapi/
~$:python setup.py install
```

#### basic usage

```python
import gosuapi

gosuapi.headlines(section="dota2")

result:
{
  "data": [
     "headline":"Summit 13 kicks off with Open Qualifiers this weekend",
     "href": "https://www.gosugamers.net/dota2/news/52935-summit-13-kicks-off-with-open-qualifiers-this-weekend",
     "img": "https://static.gosugamers.net/836x_/fe/a9/3f/01acfb5704c6bf4d8ed8050473b8fd55f3e2ef2a1df82395fc153124a4.jpg",
  ]
}

```