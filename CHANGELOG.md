# Changelog

## 3.0.0

- Added Operating Partner constitution and risk-adjusted capital allocation across existing modes.
- Added marginal-value stop rules, local repair preference, cause-based STOP_LOSS, validation reserve, and lightweight accounting/learning.
- Added conditional references and optional gate checks for reviewed capital interruption metadata.
- Preserved V1 transport, exact material authorization, independent review and the unmet FULL gate under local-only fallback.
- Architecture version jumps from the existing 1.0.0 package to the user-requested v3; no intervening v2 release is asserted. Behavioral evidence is stored outside the installable package.

## 1.0.0

Initial public release.

### Added

- DIRECT / LIGHT / FULL routing
- Task contracts and acceptance criteria
- Evidence-based verification
- Independent ChatGPT review when supported
- Review finding triage
- Repair and recheck loops
- Direction reassessment for repeated failures
- Material authorization boundaries
- Completion gates
- Domain-skill composition
- LOCAL_REVIEW_ONLY fallback when external review is unavailable

`LOCAL_REVIEW_ONLY` reports limited review coverage; it does not satisfy a FULL gate that requires external review.
