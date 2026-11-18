/*
 * MFK Family Stories bento layout controller (merged direction).
 * Finsweet Attributes (list) filters and paginates. This script never shows or hides items:
 * after every Finsweet render it places whichever cards are on the page, in CMS order, into
 * Figma's rows on a 12-column track (single = 3 columns, double = 6), and assigns each card's
 * expressive corner. A row that can't be filled leaves an intentional gap.
 */
(() => {
  // Spans per breakpoint on the same 12-column track: 4 per row, 2 per row (tablet), 1 (phone).
  const TABLET = matchMedia('(max-width: 1000px)');
  const PHONE = matchMedia('(max-width: 600px)');
  const REDUCED = matchMedia('(prefers-reduced-motion: reduce)');
  const spans = () => {
    if (PHONE.matches) return { single: 12, double: 12 };
    if (TABLET.matches) return { single: 6, double: 12 };
    return { single: 3, double: 6 };
  };

  // Group cards into rows of 12 columns, in order. A double that doesn't fit starts a new row.
  function rowsOf(items) {
    const SPAN = spans();
    const rows = [];
    let row = [];
    let used = 0;
    for (const item of items) {
      const span = SPAN[item.dataset.size] || SPAN.single;
      if (used + span > 12) {
        rows.push(row);
        row = [];
        used = 0;
      }
      row.push({ item, span });
      used += span;
    }
    if (row.length) rows.push(row);
    return rows;
  }

  function cornerFor(card, index, length) {
    const override = card.dataset.cornerOverride;
    if (override && override !== 'auto') return override;
    if (length === 1) return 'tr';
    if (index === 0) return 'tl';
    if (index === length - 1) return 'tr';
    return 'br';
  }

  let current = [];

  function layout(elements) {
    const items = elements.filter(Boolean);
    if (!items.length) return;
    current = items;
    let above = []; // corner of the card occupying each column in the previous row

    for (const row of rowsOf(items)) {
      const thisRow = [];
      let col = 0;
      row.forEach(({ item, span }, k) => {
        const card = item.querySelector('.bento-card');
        item.style.setProperty('--start', k === 0 ? '1' : 'auto');
        item.style.setProperty('--span', span);

        // Vertical neighbours never share a corner. The play button sits top-right, so a
        // card with one never takes that corner.
        const blocked = card.querySelector('.play') ? ['tr'] : [];
        let corner = cornerFor(card, k, row.length);
        const overlaps = above.slice(col, col + span);
        if (overlaps.includes(corner) || blocked.includes(corner)) {
          corner = ['tl', 'br', 'tr'].find((c) => !overlaps.includes(c) && !blocked.includes(c))
            || ['tl', 'br'].find((c) => !blocked.includes(c));
        }
        card.dataset.corner = corner;
        for (let c = 0; c < span; c++) thisRow[col + c] = corner;
        col += span;
      });
      above = thisRow;
    }
  }

  // Phones (v4): once the chips scroll out of view while the stories are on screen, they
  // dock as a floating bar at the bottom. The slot keeps their height so nothing jumps.
  function floatFilters() {
    const form = document.querySelector('.filter-form');
    const slot = form?.parentElement;
    const section = document.querySelector('.selected-work');
    if (!form || !slot || !section) return;
    const small = matchMedia('(max-width: 700px)');
    const sync = () => {
      const s = section.getBoundingClientRect();
      const inStories = s.top < innerHeight * 0.6 && s.bottom > innerHeight * 0.4;
      const passed = slot.getBoundingClientRect().bottom < 120;
      const on = small.matches && inStories && passed;
      if (on && !form.classList.contains('is-floating')) slot.style.minHeight = `${slot.offsetHeight}px`;
      if (!on) slot.style.minHeight = '';
      form.classList.toggle('is-floating', on);
    };
    addEventListener('scroll', sync, { passive: true });
    addEventListener('resize', sync);
    small.addEventListener('change', sync);
    sync();
  }

  function init() {
    const list = document.querySelector('[fs-list-element="list"]');
    if (!list) return;

    // Before Finsweet starts (and if it never loads): lay out the CMS items as rendered.
    layout([...list.querySelectorAll(':scope > [fs-list-element="item"]')]);
    // Rows (and so corners) differ per breakpoint: recompose when it changes.
    for (const mq of [TABLET, PHONE]) mq.addEventListener('change', () => layout(current));

    // Finsweet v2 lifecycle. The render hook receives the items for the current page, after
    // filtering and pagination, in order. Use that list, never the DOM: during Finsweet's
    // enter/exit animation the DOM still holds outgoing cards.
    window.FinsweetAttributes ||= [];
    window.FinsweetAttributes.push([
      'list',
      (instances) => {
        for (const instance of instances) {
          instance.addHook('render', (items) => {
            layout(items.map((item) => item.element));
            if (turn && !REDUCED.matches) {
              items.forEach(({ element }, i) => element.animate(
                [{ opacity: 0, transform: `translateX(${turn * 32}px)` }, { opacity: 1, transform: 'none' }],
                { duration: 420, delay: i * 30, easing: 'cubic-bezier(.2,.7,.2,1)', fill: 'backwards' },
              ));
            }
            turn = 0;
            return items;
          });
        }
      },
    ]);

    // Filtering: Finsweet's starting class plays the rise-in (CSS). Paging: Finsweet adds no
    // starting class, so the render hook slides cards in from the side you're heading to (v4).
    let turn = 0;
    const setDir = (d) => { turn = d; };
    document.addEventListener('click', (event) => {
      const el = event.target.closest('[fs-list-element^="pagination-"], [fs-list-element="page-button"]');
      if (!el) return;
      const kind = el.getAttribute('fs-list-element');
      if (kind === 'pagination-next') setDir(1);
      else if (kind === 'pagination-previous') setDir(-1);
      else {
        const current = document.querySelector('[fs-list-element="page-button"][aria-current="page"]');
        setDir(Number(el.textContent) < Number(current?.textContent) ? -1 : 1);
      }
    }, true);
    document.querySelector('[fs-list-element="filters"]')?.addEventListener('input', () => setDir(0), true);
    document.querySelector('[fs-list-element="clear"]')?.addEventListener('click', () => setDir(0), true);

    floatFilters();

    // Prototype-only field toggles.
    document.querySelectorAll('[data-hide]').forEach((box) => {
      box.addEventListener('change', () => {
        document.body.classList.toggle(`hide-${box.dataset.hide}`, box.checked);
      });
    });
  }

  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', init);
  else init();
})();
