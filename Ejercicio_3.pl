padece('pedro', 'gripe').
padece('pedro', 'hepatitis').
padece('juan', ' hepatitis').
padece('maria', 'gripe').
padece('carlos', 'scidez').

sintoma_de('fiebre', 'gripe').
sintoma_de('cansancio', 'hepatitis').
sintoma_de('ardor_estomacal', 'acidez').
sintoma_de('cansancio', 'gripe').

suprime_a('paracetamol', 'fiebre').
suprime_a('melox', 'ardor_estomacal').

alivia(A, X) :- suprime_a(A, Y), sintoma_de(Y, X).

debe_tomar(A, B) :- alivia(A, X), padece(B, X).

