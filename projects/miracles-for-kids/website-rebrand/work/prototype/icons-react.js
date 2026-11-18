import React from 'react';
import { createRoot } from 'react-dom/client';
import { CreditCard, Home, Sun, ShoppingBag, TrendingUp, ArrowUpRight, Play, Video, BookOpen, Clock, Users, Gift, Mail, Send, X, Calendar, Menu } from 'react-feather';

// Feather's native 24px grid and 2px stroke; keep the visible text as the accessible label.
const icons = { CreditCard, Home, Sun, ShoppingBag, TrendingUp, ArrowUpRight, Play, Video, BookOpen, Clock, Users, Gift, Mail, Send, X, Calendar, Menu };
for (const host of document.querySelectorAll('[data-feather-icon]')) {
  const Icon = icons[host.dataset.featherIcon];
  if (Icon) createRoot(host).render(React.createElement(Icon, {
    size: 24, strokeWidth: 2, color: 'currentColor', 'aria-hidden': true, focusable: false
  }));
}
