dividea('2', '6').
dividea('2', '12').
dividea('3', '6').
dividea('3', '12').

diviseis(C) :- dividea('2', C), dividea('3', C).

