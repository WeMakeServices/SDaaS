# SDaaS

Have you ever wanted a simple REST API that enabled you to detect the subject of your photographs?

Look no further.

Subject Detection as a Service (SDaaS) provides users with an easy, robust, reliable, and atomic REST API for all of your subject detection needs. If your requirements for detecting subjects in your images fall under the following:

1. You wish to detect the subject of a **photograph**
2. Your application requires fewer than 30 subject detections per month
3. **Your application requires no greater than 50% accuracy**

Then you are welcome to use SDaaS for your subject detection needs!

# Table of Contents

1. [Usage](#usage-example)
1. [API Documentation](#api-documentation)
    1. [Cat](#cat)
    1. [Dog](#dog)
    1. [Vampire](#vampire)

# Usage Example

```python
import requests
import time
from typing import Iterator, List
from enum import Enum

class PhotographURL:
    """
    PhotographURL represents a Uniform Resource Locator
    (colloquially termed web address) that specifies the
    location of a photograph on the World Wide Web
    (colloquially termed the Internet).
    """
    def __init__(self, url: str):
        # Omitted for brevity
        if self.url_does_not_contain_photograph(url):
            raise ValueError("Invalid URL")
        self.url = url

class Subject(Enum):
    CAT = "cat"
    DOG = "dog"
    VAMPIRE = "vampire"

def perform_multiple_subject_detections(
    urls: List[PhotographURL],
    subjects: List[Subject]
) -> Iterator[bool]:
    """
    Given a list of PhotographURLs and a list of Subjects,
    will iterate over the two and call out to SDaaS (Subject
    Detection as a Service). Results from SDaaS are returned 
    synchronously.
    """
    for index, url in enumerate(urls):
        if index > 0 and index % 30 == 0:
            time.sleep(2.628e+6)
        subject = subjects[index]
        yield sdaas(url, subject)


def sdaas(url: PhotographURL, subject: Subject) -> bool:
    """
    Calls out to SDaaS API and returns the result
    """
    result = requests.get(f"https://sdaas.woohoojin.dev/{subject.value}?url={url.url}")
    return bool(result.text)
```

# API Documentation

## Cat

**URL** : `/cat?url=<url>`

**Method** : `GET`

**Auth required** : NO

**Permissions required** : None

**Rate limit** : 30 requests per month

**Description** : Returns the "True" if the photograph contains a cat. Else "False".

## Success Response

**Code** : `200 OK`

**Content examples**
For a request with `url=https://blog.imgur.com/wp-content/uploads/2016/05/dog33.jpg`

```json
True
```

Or...

```json
False
```

## Failure Responses

**Code** : `400 Bad Request`

**Content examples**

For a request with `url=not_a_url`

```json
Bad Request
```

**Code** : `429 Too Many Requests`

**Content examples**

For the 31st request made in a given month

```json
Too Many Requests
30 per 1 month
```

## Dog

**URL** : `/dog?url=<url>`

**Method** : `GET`

**Auth required** : NO

**Permissions required** : None

**Rate limit** : 30 requests per month

**Description** : Returns the "True" if the photograph contains a dog. Else "False".

## Success Response

**Code** : `200 OK`

**Content examples**
For a request with `url=https://blog.imgur.com/wp-content/uploads/2016/05/dog33.jpg`

```json
True
```

Or...

```json
False
```

## Failure Responses

**Code** : `400 Bad Request`

**Content examples**

For a request with `url=not_a_url`

```json
Bad Request
```
**Code** : `429 Too Many Requests`

**Content examples**

For the 31st request made in a given month

```json
Too Many Requests
30 per 1 month
```

## Vampire

**URL** : `/vampire?url=<url>`

**Method** : `GET`

**Auth required** : NO

**Permissions required** : None

**Rate limit** : 30 requests per month

**Description** : Returns the "True" if the photograph contains a vampire. Else "False".

## Success Response

**Code** : `200 OK`

**Content examples**
For a request with `url=https://blog.imgur.com/wp-content/uploads/2016/05/dog33.jpg`

```json
False
```

## Failure Responses

**Code** : `400 Bad Request`

**Content examples**

For a request with `url=not_a_url`

```json
Bad Request
```

**Code** : `429 Too Many Requests`

**Content examples**

For the 31st request made in a given month

```json
Too Many Requests
30 per 1 month
```