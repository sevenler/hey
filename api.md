#apis

fetch nearly question (https://github.com/sevenler/hey/blob/master/api.md#nearly_question)

question detail (https://github.com/sevenler/hey/blob/master/api.md#question)

add a question (https://github.com/sevenler/hey/blob/master/api.md#add_question)

add an answer (https://github.com/sevenler/hey/blob/master/api.md#add_answer)

agree answer (https://github.com/sevenler/hey/blob/master/api.md#agree_answer)


##nearly_question 
request:

    http://localhost:80/question/nearly/


response:

    {
        "status": 200,
        "message": "",
        "data": [
            {
                "id": 17,
                "images": [
                    "https://lh4.googleusercontent.com/-v0soe-ievYE/AAAAAAAAAAI/AAAAAAADpsQ/2_LasUaYkYU/s0-c-k-no-ns/photo.jpg"
                ],
                "text": "hello, this is google icon image",
                "created_user": {
                    "id": 1,
                    "avatar": "https://www.google.com/logos/doodles/2016/united-states-elections-2016-reminder-day-1-56698792092631",
                    "name": "Daniel"
                }
            },
            {
                "id": 17,
                "images": [
                    "https://lh4.googleusercontent.com/-v0soe-ievYE/AAAAAAAAAAI/AAAAAAADpsQ/2_LasUaYkYU/s0-c-k-no-ns/photo.jpg"
                ],
                "text": "hello, this is google icon image",
                "created_user": {
                    "id": 1,
                    "avatar": "https://www.google.com/logos/doodles/2016/united-states-elections-2016-reminder-day-1-56698792092631",
                    "name": "Daniel"
                }
            }
        ]
    }


##question
request:
    
    http://localhost:80/question/<question_id>


response:

    {
        "status": 200,
        "message": "",
        "data": {
            "id": 9,
            "images": [
                "https://www.google.com/logos/doodles/2016/united-states-elections-2016-reminder-day-1-56698792092631"
            ],
            "text": "hello, guys",
            "created_user": {
                "id": 2,
                "avatar": "https://www.google.com/logos/doodles/2016/united-states-elections-2016-reminder-day-1-56698792092631",
                "name": "Zoey"
            }
            "answers": [
                {
                    "images": [
                        "https://www.google.com/images/branding/googlelogo/2x/googlelogo_color_272x92dp.png"
                    ],
                    "text": "this is good",
                    "id": 3,
                    "answer_user": {
                        "id": 2,
                        "avatar": "https://www.google.com/logos/doodles/2016/united-states-elections-2016-reminder-day-1-56698792092631",
                        "name": "Zoey"
                    }
                },
                {
                    "images": [
                        "h"
                    ],
                    "text": "hello, this is google icon image",
                    "id": 4,
                    "answer_user": {
                        "id": 2,
                        "avatar": "https://www.google.com/logos/doodles/2016/united-states-elections-2016-reminder-day-1-56698792092631",
                        "name": "Zoey"
                    }
                }
            ],
        }
    }


##add_question

request:

    http://localhost:80/question/add/

    data:
    {
        "images": ["https://www.google.com/logos/doodles/2016/united-states-elections-2016-reminder-day-1-56698792092631"],
        "text": "this is google icon"
    }


response:

    {
        "status": 200, 
        "message": "add question success", 
        "data": {
            "id": 17,
            "images": [
                "https://lh4.googleusercontent.com/-v0soe-ievYE/AAAAAAAAAAI/AAAAAAADpsQ/2_LasUaYkYU/s0-c-k-no-ns/photo.jpg"
            ],
            "text": "hello, this is google icon image",
            "created_user": {
                "id": 1,
                "avatar": "https://www.google.com/logos/doodles/2016/united-states-elections-2016-reminder-day-1-56698792092631",
                "name": "Daniel"
            }
        }
    }


##add_answer

request:

    http://localhost:80/question/<question_id>/answer/add/

    data:
    {
        "images": ["https://www.google.com/logos/doodles/2016/united-states-elections-2016-reminder-day-1-56698792092631"],
        "text": "this is google icon"
    }


response:

    {
        "status": 200, 
        "message": "add answer success", 
        "data": true
    }


##agree_answer

request:

    http://localhost:80/answer/<answer_id>/agree/

    data:
    {

    }


response:

    {
        "status": 200, 
        "message": "enjoy answer success", 
        "data": true
    }
