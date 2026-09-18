# Email

## The encounter

The inbox comes first. Sender name, subject line and preview text are the headline; most of the decision happens there. Once opened, the email is scanned, often on a phone, sometimes with images blocked, often in dark mode.

## The format's job

Earn the open, deliver one message fast, and make one action obvious.

## Specifications

Rendering varies across email clients and changes over time: image blocking, dark-mode color inversion, CSS and interactivity support, web fonts, GIF behavior. Check current support (for example caniemail.com) and the client's ESP template constraints, and cite them. Otherwise label UNVERIFIED.

## Craft

**Design the inbox view.** Treat sender, subject and preview text as one composition written with WordSmither. The preview text should continue the subject, not repeat it or show "View in browser".

**Top of the email is the hook.** The first screen on a phone carries the idea and the primary action. Everything below is support.

**One job per email.** A single primary CTA. Secondary links are quiet.

**Stack for the phone.** Single-column modules that read as a sequence. Two-column layouts should collapse gracefully.

**Live text over text in images.** Headlines and key messages in live text survive image blocking and scale better. When type must be an image, the alt text is copy and must carry the message.

**Buttons are live text.** Large tap targets, clear label, visible without images.

**Design dark mode, do not suffer it.** Clients may invert colors. Logos on transparent backgrounds can disappear, dark text can vanish, brand colors can shift. Design a dark state deliberately: outlined or keylined logos, tested color pairs.

**Motion and interactivity degrade.** Animated GIFs are widely used, but some clients show only the first frame, so the first frame must carry the message. CSS interactivity, carousels and AMP-style experiences have limited support; design the fallback first and the enhancement second.

## What to prototype

- The inbox list view with sender, subject and preview text, on phone.
- The opened email on phone and desktop.
- Dark-mode and images-off states.
- The click-through destination's first screen, for message match.
- Any interactive or animated moment with its fallback.

## Buildability flags

- Custom web fonts (need a fallback stack), background images, overlapping layers and complex grids.
- Interactivity or animation beyond broad client support.
- Personalization or dynamic content the client's ESP or data cannot supply.
- Layouts that would require rebuilding outside the client's template system.

## Fidelity check additions

- [ ] The inbox view alone makes the email worth opening.
- [ ] The message and CTA survive images-off.
- [ ] The dark-mode state is designed, not accidental.
