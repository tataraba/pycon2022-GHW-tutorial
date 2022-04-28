# Goodbye, "Hello, World." Hello, Functional FastAPI App!

## PyCon 2022 Tutorial - References

The following references are for my tutorial session at PyCon 2022. This is intended for attendees, but it may prove useful for some of you who may have just happened upon this repository.

To those of you who were able to attend, I am extremely grateful for your time and patience with me! Hopefully some of these items can aid you in your quest to have a fully functional web application.

### Pieces Missed

In no particular order, here are some things I missed during the presentation that I wish to have covered.
-   We created a .gitignore file. I meant to have you add the value of ".env" as the first entry in that file. This is **extremely important** so that you don't accidently end up sending your secrets into your version control.
    -   I like to use a VSCode extension that generates a great .gitignore file for me (which already includes ".env"). The extension name is [.gitignore Generator](https://marketplace.visualstudio.com/items?itemName=piotrpalarz.vscode-gitignore-generator).
-   As we were building modules, I neglected to include the `if __name__ == "__main__":` statement to check our work. This is often a helpful step when building up your application.
-   I did mention this during the presentation, but a lot of what was covered in class is included in [this repository](https://github.com/tataraba/useful-python-web-app). I will continue to update it with other topics not covered in class.
-   I meant to include my contact details. So here goes:
    -   [Github](https://github.com/tataraba)
    -   Twitter [@PythonByNight](https://twitter.com/PythonByNight)
    -   pythonbynight@gmail.com


### Referenced Material

-   If you're starting out with FastAPI, you can't go wrong with the [official documentation](https://fastapi.tiangolo.com).
-   Pydantic also offers great documentation, though it can be a little heavier than FastAPI. I would focus on the [Models section](https://pydantic-docs.helpmanual.io/usage/models/) as well as the [Settings Management section](https://pydantic-docs.helpmanual.io/usage/settings/).
-   Beanie's docs are also very straightforward. The whole "Tutorial" section is good, starting with [Defining a document](https://roman-right.github.io/beanie/tutorial/defining-a-document/).


-   Most of my configuration section was based heavily on Redowan Delowar's article [Pedantic Configuration Management with Pydantic](https://rednafi.github.io/digressions/python/2020/06/03/python-configs.html)
-   Here is the website talking about the [X/Y problem](https://xyproblem.info) discussed during the session.
-   Brett Cannon wrote a blog post on [Why you should use `python -m pip`](https://snarky.ca/why-you-should-use-python-m-pip/), which is a pattern I generally follow.
-   This is a [Flask-specific blog post by Bob Waycott](https://bobwaycott.com/blog/how-i-use-flask/flask-app-organization/) talking about project structure/design. 


### Project Files

The included project is a copy of what we built in class. You can use it as a reference in case you missed something during the tutorial. I haven't checked to see if it matches the example code word for word, but I have confirmed that it runs as expected.

Make sure that your local `.env` file use the credentials discussed in class, or use your own MongoDB credentials for your own Atlas account.

### Final Notes

If there are any other things that are missing, I'll include it here. Thanks to all of you who participated in the tutorial and enjoy the rest of the conference!