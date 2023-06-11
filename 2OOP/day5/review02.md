# Review Day

## Topics Covered / Goals

- Review Object Oriented Programming in Python
  - Understand Class Objects, Instance Variables, and Instance Methods

### Lesson

- Class Objects

```python
class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def say_hello(self):
        return f"Hello my name is {self.first_name} {self.last_name} and I'm {self.age} years old."

    def celebrate_birthday(self):
        self.age = self.age + 1
        return f"Wooo! It's my birthday today! I'm {self.age}!"

    def my_age(self):
        return f"My age is {self.age}."
```

## Optional assignments (**if you finish the assessment early**)

- [School Interface III](https://classroom.google.com/w/NjEyMzM5MTczMDQ4/tc/NjEyNjM4NjQwNjk1)
- [Bowling](https://classroom.google.com/w/NjEyMzM5MTczMDQ4/tc/NjEyNjM4NjQwNjk1)

> Stuck? Have a code error? Use the ["4 Before Me"](https://docs.google.com/document/d/1nseOs5oabYBKNHfwJZNAR7GlU0zkZxNagsw63AD7XV0/edit) debugging checklist to help you solve it!

## [**Assessment-1**](https://classroom.google.com/c/NjEyMzM5MTczMDQ4?cjc=vunqfsg)