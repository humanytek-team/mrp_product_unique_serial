# Change Log
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/)
and this project adheres to [Semantic Versioning](http://semver.org/).

## [Unreleased]

## [0.1.1] - 2017-05-05
### Removed
- mrp_product_unique_serial: Remove extension of model stock.move.lots to fix the unwanted effects of domain of field lot_id in other process of production (work orders).

## [0.1.0] - 2017-04-24
### Added
- mrp_product_unique_serial: Adds domain to field lot_id in model stock.move.lots for filter by serial numbers of the product that have not been taken by another manufacturing order
