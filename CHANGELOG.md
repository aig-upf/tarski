# Changelog

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]
### Changed
- Almost-identical methods `approximate_symbol_fluency` and `classify_symbols` have been merged into one
  single method `approximate_symbol_fluency`.

### Added
 - Preliminary [readthedocs documentation](https://tarski.readthedocs.io) integrated in the repository.
   CI tests the documentation build as well.
 - Implementation of a `project_away_effect_free_variables_from_problem` transformation that for each action schema
   compiles into existential variables all action parameters that are not used in the action effects
    ([#63](https://github.com/aig-upf/tarski/issues/63)).
 - Preliminary implementation of a library of benchmark generators
    ([#43](https://github.com/aig-upf/tarski/issues/43)).

### Removed
### Deprecated
### Fixed
 - Fixed some minor bugs in FSTRIPS writer.

## [0.3.0] - 2019-08-03

### Added
 - Preliminary implementation of a `tarski.fstrips.representation` module with some representational queries 
   and transformations. 
 - Preliminary integration with [mypy static typing analysis](https://github.com/python/mypy) which is
   checked now in the CI tests.
 - Add helper function `find_domain_filename` to infer domain filenames from instance filenames.
 - Add `collect_unique_nodes` method to collect all AST nodes of any FSTRIPS expression.
 - Add namespace accessor `lang.ns` to FOL objects to allow direct access to any language element.
 
### Fixed
 - Fixed bug with fluent / static symbol classification [#66](https://github.com/aig-upf/tarski/issues/66).
 - Fixed bug with multiple conditional effects in [FSTRIPS / PDDL parser](https://github.com/aig-upf/tarski/commit/c89ac31623171b78689d5d0ae3eca07c2be2ad71).
 - Fix bug in printing of FSTRIPS instances [#69](https://github.com/aig-upf/tarski/issues/69).
 - Some other minor bugfixes.

## [0.2.0] - 2019-07-16
### Added
 - Parsing and writing of Functional STRIPS and PDDL encodings of classical planning problems.
 - Parsing and writing of RDDL encodings of Markov Decision Processes (MDPs) and hybrid planning problems.
 - Answer Set Programming-based grounding and reachability analysis for classical planning problems.
 - Description Logics module for classical planning problems.
 - Support for Existentially and Universally Quantified effects in Functional STRIPS and PDDL domain descriptions.
 - Syntax for elementary linear algebra operations with vectors and matrices.
 - Support for the evaluation of expressions involving matrices, vectors and scalars.
 - Expression simplification.


## [0.1.0] - 2018-09-15

First public release.
