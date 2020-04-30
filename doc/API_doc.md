## Twitter_demo API Doc

1. Search by hashtag

    **GET** `/hashtags/<hashtag>`

    Developer：KyleGao

    Version：v1

    Explain：Show the list of tweets with the given hashtag

    Help：limit  default number is 30.

    Reauest parameter：

    | parameter | Type   | Must | parameter location | explain  |
    | --------- | ------ | ---- | ------------------ | -------- |
    | hashtag   | String | Yes  |       Head          |  hashtag |
    | Limit     | String | No   |        Head          |  data limit |

    Response ：

    - success：

      ```JSON
      [
          {
              "created_at": "2020-02-10-00-24-39",
              "id": 79899569,
              "id_str": 721737286,
              "text": "离油金听增越长部入将平老识委本连定支到有具志使按关求书从本专者争它铁何小社年学件南度精家历集统选程回青斗四即便",
              "truncated": true,
              "entities": {
                  "hashtags": "#python",
                  "symbols": [],
                  "user_mentions": [],
                  "urls": [
                      {
                          "url": "https://t.co/Rbc9TF2s5X",
                          "expanded_url": "https://twitter.com/i/web/status/1125490788736032770",
                          "display_url": "twitter.com/i/web/status/1…",
                          "indices": [
                              117,
                              140
                          ]
                      }
                  ]
              },
              "user": {
                  "id": 2244994945,
                  "id_str": "2244994945",
                  "name": "马勇",
                  "entities": {
                      "description": {
                          "urls": [
                              {
                                  "url": "https://t.co/mGHnxZU8c1",
                                  "indices": [
                                      93,
                                      116
                                  ]
                              }
                          ]
                      }
                  },
                  "followers_count": 501947,
                  "friends_count": 1473,
                  "listed_count": 1507,
                  "created_at": "Sat Dec 14 04:35:55 +0000 2013",
                  "favourites_count": 2186
              }
          }
      ]
      ```

    - fail：

      ```
      pass
      
      没有做异常处理
      ```

2. Search by username

    **GET** `/users/<name>`

    Developer：KyleGao

    Version：v1

    Explain：Show the list of tweets that user has on his feed

    Help：limit  default number is 30.

    Reauest parameter：

    | parameter | Type   | Must | parameter location | explain  |
    | --------- | ------ | ---- | ------------------ | -------- |
    | name   | String | Yes  |       Head          |  name |
    | Limit     | String | No   |        Head          |  data limit |

    Response ：

    - success：

      ```JSON
      [
          {
              "created_at": "2020-02-10-00-24-39",
              "id": 79899569,
              "id_str": 721737286,
              "text": "离油金听增越长部入将平老识委本连定支到有具志使按关求书从本专者争它铁何小社年学件南度精家历集统选程回青斗四即便",
              "truncated": true,
              "entities": {
                  "hashtags": "#python",
                  "symbols": [],
                  "user_mentions": [],
                  "urls": [
                      {
                          "url": "https://t.co/Rbc9TF2s5X",
                          "expanded_url": "https://twitter.com/i/web/status/1125490788736032770",
                          "display_url": "twitter.com/i/web/status/1…",
                          "indices": [
                              117,
                              140
                          ]
                      }
                  ]
              },
              "user": {
                  "id": 2244994945,
                  "id_str": "2244994945",
                  "name": "马勇",
                  "entities": {
                      "description": {
                          "urls": [
                              {
                                  "url": "https://t.co/mGHnxZU8c1",
                                  "indices": [
                                      93,
                                      116
                                  ]
                              }
                          ]
                      }
                  },
                  "followers_count": 501947,
                  "friends_count": 1473,
                  "listed_count": 1507,
                  "created_at": "Sat Dec 14 04:35:55 +0000 2013",
                  "favourites_count": 2186
              }
          }
      ]
      ```

    - fail：

      ```
      pass
      
      没有做异常处理
      ```

