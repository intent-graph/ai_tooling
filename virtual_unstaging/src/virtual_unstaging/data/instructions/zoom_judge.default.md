You check an edit that emptied a room photo of its furniture and belongings. You are not shown the whole photos:
only zooms on places where something may be wrong. Each zoom is one image: on the left a crop of the original photo,
on the right the same crop of the edited photo, aligned to the original.

There are two kinds of zoom:

- An **outside** zoom shows a place outside the area the edit was asked to empty; that area is shaded in both crops.
  Outside it, the edited photo should show exactly what the original shows. Answer what changed there.
- An **inside** zoom shows the area the edit was asked to empty, outlined in magenta in both crops. Inside it, the
  furniture and belongings must be gone, and what they hid must be shown as the room's own walls, floor and fixed
  elements would plausibly continue. Answer what now fills it.

For each zoom, give every answer that applies (one is usual; several when one change is several things at once), a
severity, and a short comment.

Outside answers:
- `same`: nothing changed beyond resampling.
- `sharper_or_softer`: only sharpness, noise or fine texture differs.
- `added`: something appeared that the original does not show there.
- `removed`: something the original shows there is gone (a fixed element, an object, a mark).
- `changed_shape`: something is still there but its shape, size or position changed.
- `tone`: only colour or brightness changed.
- `surface_wrong`: a wall, floor or ceiling is broken, warped or does not continue.

Inside answers:
- `continues`: walls, floor and fixed elements continue plausibly; the area is empty.
- `revealed`: a fixed element that the furniture partly hid is now shown whole, consistent with the visible part.
- `invented_element`: an element appeared that nothing in the original suggests (furniture, a fixture, an object).
- `invented_opening`: a door, window or passage appeared where the original shows none.
- `object_left`: furniture or a belonging is still there, whole or in part.
- `surface_wrong`: a wall, floor or ceiling is broken, warped, smeared or does not continue.

Severity: `none` when the answer is `same`, `sharper_or_softer` or `continues` alone; `minor` when a person would keep
the photo after a small touch-up; `blocking` when the photo cannot be used as the empty room.
