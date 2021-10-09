# Technical Test Django

## Getting Started

These instructions will get you a clone of the project up and running on your local machine for development and testing purposes.
### Prerequisites
```
python 3.8
```
### Installing and Initial Setup

**[Optional]** 
Before the installation, a best practise would be setting a virtualenv for the project 

```
https://virtualenv.pypa.io/
```

All the necessary libraries are in requirements.txt
```
pip install -r requirements.txt
```

### Goal

In this test , you will work on  basic tasks from developing models & APIs to testing.



**Task 1: Create models based on this description**
```
File : blog/models.py
```
```
I want to create a blog with a title as required field at most 50 characters, 
the blog has also description and an image can be uploaded.
Each blog can have many comments associated with it.
A comment is just a text and must contain the time to creation as well.
```

**Task 2: Create serializers for each created model**
```
File : blog/serializers.py
```

**Task 3: Create endpoints for each created model**
```
File : blog/views.py
```
```
For Blog endpoints , you are asked to develop 2 endpoints ( one for creation and another one for listing)

For Comment endpoints , you are asked to develop only an endpoint for creation
```

**Task 4: Add endpoint urls**
```
File : blog/urls.py
```

**Task 5: Add tests to your recent endpoints**
```
File : blog/tests.py
```