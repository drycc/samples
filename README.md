# Drycc Samples

This repository contains sample implementations of the core components of the Drycc project for learning and testing purposes.

Includes:

* [buildpacks](buildpacks/)
* [dockerfile](dockerfile/)
* [dryccfiles](dryccfiles/)

## Start here:

We assume that you have already installed drycc workflow and logged into an account.

### Deploy use git push

```
$ curl -SL https://github.com/drycc/samples/archive/refs/heads/main.tar.gz | tar xvz -C .
$ cd samples-main/dryccfiles/build
$ git init; git add .; git commit --all -m "init repo"; git branch -M main
$ drycc create demo
$ git push drycc main
```

### Deploy use drycc pull

```
$ curl -SL https://github.com/drycc/samples/archive/refs/heads/main.tar.gz | tar xvz -C .
$ cd samples-main/dryccfiles/image
$ drycc create demo
$ drycc pull registry.drycc.cc/drycc/base:bookworm
```


## Development

The Drycc project welcomes contributions from all developers. The high-level process for development matches many other open source projects. See below for an outline.

* Fork this repository
* Make your changes
* [Submit a pull request][prs] (PR) to this repository with your changes, and unit tests whenever possible.
  * If your PR fixes any [issues][issues], make sure you write Fixes #1234 in your PR description (where #1234 is the number of the issue you're closing)
* Drycc project maintainers will review your code.
* After two maintainers approve it, they will merge your PR.