/* Audit markup layer for Leo's Task Hub mockup v2.
   Findings: work/interaction/ux-audit_leo-mockup-v2_2026-10-20.md
   Toggle with the "Markup" button or the M key. */
(function(){
  var A=[
    // any Workspace view
    {n:1,s:'hi',w:'ws',q:'.ds-scope',t:'Everyone sees Everyone',x:'A designer opens on all 34 agency items. "My team\'s work" is never the default.',f:'Default by role: Mine for makers, My team for CDs, Everyone for PMs and leadership. Remember the last choice.'},
    {n:2,s:'hi',w:'ws',q:'.hs-summary',t:'Seven count tiles…',x:'Total open, Active, In the queue, On hold, Overdue, Due this week, With the client: 7 numbers before any work.',f:'One header band below the view switcher (~96px, not ~330px): Overdue · On hold · Needs someone · Needs a date as inline filters, 14px, zeros hidden. Totals move to Executive.'},
    {n:3,s:'hi',w:'ws',q:'.db-hot-inbox',t:'…then six chips repeating them',x:'Overdue, On hold and In the queue appear in both rows. In the queue reads 14 above and 1 here. The whole block repeats on Weekly, Day, Calendar and Status.',f:'Merge with #2 into a single row, shown once per page.'},
    {n:4,s:'md',w:'any',q:function(){return [].slice.call(document.querySelectorAll('.side-btn')).filter(function(b){return /Executive/.test(b.textContent);})[0];},t:'Executive shows for everyone',x:'Designers see a leadership dashboard in their nav.',f:'Show nav items by role.'},
    {n:5,s:'ok',w:'ws',q:'.suf-start',t:'Copy back: guided standup',x:'Per-person prompts, "Also watch", and a wrap-up with Copy summary are better than ours.',f:'Port into our prototype.'},
    {n:6,s:'ok',w:'any',q:'#userSwitch',t:'Copy back: Viewing as',x:'A role switcher makes it easy to demo and QA role defaults.',f:'Keep in the build for admins.'},
    // Weekly
    {n:7,s:'hi',w:'week',q:'.db-week-parent',t:'Parent line on every card',x:'The project name repeats under each step title and slows scanning.',f:'Drop on the Status board. On Weekly keep one truncated secondary line.'},
    {n:8,s:'hi',w:'ws',q:'.hs-stat-name',t:'11px tracked capitals',x:'The most common label style is 11px, weight 800, uppercase, letter-spaced: client names, KPI labels. Hardest text to scan. One screen uses 18 size/weight combinations.',f:'Five-step scale: page 28 · heading 14/600 · card title 15/500 · body 14 · meta 12/500, client 12/600 sentence case. Tabular figures. No caps under 12px.'},
    {n:9,s:'hi',w:'week',q:'.db-week-card.is-late .db-week-card-meta',t:'Status chip plus overdue',x:'A late card carries a status chip and a red due pill: two signals competing.',f:'One badge per card, chosen by priority (Blocked → Overdue → …).'},
    // Status board
    {n:10,s:'md',w:'status',q:'.db-week-day[data-stat="queue"] .db-week-day-heading',t:'"In the queue" before Intake',x:'Work flows backwards at the start of the board.',f:'Intake → Ready → In progress → Internal review → QC → With client → Feedback → Done.'},
    {n:11,s:'md',w:'status',q:'.db-week-day[data-stat="hold"] .db-week-day-heading',t:'On hold buried near the end',x:'Stuck work sits between With client and Complete, off-screen at most widths.',f:'Blocked / On hold as a lane across the top of the board.'},
    {n:12,s:'md',w:'status',q:'.db-stat-board .db-week-age',t:'Unexplained "1d / 7d" box',x:'Days in stage, explained only on hover. Every card shows it in the same warning yellow.',f:'Show only past a threshold, neutral grey, labelled "7d in stage"; amber only when it threatens the date.'},
    {n:13,s:'hi',w:'status',q:'.db-week-day[data-stat="qc"] .db-week-day-heading',t:'QC checklist hidden and advisory',x:'The five-item checklist lives only on the full task page, the card shows no progress, and it never blocks With client.',f:'Show "QC 3/5" on the card and in the dialog. Stays advisory; sending under 5/5 asks for a logged reason.'},
    // Calendar
    {n:14,s:'ok',w:'cal',q:function(){var h=document.querySelector('.db-cal-head');return h&&h.parentElement;},t:'Copy back: project bars',x:'Spanning bars with "+N more" per day read better than our Calendar.',f:'Port into our prototype.'},
    // Home
    {n:15,s:'md',w:'home',q:function(){var h=document.getElementById('hmTodayH');return h&&h.closest('section');},t:'"Nothing on your list"',x:'Empty while the row above says 7 open and 5 due this week.',f:'When today is empty, show "Next up": the next three by date.'},
    // Task dialog
    {n:16,s:'hi',w:'dlg',q:'#taskDlg .dlg-title-row .st-chip',t:'Three statuses in one dialog',x:'Header chip "In the queue", a Status select, and Project status "Quality Control".',f:'One status (the project\'s); the step shows as "current step".'},
    {n:17,s:'hi',w:'dlg',q:function(){var p=[].slice.call(document.querySelectorAll('#taskDlg .dlg-label')).filter(function(e){return /project status/i.test(e.textContent);})[0];return p&&p.parentElement;},t:'Project status vs step status',x:'Same item, two stages. PMs and designers have to reconcile them.',f:'See #16.'},
    {n:18,s:'hi',w:'dlg',q:function(){var h=document.getElementById('dlgAsH');return h&&h.closest('section');},t:'Assign from the whole agency',x:'Eleven people as chips under Creative, Media and Account. The full task page already has role rows; this dialog does not.',f:'Reuse the full page Ownership rows: Account manager, Creative lead, Maker, Reviewer (not the maker). A picker, not a wall.'},
    {n:19,s:'md',w:'dlg',q:'#taskDlg',t:'Modal hides the board',x:'Detail opens centred over everything, so you lose the column you came from.',f:'Right-side sheet; keep "Open full page".'},
    // Standup
    {n:20,s:'md',w:'su',q:'#suFocusLayer .suf-pos',t:'12 steps',x:'Opens on Internal review, not on what is stuck. Steps with nothing in them still count.',f:'Start with On hold / blocked, skip empty steps.'},
    {n:21,s:'ok',w:'su',q:'#suFocusLayer .suf-who',t:'Copy back: per-person prompts',x:'What moves today · Will it make the promised date · What\'s blocking you, and who owns it?',f:'Port into our prototype.'},
    // Decisions and DesignChamp pass, 2026-10-20
    {n:22,s:'hi',w:'any',q:'.side-cta',t:'Red primary button',x:'New Task is the only filled red thing at rest, so the eye lands on it before any work, and red also means Overdue.',f:'Decided: neutral primary. Light: ink #14151A, white text. Dark: off-white #F2F2F5, ink text. One per screen. Red only for problems; Traffik red stays in the logo.'},
    {n:23,s:'hi',w:'week',q:function(){return [].slice.call(document.querySelectorAll('.db-week-card')).filter(function(c){var k=c.querySelector('.db-week-card-client');return c.offsetWidth>100&&k&&/CSUN/i.test(k.textContent);})[0];},t:'Colour has three jobs',x:'Cards are tinted and bordered by client (CSUN dark red), columns by status, and red marks severity. Nothing reads as the problem.',f:'Client as text colour on the name only; neutral card surface one step lighter than the page; status chips muted; red and amber only for problems and risk.'},
    {n:24,s:'md',w:'ws',q:'.masthead',t:'42px page title',x:'"Workspace" is the largest type on the page, then 30px counts. The work comes third.',f:'28px page title; counts become 14px inline text.'},
    {n:25,s:'md',w:'week',q:'.db-week-day-heading .dv-today, .db-week-day.is-today .db-week-day-heading',t:'Today in the red family',x:'Pink column tint plus pink "Today" borrows the Overdue colour.',f:'Neutral lighter column fill and an underline under the date.'},
    {n:26,s:'hi',w:'status',q:'.db-week-day[data-stat="progress"] .db-week-day-heading',t:'Columns tinted by status',x:'Each column has its own coloured fill and border, on top of client-coloured cards.',f:'Neutral columns; a small status dot before the column name.'},
    {n:27,s:'md',w:'any',q:'#hdrMore',t:'Personal settings',x:'Theme, Preferred team and notifications exist but save to this browser only.',f:'Decided: settings on the user profile, applied before first paint. Theme (System/Light/Dark), Text size, Density, Opens on, Default scope, Motion, Weekends, Preferred team, Notifications. Role defaults set by admin.'},
    {n:28,s:'md',w:'dlg',q:'#taskDlg [data-k="dlg-open"]',t:'Roles and QC hide behind this',x:'Ownership (AM, PM, Creative lead, Reviewer) and the five-item QC checklist exist only on the full page.',f:'Show them in the quick dialog. QC stays advisory: sending to With client under 5/5 asks for a one-line reason, logged in activity; card shows "QC 3/5 · sent early".'},
    // Gaps closed 2026-10-20 (DesignChamp full review)
    {n:29,s:'md',w:'status',q:'.db-stat-board .db-week-day[data-stat="intake"] .db-week-card',t:'No visible move confirmation',x:'After a move only screen readers hear "moved to Intake". A card dragged into an off-screen column vanishes from view, with no undo.',f:'Toast "Moved to Intake · Undo" for 5 seconds; Undo restores column and focus.'},
    {n:30,s:'hi',w:'ws',q:'.db-hot-views',t:'Phone: no work above the fold',x:'At 375px the tiles become a sideways strip clipped mid-label ("IN THE"), chips stack five rows, and the first card starts at 831px on an 812px screen. At 720px (200% zoom) the header fills the first screen.',f:'Header band collapses to one "4 issues" button on phones; at least one row of cards visible at 375, 720 and 1440px.'},
    {n:31,s:'md',w:'any',q:function(){var s=[].slice.call(document.querySelectorAll('.side-btn svg, .side-cta svg'));return s[0]&&s[0].closest('button');},t:'No icon system',x:'About 15 hand-drawn inline icons with mixed stroke widths (1.4, 1.6, 1.75) and mixed grids (12, 16, 24).',f:'Lucide (successor to Feather, ISC licence): 24px grid, stroke 1.75, drawn at 16px in UI and 20px in nav, currentColor, aria-hidden beside a text label.'},
    {n:32,s:'op',w:'status',q:'.db-week-day[data-stat="intake"] .db-week-day-heading',t:'Inline add',x:'Small items still need the full New Task form.',f:'Trello-style "+ Add a card" at the column foot: title only, lands in Intake. The full form stays.'},
  ];
  var C={hi:'#ff4d4f',md:'#ff9f1a',op:'#4da3ff',ok:'#2fd67b'}, L={hi:'Major',md:'Minor',op:'Opportunity',ok:'Keep'};
  var on=true, panel=true, open=null, root=document.createElement('div');
  root.id='mk-root';
  var css=document.createElement('style');
  css.textContent='#mk-root{position:fixed;inset:0;pointer-events:none;z-index:2147483646;font:13px/1.4 system-ui,sans-serif}'+
  '.mk-box{position:fixed;border:2px solid;border-radius:6px;pointer-events:none}'+
  '.mk-pin{position:fixed;width:24px;height:24px;border-radius:50%;color:#111;font-weight:700;font-size:12px;display:grid;place-items:center;pointer-events:auto;cursor:pointer;border:2px solid #111;box-shadow:0 2px 6px rgba(0,0,0,.5)}'+
  '.mk-note{position:fixed;width:300px;background:#fff;color:#111;border-radius:8px;padding:12px 14px;pointer-events:auto;box-shadow:0 8px 24px rgba(0,0,0,.5);border-top:5px solid}'+
  '.mk-note h4{margin:0 0 6px;font-size:14px}.mk-note p{margin:0 0 6px}.mk-note .mk-fix{margin:0;padding-top:6px;border-top:1px solid #ddd}.mk-tag{font-size:11px;font-weight:700;text-transform:uppercase;letter-spacing:.04em}'+
  '.mk-panel{position:fixed;right:12px;bottom:56px;width:300px;max-height:60vh;overflow:auto;background:#fff;color:#111;border-radius:8px;padding:10px 12px;pointer-events:auto;box-shadow:0 8px 24px rgba(0,0,0,.5)}'+
  '.mk-panel h3{margin:0 0 8px;font-size:13px}.mk-panel li{margin:0 0 6px;cursor:pointer;list-style:none}.mk-panel ul{margin:0;padding:0}'+
  '.mk-dot{display:inline-grid;place-items:center;width:18px;height:18px;border-radius:50%;font-size:10px;font-weight:700;margin-right:6px;border:1px solid #111}'+
  '.mk-toggle{position:fixed;right:12px;bottom:12px;pointer-events:auto;background:#111;color:#fff;border:1px solid #fff;border-radius:6px;padding:8px 12px;font:600 13px system-ui;cursor:pointer}';
  document.head.appendChild(css);

  function view(){
    var dl=document.querySelector('dialog[open]');
    if(dl&&dl.id==='taskDlg')return 'dlg';
    if(dl&&dl.id==='suFocusLayer')return 'su';
    var h=location.hash;
    if(/^#weekly\/status/.test(h))return 'status';
    if(/^#weekly\/cal/.test(h))return 'cal';
    if(/^#weekly\/day/.test(h))return 'day';
    if(/^#weekly/.test(h))return 'week';
    if(/^#home/.test(h)||h==='')return 'home';
    return 'other';
  }
  function applies(a,v){if(v==='dlg'||v==='su')return a.w===v;return a.w==='any'||a.w===v||(a.w==='ws'&&/^(week|day|cal|status)$/.test(v));}
  function vis(e){var r=e.getBoundingClientRect();return r.width>=20&&r.height>=8&&r.bottom>0&&r.top<innerHeight&&r.right>0&&r.left<innerWidth&&getComputedStyle(e).visibility!=='hidden';}
  function el(a){
    if(typeof a.q==='function'){var x=a.q();return x&&vis(x)?x:null;}
    var all=[].slice.call(document.querySelectorAll(a.q)).filter(vis);
    all.sort(function(m,n){var r=m.getBoundingClientRect(),q=n.getBoundingClientRect();return (r.top-q.top)||(r.left-q.left);});
    return all.filter(function(e){return e.getBoundingClientRect().width>60;})[0]||all[0]||null;
  }
  function esc(s){return String(s).replace(/[&<>"]/g,function(c){return {'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c];});}

  function draw(){
    var host=document.querySelector('dialog[open]')||document.body;
    if(root.parentNode!==host)host.appendChild(root);
    var v=view(), html='', list=[];
    if(on){
      A.forEach(function(a){
        if(!applies(a,v))return;
        var e=el(a); if(!e)return;
        var r=e.getBoundingClientRect(); if(!r.width&&!r.height)return;
        list.push(a);
        var c=C[a.s];
        html+='<div class="mk-box" style="left:'+(r.left-3)+'px;top:'+(r.top-3)+'px;width:'+(r.width+2)+'px;height:'+(r.height+2)+'px;border-color:'+c+'"></div>';
        var px=Math.max(4,Math.min(innerWidth-28,r.left-12)), py=Math.max(4,r.top-12);
        html+='<div class="mk-pin" data-mk="'+a.n+'" style="left:'+px+'px;top:'+py+'px;background:'+c+'" title="'+esc(a.t)+'">'+a.n+'</div>';
        if(open===a.n){
          var nx=Math.min(innerWidth-312,px+30), ny=Math.min(innerHeight-200,py);
          html+='<div class="mk-note" style="left:'+nx+'px;top:'+Math.max(4,ny)+'px;border-color:'+c+'"><span class="mk-tag" style="color:'+(a.s==='lo'?'#8a7a00':c)+'">#'+a.n+' · '+L[a.s]+'</span><h4>'+esc(a.t)+'</h4><p>'+esc(a.x)+'</p><p class="mk-fix"><b>'+(a.s==='ok'?'Action':'Fix')+':</b> '+esc(a.f)+'</p></div>';
        }
      });
      if(panel)html+='<div class="mk-panel"><h3>Findings on this view ('+list.length+')</h3><ul>'+list.map(function(a){return '<li data-mk="'+a.n+'"><span class="mk-dot" style="background:'+C[a.s]+'">'+a.n+'</span>'+esc(a.t)+'</li>';}).join('')+'</ul></div>';
    }
    if(panel)html+='<button class="mk-toggle" data-mk-toggle>'+(on?'Hide markup (M)':'Show markup (M)')+'</button>';
    if(root.innerHTML!==html)root.innerHTML=html;
  }
  root.addEventListener('click',function(ev){
    var t=ev.target.closest('[data-mk],[data-mk-toggle]'); if(!t)return;
    ev.stopPropagation(); ev.preventDefault();
    if(t.hasAttribute('data-mk-toggle')){on=!on;open=null;}
    else{var n=+t.getAttribute('data-mk');open=open===n?null:n;}
    draw();
  },true);
  document.addEventListener('keydown',function(ev){
    if(ev.key&&ev.key.toLowerCase()==='m'&&!/INPUT|TEXTAREA|SELECT/.test(document.activeElement.tagName)){on=!on;open=null;draw();}
  });
  window.__markup={print:function(){open=null;panel=false;draw();return [].slice.call(root.querySelectorAll('.mk-pin')).map(function(e){return +e.dataset.mk;});},show:function(n){on=true;open=n;draw();},hideNotes:function(){open=null;draw();},list:A};
  setInterval(draw,250);
  addEventListener('scroll',draw,true); addEventListener('resize',draw);
})();
