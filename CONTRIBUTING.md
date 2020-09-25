# Contributing to the OSCAL Content Project

This page is for potential contributors to this project. It provides basic information on the project, describes the main ways people can make contributions, explains how to report issues relating to the project and project artifacts, and lists pointers to additional sources of information.

## Project approach

This project uses an agile approach for development, where we focus on implementing the 20% of the functionality that solves 80% of the problem. We’re trying to focus on the core capabilities that are needed to provide the greatest amount of benefit. Because we’re working on a small set of capabilities, this allows us to make very fast progress. We’re building the features that we believe solve the biggest problems to provide the most value. We provide extension points that allow uncovered cases to be supported by others.

## Making Contributions

Contributions are welcome to this project repository.

For more information on the project's current needs and priorities, see the project's GitHub issue tracker (discussed below). Please refer to the [guide on how to contribute to open source](https://opensource.guide/how-to-contribute/) for general information on contributing to an open source project.

## Issue reporting and handling

All requests for changes and enhancements to the repository are initiated through the project's [GitHub issue tracker](../../issues). To initiate a request, please [create a new issue](https://help.github.com/articles/creating-an-issue/). The following issue templates exist for creating a new issue:
* [User Story](../../issues/new?template=feature_request.md&labels=enhancement%2C+User+Story): Use to describe a new feature or capability to be added to the project.
* [Defect Report](../../issues/new?template=bug_report.md&labels=bug): Use to report a problem with an existing feature or capability.
* [Question](../../issues/new?labels=question&template=question.md): Use to ask a question about the project or the contents of the repository.

The project team regularly reviews the open issues, prioritizes their handling, and updates the issue statuses, proving comments on the current status as needed.

## Contributing to this GitHub repository

This project uses a typical GitHub fork and pull request [workflow](https://guides.github.com/introduction/flow/). To establish a development environment for contributing to the project, you must do the following:

1. Fork the repository to your personal workspace. Please refer to the Github [guide on forking a repository](https://help.github.com/articles/fork-a-repo/) for more details.
1. Create a feature branch from the master branch for making changes. You can [create a branch in your personal repository](https://help.github.com/articles/creating-and-deleting-branches-within-your-repository/) directly on GitHub or create the branch using a Git client. For example, the ```git branch working``` command can be used to create a branch named *working*.
1. You will need to make your modifications by adding, removing, and changing the content in the branch, then staging your changes using the ```git add``` and ```git rm``` commands.
1. Once you have staged your changes, you will need to commit them. When committing, you will need to include a commit message. The commit message should describe the nature of your changes (e.g., added new feature X which supports Y). You can also reference an issue from the project repository by using the hash symbol. For example, to reference issue #34, you would include the text "#34". The full command would be: ```git commit -m "added new feature X which supports Y addressing issue #34"```.
1. Next, you must push your changes to your personal repo. You can do this with the command: ```git push```.
1. Finally, you can [create a pull request](https://help.github.com/articles/creating-a-pull-request-from-a-fork/).

### Repository structure

This repository consists of the following directories and files pertaining to the project:

- [.github](.github): Contains GitHub issue and pull request templates for the project.
[CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md): This file contains a code of conduct for all project contributors.
- [CONTRIBUTING.md](CONTRIBUTING.md): This file is for potential contributors to the project. It provides basic information on the project, describes the main ways people can make contributions, explains how to report issues, and lists pointers to additional sources of information. It also has instructions on establishing a development environment for contributing to the project.
- [LICENSE.md](LICENSE.md): This file contains license information for the files in this GitHub repository.

## Contributing to a Development Sprint

This project is uses GitHub [issues](../../issues) feature to track development work items as part of the core project work stream.

### User Stories

[User stories](../../issues?q=is%3Aopen+is%3Aissue+label%3A%22User+Story%22) represent features, actions, or enhancements that are intended to be worked on. Each user story is based on a [template](../../issues/new?template=feature_request.md&labels=enhancement%2C+User+Story) and describes the basic problem or need to be addressed, a set of detailed goals to accomplish, any dependencies that must be addressed to start or complete the user story, and the criteria for acceptance of the contribution.

The goals in a user story will be bulleted, indicating that each goal can be worked on in parallel, or numbered, indicating that each goal must be worked on sequentially. Each goal will be assigned to one or more individuals to accomplish.

### Reporting User Story Status

When working on a goal that is part of a user story you will want to provide a periodic report on any progress that has been made until that goal has been completed. This status must be reported as a comment to the associated user story issue.

When describing any open issues encountered use an "\@mention" of the individual who needs to respond to the issue. This will ensure that the individual is updated with this status. Please also raise any active, unresolved issues on the weekly status calls.

## Communications mechanisms

This project originated as part of the Open Security Controls Assessment Language (OSCAL) project. We are still using the OSCAL lists for this project. There are two mailing lists for the project:

- *oscal-dev@nist.gov* for communication among parties interested in contributing to the development of OSCAL or exchanging ideas. Subscribe by sending an email to [oscal-dev-join@nist.gov](mailto:oscal-dev-join@nist.gov). To unsubscribe send an email to [oscal-dev-leave@nist.gov](mailto:oscal-dev-leave@nist.gov).
- *oscal-updates@nist.gov* for low-frequency updates on the status of the OSCAL project. Subscribe by sending an email to [oscal-updates-join@nist.gov](mailto:oscal-updates-join@nist.gov). To unsubscribe send an email to [oscal-updates-leave@nist.gov](mailto:oscal-updates-leave@nist.gov).

# Licenses and attribution

## This project is in the public domain

This project is in the worldwide public domain.

This project is in the public domain within the United States, and copyright and related rights in the work worldwide are waived through the [CC0 1.0 Universal public domain](https://creativecommons.org/publicdomain/zero/1.0/) dedication.

## Contributions will be released into the public domain

All contributions to this project will be released under the CC0 dedication. By submitting a pull request, you are agreeing to comply with this waiver of copyright interest.
