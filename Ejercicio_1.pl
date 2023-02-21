padrede('Juan', 'Maria').
padrede('Pablo', 'Juan').
padrede('Pablo', 'Marcela').
padrede('Carlos', 'Debora').

hijode(A, B):- padrede(B, A).
abuelode(A, B):- padrede(A, C), padrede(C, B).
hermanode(A, B):- padrede(C, A),padrede(C, B), A \== B.
familiarde(A, B) :- padrede(A, B).
familiarde(A, B) :- hijode(A, B).
familiarde(A, B) :- hermanode(A, B).
