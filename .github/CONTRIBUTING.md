# Contributing

1. [Fork the repository.][fork]
2. [Create a topic branch.][branch]
3. Install the necessary dependencies `pipenv install --dev`.
4. Implement your feature or bug fix.
5. Don't forget to add tests and make sure they pass by running `pipenv run pytest`. Tests will be linted automatically.
6. Make sure your code complies with the style guide by running `pipenv run pylint lokalise/`. `pipenv run autopep8 -i -r lokalise/ -a` can automatically fix many issues for you.
7. We use type hinting so check if everything is okay by running `pipenv run mypy lokalise/`.
8. If necessary, add documentation for your feature or bug fix.
9. Commit and push your changes.
10. [Submit a pull request.][pr]

[fork]: http://help.github.com/fork-a-repo/
[branch]: https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/about-branches
[pr]: https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/about-pull-requests
