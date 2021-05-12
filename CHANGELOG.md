# Changelog

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]
### Changed
### Added
### Removed
### Deprecated
### Fixed

## [0.7.0]
### Added
  - Added some basic forward search capabilities (#101).
  - Import psutil module conditionally, to offer better support for non-Linux 
    platforms where it is not available (see discussion in #99). 

### Removed
  - Removed support for `PySDD` and `sdd` extra, which was largely unused, and
    hard to integrate into the CI testing.

### Deprecated
  - Model.set() is now deprecated

### Fixed
 - Fixed a bug in `check_hypergraph_acyclicity` reported by @abcorrea.


## [0.6.0]- 2020-09-18
### Changed
  - Switched license to the Apache Software Licence 2.0 (#92)

### Fixed
  - Minor bugfixes and improvements.
  - Better compliance with pylint warnings and errors.  


## [0.5.1] - 2020-04-17
### Fixed
  - Fixed some silly releasing mistakes... through a new release :-)


## [0.5.0] - 2020-04-17
### Added
  - Improved documentation (still work in progress though).
  - Added methods to simplify problems, actions, logical expressions based on evaluation
  of static atoms and terms.
  - Added method to compile away negated literals in action preconditions, action effect conditions
  and goal, using the standard mechanism of creating additional predicates.
  - Almost all benchmarks from the IPC competitions 2008, 2011, 2014, 2018 are now correctly parsed by Tarski.
  The unit tests also make sure this keeps being true. The only domain that Tarski cannot parse
  correctly is Tidybot, where "cart" is used both as type name and object name. This does not bode well with 
  the assumptions made in Tarski first-order languages. Problems from domains Floortile and GED need to be parsed
  with caution as well, by using, respectively, the parser options `strict_with_requirements=False` and
  `case_insensitive=True`, since the first one uses action costs without declaring them in the "requirements" section,
  whereas the second one uses lowercase in the domain file, and uppercase in the instance file.
  - Improved support for representation and parsing of action costs. 
  - Added methods to check applicability of an action in a state (model) and to progress a state through an action. 
  - Added some methods to the `fstrips.representation` module to check and compute delete-free relaxations of problems.
  - Modularize Tarski dependencies so that the use and  installation of numpy, scipy, etc. is optional.
  - Generation of action schema CSPs.


## [0.4.0] - 2019-12-28
### Changed
- Almost-identical methods `approximate_symbol_fluency` and `classify_symbols` have been merged into one
  single method `approximate_symbol_fluency`.

### Added
 - Preliminary [readthedocs documentation](https://tarski.readthedocs.io) integrated in the repository.
   CI tests the documentation build as well.
 - Integration with the [PySDD package](https://github.com/wannesm/PySDD) for sentential decision diagrams
 to process action schema preconditions.
 - Implementation of a `project_away_effect_free_variables_from_problem` transformation that for each action schema
   compiles into existential variables all action parameters that are not used in the action effects
    ([#63](https://github.com/aig-upf/tarski/issues/63)).
 - Implementation of a `compile_universal_effects_away` transformation that expands universal effects in actions. 
 - Reachability module now processes problems with cost-related functions (010d79df)
 - Preliminary implementation of a library of benchmark generators
    ([#43](https://github.com/aig-upf/tarski/issues/43)).
 - Added some preliminary support for the NDL representation language.

### Fixed
 - Fixed some minor bugs in FSTRIPS writer.
 - Fixed bug in ReachabilityLPCompiler when problem has an action and a predicate with the same name (7e9a684).
 - Remove temporary files created by the LP based grounder.
 - Model.list_all_extensions now returns empty extensions if necessary (ffbc96d1)


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
