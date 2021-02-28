# Stock Checker App

## Setup

This repo uses the `nvie/gitflow` git extension to make it so easy to use the
popular gitflow branching model.

We also use the [`commitizen`](https://github.com/commitizen/cz-cli) command-line
tool to ensure memorable and epic git commit messages that our commit conventions,
based on the awesome conventional commits standard.

Also to clone the repo you have to set up github with SSH and can't use HTTPS to clone it.

### Gitflow

- To set it up, [follow the instructions here](https://github.com/nvie/gitflow/wiki/Installation)
- Run `git flow init` in the repository directory, applying the following options:

```
$ git flow init
Which branch should be used for bringing forth production releases?
   - main       <-- pick this in the list of branches that appears
Branch name for production releases: [main] main
Which branch should be used for integration of the "next release"?
   - staging      <-- pick this in the list of branches that appears
Branch name for "next release" development: [main] staging
How to name your supporting branch prefixes?
Feature branches? [feature/]      <-- hit enter to pick default
Release branches? [release/]      <-- same here
Hotfix branches? [hotfix/]        <-- same here
Support branches? [support/]      <-- same here
Version tag prefix?               <-- same here
```

### Commitizen

The repo uses [commitizen](https://github.com/commitizen/cz-cli) to automate
git commit conventions.

- To set it up, run `npm install` in this repo.
- To use it, use `git cz` instead of `git commit`

Ex:

```sh
$ git add .
$ git cz
cz-cli@4.0.3, cz-conventional-changelog@3.1.0

? Select the type of change that you're committing: chore:    Other changes that don't modify src or test files
? What is the scope of this change (e.g. component or file name): (press enter to skip) project
? Write a short, imperative tense description of the change (max 84 chars):
 (17) integrate commitizen
```

## Workflow notes

### Gitflow

Use the following gitflow commands to perform various operations:
| Operation | Command |
| ------------------------------------- | ------------------------------------------ |
| Create a feature branch | `git flow feature start FEATURE_NAME` |
| Push commits on a feature branch | `git flow feature publish FEATURE_NAME` |
| Pull latest changes on feature branch | `git flow feature pull origin FEATURE_NAME` |
| Complete and merge feature branch | `git flow feature finish FEATURE_NAME` |
