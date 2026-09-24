# 3 Build

> Write code, test it, document it.

## Table of Contents

1. [Stage Overview](#stage-overview) _(Lines 45-47)_
   1. [Why Interleaving Matters](#why-interleaving-matters) _(Lines 50-60)_
   1. [What Happens Here](#what-happens-here) _(Lines 63-69)_
   1. [The Development Rhythm](#the-development-rhythm) _(Lines 72-86)_
   1. [Entry Criteria](#entry-criteria) _(Lines 89-94)_
   1. [Exit Criteria](#exit-criteria) _(Lines 97-110)_
1. [Implementation Phase](#implementation-phase) _(Lines 113-115)_
   1. [The Implementation Mindset](#the-implementation-mindset) _(Lines 118-120)_
   1. [Naming](#naming) _(Lines 123-158)_
   1. [Typing](#typing) _(Lines 161-184)_
   1. [Functions](#functions) _(Lines 187-206)_
   1. [Classes](#classes) _(Lines 209-245)_
   1. [Error Handling](#error-handling) _(Lines 248-272)_
1. [Testing Phase](#testing-phase) _(Lines 275-277)_
   1. [The Testing Mindset](#the-testing-mindset) _(Lines 280-282)_
   1. [Test Structure (AAA)](#test-structure-aaa) _(Lines 285-302)_
   1. [Unit Tests](#unit-tests) _(Lines 305-324)_
   1. [Integration Tests](#integration-tests) _(Lines 327-347)_
   1. [Test Organization](#test-organization) _(Lines 350-361)_
   1. [Coverage](#coverage) _(Lines 364-385)_
1. [Documentation Phase](#documentation-phase) _(Lines 388-390)_
   1. [Documentation Levels](#documentation-levels) _(Lines 393-403)_
   1. [Docstrings](#docstrings) _(Lines 406-444)_
   1. [README Structure](#readme-structure) _(Lines 447-480)_
   1. [Inline Comments](#inline-comments) _(Lines 483-500)_
1. [Stage Checklist](#stage-checklist) _(Lines 503-505)_
   1. [Implementation Checklist](#implementation-checklist) _(Lines 508-516)_
   1. [Testing Checklist](#testing-checklist) _(Lines 519-526)_
   1. [Documentation Checklist](#documentation-checklist) _(Lines 529-534)_
   1. [Quick Verification](#quick-verification) _(Lines 537-547)_
1. [Navigation](#navigation) _(Lines 550-556)_



---

## Stage Overview
<!-- Lines 45-47 -->

The Build stage is the **core development loop**: write code, test it, document it. These three activities are interleaved, not sequential. You don't write all code, then all tests, then all docs—you build incrementally, testing and documenting as you go.

### Why Interleaving Matters
<!-- Lines 50-60 -->

**Writing tests with code:**
- Tests clarify requirements before you code
- Tests catch bugs immediately, not later
- Untested code tends to stay untested

**Writing docs with code:**
- Fresh understanding produces better documentation
- Docstrings explain intent while it's clear
- Documentation gaps reveal API problems

### What Happens Here
<!-- Lines 63-69 -->

This stage has three interleaved phases:

1. **Implementation (3.1):** Writing the actual code
2. **Testing (3.2):** Verifying code works correctly
3. **Documentation (3.3):** Explaining how to use and maintain

### The Development Rhythm
<!-- Lines 72-86 -->

A typical cycle:

```
1. Pick a capability from design
2. Write a failing test for it
3. Implement until test passes
4. Write docstring explaining the interface
5. Refactor if needed
6. Commit
7. Repeat
```

This is essentially Test-Driven Development (TDD), though the exact order can vary.

### Entry Criteria
<!-- Lines 89-94 -->

You enter this stage when:
- Requirements and design are complete (from Stage 1)
- Environment and structure are set up (from Stage 2)
- You're ready to write production code

### Exit Criteria
<!-- Lines 97-110 -->

You exit this stage when:
- All planned capabilities are implemented
- Tests pass with adequate coverage
- Code is documented (docstrings, README)
- Code passes linting and type checking

**Philosophy connections:**
- [0.5 Communication as UX](../LOD_0_philosophy/0.5_communication_ux.md) — Naming and documentation
- [0.7 Polyglot Pragmatism](../LOD_0_philosophy/0.7_polyglot_pragmatism.md) — Right paradigm for each problem
- [0.6 Reproducibility](../LOD_0_philosophy/0.6_reproducibility.md) — Tests ensure reproducible behavior

---

## Implementation Phase
<!-- Lines 113-115 -->

Implementation is where design becomes code.

### The Implementation Mindset
<!-- Lines 118-120 -->

Good implementation is **translation**, not **invention**. If you did Stage 1 well, you're translating a design into code. If you find yourself making major design decisions while coding, return to Stage 1.

### Naming
<!-- Lines 123-158 -->

Names are the primary communication channel. Invest in them.

**Variables:** Describe content, not type
```python
# Bad: Type in name, vague
user_list = []
data_dict = {}

# Good: Purpose is clear
active_users = []
session_tokens = {}
```

**Functions:** Verb + object, describe action
```python
# Bad: Vague
def process(data): ...
def handle(request): ...

# Good: Specific action
def validate_email(email: str) -> bool: ...
def create_user_session(user: User) -> Session: ...
```

**Classes:** Nouns, describe entities
```python
# Bad: Vague or verb-like
class Manager: ...
class Processor: ...

# Good: Clear entity
class UserAccount: ...
class PaymentTransaction: ...
```

### Typing
<!-- Lines 161-184 -->

Type hints serve as executable documentation:

```python
from typing import Optional
from uuid import UUID

def get_user(user_id: UUID) -> Optional[User]:
    """Retrieve a user by ID.

    Args:
        user_id: The unique identifier for the user.

    Returns:
        The User if found, None otherwise.
    """
    return self.repository.get(user_id)
```

**Typing strategy:**
- Always type function signatures
- Type complex variables
- Use `mypy` to verify

### Functions
<!-- Lines 187-206 -->

Keep functions focused and testable:

```python
# Bad: Does too much
def process_order(order_data: dict) -> Order:
    # Validates, transforms, saves, notifies... 100 lines

# Good: Single responsibility
def validate_order(data: dict) -> ValidatedOrder: ...
def calculate_totals(order: ValidatedOrder) -> PricedOrder: ...
def persist_order(order: PricedOrder) -> Order: ...
def notify_customer(order: Order) -> None: ...
```

**Guidelines:**
- Functions should do one thing
- Prefer pure functions where possible
- Side effects should be explicit and at boundaries

### Classes
<!-- Lines 209-245 -->

Use classes when you have entities with identity and behavior:

```python
@dataclass
class ShoppingCart:
    """A user's shopping cart."""

    items: list[CartItem] = field(default_factory=list)

    def add_item(self, product: Product, quantity: int = 1) -> None:
        """Add a product to the cart."""
        existing = self._find_item(product.id)
        if existing:
            existing.quantity += quantity
        else:
            self.items.append(CartItem(product=product, quantity=quantity))

    @property
    def total(self) -> Decimal:
        """Calculate cart total."""
        return sum(item.subtotal for item in self.items)

    def _find_item(self, product_id: UUID) -> CartItem | None:
        return next((i for i in self.items if i.product.id == product_id), None)
```

**When to use classes:**
- Entity with identity and lifecycle
- State that needs encapsulation
- Behavior attached to data

**When to use functions:**
- Stateless transformations
- Utility operations
- Simple actions

### Error Handling
<!-- Lines 248-272 -->

Handle errors explicitly:

```python
# Define domain exceptions
class OrderError(Exception):
    """Base exception for order operations."""

class InsufficientStockError(OrderError):
    """Raised when product stock is insufficient."""

# Use them clearly
def reserve_stock(product_id: UUID, quantity: int) -> None:
    stock = self.get_stock(product_id)
    if stock < quantity:
        raise InsufficientStockError(
            f"Requested {quantity} but only {stock} available for {product_id}"
        )
    self._decrease_stock(product_id, quantity)
```

**Cross-ref:** → [3.1 Implementation](../LOD_2_phases/3.1_implementation.md) for detailed guidance

---

## Testing Phase
<!-- Lines 275-277 -->

Tests verify that code works and continues to work.

### The Testing Mindset
<!-- Lines 280-282 -->

Tests are **specifications that execute**. A well-written test describes what the code should do; passing tests prove it does.

### Test Structure (AAA)
<!-- Lines 285-302 -->

Every test follows Arrange-Act-Assert:

```python
def test_add_item_to_empty_cart():
    # Arrange: Set up preconditions
    cart = ShoppingCart()
    product = Product(id=uuid4(), name="Widget", price=Decimal("9.99"))

    # Act: Perform the action
    cart.add_item(product, quantity=2)

    # Assert: Verify the outcome
    assert len(cart.items) == 1
    assert cart.items[0].quantity == 2
    assert cart.total == Decimal("19.98")
```

### Unit Tests
<!-- Lines 305-324 -->

Test individual functions and methods in isolation:

```python
class TestEmailValidation:
    def test_valid_email_returns_true(self):
        assert is_valid_email("user@example.com") is True

    def test_missing_at_sign_returns_false(self):
        assert is_valid_email("userexample.com") is False

    def test_empty_string_returns_false(self):
        assert is_valid_email("") is False
```

**Unit test characteristics:**
- Fast (milliseconds)
- Isolated (no external dependencies)
- Deterministic (same result every time)

### Integration Tests
<!-- Lines 327-347 -->

Test component interactions:

```python
@pytest.fixture
def database():
    """Provide a test database."""
    db = create_test_database()
    yield db
    db.cleanup()

def test_user_creation_persists(database):
    service = UserService(database)

    user = service.create_user(email="test@example.com", name="Test")

    retrieved = service.get_user(user.id)
    assert retrieved is not None
    assert retrieved.email == "test@example.com"
```

### Test Organization
<!-- Lines 350-361 -->

```
tests/
├── conftest.py           # Shared fixtures
├── unit/
│   ├── test_models.py
│   └── test_services.py
└── integration/
    ├── test_api.py
    └── test_database.py
```

### Coverage
<!-- Lines 364-385 -->

Aim for meaningful coverage, not 100%:

```bash
# Run with coverage
pytest --cov=myproject --cov-report=term-missing

# Focus on:
# - Business logic: High coverage
# - Edge cases: Explicitly tested
# - Error paths: Tested
```

**Coverage targets:**
- 80%+ for business logic
- 100% for critical paths
- Don't chase coverage for its own sake

**Cross-ref:** → [3.2 Testing](../LOD_2_phases/3.2_testing.md) for detailed guidance

---

## Documentation Phase
<!-- Lines 388-390 -->

Documentation explains how to use and maintain code.

### Documentation Levels
<!-- Lines 393-403 -->

From most granular to most broad:

| Level | Audience | Location |
|-------|----------|----------|
| Code comments | Maintainers | Inline |
| Docstrings | Developers | Functions/classes |
| README | Users | `README.md` |
| API docs | Developers | Generated/external |
| User guides | End users | External |

### Docstrings
<!-- Lines 406-444 -->

Every public function and class needs a docstring:

```python
def create_order(
    user_id: UUID,
    items: list[OrderItem],
    *,
    shipping_address: Address | None = None,
) -> Order:
    """Create a new order for a user.

    Creates an order with the given items and optional shipping address.
    If no shipping address is provided, uses the user's default address.

    Args:
        user_id: The ID of the user placing the order.
        items: List of items to include in the order.
        shipping_address: Optional shipping address. Defaults to user's
            saved address if not provided.

    Returns:
        The newly created Order with a generated ID.

    Raises:
        UserNotFoundError: If user_id doesn't exist.
        EmptyOrderError: If items list is empty.
        InsufficientStockError: If any item has insufficient stock.

    Example:
        >>> order = create_order(
        ...     user_id=user.id,
        ...     items=[OrderItem(product_id=p.id, quantity=2)],
        ... )
        >>> print(order.status)
        OrderStatus.PENDING
    """
```

### README Structure
<!-- Lines 447-480 -->

Every project needs a README:

```markdown
# Project Name

Brief description of what it does.

## Installation
<!-- Lines 460-464 -->

```bash
pip install myproject
```

## Quick Start
<!-- Lines 467-472 -->

```python
from myproject import main_function
result = main_function()
```

## Documentation
<!-- Lines 475-477 -->

Link to full docs.

## License
<!-- Lines 480-483 -->

MIT
```

### Inline Comments
<!-- Lines 483-500 -->

Comment **why**, not **what**:

```python
# Bad: Explains what (obvious from code)
# Increment counter by 1
counter += 1

# Good: Explains why (not obvious)
# Retry limit is 3 because external service has 99.9% uptime
# and 3 retries gives us 99.9999% effective availability
MAX_RETRIES = 3
```

**Cross-ref:** → [3.3 Documentation](../LOD_2_phases/3.3_documentation.md) for detailed guidance

---

## Stage Checklist
<!-- Lines 503-505 -->

Before leaving the Build stage, verify:

### Implementation Checklist
<!-- Lines 508-516 -->

- [ ] All planned capabilities are implemented
- [ ] Code follows naming conventions
- [ ] Type hints are complete
- [ ] Functions are focused (single responsibility)
- [ ] Error handling is explicit
- [ ] Linter passes (`ruff check .`)
- [ ] Type checker passes (`mypy src/`)

### Testing Checklist
<!-- Lines 519-526 -->

- [ ] Unit tests exist for business logic
- [ ] Integration tests verify component interactions
- [ ] Tests follow AAA pattern
- [ ] Tests are deterministic (no flakiness)
- [ ] Coverage is adequate (80%+ for core logic)
- [ ] All tests pass (`pytest`)

### Documentation Checklist
<!-- Lines 529-534 -->

- [ ] All public functions have docstrings
- [ ] README explains installation and basic usage
- [ ] Complex logic has explanatory comments
- [ ] API changes are documented

### Quick Verification
<!-- Lines 537-547 -->

```bash
# All should pass
ruff check .
ruff format --check .
mypy src/
pytest --cov=myproject
```

---

## Navigation
<!-- Lines 550-556 -->

**Cross-refs:**
- ↑ Parent: [LOD_1 Stages Index](0_index.md)
- ↑ Philosophy: [0.5 Communication as UX](../LOD_0_philosophy/0.5_communication_ux.md), [0.7 Polyglot Pragmatism](../LOD_0_philosophy/0.7_polyglot_pragmatism.md)
- ← Previous Stage: [2 Setup](2_setup.md)
- → Next Stage: [4 Ship](4_ship.md)
- ↓ Child Phases: [3.1 Implementation](../LOD_2_phases/3.1_implementation.md), [3.2 Testing](../LOD_2_phases/3.2_testing.md), [3.3 Documentation](../LOD_2_phases/3.3_documentation.md)
