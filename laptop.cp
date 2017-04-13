:-sorts
objectid.
:-objects
laptop :: objectid.

:-variables
A, B :: objectid.

:-constants
closed, opened, held, put, watching, playing, taken :: inertialFluent;

closing_laptop, opening_laptop, holding_laptop, putting_laptop_somewhere, watching_on_laptop,
playing_on_laptop, taking_laptop_somehwere :: inertialFluent;

close(objectid), open(objectid), hold(objectid), put(objectid),
watch(objectid), play(objectid), take(objectid) :: exogenousAction.

close(A) causes closing_laptop.
close(A) causes -opening_laptop.
caused closed if closing_laptop.
caused -closed if -closing_laptop.
caused -watching_on_laptop if closing_laptop.
caused -playing_on_laptop if closing_laptop.
nonexecutable close(A) if closing_laptop.
nonexecutable close(A) if -holding_laptop.

open(A) causes opening_laptop.
open(A) causes -closing_laptop.
caused opened if opening_laptop.
caused -opened if -opening_laptop.
nonexecutable open(A) if opening_laptop.
nonexecutable open(A) if -holding_laptop.

hold(A) causes holding_laptop.
caused held if holding_laptop.
caused -held if -holding_laptop.
nonexecutable hold(A) if holding_laptop.

put(A) causes putting_laptop_somewhere.
caused put if putting_laptop_somewhere.
caused -watching_on_laptop if putting_laptop_somewhere.
caused -playing_on_laptop if putting_laptop_somewhere.
caused -put if -putting_laptop_somewhere.
nonexecutable put(A) if -holding_laptop.
nonexecutable put(A) if putting_laptop_somewhere.

watch(A) causes watching_on_laptop.
caused watching if watching_on_laptop.
caused -watching if -watching_on_laptop.
nonexecutable watch(A) if watching_on_laptop.
nonexecutable watch(A) if closing_laptop.
nonexecutable watch(A) if -opening_laptop.

play(A) causes playing_on_laptop.
caused playing if playing_on_laptop.
caused -playing if -playing_on_laptop.
caused watching_on_laptop if playing_on_laptop after watch(A).
caused -watching_on_laptop if -playing_on_laptop.
nonexecutable play(A) if playing_on_laptop.
nonexecutable play(A) if putting_laptop_somewhere.
nonexecutable play(A) if closing_laptop.
nonexecutable play(A) if -opening_laptop.

take(A) causes taking_laptop_somehwere.
caused taken if taking_laptop_somehwere.
caused -taken if -taking_laptop_somehwere.
nonexecutable take(A) if taking_laptop_somehwere.

nonexecutable close(A) if open(A).
nonexecutable close(A) if hold(A).
nonexecutable close(A) if put(A).
nonexecutable close(A) if watch(A).
nonexecutable close(A) if play(A).
nonexecutable close(A) if take(A).

nonexecutable open(A) if hold(A).
nonexecutable open(A) if put(A).
nonexecutable open(A) if watch(A).
nonexecutable open(A) if play(A).
nonexecutable open(A) if take(A).

nonexecutable hold(A) if put(A).
nonexecutable hold(A) if watch(A).
nonexecutable hold(A) if play(A).
nonexecutable hold(A) if take(A).

nonexecutable put(A) if watch(A).
nonexecutable put(A) if play(A).
nonexecutable put(A) if take(A).

nonexecutable watch(A) if play(A).
nonexecutable watch(A) if take(A).

nonexecutable play(A) if take(A).

:- query
label :: 1;
maxstep :: 1..5;
0: -closing_laptop&-opening_laptop&-holding_laptop&-putting_laptop_somewhere&-watching_on_laptop&-playing_on_laptop&-taking_laptop_somehwere;
maxstep: watching.
