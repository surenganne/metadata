#  Copyright 2021 Collate
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#  http://www.apache.org/licenses/LICENSE-2.0
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
"""
Defines the Elasticsearch mapping for Glossaries
"""
import textwrap

GLOSSARY_TERM_ELASTICSEARCH_INDEX_MAPPING = textwrap.dedent(
    """
{
  "settings": {
    "analysis": {
      "normalizer": {
        "lowercase_normalizer": {
          "type": "custom",
          "char_filter": [],
          "filter": [
            "lowercase"
          ]
        }
      },
      "analyzer": {
        "om_analyzer": {
          "tokenizer": "letter",
          "filter": [
            "lowercase",
            "om_stemmer"
          ]
        },
        "om_ngram": {
          "tokenizer": "ngram",
          "min_gram": 1,
          "max_gram": 2
        }
      },
      "filter": {
        "om_stemmer": {
          "type": "stemmer",
          "name": "english"
        }
      }
    }
  },
  "mappings": {
    "properties": {
      "id": {
        "type": "text"
      },
      "name": {
        "type": "keyword",
        "fields": {
          "keyword": {
            "type": "keyword",
            "ignore_above": 256
          }
        }
      },
      "fullyQualifiedName": {
        "type": "keyword",
        "normalizer": "lowercase_normalizer"
      },
      "displayName": {
        "type": "text",
        "analyzer": "om_analyzer",
        "fields": {
          "keyword": {
            "type": "keyword",
            "ignore_above": 256
          },
          "ngram": {
            "type": "text",
            "analyzer": "om_ngram"
          }
        }
      },
      "description": {
        "type": "text"
      },
      "version": {
        "type": "float"
      },
      "updatedAt": {
        "type": "date",
        "format": "epoch_second"
      },
      "updatedBy": {
        "type": "text"
      },
      "href": {
        "type": "text"
      },
      "synonyms": {
        "type": "text",
        "fields": {
          "keyword": {
            "type": "keyword",
            "ignore_above": 256
          },
          "ngram": {
            "type": "text",
            "analyzer": "om_ngram"
          }
        }
      },
      "glossary": {
        "properties": {
          "id": {
            "type": "keyword",
            "fields": {
              "keyword": {
                "type": "keyword",
                "ignore_above": 36
              }
            }
          },
          "type": {
            "type": "keyword"
          },
          "name": {
            "type": "text",
            "fields": {
              "keyword": {
                "type": "keyword",
                "ignore_above": 256
              },
              "ngram": {
                "type": "text",
                "analyzer": "om_ngram"
              }
            }
          },
          "displayName": {
            "type": "text",
            "analyzer": "om_analyzer",
            "fields": {
              "keyword": {
                "type": "keyword",
                "ignore_above": 256
              },
              "ngram": {
                "type": "text",
                "analyzer": "om_ngram"
              }
            }
          },
          "fullyQualifiedName": {
            "type": "text"
          },
          "description": {
            "type": "text"
          },
          "deleted": {
            "type": "text"
          },
          "href": {
            "type": "text"
          }
        }
      },
      "children": {
        "properties": {
          "id": {
            "type": "keyword",
            "fields": {
              "keyword": {
                "type": "keyword",
                "ignore_above": 36
              }
            }
          },
          "type": {
            "type": "keyword"
          },
          "name": {
            "type": "keyword",
            "fields": {
              "keyword": {
                "type": "keyword",
                "ignore_above": 256
              }
            }
          },
          "fullyQualifiedName": {
            "type": "text"
          },
          "description": {
            "type": "text"
          },
          "deleted": {
            "type": "text"
          },
          "href": {
            "type": "text"
          }
        }
      },
      "relatedTerms": {
        "properties": {
          "id": {
            "type": "keyword",
            "fields": {
              "keyword": {
                "type": "keyword",
                "ignore_above": 36
              }
            }
          },
          "type": {
            "type": "keyword"
          },
          "name": {
            "type": "keyword",
            "fields": {
              "keyword": {
                "type": "keyword",
                "ignore_above": 256
              }
            }
          },
          "fullyQualifiedName": {
            "type": "text"
          },
          "description": {
            "type": "text"
          },
          "deleted": {
            "type": "text"
          },
          "href": {
            "type": "text"
          }
        }
      },
      "reviewers": {
        "properties": {
          "id": {
            "type": "keyword",
            "fields": {
              "keyword": {
                "type": "keyword",
                "ignore_above": 36
              }
            }
          },
          "type": {
            "type": "keyword"
          },
          "name": {
            "type": "keyword",
            "fields": {
              "keyword": {
                "type": "keyword",
                "ignore_above": 256
              }
            }
          },
          "displayName": {
            "type": "keyword",
            "fields": {
              "keyword": {
                "type": "keyword",
                "ignore_above": 256
              }
            }
          },
          "fullyQualifiedName": {
            "type": "text"
          },
          "description": {
            "type": "text"
          },
          "deleted": {
            "type": "text"
          },
          "href": {
            "type": "text"
          }
        }
      },
      "usageCount": {
        "type": "integer"
      },
      "tags": {
        "properties": {
          "tagFQN": {
            "type": "keyword"
          },
          "labelType": {
            "type": "keyword"
          },
          "description": {
            "type": "text"
          },
          "source": {
            "type": "keyword"
          },
          "state": {
            "type": "keyword"
          }
        }
      },
      "deleted": {
        "type": "text"
      },
      "status": {
        "type": "text"
      },
      "suggest": {
        "type": "completion",
        "contexts": [
          {
            "name": "deleted",
            "type": "category",
            "path": "deleted"
          }
        ]
      }
    }
  }
}
"""
)
