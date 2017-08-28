# Change Log
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/)
and this project adheres to [Semantic Versioning](http://semver.org/).

## [Unreleased]
### added
- Adds filter of series for final product produced in workorders of more of one unity of products to produce. 

## [0.3.2] - 2017-08-18
### Changed
- Fix error in form view of workorder on filter of series for raw material and product finished. Also the code was refactored.

## [0.3.1] - 2017-08-08
### Changed
- Fix error in form view of workorder on filter of series for raw material and product finished. Also the code was refactored.

## [0.3.0] - 2017-06-11
### Changed
- mrp_product_unique_serial: Add domain to field final_lot_id in form view of workorders to filter serial numbers for the product final that have not used in other production process.

## [0.2.0] - 2017-05-09
### Added
- mrp_product_unique_serial: Adds computed field to model mrp.workorder to calculate if a lot/serial number is available for use in a product in a workorder (form view).

## [0.1.1] - 2017-05-05
### Removed
- mrp_product_unique_serial: Remove extension of model stock.move.lots to fix the unwanted effects of domain of field lot_id in other process of production (work orders).

## [0.1.0] - 2017-04-24
### Added
- mrp_product_unique_serial: Adds domain to field lot_id in model stock.move.lots for filter by serial numbers of the product that have not been taken by another manufacturing order
